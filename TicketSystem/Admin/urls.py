from django.urls import path
from . views import *

urlpatterns = [
    path('admin_login',admin_login,name='admin_login'),
    path('create_department',create_department,name='create_department'),
    path('get_all_departments',get_all_departments,name='get_all_departments'),
    path('update_department/<int:id>',update_department,name='update_department'),
    path('get_department/<int:id>',get_department,name='get_department'),
    path('departments',department_list,name='department_list'),
    path('delete_department/<int:id>',delete_department,name='delete_department'),
    path('create_user',create_user,name='create_user'),
    path('get_all_tickets',get_all_tickets,name='get_all_tickets')
]
