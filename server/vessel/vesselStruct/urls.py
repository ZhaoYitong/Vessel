from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('default_page/', views.default_page_iframe, name='default_page_iframe'),
    path('vesselStruct/ves_basic/', views.ves_basic, name='ves_basic'),
    path('vesselStruct/page_not_found/', views.page_not_found, name='page_not_found'),
    path('vesselStruct/add_vessel_page/', views.add_vessel_page, name='add_vessel_page'),
    path('vesselStruct/bay_struct_define/', views.bay_struct_define, name='bay_struct_define'),
    path('vesselStruct/edit_bay/', views.edit_bay, name='edit_bay'),
    path('vesselStruct/reset_bay_combine/', views.reset_bay_combine, name='reset_bay_combine'),
    path('vesselStruct/ves_struct/', views.create_ves_struct, name='create_ves_struct'),
    path('vesselStruct/con_pend_info/', views.get_con_pend_info, name='get_con_pend_info'),
    path('vesselStruct/test_connect_to_db/', views.test_connect_to_db, name='test_connect_to_db'),
    path('vesselStruct/test_creat_pend_info/', views.test_creat_pend_info, name='test_creat_pend_info'),
    path('vesselStruct/add_vessel/', views.add_vessel, name='add_vessel'),
    path('vesselStruct/define_bay_struct/', views.define_bay_struct, name='define_bay_struct'),
    path('vesselStruct/operation_basic/', views.operation_basic, name='operation_basic'),
    path('vesselStruct/operation_load/', views.operation_load, name='operation_load'),
    path('vesselStruct/stowage_info/', views.stowage_info, name='stowage_info'),
    path('vesselStruct/all_bays_struct/', views.all_bays_struct, name='all_bays_struct'),
]