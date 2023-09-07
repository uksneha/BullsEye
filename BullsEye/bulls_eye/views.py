from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
import requests
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def get_data_from_api(comp_isin):
    url = f"http://localhost:6050/corporate_data/companyinfo?isin={comp_isin}"
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        return None


def search_result(request):
    isin = request.GET.get('isin')
    data = get_data_from_api(isin)
    if data:
        return render(request, 'search_result.html', {'data': data})
    else:
        return render(request, 'error.html')
