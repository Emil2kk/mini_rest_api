from django.http import JsonResponse
from .models import Cars
from .serializers import Carspec
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def cars_list(request):
    if request.method=='GET':
        cars=Cars.objects.all()
        serializer=Carspec(cars,many=True)
        return Response(serializer.data)

    
    if request.method=='POST':
        serializer=Carspec(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def cars_detail(request,id):
    try:
        car=Cars.objects.get(pk=id)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=Carspec(car )
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=Carspec(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)