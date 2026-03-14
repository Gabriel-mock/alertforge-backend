import requests


def get_crypto_price(symbol: str):
    symbol = symbol.upper()

    coin_map = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "SOL": "solana"
    }

    coin_id = coin_map.get(symbol)

    if not coin_id:
        return None

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get(coin_id, {}).get("usd")