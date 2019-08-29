from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def homes(request):
	
	return render(request,'homes.html')
# Create your views here.
