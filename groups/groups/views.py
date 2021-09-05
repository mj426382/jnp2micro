from django.http import JsonResponse

import json

from django.core import serializers

import requests

def add_group_task(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'optional_description': request.POST.get('optional_description'),
            'directory_name': request.POST.get('directory_name'),
            'filename': request.POST.get('filename')
        }
        response = requests.post('http://127.0.0.1:2137/database/add_group_task/',data=json_data)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)

def delete_task(request, id):
    response = requests.get('http://127.0.0.1:2137/database/delete_task/' + str(id) + '/')
    print(response.content)
    return JsonResponse({}, status=200)


def get_group_tasks(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2137/database/get_group_tasks')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def delete_group_project(request, id):
    response = requests.get('http://127.0.0.1:2137/database/delete_group_project/' + str(id) + '/')
    return JsonResponse({}, status=200)

def get_task(request, id, task_id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2137/database/get_task/' + str(id) + '/' + str(task_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)

    else:
        return JsonResponse({}, status=400)

def get_project(request, id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2137/database/get_project/' + str(id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def get_group_projects(request, login):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:2137/database/get_group_projects/' + login + '/')
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
            'owner': request.POST.get('owner'),
            'filename': request.POST.get('filename')
        }
        response = requests.post('http://127.0.0.1:2137/database/make_group_project/',data=json_data)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400);
