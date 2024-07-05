import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import google.generativeai as genai

# Create your views here.
def index(request):
    return render(request, 'index.html')
@csrf_exempt
def ball_or_not(request):
    if request.method == 'POST':
        region = request.POST['text']
        weather = get_weather(region)
        result = can_i_ball(weather)
        return JsonResponse({'content': result})
    else:
        return redirect('/')
    
def get_weather(region):
    id_url = f"https://www.meteosource.com/api/v1/free/find_places?text={region}&language=en&key="
    place_id = requests.get(id_url).json()[0]["place_id"]
    url = f"https://www.meteosource.com/api/v1/free/point?place_id={place_id}&sections=hourly&language=en&units=auto&key="
    data = requests.get(url).json()["hourly"]["data"]
    return data

def can_i_ball(weather):
    print(weather)
    API_KEY = ""

    