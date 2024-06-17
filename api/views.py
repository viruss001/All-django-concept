from django.shortcuts import redirect, render
from rest_framework import viewsets

# Create your views here.here we not using any serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .models import username
from .serializers import *


@api_view(["GET", "POST"])
def home(request):
    if request.method == "GET":
        # get is used for backend to frontend
        return Response({"message": "Hello, world!"})
    elif request.method == "POST":
        # post is used for frontend to backend
        data = request.data
        print(data)
        return Response(data)


# getting the data from backend to frontend
@api_view(["GET"])
def geting(request):
    if request.method == "GET":
        obj = username.objects.filter(userid__isnull=False)
        print(obj)
        data = usernameserlizer(obj, many=True)
        return Response(data.data)


# send data  frontend to backend
@api_view(["POST"])
def posting(request):
    if request.method == "POST":
        data = request.data
        obj = usernameserlizer(data=data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data)
        return Response(obj.errors)


"""now we see a update there are two type of update put and patch 
patch do a partial update where put do a complete update
"""
"""{
        "id": 1,
        "fname": "suraj",
        "age": 80
    }
    this is put method we requerd all data
    """


@api_view(["PUT"])
def puting(request, id):
    if request.method == "PUT":
        data = request.data
        obj = username.objects.get(id=id)
        objser = usernameserlizer(obj, data=data)
        if objser.is_valid():
            objser.save()
            return Response(objser.data)
        return Response(objser.errors)


"""{
        "id": 1,
      
        "age": 50
    }
    like this in patch"""


@api_view(["PATCH"])
def patching(request, id):
    if request.method == "PATCH":
        data = request.data
        obj = username.objects.get(id=id)
        objser = usernameserlizer(obj, data=data, partial=True)
        if objser.is_valid():
            objser.save()
            return Response(objser.data)
        return Response(objser.errors)


@api_view(["DELETE"])
def delete(request, id):
    data = request.data
    obj = username.objects.get(id=id)
    obj.delete()
    """
class APIS(APIView):
    def get(self, request):
        return Response({       
        "meg": "get"        
    })
    def post(self, request):
        return Response({       
        "meg": "post"        
    })
    def put(self, request):
        return Response({       
        "meg": "put"        
    })
    def patch(self, request):
        return Response({       
        "meg": "patch"        
    })
    def delete(self, request):
        return Response({       
        "meg": "delete"        
    })
    """


# all crud opration
class UsernameViewSet(viewsets.ModelViewSet):
    serializer_class = usernameserlizer
    queryset = username.objects.all()


class userid(viewsets.ModelViewSet):
    serializer_class = useridserlizer
    queryset = Userid.objects.all()


from django.contrib.auth.models import User


class Registeruser(APIView):
    viewsets.ModelViewSet

    def post(self, request):
        data = request.data
        serializer = Registerus(data=data)
        # wehave to chack the user indata base or not in serializer
        if not serializer.is_valid():
            return Response({"status": False, "msg": serializer.errors})
        serializer.save()  # save in db
        return Response({"status": True, "msg": "user created"})
