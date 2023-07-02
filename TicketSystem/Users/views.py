from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from . serializers import *
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

@api_view(['GET','POST'])       
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]  
    
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.Email
        token['name']  = user.Name
        token['phone'] = user.phone_number
        token['id'] = user.id
        
        # ...
        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['POST'])
def add_ticket(request):
    data = request.data
    print('daa',data)
    username = 'roshan1arshed@gmail.com'
    api_token = 'api_token'
    
    # Create headers with authentication credentials
    headers = {
        'Content-Type': 'application/json',
    }
    auth = (username + '/token', api_token) 
    serializer = TicketSerializer(data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'Message':'Ticket create succesfully'})
    else:
        response = requests.post('http://brototype7362.zendesk.com/api/v2/tickets', json=data,headers=headers, auth=auth)
        return Response(serializer.errors)


@api_view(['GET'])
def get_ticket_by_user(request,email):
    try:
        ticket = Tickets.objects.filter(Email = email)
        serializer = TicketSerializer(ticket,many = True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("Object not found")
    
    
    
    



# def create_ticket(data):
#     # ZenDesk API endpoint for creating a ticket
#     url = 'https://your_subdomain.zendesk.com/api/v2/tickets.json'
    
#     # Set your ZenDesk API credentials (username/email and API token)
#     username = 'your_username_or_email'
#     api_token = 'your_api_token'
    
#     # Create headers with authentication credentials
#     headers = {
#         'Content-Type': 'application/json',
#     }
#     auth = (username + '/token', api_token)
    
#     # Send the POST request to create the ticket
#     response = requests.post(url, json=data, headers=headers, auth=auth)
    
#     # Check the response status code
#     if response.status_code == 201:
#         # Ticket created successfully
#         ticket_data = response.json()
#         return ticket_data
#     else:
#         # Error creating the ticket
#         return None

# # Example usage
# ticket_data = {
#     'subject': 'Ticket Subject',
#     'description': 'Ticket Description',
#     'requester': {
#         'name': 'John Doe',
#         'email': 'john.doe@example.com'
#     }
# }

# response_data = create_ticket(ticket_data)

# if response_data:
#     print('Ticket created successfully:', response_data)
# else:
#     print('Failed to create the ticket.')
    
    
    
    


