from django.urls import path

from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_file_acc/', views.add_file_acc, name='add_file_acc'),
    path('add_directory_acc/', views.add_directory_acc, name='add_directory_acc'),
    path('delete_directory/<int:directory_id>/', views.delete_directory_number, name='delete_directory_number'),
    path('delete_file/<int:file_id>/', views.delete_file_number, name='delete_file_number'),
    path('login/', views.login, name='login'),
    path('login/terminate/', views.login_terminate, name='login_terminate'),
    path('register/', views.register, name='register'),
    path('register/terminate/', views.register_terminate, name='register_terminate'),
    path('logout/', views.logout, name='logout'), 
    path('get_json_data/', views.get_json_data, name='get_json_data'),
    path('get_json_data/files/', views.get_json_data_files, name='get_json_data_files'),
    path('get_json_data/<int:dir_id>/', views.get_json_data_directory, name='get_json_data_directory'),
    path('get_json_data/<int:dir_id>/<int:file_id>/', views.get_json_data_file, name='get_json_data_file'),
    path('make_group_project/', views.make_group_project, name='make_group_project'),
    path('get_group_projects/', views.get_group_projects, name='get_group_projects'),
    path('get_project/<int:id>/', views.get_project, name='get_project'),
    path('get_task/<int:id>/<int:task_id>/', views.get_task, name='get_task'),
    path('delete_group_project/<int:id>/', views.delete_group_project, name='delete_group_project'),
    path('get_group_tasks/', views.get_group_tasks, name='get_group_tasks'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('add_group_task/', views.add_group_task, name='add_group_task'),
    path('notification/', views.notification, name='notification'),
]