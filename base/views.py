from django.shortcuts import render
from rest_framework.response import Response
from .models import Advocate
from .serializer import AdvocateSeriazer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.views import APIView

# @api_view(['GET', 'POST'])
# def Advocate_list(request):
#     if request.method == "GET":
#         query = request.GET.get('query')
#         if query == None:
#             query = ''
#         advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains =query))
#         serializer = AdvocateSeriazer(advocates, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST':
#         advocates = Advocate.objects.create(
#             username= request.data['username'],
#             bio= request.data['bio']
#         )
#         serializer = AdvocateSeriazer(advocates, many=False)
#         return Response(serializer.data)

class Advocate_list(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains =query))
        serializer = AdvocateSeriazer(advocates, many=True)
        return Response(serializer.data)

    def post(self, request):
        advocates = Advocate.objects.create(
            username= request.data['username'],
            bio= request.data['bio']
        )
        serializer = AdvocateSeriazer(advocates, many=False)
        return Response(serializer.data)

class Advocate_detail(APIView):
    def get(self, request, username):
        data = Advocate.objects.get(username=username)
        serializer = AdvocateSeriazer(data, many=False)

        return Response(serializer.data)


    def post(self, request, username):
        data = Advocate.objects.get(username=username)
        data.username= request.data['username'],
        data.bio= request.data['bio']
        data.save()
        serializer = AdvocateSeriazer(data, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        data = Advocate.objects.get(username=username)
        data.delete()
        return Response({'message': 'Object deleted successfully'})



# @api_view(['GET', 'PUT', 'DELETE'])
# def Advocate_detail(request, username):
#     if request.method =='GET':
#         data = Advocate.objects.get(username=username)
#         serializer = AdvocateSeriazer(data, many=False)

#         return Response(serializer.data)

#     elif request.method =='PUT':
#         data = Advocate.objects.get(username=username)
#         data.username= request.data['username'],
#         data.bio= request.data['bio']
#         data.save()
#         serializer = AdvocateSeriazer(data, many=False)
#         return Response(serializer.data)
#     elif request.method =='DELETE':
#         data = Advocate.objects.get(username=username)
#         data.delete()
#     return Response({'message': 'Object deleted successfully'})