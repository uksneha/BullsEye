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


def get_data_from_api():
    url = "http://localhost:6050/sample/INE208C01025"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None


def search_result(request):
    data = get_data_from_api()
    if data:
        return render(request, 'search_result.html', {'data': data})
    else:
        return render(request, 'error.html')

# def search_api(request):
#     query = request.GET.get('q', '')
#     results = Item.objects.filter(CompanyName__icontains=query)[:5]
#     data = [{'ISIN': result.ISIN, 'CompanyName': result.CompanyName} for result in results]
#     return JsonResponse(data, safe=False)
#
#     items = []
#     for hit in search_results['hits']['hits']:
#         item_id = hit['_id']
#         item = Item.objects.get(id=item_id)
#         items.append(item)
#
#     return render(request, 'search.html', {'items': items})
