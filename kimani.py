"""
Simple crypto trading bot (single-file example)

Features:
- Uses ccxt to fetch OHLCV from Binance (or other exchange supported by ccxt)
- Simple moving-average (SMA) crossover strategy (fast & slow SMA)
- Basic position sizing and safety checks
- Works in testnet mode if you set a testnet flag (recommended)

Important safety notes:
- This is example code for educational purposes only. Not financial advice.
- Test on a paper-trading or testnet account before risking real funds.
- Understand the code before running with live API keys.

Requirements:
- Python 3.8+
- pip install ccxt pandas

Usage:
- Edit the CONFIG section below (api keys, symbol, timeframe, sizes).
- Run: python simple_crypto_bot.py

"""

import time
import logging
import ccxt
import pandas as pd
from datetime import datetime


API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
EXCHANGE_ID = "binance"            
USE_TESTNET = True                  
SYMBOL = "BTC/USDT"
TIMEFRAME = "1m"                   
FAST_SMA = 7
SLOW_SMA = 25
TRADE_AMOUNT_USD = 50               
POLL_INTERVAL = 15                  
MAX_RETRIES = 3

# ------------------------- LOGGER -------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ------------------------- HELPERS -------------------------

def init_exchange():
    exchange_class = getattr(ccxt, EXCHANGE_ID)
    exchange = exchange_class({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
    })

    # Binance-specific testnet flag
    if EXCHANGE_ID == 'binance' and USE_TESTNET:
        # For CCXT, set the 'options' endpoint or use binanceusdm/testnet variations.
        # This example uses the testnet for "binance" (spot sandbox) if available in your ccxt build.
        exchange.set_sandbox_mode(True)
        logger.info('Sandbox/testnet mode enabled')

    return exchange


def fetch_ohlcv_df(exchange, symbol, timeframe, limit=200):
    # returns a pandas DataFrame with columns: timestamp, open, high, low, close, volume
    raw = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df


def compute_sma(df, window):
    return df['close'].rolling(window=window).mean()


def get_balance_usdt(exchange):
    try:
        bal = exchange.fetch_balance()
        # try common keys
        if 'USDT' in bal['free']:
            return float(bal['free']['USDT'])
        # fallback: try quote currency from SYMBOL
        quote = SYMBOL.split('/')[1]
        return float(bal['free'].get(quote, 0.0))
    except Exception as e:
        logger.warning('Could not fetch balance: %s', e)
        return 0.0


def calculate_amount(exchange, price, spend_usd):
    # calculate base currency amount we can buy with spend_usd at current price
    amount = float(spend_usd) / float(price)
    # round according to exchange precision -- simple fallback
    return round(amount, 6)

# ------------------------- STRATEGY / ORDER -------------------------

def place_order_buy(exchange, symbol, amount):
    try:
        logger.info('Placing MARKET BUY for %s %s', amount, symbol)
        order = exchange.create_market_buy_order(symbol, amount)
        logger.info('Order result: %s', order)
        return order
    except Exception as e:
        logger.error('Buy order failed: %s', e)
        return None


def place_order_sell(exchange, symbol, amount):
    try:
        logger.info('Placing MARKET SELL for %s %s', amount, symbol)
        order = exchange.create_market_sell_order(symbol, amount)
        logger.info('Order result: %s', order)
        return order
    except Exception as e:
        logger.error('Sell order failed: %s', e)
        return None

#----------------------tracking position-----------------------
position = {
    'side': None,    
    'amount': 0.0,
    'entry_price': 0.0,
}

# ------------------------- MAIN LOOP -------------------------

def run():
    exchange = init_exchange()

    logger.info('Starting simple SMA crossover bot for %s on %s', SYMBOL, EXCHANGE_ID)

    while True:
        try:
            df = fetch_ohlcv_df(exchange, SYMBOL, TIMEFRAME)
            df['sma_fast'] = compute_sma(df, FAST_SMA)
            df['sma_slow'] = compute_sma(df, SLOW_SMA)

            # take the latest completed candle (last row)
            row = df.iloc[-1]
            prev = df.iloc[-2]

            price = float(row['close'])
            prev_price = float(prev['close'])

            sma_fast = float(row['sma_fast'])
            sma_slow = float(row['sma_slow'])
            prev_fast = float(prev['sma_fast'])
            prev_slow = float(prev['sma_slow'])

            logger.info('Price: %s | fast: %.4f slow: %.4f', price, sma_fast, sma_slow)

            # generate signals: crossover
            # buy signal: previous fast <= prev slow and current fast > current slow
            buy_signal = (prev_fast <= prev_slow) and (sma_fast > sma_slow)
            sell_signal = (prev_fast >= prev_slow) and (sma_fast < sma_slow)

            # simple execution logic
            if buy_signal and position['side'] is None:
                logger.info('Buy signal detected')
                # calculate amount to buy using TRADE_AMOUNT_USD
                amount = calculate_amount(exchange, price, TRADE_AMOUNT_USD)
                if amount <= 0:
                    logger.warning('Calculated amount is zero, skipping buy')
                else:
                    order = place_order_buy(exchange, SYMBOL, amount)
                    if order:
                        position['side'] = 'long'
                        position['amount'] = amount
                        position['entry_price'] = price

            elif sell_signal and position['side'] == 'long':
                logger.info('Sell signal detected')
                amount = position['amount']
                if amount <= 0:
                    logger.warning('No amount in position, skipping sell')
                else:
                    order = place_order_sell(exchange, SYMBOL, amount)
                    if order:
                        position['side'] = None
                        position['amount'] = 0.0
                        position['entry_price'] = 0.0

            else:
                logger.info('No trade this iteration')

        except Exception as e:
            logger.exception('Unexpected error in main loop: %s', e)

        # wait before next check
        time.sleep(POLL_INTERVAL)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        logger.info('Bot stopped by user')

# ------------------------- END -------------------------

