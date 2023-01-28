from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics

# Create your views here.
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from rest_framework.filters import SearchFilter

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0797292290'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        #return HttpResponse("STK Push in Django👋")
        return HttpResponse(data)

class UsersLists(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends =  [SearchFilter]
    search_fields = ['name', 'phone']

