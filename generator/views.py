from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):

	pwd = ""
	character = list("abcdefghijklmnopqrstuvwxyz")
	if request.GET.get('uppercase'):
		character.extend(list('ABCDEDFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		character.extend(list('!@$*%^'))
	if request.GET.get('numbers'):
		character.extend(list('01256789'))
	length = int(request.GET.get('length',12))
	for x in range(length):
		pwd += random.choice(character)
	return render(request, 'generator/password.html', {'password':pwd})
