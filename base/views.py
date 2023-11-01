from django.shortcuts import render
from rest_framework.response import Response
from .models import Advocate
from .serializer import AdvocateSeriazer
from rest_framework.decorators import api_view
from django.db.models import Q

@api_view(['GET', 'POST'])
def Advocate_list(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains =query))
        serializer = AdvocateSeriazer(advocates, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        advocates = Advocate.objects.create(
            username= request.data['username'],
            bio= request.data['bio']
        )
        serializer = AdvocateSeriazer(advocates, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def Advocate_detail(request, username):
    data = Advocate.objects.get(username=username)
    serializer = AdvocateSeriazer(data, many=False)

    return Response(serializer.data)