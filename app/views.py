from django.shortcuts import render,redirect
from .models import Slider,Main_Category
# Create your views here.

def home(request):
	sliders = Slider.objects.all()
	main_category = Main_Category.objects.all()
	context = {
		'sliders':sliders,
		'main_category':main_category
	}
	return render(request, 'Main/home.html',context)


def base(request):
	
	return render(request, 'base.html')
