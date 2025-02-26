import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()

def weather_dashboard(request):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Load from environment variable
    city = request.GET.get('city', 'London')  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        context = {
            'city': city,
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
        }
    else:
        context = {'error': 'City not found. Please try again.'}
    
    return render(request, 'weather/dashboard.html', context)
