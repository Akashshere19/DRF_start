from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=20)

    def create(self,validate_data):
      print('val value:',validate_data)
      return  Employee.objects.create(**validate_data)

    def update(self,employee,validated_data):
      newEmployee = Employee(**validated_data)
      newEmployee.id = employee.id
      newEmployee.save()  
      return newEmployee


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)    
    