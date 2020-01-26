from django.http import HttpResponse
from django.shortcuts import render
from fruits.models import Fruit

from django.views.generic import ListView

# Create your views here.
def fruit_detail_view(request, number):

	obj = Fruit.objects.get(id = number)
	context = {
	'name': obj.name,
	'price': obj.price
	}
	
	

	return render(request, "fruit_detail_view.html", context)

def fruit_list_view(request):

	queryset = Fruit.objects.all()
	context = {
	'fruits_list': queryset
	}
	
	

	return render(request, "fruit_list_view.html", context)