from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, AppUser
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            details = Event.objects.filter(user=request.user.id).values()
            user_f_name = request.user.first_name
            user_l_name = request.user.last_name
            user_data = {'name': user_f_name, 'last_name': user_l_name}
            data = {'details': details,
                    'user_data': user_data}
            return render(request, 'pages/index.html', data)
    return render(request, 'pages/index.html')

@csrf_exempt
def new_event(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body['name']
        description = body['description']
        startsAt = body['startsAt']
        endsAt = body['endsAt']
        new_event = Event(user = request.user, name = name, description = description, starts_at = startsAt, ends_at = endsAt)
        new_event.full_clean()
        new_event.save()
        return JsonResponse({'Status':'Got it'})     
    return render(request, 'pages/new_event.html')

def delete(request, id):
    event_by_id = Event.objects.filter(id=id)
    event_by_id.delete()
    return redirect('calendar:index')

def details(request, id):
    event_by_id = Event.objects.filter(id=id).values()[0]
    data = {'event_by_id': event_by_id}
    return render(request, 'pages/details.html', data)

@csrf_exempt
def update(request, id):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body['name']
        description = body['description']
        startsAt = body['startsAt']
        endsAt = body['endsAt']
        event_by_id = Event.objects.get(id=id)
        event_by_id.name = name
        event_by_id.save()
        event_by_id.description = description
        event_by_id.save()
        event_by_id.starts_at = startsAt
        event_by_id.save()
        event_by_id.ends_at = endsAt
        event_by_id.save()
        return JsonResponse({'Status':'Event updated succesfully!'})
    event_by_id = Event.objects.filter(id=id).values()[0]
    data = {'event_by_id': event_by_id}
    return render(request, 'pages/update.html', data)

@csrf_exempt
def sign_up(request):
    if request.method == 'POST' :
        try:
            data = json.loads(request.body)
            first_name = data['firstName']
            last_name = data['lastName']
            email = data['email']
            password = data['password']
            AppUser.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        except Exception as e:
            print('Error message below!')
            print(str(e))
        return JsonResponse({'Status':'User created succesfully'})
    return render(request, 'pages/signup.html')

@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                except Exception as e:
                    print('Error message below')
                    print(str(e))
                return JsonResponse({'Status': 'Succesfully logged in!'})
            else:
                return HTTPResponse('Account not active!')
        else:
            return JsonResponse({'Status': 'Succesfully logged in!'})
    return render(request, 'pages/login.html')

@csrf_exempt
def log_out(request):
    logout(request)
    return render(request, 'pages/index.html')