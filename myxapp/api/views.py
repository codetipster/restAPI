from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view  #Allows us use the decorator.
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status, views

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




@api_view(['GET'])
def userList(request):
    """Displays the list of all registered users"""

    users = User.objects.all()  #Query database for all users
    serializer = UserSerializer(users, many=True) #Serialize the result and store in a serializer variable
    return Response(serializer.data)  #return the data within the serializer variable



@api_view(['GET'])
def userDetail(request, pk):
    """Displays the details of a registered user"""

    user = User.objects.get(id=pk)  #Query database for a particular user
    serializer = UserSerializer(user, many=False) #Serialize the result and store in a serializer variable
    return Response(serializer.data)  #return the data within the serializer variable


# @api_view(['POST'])
class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        """Registers/Adds a new user to our database"""

        serializer = UserSerializer(data=request.data) #Serialize the user inputs and store in a serializer variable
        #Now validate and save the user inputs
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  #return the data within the serializer variable
