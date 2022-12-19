import requests
from django.http import JsonResponse

from src.exchange_rates.services import AlphavantageResponse, url_creator


def convert(request):
    response = requests.get(url_creator(request))
    alphavantage_response = AlphavantageResponse(**response.json())
    return JsonResponse(alphavantage_response.dict())
