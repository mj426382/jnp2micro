from django.urls import path

from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'users'
urlpatterns = [
    path('add_file_acc/', views.add_file_acc, name='add_file_acc'),
    path('add_directory_acc/', views.add_directory_acc, name='add_directory_acc'),
    path('delete_directory/<int:directory_id>/', views.delete_directory_number, name='delete_directory_number'),
    path('delete_file/<int:file_id>/', views.delete_file_number, name='delete_file_number'),
    path('login_terminate/', views.login_terminate, name='login_terminate'),
    path('register_terminate/', views.register_terminate, name='register_terminate'),
    path('get_json_data/<slug:login>/', views.get_json_data, name='get_json_data'),
    path('get_json_data_files/<slug:login>/', views.get_json_data_files, name='get_json_data_files'),
    path('get_json_data_directory/<int:dir_id>/', views.get_json_data_directory, name='get_json_data_directory'),
    path('get_json_data_file/<int:dir_id>/<int:file_id>/', views.get_json_data_file, name='get_json_data_file'),
]