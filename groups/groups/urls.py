from django.urls import path

from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'groups'
urlpatterns = [
    path('make_group_project/', views.make_group_project, name='make_group_project'),
    path('get_group_projects/<slug:login>/', views.get_group_projects, name='get_group_projects'),
    path('get_project/<int:id>/', views.get_project, name='get_project'),
    path('get_task/<int:id>/<int:task_id>/', views.get_task, name='get_task'),
    path('delete_group_project/<int:id>/', views.delete_group_project, name='delete_group_project'),
    path('get_group_tasks/', views.get_group_tasks, name='get_group_tasks'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('add_group_task/', views.add_group_task, name='add_group_task'),
]