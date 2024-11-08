import requests
import yfinance as  yf

# Define base currency for conversion
base_currency = "HUF"

# List of currencies to convert (ISO codes for fiat, symbols for crypto)
fiat_currencies = [
    "USD", "EUR", "GBP", "CHF", "PLN", "CZK", "RON", "HRK",
    "SEK", "NOK", "DKK", "CAD", "AUD", "JPY", "CNY"
]
crypto_currencies = [
    "bitcoin", "ethereum", "litecoin", "dogecoin", "binancecoin",
    "ripple", "cardano", "solana", "polkadot", "polygon",
    "shiba-inu", "avalanche-2", "uniswap", "monero", "cosmos"
]
# List of 20 common stocks
common_stocks = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "TSLA",
    "NVDA", "META", "BRK.B", "JPM", "JNJ",
    "V", "PG", "UNH", "HD", "PFE",
    "DIS", "KO", "XOM", "SPY", "VTI"
]
hungarian_stocks = [
    "MTEL.BD",  # Magyar Telekom
    "MOL.BD",   # MOL Group
    "OTP.BD",   # OTP Bank
    "RICHT.BD", # Richter Gedeon
    "EON.BD",    # FHB Mortgage Bank
    "MERC.BD",
    "ADID.BD",
    "ZWACK.BD",
    "RABA.BD"
]

def get_fiat_rates(base):
    """Fetch fiat currency exchange rates relative to the base currency."""
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("rates", {})
    else:
        print(f"Failed to fetch fiat rates: {response.status_code}")
        return {}

def get_crypto_rates(base):
    """Fetch crypto currency rates relative to the base currency."""
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_currencies),  # Join all crypto currencies with commas
        "vs_currencies": base
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch crypto rates: {response.status_code}")
        return {}
    
def get_stock_prices(stock_list):
    """Fetch stock prices for selected stocks."""
    stock_prices = {}
    for symbol in stock_list:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(period="1d")  # Get the latest data
        if not stock_info.empty:
            price = stock_info["Close"].iloc[-1]
            stock_prices[symbol] = price
        else:
            stock_prices[symbol] = None
    return stock_prices

# Fetch rates
fiat_rates = get_fiat_rates(base_currency)
crypto_rates = get_crypto_rates(base_currency.lower())
global_stock = get_stock_prices(common_stocks)
hun_stocks = get_stock_prices(hungarian_stocks)

print(f"Exchange rates relative to {base_currency} (Fiat):")
for currency in fiat_currencies:
    rate = fiat_rates.get(currency)
    if rate:
        huf_rate = 1 / rate  # Invert to get HUF per 1 unit of foreign currency
        print(f"{currency} = {huf_rate:.2f} {base_currency}")

# Display crypto conversion rates
print(f"\nExchange rates relative to {base_currency} (Crypto):")
for crypto in crypto_currencies:
    rate = crypto_rates.get(crypto, {}).get(base_currency.lower())
    if rate:
        print(f"{crypto.capitalize()} = {rate} {base_currency}")

print(f"\nStock prices in {base_currency} (global):")
for symbol, price in global_stock.items():
    if price:
        print(f"{symbol}: {round(price, 2)} $")
    else:
        print(f"{symbol}: Price not available")

print(f"\nStock prices in {base_currency} (Hungarian):")
for symbol, price in hun_stocks.items():
    if price:
        print(f"{symbol}: {round(price, 2)} {base_currency}")
    else:
        print(f"{symbol}: Price not available")

