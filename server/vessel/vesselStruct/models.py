from django.db import models
from django.utils.timezone import now
# TODO: 升级并统一字符长度类型， 模块方式导入
# length setting
# short: 10
# middle: 50
# big: 100
# supper: 500
# supsuper: 1000
# TODO: SET PRIMARY KEY AND FOREIGN KEY
# TODO: choices in mysql


# 船舶航次信息
class vessel_voy_info(models.Model):
    
    TASK_FIN_SIG_CHOICES = (
        ('1', '正在卸船（未装船）'),
        ('2', '正在装船（未卸船）'),
        ('3', '正在装卸船(两者同时开展)'),
        ('4', '卸船完成，正在装船'),
        ('5', '装卸船都完成'),
    )

    UNB_STATUS_CHOICES = (
        ('1', '装卸船已经完成，正在离泊准备'),
        ('2', '正在离泊作业'),
        ('3', '离泊完成')
    )

    Vessel = models.CharField(max_length=50, verbose_name='船名') #
    ImpVoy = models.CharField(max_length=50, verbose_name='进口航次') #
    ExpVoy = models.CharField(max_length=50, verbose_name='出口航次') #
    VesType = models.CharField(null=True, blank=True, max_length=50, verbose_name='船型')
    PlaBerThgTim = models.DateTimeField(verbose_name='计划靠泊', default=now) #
    PlaUnbThgTim = models.DateTimeField(verbose_name='计划离泊', default=now)#
    ReaBerThgTim = models.DateTimeField(verbose_name='实际靠泊（时间）', default=now)#
    ActUnbTim = models.DateTimeField(null=True, blank=True, verbose_name='实际离泊', default=now)
    PlaBerThgPos = models.CharField(max_length=50, verbose_name='计划靠泊位置')#
    ActBerPos = models.FloatField(verbose_name='实际靠泊位置')#
    BerThgDir = models.CharField(max_length=50, verbose_name='靠泊方向')#
    VesDrauMax = models.FloatField(null=True, blank=True, verbose_name='进出最大吃水')
    PlaClosCustTim = models.DateTimeField(null=True, blank=True, verbose_name='计划截关时间', default=now)
    ClosCustTim = models.DateTimeField(null=True, blank=True, verbose_name='截关时间', default=now)
    OpAssSign = models.CharField(null=True, blank=True, max_length=50, verbose_name='已安排作业', default='hh')
    EntPlanMakSig = models.CharField(null=True, blank=True, max_length=50, verbose_name='已安排集港', default='jj')
    TaskFiniSig = models.CharField(null=True, blank=True, max_length=10,
                                   choices=TASK_FIN_SIG_CHOICES, verbose_name='作业完成情况', default='1')
    UnBSta = models.CharField(null=True, blank=True, max_length=10,
                              choices=UNB_STATUS_CHOICES, verbose_name='离泊情况', default='1')
    PlaLoaDraCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划进危20')
    PlaUloDraCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划出危20')
    PlaLoaEmpCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划进空20')
    PlaUloEmpCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划出空20')
    PlaLoaGPCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划进重20')
    PlaUloGPCtnTweNum = models.IntegerField(null=True, blank=True, verbose_name='计划出重20')
    PlaLoaGPCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划进重40')
    PlaLoaEmpCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划进空40')
    PlaLoaDraCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划进危40')
    PlaLoaGPCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划进重45')
    PlaLoaEmpCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划进空45')
    PlaLoaDraCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划进危45')
    PlaUloGPCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划出重40')
    PlaUloEmpCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划出空40')
    PlaUloDraCtnFotNum = models.IntegerField(null=True, blank=True, verbose_name='计划出危40')
    PlaUloGPCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划出重45')
    PlaUloEmpCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划出空45')
    PlaUloDraCtnFotFivNum = models.IntegerField(null=True, blank=True, verbose_name='计划出危45')


# 船舶结构（针对某一船舶型号）
class ves_struct(models.Model):

    DANGER_CON_ALLOW_CHOICES = (
        ('1', '允许'),
        ('0', '不允许'),
    )
    Vessel = models.CharField(max_length=50, verbose_name='船名')
    VesLeng = models.FloatField(verbose_name='船长') #
    VesWidth = models.FloatField(verbose_name='船舶宽度') #
    VesFrLeng = models.FloatField(verbose_name='船首长度（米）') #
    TweBayNum = models.IntegerField(verbose_name='20尺贝数') #
    FotBayNum = models.IntegerField(null=True, blank=True, verbose_name='40尺贝数')
    FotBayCom = models.CharField(null=True, blank=True, max_length=500, verbose_name='40组贝')
    EngRomPos = models.IntegerField(verbose_name='机舱位置') #
    EngRomWid = models.IntegerField(verbose_name='机舱宽度') #
    MidBayDeaWit = models.BooleanField(null=True, blank=True, verbose_name='中间贝处理')  # set to 00 ? true:false
    RefCtnCap = models.FloatField(null=True, blank=True, verbose_name='冷冻容量')
    VesEntBerSpd = models.FloatField(null=True, blank=True, verbose_name='船舶进港速度')
    VesBerSpd = models.FloatField(null=True, blank=True, verbose_name='船舶靠泊速度')
    HigCtnCap = models.FloatField(null=True, blank=True, verbose_name='高箱容量')
    CapCtnFotFiv = models.FloatField(null=True, blank=True, verbose_name='45尺容量')
    VesEmpGrvHeg = models.CharField(null=True, blank=True, max_length=50, verbose_name='空船重心高')
    VesAtt = models.CharField(null=True, blank=True, max_length=50, verbose_name='全隔槽？')
    LoadWeigth = models.FloatField(null=True, blank=True, verbose_name='载重量')
    DeckCapWegt = models.FloatField(null=True, blank=True, verbose_name='甲板容量T')
    CabCap = models.FloatField(null=True, blank=True, verbose_name='舱内容量T')
    DanCtnAlw = models.CharField(null=True, blank=True, max_length=10, verbose_name='允装危险品')
    DeckLayNumMax = models.IntegerField(verbose_name='甲板最大层高') #
    CabLayNumMax = models.IntegerField(verbose_name='舱内最大层深') #
    DeckColNumMax = models.IntegerField(verbose_name='甲板最大列数') #
    CabColNumMax = models.IntegerField(verbose_name='舱内最大列数') #


# 船舶贝位结构
class ves_bay_struct(models.Model):

    BAY_COM_CHOICES = (
        ('0', '不组贝'),
        ('1', '向右组贝'),
        ('2', '向左组贝'),
    )

    HAT_COVER_CHOICES = (
        ('0', '自开式'),
        ('1', '数目1'),
        ('2', '数目2'),
        ('3', '数目3'),
        ('4', '数目4'),
    )

    MID_BAY_DEAL_WIT_CHOICES = (
        ('0', '00行'),
        ('1', '非00行'),
    )
    Vessel = models.CharField(max_length=50, verbose_name='船名')
    BayNo = models.CharField(max_length=50, verbose_name='贝号')
    BaySiz = models.CharField(null=True, blank=True, max_length=50, verbose_name='贝尺寸')
    BayCom = models.CharField(null=True, blank=True, max_length=10,
                              choices=BAY_COM_CHOICES, default='0', verbose_name='贝组')
    DeckHeg = models.IntegerField(null=True, blank=True, verbose_name='甲板层高')
    DeckWidMax = models.IntegerField(null=True, blank=True, verbose_name='甲板最宽')
    CabHeg = models.IntegerField(null=True, blank=True, verbose_name='舱内层高')
    CabWidMax = models.IntegerField(null=True, blank=True, verbose_name='舱内最宽')
    HatCovKind = models.CharField(max_length=10, choices=HAT_COVER_CHOICES,
                                  default='0', verbose_name='舱盖板类型')  # choice
    HatCovPos = models.CharField(max_length=50, verbose_name='舱盖板明细')
    BayX = models.IntegerField(null=True, blank=True, verbose_name='贝X坐标')
    BayY = models.IntegerField(null=True, blank=True, verbose_name='贝Y坐标')
    MidBayDeaWit = models.CharField(null=True, blank=True, max_length=10,
                                    choices=MID_BAY_DEAL_WIT_CHOICES, verbose_name='中间贝处理')


# 船舶贝位层信息
class ves_bay_lay_struct(models.Model):

    DECK_CAG_SIG_CHOICES = (
        ('0', '甲板'),
        ('1', '舱内'),
    )

    Vessel = models.CharField(max_length=50, verbose_name='船名')
    BayNo = models.CharField(max_length=10, verbose_name='贝号')
    TireNo = models.CharField(max_length=100, verbose_name='层号')
    DeckCagSig = models.CharField(max_length=10, verbose_name='甲板or舱内')  # choice
    BayWid = models.IntegerField(verbose_name='宽度')
    BayTieCtnLay = models.CharField(max_length=50, verbose_name='层箱位分布')
    BayHigh = models.IntegerField(null=True, blank=True, verbose_name='离底层(该层层号)')
    CellSpeSig = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱位特标')
    RefSig = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱位冷冻标')


# add container distritube info
# 待作业集装箱信息（基于配载信息）
class con_pend_info(models.Model):
    HAT_COVER_CHOICES = (
        ('0', '自开式'),
        ('1', '数目1'),
        ('2', '数目2'),
        ('3', '数目3'),
        ('4', '数目4'),
    )

    Vessel = models.CharField(max_length=50, verbose_name='船名')
    BayNo = models.CharField(max_length=50, verbose_name='贝号')
    DeckLodNum = models.IntegerField(null=True, blank=True, verbose_name='甲板装数')
    DeckUloNum = models.IntegerField(null=True, blank=True, verbose_name='甲板卸数')
    CabLoaNum = models.IntegerField(null=True, blank=True, verbose_name='舱内装数')
    CabUloNum = models.IntegerField(null=True, blank=True, verbose_name='舱内卸数')
    HatCovKind = models.CharField(null=True, blank=True, max_length=10, choices=HAT_COVER_CHOICES,
                                  default='0', verbose_name='舱盖板类型')  # choice


# 岸桥信息
class qc_info(models.Model):
    QC_STAT_CHOICES = (
        ('0', '空闲'),
        ('1', '忙碌'),
        ('2', '维护'),
    )

    QCNo = models.CharField(max_length=10, verbose_name='岸桥编号')
    QcOpLengFr = models.FloatField(verbose_name='外伸作业距')
    QcHeg = models.FloatField(verbose_name='岸桥高度')
    QcOpHeg = models.FloatField(verbose_name='作业高度')
    QcPos = models.FloatField(verbose_name='岸桥位置')
    QCSta = models.CharField(max_length=10, choices=QC_STAT_CHOICES, verbose_name='岸桥状态')
    OpVes = models.CharField(null=True, blank=True, max_length=50, verbose_name='作业船舶')
    NowOpVesCel = models.CharField(null=True, blank=True, max_length=50, verbose_name='当前作业船箱位')
    QcNoLeft = models.CharField(null=True, blank=True, max_length=50, verbose_name='左侧岸桥编号')
    QcNoRight = models.CharField(null=True, blank=True, max_length=50, verbose_name='右侧岸桥编号')
    QCEffMovPeH = models.IntegerField(null=True, blank=True, verbose_name='岸吊作业效率') # con/h
    PlaQcMtnFiniTim = models.DateTimeField(null=True, blank=True, verbose_name='岸吊预期修复时间')  # timeStamp


# 岸桥调度计划输出
class qc_dis_plan_out(models.Model):
    TASK_CLU_KIND_CHOICES = PRE_TASK_CLU_KIND_CHOICES = (
        ('1', '表示甲板卸'),
        ('2', '表示卸舱盖板'),
        ('3', '表示舱内卸'),
        ('4', '表示舱内装'),
        ('5', '表示装舱盖板'),
        ('6', '表示甲板装'),
    )

    QCNo = models.CharField(max_length=10, verbose_name='岸桥编号')
    TaskCluVes = models.CharField(max_length=50, verbose_name='作业船舶')
    TaskCluBay = models.CharField(max_length=10, verbose_name='作业贝位')
    BayInnTaskCluNo = models.CharField(null=True, blank=True,
                                       max_length=1000, verbose_name='作业贝位内任务簇编号(贝位作业的再划分)')
    TaskCluKind = models.CharField(max_length=3, choices=TASK_CLU_KIND_CHOICES, verbose_name='作业类别')  # choices
    PreTaskCluVes = models.CharField(null=True, blank=True, max_length=50, verbose_name='紧前作业船舶')
    PreTaskCluBay = models.CharField(null=True, blank=True, max_length=50, verbose_name='紧前作业贝位')
    PreBayInnTaskCluNo = models.CharField(null=True, blank=True,
                                          max_length=1000, verbose_name='紧前作业贝位内任务簇编号')
    PreTaskCluKind = models.CharField(null=True, blank=True, max_length=3,
                                      choices=PRE_TASK_CLU_KIND_CHOICES, verbose_name='作业紧前类别')  # choices
    TaskCluEstBegTim = models.DateTimeField(verbose_name='作业开始时间（估计）')
    TaskCluEstEndtim = models.DateTimeField(verbose_name='作业结束时间（估计） ')
    ModPlanKind = models.CharField(null=True, blank=True, max_length=50, verbose_name='模型计划类型')
    EffFactr = models.CharField(null=True, blank=True, max_length=500, verbose_name='影响因素')
    ModFud = models.CharField(null=True, blank=True, max_length=500, verbose_name='模型基础')
    ModObj = models.CharField(null=True, blank=True, max_length=500, verbose_name='模型目标')
    ModCons = models.CharField(null=True, blank=True, max_length=500, verbose_name='模型约束')


# abandone !!!!
# 船舶积载（进口箱的积载）
class con_stowage_import(models.Model):
    Vessel = models.CharField(null=True, blank=True, max_length=50, verbose_name='船名')
    Voyage = models.CharField(null=True, blank=True, max_length=50, verbose_name='航次')
    VesCellNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='船箱位')
    # TODO: ColNo is tinyint?
    ColNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='列号') # tinyint
    DeckCagSig = models.CharField(null=True, blank=True, max_length=50, verbose_name='甲板or舱内')
    CtnNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱号')
    CtnTyp = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱型')
    Size = models.CharField(null=True, blank=True, max_length=50, verbose_name='尺寸')
    Status = models.CharField(null=True, blank=True, max_length=50, verbose_name='状态')
    CtnWegt = models.FloatField(null=True, blank=True, verbose_name='箱重')
    Owner = models.CharField(null=True, blank=True, max_length=50, verbose_name='持箱人')
    GForce = models.CharField(null=True, blank=True, max_length=1000, verbose_name='货特要求')
    StaPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='起运港')
    UnloadPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='卸货港')
    DesPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='目的港')
    StrPickAwayCtn = models.CharField(null=True, blank=True, max_length=50, verbose_name='直提箱')
    CtnOpeSta = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱作业状态')
    PlaCtnCel = models.CharField(null=True, blank=True, max_length=50, verbose_name='计划箱位')


# 出口箱配载计划
class con_stowage_export(models.Model):
    Vessel = models.CharField(null=True, blank=True, max_length=50, verbose_name='船名')
    Voyage = models.CharField(null=True, blank=True, max_length=50, verbose_name='航次')
    VesCellNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='船箱位')
    # TODO: ColNo is tinyint?
    BayNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='贝号')
    ColNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='列号') # tinyint
    TireNo = models.CharField(null=True, blank=True, max_length=100, verbose_name='层号')
    DeckCagSig = models.CharField(null=True, blank=True, max_length=50, verbose_name='甲板or舱内')
    CtnNo = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱号')
    CtnTyp = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱型')
    Size = models.CharField(null=True, blank=True, max_length=50, verbose_name='尺寸')
    Status = models.CharField(null=True, blank=True, max_length=50, verbose_name='状态')
    CtnWegt = models.FloatField(null=True, blank=True, verbose_name='箱重')
    GForce = models.CharField(null=True, blank=True, max_length=1000, verbose_name='货特要求')
    StaPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='起运港')
    UnloadPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='卸货港')
    DesPort = models.CharField(null=True, blank=True, max_length=50, verbose_name='目的港')
    CtnOpeSta = models.CharField(null=True, blank=True, max_length=50, verbose_name='箱作业状态')
    YardCel = models.CharField(null=True, blank=True, max_length=50, verbose_name='堆场箱位')
