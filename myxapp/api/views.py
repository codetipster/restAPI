from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view  #Allows us use the decorator.
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    """ This lists all our API node points when user goes to url/api"""

    api_urls = {
        'ListUsers': '/user-list/',
        'UserDetail': '/user-detail/<str:pk>/',
        'CreateUser': '/register/',
        'Update': '/profile-update/<str:pk>/',
        'Auth' : '/login/<str:pk>' 
    }

    return Response(api_urls)

def user_login(request):
    pass

def user_logout(request):
    pass
