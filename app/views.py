from django.shortcuts import render,redirect
from .models import Slider
# Create your views here.

def home(request):
	sliders = Slider.objects.all()
	context = {
		'sliders':sliders
	}
	return render(request, 'Main/home.html',context)


def base(request):
	
	return render(request, 'base.html')
