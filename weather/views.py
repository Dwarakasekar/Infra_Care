from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    recommendation = ""
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'YOUR_OPENWEATHER_API_KEY'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"df2206d6808c9a49ab2d8093b9e80e1e"}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()  
            condition = weather_data['weather'][0]['main'].lower()
            temp = weather_data['main']['temp']

            # Simple recommendation logic
            if condition in ['rain', 'thunderstorm', 'snow']:
                recommendation = "Not recommended for construction work today due to weather conditions."
            elif temp < 5 or temp > 40:
                recommendation = "Temperature is not ideal for construction work."
            else:
                recommendation = "Good weather for construction work."

        else:
            weather_data = None
            recommendation = "City not found or API error."

    return render(request, 'weather.html', {
        'weather_data': weather_data,
        'recommendation': recommendation
    })
