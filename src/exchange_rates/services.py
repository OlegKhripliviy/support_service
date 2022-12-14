import requests
from django.conf import settings

from exchange_rates.domain import (
    AlphavantageResponse,
    ExchangeRatesServiceRequest,
    ExchangeRatesServiceResponse,
)


class ExchangeRatesService:
    def __init__(self, request: ExchangeRatesServiceRequest) -> None:
        self._request: ExchangeRatesServiceRequest = request

    def _build_url(self) -> str:
        return (
            f"{settings.ALPHA_VANTAGE_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency={self._request.from_currency}&to_currency={self._request.to_currency}"
            f"&apikey={settings.ALPHA_VANTAGE_API_KEY}"
        )

    def convert(self) -> ExchangeRatesServiceResponse:
        url: str = self._build_url()
        response: requests.Response = requests.get(url)
        alphavantage_response = AlphavantageResponse(**response.json())

        return ExchangeRatesServiceResponse(
            rate=alphavantage_response.results.exchange_rate
        )
