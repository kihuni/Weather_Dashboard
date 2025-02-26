# Real-Time Weather Dashboard 🌦️  

A Django-based web application that fetches live weather data using the OpenWeather API and displays it in a user-friendly interface.  

## Features  
✅ Search for weather conditions by city  
✅ Displays temperature, humidity, and weather description  
✅ Auto-refreshes every 5 minutes  
✅ User-friendly interface  

## Setup Instructions  

### 1. Clone the Repository  
```
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard

```
### 2 Create a Virtual Environment & Install Dependencies
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```
### 3  Set Up API Key

Create a .env file in the project root and add:

`OPENWEATHER_API_KEY=your_api_key_here`

### 4. Run the Project

`python manage.py runserver`

Visit localhost:8000 to see the dashboard in action!

Blog Post 📖

For a detailed step-by-step guide on how this project was built, check out the full blog post:

👉 [Building a Real-Time Weather Dashboard with Django and OpenWeather API ](https://dev.to/kihuni/building-a-real-time-weather-dashboard-with-openweather-api-and-django-35c5)
