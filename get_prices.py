import requests, json

url = "https://api.nobitex.ir/v2/orderbook/"

basecoins = {"BTC":"BTCUSDT", "ETH":"ETHUSDT", "SOL":"SOLUSDT"}

popular_coins = {"USDTIRT":["USDTIRT"], "TON":["TONIRT", "TONUSDT"], "NOT":["NOTIRT", "NOTUSDT"], "DOGS":["DOGSIRT", "DOGSUSDT"]}


def format_number(num_str):
    
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
    else:
        integer_part, decimal_part = num_str, ''
    
    if len(integer_part) > 3:
        formatted_integer = ""
        count = 0
        
        for digit in reversed(integer_part):
            formatted_integer = digit + formatted_integer
            count += 1
            
            if count % 3 == 0 and count != len(integer_part):
                formatted_integer = ',' + formatted_integer
        
        if decimal_part:
            return formatted_integer + '.' + decimal_part
        else:
            return formatted_integer
    else:
        return num_str



def get_data():
    
    basecoins_data = {}
    popular_coins_data = {}
    
    for symbol, api_symbol in basecoins.items():
        r = requests.get(url+api_symbol).text
        r = json.loads(r)
        price = r['lastTradePrice']
        basecoins_data[symbol] = format_number(price)
        
    
    for symbol, api_symbols in popular_coins.items(): 
        d = []
        i = 0
        for api_symbol in api_symbols:
            r = requests.get(url+api_symbol).text
            r = json.loads(r)
            price = r['lastTradePrice']
            if i == 0:
                i = 1
                if price[-1] != "0":
                    price = int(price)/10
                    price = str(price)
                else:
                    price = price[:-1]
                    
            
            d.append(format_number(price))
                
            
        popular_coins_data[symbol] = d  
        
    return basecoins_data, popular_coins_data
    