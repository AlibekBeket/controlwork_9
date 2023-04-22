import json

from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from gallery.models import Photo


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def favorite_add_view(request, *args, **kwargs):
    response_data = {'favorite': 'Добавление из избранных'}
    response = JsonResponse(response_data)
    response.status_code = 200
    json_dict = json.loads(request.body)
    user_id = json_dict.get('user_id')
    user_add = User.objects.get(id=user_id)
    users = Photo.objects.filter(id=kwargs['pk']).first().favorites.all()
    for user in users:
        if user_add == user:
            return response
    object = Photo.objects.filter(id=kwargs['pk']).first()
    object.favorites.add(user_add)
    object.save()
    return response


def favorite_delete_view(request, *args, **kwargs):
    response_data = {'favorite': 'Удаление из избранных'}
    response = JsonResponse(response_data)
    response.status_code = 200
    json_dict = json.loads(request.body)
    user_id = json_dict.get('user_id')
    user_delete = User.objects.get(id=user_id)
    users = Photo.objects.filter(id=kwargs['pk']).first().favorites.all()
    for user in users:
        if user == user_delete:
            user.delete()
            users.save()
            return response
    return response
