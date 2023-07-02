from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
    
    def validate(self,data):
        email = data.get('Email')
        password = data.get('Password')
        
        print('email',email)
        print('pa',password)
        if email and password:
            admin = Admin.objects.filter(Email=email, Password=password).first()
            print('admin',admin)
        else:
            raise serializers.ValidationError('Must provide both email and password.')

        data['admin'] = admin
        return data

class DepartmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
    