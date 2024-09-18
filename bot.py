import requests
from time import sleep
from get_prices import get_data
    
token = "1397192453:AAESA-TYUZuoO6212m3C27UWMydBGtTy5Es"
url = f"https://api.telegram.org/bot{token}/"

c_chat_id = -1002271644971

u = f"https://api.telegram.org/bot1397192453:AAESA-TYUZuoO6212m3C27UWMydBGtTy5Es/sendmessage?chat_id={c_chat_id}&text="

while True:
    basecoins, popular_coins = get_data()
    
    
    text = f"- بیت کوین (BTC):\n{basecoins['BTC']} —>  USDT\n\n- اتریوم (ETH):\n{basecoins['ETH']} —>  USDT\n\n- سولانا (SOL):\n{basecoins['SOL']} —>  USDT\n\n……………………………………\n\n💵 قیمت دلار(تتر) : {popular_coins['USDTIRT'][0]} تومان\n\n……………………………………\n\n- تون کوین (TON): \n{popular_coins['TON'][1]} —>  USDT\n{popular_coins['TON'][0]} —>  IRT\n\n- نات کوین (NOT): \n{popular_coins['NOT'][1]} —>  USDT\n{popular_coins['NOT'][0]} —>  IRT\n\n- داگز (DOGS):\n{popular_coins['DOGS'][1]} —>  USDT\n{popular_coins['DOGS'][0]} —>  IRT"

    print(requests.get(u+text).text)
    sleep(60)
    
