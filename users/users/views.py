from django.http import JsonResponse

import json

import requests

def get_json_data(request, login):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/get_json_data/' + login + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def get_json_data_files(request, login):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/get_json_data_files/' + login + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def get_json_data_directory(request, dir_id):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/get_json_data_directory/' + str(dir_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)


def get_json_data_file(request, dir_id, file_id):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/get_json_data_file/' + str(dir_id) + '/' + str(file_id) + '/')
        print(json.loads(response.content))
        return JsonResponse(json.loads(response.content), status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def login_terminate(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'login': request.POST.get('login'),
            'password': request.POST.get('password')
        }
        response = requests.post('http://database-docker.herokuapp.com/database/login_terminate/',data=json_data)
        print(response)
        if response.status_code == 200:
            return JsonResponse({}, status=200, safe=False)

    return JsonResponse({}, status=403, safe=False)


def register_terminate(request):
    if request.method == 'POST':
        print(request.POST)
        json_data = {
            'login': request.POST.get('login'),
            'password': request.POST.get('password'),
            'password_again': request.POST.get('password_again')
        }
        response = requests.post('http://database-docker.herokuapp.com/database/register_terminate/',data=json_data)
        print(response)
        if response.status_code == 200:
            return JsonResponse({}, status=200, safe=False)

    return JsonResponse({}, status=403, safe=False)


def add_file_acc(request):
    if request.method == 'POST':
        if request.POST.get('directory_name') and request.POST.get('optional_description') and request.POST.get('filename'):
            json_data = {
                'directory_name': request.POST.get('directory_name'),
                'optional_description': request.POST.get('optional_description'),
                'owner': request.POST.get('owner'),
                'filename': request.POST.get('filename')
            }
            response = requests.post('http://database-docker.herokuapp.com/database/add_file_acc/',data=json_data)

    return JsonResponse({}, status=200)


def delete_file_number(request, file_id):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/delete_file/' + str(file_id) + '/')

        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)



def delete_directory_number(request, directory_id):
    if request.method == 'GET':
        response = requests.get('http://database-docker.herokuapp.com/database/delete_directory/' + str(directory_id) + '/')

        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)


def add_directory_acc(request):
    if request.method == 'POST':
        if request.POST.get('directory_name'):
            json_data = {
                'directory_name': request.POST.get('directory_name'),
                'owner': request.POST.get('owner')
            }
            response = requests.post('http://database-docker.herokuapp.com/database/add_directory_acc/',data=json_data)

    return JsonResponse({}, status=200)


    
