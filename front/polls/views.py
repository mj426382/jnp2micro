from django.template import loader

from django.http import Http404

from django.db.models import Q

from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect

import csv

from django.urls import reverse

from .models import User, Status_data, Directory, File ,File_section, Section_category, Section_status, FramaOutput, Group_project, Group_task

import os

import datetime

import subprocess

from django.http import JsonResponse

import json

from django.core import serializers

from django.utils import timezone

import requests

notif = False

coowner_project = False

def notification(request):
    if request.method == 'POST':
        print(request.POST)
        coowner = request.POST['coowner']
        project_name = request.POST['project_name']
        date = request.POST['date']
        print(coowner)
        global coowner_project
        coowner_project = coowner
        global notif
        notif = 'new project:' + str(project_name) + ' made in ' + str(date)
        print('bleee' + str(notif))
        
        return JsonResponse({}, status=200);
    else:
        return JsonResponse({}, status=400);

def add_group_task(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'optional_description': request.POST.get('optional_description'),
            'directory_name': request.POST.get('directory_name'),
            'filename': request.POST.get('filename')
        }
        response = requests.post('http://127.0.0.1:2300/groups/add_group_task/',data=json_data)
        return redirect('/polls/')
    else:
        return JsonResponse({}, status=400);

def delete_task(request, id):
    response = requests.get('http://127.0.0.1:2300/groups/delete_task/' + str(id) + '/')
    print(response.content)
    return redirect('/polls/')
    

def get_group_tasks(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2300/groups/get_group_tasks')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)  

def delete_group_project(request, id):
    response = requests.get('http://127.0.0.1:2300/groups/delete_group_project/' + str(id) + '/')
    return redirect('/polls/')

def get_task(request, id, task_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2300/groups/get_task/' + str(id) + '/' + str(task_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)

    else:
        return JsonResponse({}, status=400)

def get_project(request, id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2300/groups/get_project/' + str(id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400) 

def get_group_projects(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2300/groups/get_group_projects/' + str(request.session['login']) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)  
        

def make_group_project(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'cooperator': request.POST.get('cooperator'),
            'optional_description': request.POST.get('optional_description'),
            'owner': request.session.get('login'),
            'filename': request.POST.get('filename')
        }
        response = requests.post('http://127.0.0.1:2300/groups/make_group_project/',data=json_data)
        return redirect('/polls/')
    else:
        return JsonResponse({}, status=400);

def get_json_data(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/get_json_data/' + request.session['login'] + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400) 
        
def get_json_data_files(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/get_json_data_files/' + request.session['login'] + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400) 
        
def get_json_data_directory(request, dir_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/get_json_data_directory/' + str(dir_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400) 
        
        
def get_json_data_file(request, dir_id, file_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/get_json_data_file/' + str(dir_id) + '/' + str(file_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)    

def add_file_acc(request):
    if  not 'login' in request.session:
        request.session['login'] = False
    if  not 'Unhide' in request.session:
        request.session['Unhide'] = True
    if request.method == 'POST':
        if request.POST.get('directory_name') and request.POST.get('optional_description') and request.POST.get('filename'):
            json_data = {
                'directory_name': request.POST.get('directory_name'),
                'optional_description': request.POST.get('optional_description'),
                'owner': request.session['login'],
                'filename': request.POST.get('filename')
            }
            response = requests.post('http://127.0.0.1:2200/users/add_file_acc/',data=json_data)
    
    return redirect('/polls/')
    
    
def delete_file_number(request, file_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/delete_file/' + str(file_id) + '/')
        return redirect('/polls/')
    else:
        return JsonResponse({}, status=400)    

    
    
def delete_directory_number(request, directory_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2200/users/delete_directory/' + str(directory_id) + '/')
        return redirect('/polls/')
    else:
        return JsonResponse({}, status=400)    
    
    
def add_directory_acc(request):
    if  not 'login' in request.session:
        request.session['login'] = False
    if  not 'Unhide' in request.session:
        request.session['Unhide'] = True
    if request.method == 'POST':
        if request.POST.get('directory_name'):
            json_data = {
                'directory_name': request.POST.get('directory_name'),
                'owner': request.session['login']
            }
            response = requests.post('http://127.0.0.1:2200/users/add_directory_acc/',data=json_data)
    
    return redirect('/polls/')
    
def login(request):
    context = {}
    return render(request, 'polls/login.html', context)
    
def login_terminate(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'login': request.POST.get('login'),
            'password': request.POST.get('password')
        }
        response = requests.post('http://127.0.0.1:2200/users/login_terminate/',data=json_data)
        print(response)
        if response.status_code == 200:
            request.session['login'] = request.POST.get('login')
            return redirect('/polls/')
    
    context = {'login_error': 'Incorrect login or password'}
    return render(request, 'polls/login.html', context)
    
    
def register(request):
    context = {}
    return render(request, 'polls/register.html', context)
    
def register_terminate(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'login': request.POST.get('login'),
            'password': request.POST.get('password'),
            'password_again': request.POST.get('password_again')
            }
        response = requests.post('http://127.0.0.1:2200/users/register_terminate/',data=json_data)
        print(response)
        if response.status_code == 200:
            request.session['login'] = request.POST.get('login')
            return redirect('/polls/')
    
    context = {'login_error': 'Incorrect login or password or password_again'}
    return render(request, 'polls/register.html', context)
    
def logout(request):
    request.session['login'] = False
    return redirect('/polls/')

def index(request):
    if not 'login' in request.session:
        request.session['login'] = False
    
    if request.session['login'] == False:
        return render(request, 'polls/index.html', {})
    
    response = requests.get('http://127.0.0.1:2200/users/get_json_data/' + request.session['login'] + '/')
    list = json.loads(response.content)
    print(list)
    print(notif)
    notify = False
    if request.session['login'] == coowner_project and coowner_project != False:
        notify = notif
        
    context = {
    'latest_directories_list': list,
    'login': request.session['login'],
    'notification': notify
    }
    return render(request, 'polls/index.html', context)