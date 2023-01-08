from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status



# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':

        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees,many=True)
        return JsonResponse(serializers.data,safe=False)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        print(jsonData)
        serializers = EmployeeSerializer(data = jsonData)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,safe=False)
        else:
            return JsonResponse(serializers.errors,safe=False)
@csrf_exempt
def employeeDetailsView(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)
        
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        print(jsonData)
        serializers = EmployeeSerializer(employee,data = jsonData)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,safe=False)
        else:
            return JsonResponse(serializers.errors,safe=False)


def usersListView(request):
    users =   User.objects.all()
    print(users)  
    serializer = UserSerializer(users,many=True)
    return JsonResponse(serializer.data,safe=False)