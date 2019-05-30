from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.http import JsonResponse
from django.apps import apps
from .models import vessel_voy_info, ves_struct, ves_bay_struct, \
    ves_bay_lay_struct, con_pend_info, qc_info, qc_dis_plan_out,\
con_stowage_export, con_stowage_import
from django.db.models import Count,Min,Max,Sum
from .methods import index_to_num, combined_bay_list,\
    create_engine_index, create_index_list, num_to_index,\
    bay_num_to_index_list, layer_con_list_to_db, \
    db_layer_info_to_list, get_bay_width, bay20_num_index_list

# TODO:
# display value in choices
#  https://my.oschina.net/esdn/blog/832982

# const
confirm_of_bay_edit = 'RESPONSE_AFTER_CONFIRM_COMBINATION'
ves_side_view = 'VESSEL_SIDE_VIEWING'
con_pending_info = 'VESSEL_CONTAINER_PENDING_INFO'
get_basic_bay_combine = 'GET_BASIC_BAY_COMBINE_INFO'
data_operation_load = 'OPERATION_LOAD_BAY_STRUCT',
data_define_bay_struct = 'DEFINE_BAY_STRUCT',
all_bays_struct_info = 'ALL_BAYS_STRUCT_INFO',


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def default_page_iframe(request):
    if request.method == 'GET':
        return render(request, 'defaultPage.html')


def page_not_found(request):
    if request.method == 'GET':
        return render(request, '404.html')


def ves_basic(request):
    if request.method == 'GET':
        all_vessel = [item.Vessel for item in vessel_voy_info.objects.all()]
        return render(request, 'VESSEL/vessel.view.html', {'all_vessel': all_vessel})


@csrf_exempt
def add_vessel_page(request):
    if request.method == 'GET':
        all_vessel = [item.Vessel for item in vessel_voy_info.objects.all()]
        return render(request, 'VESSEL/vessel.input.basicInfo.html', {'all_vessel': all_vessel})


@csrf_exempt
def bay_struct_define(request):
    if request.method == 'GET':
        all_vessel = [item.Vessel for item in vessel_voy_info.objects.all()]
        return render(request, 'VESSEL/vessel.input.bayStructDefine.html', {'all_vessel': all_vessel})
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        ves_name = data['vessel']
        ves_bay = data['bay_index']
        data_deck = data['deck']
        data_cab = data['cab']
        for i in data_deck:
            idx_list = layer_con_list_to_db(i['data_list'])
            ves_bay_lay_struct.objects.create(Vessel=ves_name,
                                              BayNo=ves_bay,
                                              TireNo=i['layer_index'],
                                              DeckCagSig='1',
                                              BayWid=get_bay_width(idx_list),
                                              BayTieCtnLay=idx_list),
        for j in data_cab:
            idx_list = layer_con_list_to_db(j['data_list'])
            ves_bay_lay_struct.objects.create(Vessel=ves_name,
                                              BayNo=ves_bay,
                                              TireNo=j['layer_index'],
                                              DeckCagSig='0',
                                              BayWid=get_bay_width(idx_list),
                                              BayTieCtnLay=idx_list)
        res = {'bay_edit_status': 'success'}
        return JsonResponse(res)


@csrf_exempt
def edit_bay(request):
    if request.method == 'GET':
        ves_name = request.GET['name']
        obj_bay_inch20 = ves_bay_struct.objects.filter(Vessel=ves_name, BaySiz='20')
        obj_temp_inch40 = ves_struct.objects.get(Vessel=ves_name)
        bay_inch20_list = sorted(index_to_num([item.BayNo for item in obj_bay_inch20]))
        if obj_temp_inch40.FotBayCom:
            bay_inch40_list = sorted(index_to_num(obj_temp_inch40.FotBayCom.split(",")))
        else:
            bay_inch40_list = []
        data_bay_list = combined_bay_list(bay_inch20_list, bay_inch40_list)
        obj = ves_struct.objects.get(Vessel=ves_name)
        bay_num = obj.TweBayNum
        engine_pos = obj.EngRomPos
        engine_width = obj.EngRomWid
        eng_body_list = create_engine_index(engine_pos, engine_width)
        bay_dir = vessel_voy_info.objects.get(Vessel=ves_name).BerThgDir
        data = {
                'dataType': get_basic_bay_combine,
                'number': bay_num,
                'vessel_IMO': "001",
                'bayDirection': bay_dir,
                'engineRoomIndex': eng_body_list,
                'vessel_name': ves_name,
                'data': data_bay_list,
                }
        return JsonResponse(data)

    elif request.method == 'POST':
        content = json.loads(request.body.decode('utf-8'))
        ves_name = content['vessel_name']
        bay_inch40 = content['bayInch40s']
        fot_bay_num = len(bay_inch40)
        temp_fot_bay_com = ''
        for i in bay_inch40:
            temp_fot_bay_com += (i + ',')
        fot_bay_com = temp_fot_bay_com[:-1]
        # Update DB
        obj_ves_struct = ves_struct.objects.get(Vessel=ves_name)
        obj_ves_struct.FotBayCom = fot_bay_com
        obj_ves_struct.FotBayNum = fot_bay_num
        obj_ves_struct.save()
        # Update DB: clear bay_struct_layer info
        ves_bay_lay_struct.objects.filter(Vessel=ves_name).delete()
        # Get From DB
        obj_bay_inch20 = ves_bay_struct.objects.filter(Vessel=ves_name, BaySiz='20')
        obj_temp_inch40 = ves_struct.objects.get(Vessel=ves_name)
        bay_inch20_list = sorted(index_to_num([item.BayNo for item in obj_bay_inch20]))

        if obj_temp_inch40.FotBayCom:
            bay_inch40_list = sorted(index_to_num(obj_temp_inch40.FotBayCom.split(",")))
        else:
            bay_inch40_list = []
        data_bay_list = combined_bay_list(bay_inch20_list, bay_inch40_list)
        bay_dir = vessel_voy_info.objects.get(Vessel=ves_name).BerThgDir

        data_bay = {
            'dataType': confirm_of_bay_edit,
            'vessel_IMO': "001",
            'vessel_name': ves_name,
            'data': data_bay_list,
            'bayDirection': bay_dir,
        }
        ####################################
        # TODO: add random value after bay combination
        # generate random container pending info
        for i in obj_bay_inch20:
            obj = con_pend_info.objects.get(Vessel=ves_name, BayNo=i.BayNo)
            obj.DeckLodNum = random.randrange(0, 50, 1)
            obj.DeckUloNum = random.randrange(0, 50, 1)
            obj.CabLoaNum = random.randrange(0, 50, 1)
            obj.CabUloNum = random.randrange(0, 50, 1)
            obj.save()
        for j in bay_inch40:
            obj = con_pend_info.objects.get(Vessel=ves_name, BayNo=j)
            obj.DeckLodNum = random.randrange(0, 50, 1)
            obj.DeckUloNum = random.randrange(0, 50, 1)
            obj.CabLoaNum = random.randrange(0, 50, 1)
            obj.CabUloNum = random.randrange(0, 50, 1)
            obj.save()
        ####################################
        return JsonResponse(data_bay)


@csrf_exempt
def reset_bay_combine(request):
    # delete and reset bay combination
    if request.method == 'POST':
        ves_name = request.POST['name']
        # delete DB
        obj = ves_struct.objects.get(Vessel=ves_name)
        obj.FotBayCom = None
        obj.FotBayNum = None
        obj.save()
        # TODO: delete other info in DBs
        # get from DB
        obj_bay_inch20 = ves_bay_struct.objects.filter(Vessel=ves_name, BaySiz='20')
        obj_temp_inch40 = ves_struct.objects.get(Vessel=ves_name)
        bay_inch20_list = sorted(index_to_num([item.BayNo for item in obj_bay_inch20]))
        if obj_temp_inch40.FotBayCom:
            bay_inch40_list = sorted(index_to_num(obj_temp_inch40.FotBayCom.split(",")))
        else:
            bay_inch40_list = []
        data_bay_list = combined_bay_list(bay_inch20_list, bay_inch40_list)
        obj = ves_struct.objects.get(Vessel=ves_name)
        bay_num = obj.TweBayNum
        engine_pos = obj.EngRomPos
        engine_width = obj.EngRomWid
        eng_body_list = create_engine_index(engine_pos,engine_width)
        bay_dir = vessel_voy_info.objects.get(Vessel=ves_name).BerThgDir
        data = {
            'dataType': get_basic_bay_combine,
            'number': bay_num,
            'vessel_IMO': "001",
            'bayDirection': bay_dir,
            'engineRoomIndex': eng_body_list,
            'vessel_name': ves_name,
            'data': data_bay_list,
        }
        return JsonResponse(data)


@csrf_exempt
def create_ves_struct(request):
    if request.method == 'GET':
        name = request.GET['name']
        obj = ves_struct.objects.get(Vessel=name)
        ves_name = obj.Vessel
        ves_length = obj.VesLeng
        ves_width = obj.VesWidth
        ves_front_length = obj.VesFrLeng
        ves_bay_inch20_num = obj.TweBayNum
        ves_bay_inch40_num = obj.FotBayNum
        ves_eng_pos = obj.EngRomPos
        ves_eng_wid = obj.EngRomWid
        ves_mid_bay_deal_wit = obj.MidBayDeaWit
        ves_load_weight = obj.LoadWeigth
        ves_deck_cap_weight = obj.DeckCapWegt
        ves_cab_cap = obj.CabCap
        ves_deck_lay_num_max = obj.DeckLayNumMax
        ves_cab_lay_num_max = obj.CabLayNumMax
        ves_deck_col_num_max = obj.DeckColNumMax
        ves_cab_col_num_max = obj.CabColNumMax
        ves_bay_dir = vessel_voy_info.objects.get(Vessel=name).BerThgDir
        eng_body_list = create_engine_index(ves_eng_pos, ves_eng_wid)#?

        # min to max (down to up)
        ves_deck_lay_list = create_index_list(ves_deck_lay_num_max)
        ves_cab_lay_list = create_index_list(ves_cab_col_num_max)
        # TODO: vessel_info !
        data_content = {
            'dataType': ves_side_view,
            'bayDirection': ves_bay_dir,
            'vessel_name': ves_name,
            'vessel_width': ves_width,
            'vessel_frontLength': ves_front_length,
            'vessel_length': ves_length,
            'bay_inch20_num': ves_bay_inch20_num,
            'bay_inch40_num': ves_bay_inch40_num,
            'max_layer_above_number': ves_deck_lay_num_max,
            'max_layer_below_number': ves_cab_lay_num_max,
            'engine_room_index': eng_body_list,
            'mid_bay_deal': ves_mid_bay_deal_wit,
            'load_weight': ves_load_weight,
            'deck_capacity': ves_deck_cap_weight,
            'cabin_capacity': ves_cab_cap,
            'max_col_above_number': ves_deck_col_num_max,
            'max_col_below_number': ves_cab_col_num_max,
            'vessel': [

            ],
        }
        # printprint('\n'.join('{}: {}'.format(*k) for k in enumerate(data_content)))
        return JsonResponse(data_content)
    elif request.method == 'POST':
        return JsonResponse({'ves_struct': 'bbb'})


@csrf_exempt
def test_connect_to_db(request):
    if request.method == 'GET':
        return JsonResponse({'response': 'hhh'})
    elif request.method == 'POST':
        testV = {'hhh': 'connected'}
        return JsonResponse(testV)


@csrf_exempt
def get_con_pend_info(request):
    # TODO: update DB, CLEAR table: con_pend_info
    if request.method == 'GET':
        ves_name = request.GET['name']
        # Get From DB
        obj_bay_inch20 = ves_bay_struct.objects.filter(Vessel=ves_name, BaySiz='20')
        obj_temp_inch40 = ves_struct.objects.get(Vessel=ves_name)
        bay_inch20_list = sorted(index_to_num([item.BayNo for item in obj_bay_inch20]))
        if obj_temp_inch40.FotBayCom:
            bay_inch40_list = sorted(index_to_num(obj_temp_inch40.FotBayCom.split(",")))
        else:
            bay_inch40_list = []
        data_bay_list = combined_bay_list(bay_inch20_list, bay_inch40_list)
        bay_dir = vessel_voy_info.objects.get(Vessel=ves_name).BerThgDir
        # con_pending_data
        bay_inch20_pend_list = []
        bay_inch40_pend_list = []
        for bay_20_index in bay_inch20_list:
            index_bay = num_to_index(bay_20_index)
            obj = con_pend_info.objects.get(Vessel=ves_name, BayNo=index_bay)
            above_load = obj.DeckLodNum
            above_unload = obj.DeckUloNum
            below_load = obj.CabLoaNum
            below_unload = obj.CabUloNum
            bay_inch20_pend_list.append({
                'type': 'inch20',
                'index': index_bay,
                'data': {
                    'above_load': above_load,
                    'above_unload': above_unload,
                    'below_load': below_load,
                    'below_unload': below_unload,
                }
            })
        for bay_40_index in bay_inch40_list:
            index_bay = num_to_index(bay_40_index)
            obj = con_pend_info.objects.get(Vessel=ves_name, BayNo=index_bay)
            above_load = obj.DeckLodNum
            above_unload = obj.DeckUloNum
            below_load = obj.CabLoaNum
            below_unload = obj.CabUloNum
            bay_inch40_pend_list.append({
                'type': 'inch40',
                'index': index_bay,
                'data': {
                    'above_load': above_load,
                    'above_unload': above_unload,
                    'below_load': below_load,
                    'below_unload': below_unload,
                }
            })
        # engine_list
        obj = ves_struct.objects.get(Vessel=ves_name)
        engine_pos = obj.EngRomPos
        engine_width = obj.EngRomWid
        eng_body_list = create_engine_index(engine_pos, engine_width)
        data_content = {
            'dataType': con_pending_info,
            'vessel_IMO': "001",
            'vessel_name': ves_name,
            'bay_list': data_bay_list,
            'bayDirection': bay_dir,
            'data_list': {
                'inch20': bay_inch20_pend_list,
                'inch40': bay_inch40_pend_list,
            },
            'engineRoomIndex': eng_body_list,
        }
        return JsonResponse(data_content)


@csrf_exempt
def test_creat_pend_info(request):
    if request.method == 'GET':
        name = request.GET['name']
        obj_bay_inch20 = ves_bay_struct.objects.filter(Vessel=name,BaySiz='20')
        obj_temp_inch40 = ves_struct.objects.get(Vessel=name)
        bay_inch20_list = sorted(index_to_num([item.BayNo for item in obj_bay_inch20]))

        if obj_temp_inch40.FotBayCom:
            bay_inch40_list = sorted(index_to_num(obj_temp_inch40.FotBayCom.split(",")))
        else:
            bay_inch40_list = []
        data_bay_list = combined_bay_list(bay_inch20_list,bay_inch40_list)
        bay_dir = vessel_voy_info.objects.get(Vessel=name).BerThgDir

        context = {
            'dataType': 'EDIT_CONTAINER_PENDING_INFO',
            'vessel_IMO': "001",
            'vessel_name': name,
            'data': data_bay_list,
            'bayDirection': bay_dir,
        }
        return JsonResponse(context)

    elif request.method == 'POST':
        temp_lists = json.loads(request.body.decode('utf-8'))
        vessel_name = temp_lists['vessel_name']
        test = {'hhh': 'test_creat_pend_info'}
        unload_40_list = temp_lists['unload_40_list']
        unload_20_list = temp_lists['unload_20_list']
        load_40_list = temp_lists['load_40_list']
        load_20_list = temp_lists['load_20_list']
        for item in unload_40_list:
            index = item['index']
            num = item['num']
            obj = con_pend_info.objects.get(Vessel=vessel_name, BayNo=index)
        return JsonResponse(test)


@csrf_exempt
def add_vessel(request):
    if request.method == 'POST':
        content = json.loads(request.body.decode('utf-8'))
        ves_name = content['ves_name']
        ves_length = float(content['ves_len'])
        ves_width = float(content['ves_wid'])
        ves_front_length = float(content['ves_fr_len'])
        ves_bay_20_num = int(content['bay_20_num'])
        ves_eng_pos = int(content['eng_pos'])
        ves_eng_wid = int(content['eng_wid'])
        ves_deck_max_lay = int(content['deck_max_lay'])
        ves_cab_max_lay = int(content['cab_max_lay'])
        ves_deck_max_col = int(content['deck_max_col'])
        ves_cab_max_col = int(content['cab_max_col'])
        ves_imp_voy = content['ves_imp_voy']
        ves_exp_voy = content['ves_exp_voy']
        plan_ber_pos = content['plan_ber_pos']
        real_ber_pos = float(content['real_ber_pos'])
        ves_ber_dir = content['ves_ber_dir']

        # check if vessel_name exists
        try:
            obj = ves_struct.objects.get(Vessel=ves_name)
        except ves_struct.DoesNotExist:
            obj = None

        if obj is None:
            bay_index_list = bay_num_to_index_list(ves_bay_20_num)
            # add to DB
            ves_struct.objects.create(Vessel=ves_name,
                                      VesLeng=ves_length,
                                      VesWidth=ves_width,
                                      VesFrLeng=ves_front_length,
                                      TweBayNum=ves_bay_20_num,
                                      EngRomPos=ves_eng_pos,
                                      EngRomWid=ves_eng_wid,
                                      DeckLayNumMax=ves_deck_max_lay,
                                      CabLayNumMax=ves_cab_max_lay,
                                      DeckColNumMax=ves_deck_max_col,
                                      CabColNumMax=ves_cab_max_col)
            vessel_voy_info.objects.create(Vessel=ves_name,
                                           ImpVoy=ves_imp_voy,
                                           ExpVoy=ves_exp_voy,
                                           PlaBerThgPos=plan_ber_pos,
                                           ActBerPos=real_ber_pos,
                                           BerThgDir=ves_ber_dir)
            for i in bay_index_list:
                con_pend_info.objects.create(Vessel=ves_name,
                                             BayNo=i['index'])
                ves_bay_struct.objects.create(Vessel=ves_name,
                                              BayNo=i['index'],
                                              BaySiz=i['size'])
            return JsonResponse({'CREATE VESSEL': 'DONE!'})
        else:
            return JsonResponse({'WARNING': 'vessel_name is already exist'})


@csrf_exempt
def define_bay_struct(request):
    if request.method == 'GET':
        ves_name = request.GET['name']
        bay_index = request.GET['index']
        # get max
        obj1 = ves_struct.objects.get(Vessel=ves_name)
        deck_lay_num_max = obj1.DeckLayNumMax
        cab_lay_num_max = obj1.CabLayNumMax
        deck_col_num_max = obj1.DeckColNumMax
        cab_col_num_max = obj1.CabColNumMax
        # get real
        obj2 = ves_bay_struct.objects.filter(Vessel=ves_name,
                                             BayNo=bay_index)
        deck_lay_num_real = obj2[0].DeckHeg
        cab_lay_num_real = obj2[0].CabHeg
        deck_col_num_real = obj2[0].DeckWidMax
        cab_col_num_real = obj2[0].CabWidMax

        bay_layers = ves_bay_lay_struct.objects.filter(Vessel=ves_name,
                                                       BayNo=bay_index)
        bay_layer_con_zone = [
            {'layer_index': item.TireNo,
             'con_zone_list': db_layer_info_to_list(item.BayTieCtnLay),
            } for item in bay_layers]
        data = {
            'data_type': data_define_bay_struct,
            'ves_name': ves_name,
            'bay_index': bay_index,
            'bay_struct_max': {
                'deck_lay_num_max': deck_lay_num_max,
                'cab_lay_num_max': cab_lay_num_max,
                'deck_col_num_max': deck_col_num_max,
                'cab_col_num_max': cab_col_num_max,
            },
            'real_bay_struct': {
                'deck_lay_num_real': deck_lay_num_real,
                'cab_lay_num_real': cab_lay_num_real,
                'deck_col_num_real': deck_col_num_real,
                'cab_col_num_real': cab_col_num_real,
            },
            'bay_layer_con_zone': bay_layer_con_zone,
        }
        return JsonResponse(data)


@csrf_exempt
def operation_basic(request):
    if request.method == 'GET':
        all_vessel = [item.Vessel for item in vessel_voy_info.objects.all()]
        return render(request,
                      'OPERATION/operation.load.html',
                      {'all_vessel': all_vessel})


@csrf_exempt
def operation_load(request):
    if request.method == 'GET':
        ves_name = request.GET['name']
        bay_index = request.GET['index']
        # get max
        obj1 = ves_struct.objects.get(Vessel=ves_name)
        deck_lay_num_max = obj1.DeckLayNumMax
        cab_lay_num_max = obj1.CabLayNumMax
        deck_col_num_max = obj1.DeckColNumMax
        cab_col_num_max = obj1.CabColNumMax
        # get real
        obj2 = ves_bay_struct.objects.filter(Vessel=ves_name, BayNo=bay_index)
        deck_lay_num_real = obj2[0].DeckHeg
        cab_lay_num_real = obj2[0].CabHeg
        deck_col_num_real = obj2[0].DeckWidMax
        cab_col_num_real = obj2[0].CabWidMax

        bay_layers = ves_bay_lay_struct.objects.filter(Vessel=ves_name,
                                                       BayNo=bay_index)
        bay_layer_con_zone = [
            {'layer_index': item.TireNo,
             'con_zone_list': db_layer_info_to_list(item.BayTieCtnLay),
            } for item in bay_layers]
        # get vessel's stowage
        obj3s = con_stowage_export.objects.filter(Vessel=ves_name,
                                                 BayNo=bay_index)
        container_on_vessel = []
        for item in obj3s:
            container_on_vessel.append({
                'BayNo': item.BayNo,
                'ColNo': item.ColNo,
                'TireNo': item.TireNo,
                'CtnNo': item.CtnNo,
                'CtnTyp': item.CtnTyp,
                'Size': item.Size,
                'YardCel': item.YardCel,
                'VesCellNo': item.VesCellNo,
            })

        data = {
            'data_type': data_operation_load,
            'ves_name': ves_name,
            'bay_index': bay_index,
            'bay_struct_max': {
                'deck_lay_num_max': deck_lay_num_max,
                'cab_lay_num_max': cab_lay_num_max,
                'deck_col_num_max': deck_col_num_max,
                'cab_col_num_max': cab_col_num_max,
            },
            'real_bay_struct': {
                'deck_lay_num_real': deck_lay_num_real,
                'cab_lay_num_real': cab_lay_num_real,
                'deck_col_num_real': deck_col_num_real,
                'cab_col_num_real': cab_col_num_real,
            },
            'bay_layer_con_zone': bay_layer_con_zone,
            'con_on_vessel': container_on_vessel,
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ves_name = data['ves_name']
        con_loaded = data['loaded']
        print(ves_name)
        print(con_loaded)
        # get model from another app
        yard = apps.get_model('yardMon', 'yard')
        # add container into
        for con in con_loaded:
            obj1 = yard.objects.filter(YardCel=con['pos_yard'])
            CtnNo = obj1[0].CtnNo
            # StrLoaUnlSig = obj1[0].StrLoaUnlSig
            CtnTyp = obj1[0].CtnTyp
            # CtnWegt = obj1[0].CtnWegt
            UnloadPort = obj1[0].UnloadPort
            Size = obj1[0].Size
            # Owner = obj1[0].Owner
            # LoaVesTim = obj1[0].LoaVesTim

            # get bay col
            # add con info in stowage
            con_stowage_export.objects.create(Vessel=ves_name,
                                              CtnNo=CtnNo,
                                              CtnTyp=CtnTyp,
                                              # CtnWegt=CtnWegt,
                                              UnloadPort=UnloadPort,
                                              Size=Size,
                                              VesCellNo=con['pos_vessel'],
                                              BayNo=con['pos_vessel'][0:2],
                                              ColNo=con['pos_vessel'][2:4],
                                              TireNo=con['pos_vessel'][4:6],
                                              YardCel=con['pos_yard'])
        # delete container info in yard
        for item in con_loaded:
            yard.objects.filter(YardCel=item['pos_yard']).update(
                Status=None,
                CtnNo=None,
                StrLoaUnlSig=None,
                CtnTyp=None,
                CtnWegt=None,
                UnloadPort=None,
                Size=None,
                Owner=None,
                LoaVesTim=None,
                Color='wheat',
            )
        res = {'operation': 'done'}
        return JsonResponse(res)


@csrf_exempt
def stowage_info(request):
    if request.method == 'GET':
        ves_name = request.GET['name']
        
        print(ves_name)
        test = {'hhh':'stowage'}
        return JsonResponse(test)

# @csrf_exempt
# def operation_load_yard(request):
#     if request.method == 'POST':
@csrf_exempt
def all_bays_struct(request):
    if request.method == 'GET':
        ves_name = request.GET['name']
        # get max of all from ves_struct
        obj1 = ves_struct.objects.get(Vessel=ves_name)
        ves_bay_20_num = obj1.TweBayNum
        deck_lay_num_max = obj1.DeckLayNumMax
        cab_lay_num_max = obj1.CabLayNumMax
        deck_col_num_max = obj1.DeckColNumMax
        cab_col_num_max = obj1.CabColNumMax

        bay_index_list = bay20_num_index_list(ves_bay_20_num)
        content = []
        for bay_index in bay_index_list:
            # get real
            obj2 = ves_bay_struct.objects.filter(Vessel=ves_name,
                                                 BayNo=bay_index)
            deck_lay_num_real = obj2[0].DeckHeg
            cab_lay_num_real = obj2[0].CabHeg
            deck_col_num_real = obj2[0].DeckWidMax
            cab_col_num_real = obj2[0].CabWidMax
            bay_layers = ves_bay_lay_struct.objects.filter(Vessel=ves_name,
                                                           BayNo=bay_index)
            bay_layer_con_zone = [
                {'layer_index': item.TireNo,
                 'con_zone_list': db_layer_info_to_list(item.BayTieCtnLay),
                 } for item in bay_layers]
            content.append({
                'bay_index': bay_index,
                'bay_struct_max': {
                    'deck_lay_num_max': deck_lay_num_max,
                    'cab_lay_num_max': cab_lay_num_max,
                    'deck_col_num_max': deck_col_num_max,
                    'cab_col_num_max': cab_col_num_max,
                },
                'real_bay_struct': {
                    'deck_lay_num_real': deck_lay_num_real,
                    'cab_lay_num_real': cab_lay_num_real,
                    'deck_col_num_real': deck_col_num_real,
                    'cab_col_num_real': cab_col_num_real,
                },
                'bay_layer_con_zone': bay_layer_con_zone,
            })
        data = {
            'data_type': all_bays_struct_info,
            'ves_name': ves_name,
            'content': content,
        }
        return JsonResponse(data)
