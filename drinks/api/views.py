from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import DrinkSerializer

# Create your views here.

@api_view('GET', 'POST')
def drinks(request):
    if request.method == 'GET':
        pass