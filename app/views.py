from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 


# Create your views here.
@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':

        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        
        
        serializers = EmployeeSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

@api_view(['DELETE','GET','PUT'])
def employeeDetailsView(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)
        
    except Employee.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
      
        serializers = EmployeeSerializer(employee,data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


def usersListView(request):
    users =   User.objects.all()
    print(users)  
    serializer = UserSerializer(users,many=True)
    return JsonResponse(serializer.data,safe=False)