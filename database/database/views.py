from django.template import loader

from django.db.models import Q

from django.shortcuts import get_object_or_404, render, redirect

import csv

from .models import User, Status_data, Directory, File ,File_section, Section_category, Section_status, FramaOutput, Group_project, Group_task

import datetime

from django.http import JsonResponse

import json

from django.core import serializers

from django.utils import timezone

import pika

def add_to_queue(coowner_name, project_name, date):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='rabbit')

    content = str(coowner_name) + '~' + str(project_name) + '~' + str(date)

    channel.basic_publish(exchange='', routing_key='rabbit', body=content)
    print(content)
    connection.close()

def add_group_task(request):
    if request.method == 'POST':
        print(request.POST)
        description = request.POST.get('optional_description')
        project_name = request.POST.get('directory_name')
        name = request.POST.get('filename')
        post = Group_task()
        post.name = name
        post.project_name = project_name
        post.optional_description = description
        post.validity_flag = True
        post.pub_date = datetime.datetime.now()
        post.save()
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)

def delete_task(request, id):
    file = Group_task.objects.order_by('-pub_date').get(id=id)
    file.validity_flag = False
    file.save()
    return JsonResponse(True, status=200, safe=False)
    

def get_group_tasks(request):
    if request.method == 'GET':
        files = Group_task.objects.order_by('-pub_date').filter(validity_flag=True)
        print(serializers.serialize('json', files))
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)  

def delete_group_project(request, id):
    dir = Group_project.objects.order_by('-pub_date').get(id=id)
    dir.validity_flag = False
    dir.save()
    files = Group_task.objects.order_by('-pub_date').filter(project_name=dir.name)
    for file in files:
        file.validity_flag = False
        file.save()
    return JsonResponse({}, status=200)

def get_task(request, id, task_id):
    if request.method == 'GET':
        files = Group_task.objects.order_by('-pub_date').filter(id=task_id)
        print(files)
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)  

def get_project(request, id):
    if request.method == 'GET':
        dir = Group_project.objects.order_by('-pub_date').filter(id=id)
        print(dir)
        files = Group_task.objects.order_by('-pub_date').filter(project_name=dir[0].name)
        files = files.filter(validity_flag=True)
        print(files)
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)

def get_group_projects(request, login):
    if request.method == 'GET':
        files = Group_project.objects.order_by('-pub_date').filter(Q(owner=login) | Q(coowner = login))
        files = files.filter(validity_flag=True)
        print(files)
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)
        

def make_group_project(request):
    if request.method == 'POST':
        coowner = request.POST.get('cooperator')
        description = request.POST.get('optional_description')
        owner = request.POST.get('owner')
        name = request.POST.get('filename')
        post = Group_project()
        post.coowner = coowner
        post.owner = owner
        post.name = name
        post.optional_description = description
        post.validity_flag = True
        post.pub_date = datetime.datetime.now()
        post.save()
        print(post)
        add_to_queue(coowner, name, post.pub_date)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)

def get_json_data(request, login):
    if request.method == 'GET':
        files = Directory.objects.filter(owner=login, validity_flag=True).order_by('-creation_date')
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)
        
def get_json_data_files(request, login):
    if request.method == 'GET':
        files = File.objects.filter(owner=login, validity_flag=True).order_by('-creation_date')
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)
        
def get_json_data_directory(request, dir_id):
    if request.method == 'GET':
        files = File.objects.order_by('-creation_date')
        this_directory = Directory.objects.order_by('-creation_date').get(id=dir_id)
        dir_name = this_directory.name
        files = files.filter(directory_name=dir_name)
        files = files.filter(validity_flag=True)
        print(files)
        return JsonResponse(serializers.serialize('json', files), status=200, safe=False)
        
    else:
        return JsonResponse({}, status=400)
        
        
def get_json_data_file(request, dir_id, file_id):
    if request.method == 'GET':
        latest_files_list = File.objects.order_by('-creation_date')
        this_directory = Directory.objects.order_by('-creation_date').get(id=dir_id)
        dir_name = this_directory.name
        
        file = latest_files_list.filter(id=file_id)
        
        return JsonResponse(serializers.serialize('json', file), status=200, safe=False)
    
def login_terminate(request):
    if request.POST.get('login') and request.POST.get('password'):
        login = request.POST.get('login')
        password = request.POST.get('password')
        query = User.objects.filter(login=login, password=password)
        if query:
            print('smiga')
            return JsonResponse({}, status=200, safe=False)
    
    
    return JsonResponse({}, status=403, safe=False)
    
    
def register_terminate(request):
    if request.POST.get('login') and request.POST.get('password') and request.POST.get('password_again'):
        login = request.POST.get('login')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')
        if password != password_again:
            return JsonResponse({}, status=403, safe=False)
        query = User.objects.filter(login=login)
        print(query)
        if query:
            return JsonResponse({}, status=403, safe=False)
        post = User()
        post.login = login
        post.password = password
        post.validity_flag = True
        post.name = login
        post.pub_date = datetime.datetime.now()
        post.save()
        return JsonResponse({}, status=200, safe=False)

    return JsonResponse({}, status=403, safe=False)
    
def add_file_acc(request):
    if  not 'login' in request.session:
        request.session['login'] = False
    if  not 'Unhide' in request.session:
        request.session['Unhide'] = True
    if request.method == 'POST':
        if request.POST.get('directory_name') and request.POST.get('optional_description') and request.POST.get('filename'):
            post = File()
            post.directory_name = request.POST.get('directory_name')
            post.optional_description = request.POST.get('optional_description')
            post.creation_date = datetime.datetime.now()
            post.owner = request.POST.get('owner')
            post.filepath = ""
            post.name = request.POST.get('filename')
            post.validity_flag = True
            post.save()

    return JsonResponse({}, status=200)
    
def delete_file_number(request, file_id):
    if  not 'login' in request.session:
        request.session['login'] = False
    if  not 'Unhide' in request.session:
        request.session['Unhide'] = True
    latest_files_list = File.objects.order_by('-creation_date')
    file_to_delete = latest_files_list.get(id=file_id)
    file_to_delete.validity_flag = False
    file_to_delete.save()
    
    return JsonResponse({}, status=200)
    
    
def delete_directory_number(request, directory_id):
    dir_to_delete = Directory.objects.get(id=directory_id)
    dir_to_delete.validity_flag = False
    dir_to_delete.save()
    
    latest_files_list = File.objects.order_by('-creation_date')
    this_directory = Directory.objects.order_by('-creation_date').get(id=directory_id)
    dir_name = this_directory.name
    files_to_show = latest_files_list.filter(directory_name=dir_name)
    for f in files_to_show:
        f.validity_flag = False
        f.save()
        
    return JsonResponse({}, status=200)
    
def add_directory_acc(request):
    if request.method == 'POST':
        if request.POST.get('directory_name') and not Directory.objects.filter(name=request.POST.get('directory_name')):
            post = Directory()
            post.name = request.POST.get('directory_name')
            post.optional_description = ""
            post.owner = request.POST.get('owner')
            post.creation_date = datetime.datetime.now()
            post.validity_flag = True
            dirname = post.name
            post.save()
            
    return JsonResponse({}, status=200)
    
