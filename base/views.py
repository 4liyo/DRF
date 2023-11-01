from django.shortcuts import render
from rest_framework.response import Response
from .models import Advocate
from .serializer import AdvocateSeriazer
from rest_framework.decorators import api_view

@api_view(['GET'])
def Advocate_list(request):
    advocates = Advocate.objects.all()
    serializer = AdvocateSeriazer(advocates, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def Advocate_detail(request, username):
    data = Advocate.objects.get(username=username)
    serializer = AdvocateSeriazer(data, many=False)

    return Response(serializer.data)