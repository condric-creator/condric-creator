import os
import time
import math
from binance.client import Client
from binance.exceptions import BinanceAPIException

API_KEY = os.getenv("BINANCE_API_KEY") or "YOUR_API_KEY"
API_SECRET = os.getenv("BINANCE_API_SECRET") or "YOUR_API_SECRET"
client = Client(API_KEY, API_SECRET)

symbol = "BTCUSDT"
interval = "1m"
short_window = 5
long_window = 20
trade_pct = 0.1
qty_precision = 6
sleep_seconds = 60

while True:
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=long_window + 5)
        closes = [float(k[4]) for k in klines]
        short_sma = sum(closes[-short_window:]) / short_window
        long_sma = sum(closes[-long_window:]) / long_window
        account = client.get_account()
        balances = {b["asset"]: float(b["free"]) for b in account["balances"]}
        usdt_balance = balances.get("USDT", 0.0)
        btc_balance = balances.get("BTC", 0.0)
        if short_sma > long_sma and usdt_balance > 10 and btc_balance == 0:
            spend = usdt_balance * trade_pct
            price = closes[-1]
            qty = math.floor((spend / price) * (10 ** qty_precision)) / (10 ** qty_precision)
            if qty > 0:
                client.order_market_buy(symbol=symbol, quantity=qty)
        if short_sma < long_sma and btc_balance > 0:
            qty = math.floor(btc_balance * (10 ** qty_precision)) / (10 ** qty_precision)
            if qty > 0:
                client.order_market_sell(symbol=symbol, quantity=qty)
    except BinanceAPIException as e:
        print("binance error", e)
    except Exception as e:
        print("error", e)
    time.sleep(sleep_seconds)
