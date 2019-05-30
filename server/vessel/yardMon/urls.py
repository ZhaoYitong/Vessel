from django.urls import path
from . import views


urlpatterns = [
    path('yardMon/yard_layout/', views.yard_layout, name='yard_layout'),
    path('yard/operation/load/', views.operation_load, name='operation_load'),
]