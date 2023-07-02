from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from .serializers import *
from django.http import HttpResponse
from rest_framework.response import Response
from . models import *
from Users . serializers import UserSerializer,TicketSerializer
from Users . models import *

# Create your views here.

@api_view(['POST'])
def admin_login(request):
    serializer = AdminSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    admin = serializer.validated_data['admin']
    response_data = {'message': 'success', 'admin_email': admin.Email}
    return Response(response_data, status=200)

@api_view(['POST'])
def create_department(request):
    data = request.data
    serializer = DepartmentSerilaizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerilaizer(departments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_department(request, id):
    try:
        department = Department.objects.get(id=id)
        serializer = DepartmentSerilaizer(department)
        return Response(serializer.data)
    except Department.DoesNotExist:
        return Response({'message': 'Department not found'}, status=404)

@api_view(['PUT'])
def update_department(request, id):
    try:
        department = Department.objects.get(id=id)
        data = request.data
        serializer = DepartmentSerilaizer(department, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    except Department.DoesNotExist:
        return Response({'message': 'Department not found'}, status=404)

@api_view(['DELETE'])
def delete_department(request, id):
    try:
        department = Department.objects.get(id=id, status=False)
        department.delete()
        return Response({'message': 'Department deleted successfully'})
    except Department.DoesNotExist:
        return Response({'message': 'Department not found or assigned to a user'}, status=404)

@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerilaizer(departments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    department = Department.objects.get(id = data['department'])
    department.status = True
    department.save()
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
@api_view(['GET'])
def get_all_tickets(request):
    tickets = Tickets.objects.all()
    ticketSerializer = TicketSerializer(tickets, many=True)
    if tickets:
        return Response(ticketSerializer.data)
    else:
        return Response({"message": "There are no tickets"})

    
    
    

    
    
    
    
    
    
    


