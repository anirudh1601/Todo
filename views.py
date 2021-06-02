from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Post
from .models import City
from .forms import CityForm
import requests

class Home(CreateView):
	model = Post
	template_name='post/home.html'
	fields='__all__'

	

def posted(request):
	post = Post.objects.all()
	return render(request,'post/posted.html',{'post':post})

def delete(request,list_id):
	item = Post.objects.get(pk=list_id)
	item.delete()
	return redirect('posted')

def cross_off(request,list_id):
	item = Post.objects.get(pk=list_id)
	item.completed=True
	item.save()
	return redirect('posted')

def uncross_off(request,list_id):
	item = Post.objects.get(pk=list_id)
	item.completed=False
	item.save()
	return redirect('posted')

def wheather(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=78cf25f1a8b1938bac63c1c26538d2ad'
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form =CityForm()

	cities= City.objects.all()
	weather_data = []
	
	for city in cities:
		r = requests.get(url.format(city)).json()
		city_weather = {
			'city':city,
			'weather': r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon':r['weather'][0]['icon'],
		}

		weather_data.append(city_weather)
	

	context = {'city_weather':weather_data, 'form': form}



	return render(request,'post/wheather.html',context)

	


