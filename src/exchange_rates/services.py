import json

from django.conf import settings
from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    exchange_rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


def url_creator(request, from_currency="USD", to_currency="EUR") -> str:
    if request.method == "POST":
        request_json = json.loads(request.body)
        from_currency = request_json["from"]
        to_currency = request_json["to"]
    url = (
        f"{settings.ALPHA_VANTAGE_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&to_currency={to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    )
    return url
