from unittest import result
from django.shortcuts import render
import requests
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=ead90839fdcd2d6278c89e0bb6e6f45f&units=metric');
	return res.json()
def index(request):

    return render(request,'index.html')

def print_weather(result,city):
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
    
def weather(request):
    context = {
        'fech':False
    }
    if request.method == 'POST':
        city = request.POST.get('city')

        try:
            query = 'q='+city
            result = weather_data(query)
            
            context['fech'] = True 
            context['temp'] = result['main']['temp']
            context['wspeed'] = result['wind']['speed']
            context['description'] = result['weather'][0]['description']
            context['weather'] = result['weather'][0]['main']

        except:
            context['result'] = "City Name Not found !!"

    return render(request,'weather.html',context)
