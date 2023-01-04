import json

from django.http import JsonResponse

from exchange_rates.domain import (
    ExchangeRatesServiceRequest,
    ExchangeRatesServiceResponse,
)
from exchange_rates.services import ExchangeRatesService


def convert(request):
    if request.method == "POST":
        request_json = json.loads(request.body)
        from_currency = request_json["from"]
        to_currency = request_json["to"]
    else:
        from_currency = "USD"
        to_currency = "EUR"

    exchange_rates_service = ExchangeRatesService(
        request=ExchangeRatesServiceRequest(
            from_currency=from_currency,
            to_currency=to_currency,
        )
    )

    result: ExchangeRatesServiceResponse = exchange_rates_service.convert()
    return JsonResponse(result.dict())
