from binance import Client


api_key = '123'
api_secret = '123'
client = Client(api_key, api_secret)
#Все данные
all_tickers = client.get_ticker()

btc = client.get_ticker(symbol='BTCUSDT')
eth = client.get_ticker(symbol='ETHUSDT')
bnb = client.get_ticker(symbol='BNBUSDT')
sol = client.get_ticker(symbol='SOLUSDT')
xrp = client.get_ticker(symbol='XRPUSDT')
ltc = client.get_ticker(symbol='LTCUSDT')


a1 = 'Последняя цена:  ' + btc['lastPrice'] + ' $'
a2 = 'Изменение цены:  ' + btc['priceChangePercent'] + ' %'
a3 = 'Средняя цена:    ' + btc['weightedAvgPrice'] + ' $'
a4 = 'Минимум:         ' + btc['lowPrice'] + ' $'
a5 = 'Максимум:        ' + btc['highPrice'] + ' $'
a6 = 'Объем в токенах: ' + btc['volume'] + ' BTC'
a7 = 'Объем в $:       ' + btc['quoteVolume'] + ' $'

b1 = 'Последняя цена:  ' + eth['lastPrice'] + ' $'
b2 = 'Изменение цены:  ' + eth['priceChangePercent'] + ' %'
b3 = 'Средняя цена:    ' + eth['weightedAvgPrice'] + ' $'
b4 = 'Минимум:         ' + eth['lowPrice'] + ' $'
b5 = 'Максимум:        ' + eth['highPrice'] + ' $'
b6 = 'Объем в токенах: ' + eth['volume'] + ' ETH'
b7 = 'Объем в $:       ' + eth['quoteVolume'] + ' $'

c1 = 'Последняя цена:  ' + bnb['lastPrice'] + ' $'
c2 = 'Изменение цены:  ' + bnb['priceChangePercent'] + ' %'
c3 = 'Средняя цена:    ' + bnb['weightedAvgPrice'] + ' $'
c4 = 'Минимум:         ' + bnb['lowPrice'] + ' $'
c5 = 'Максимум:        ' + bnb['highPrice'] + ' $'
c6 = 'Объем в токенах: ' + bnb['volume'] + ' BNB'
c7 = 'Объем в $:       ' + bnb['quoteVolume'] + ' $'

d1 = 'Последняя цена:  ' + sol['lastPrice'] + ' $'
d2 = 'Изменение цены:  ' + sol['priceChangePercent'] + ' %'
d3 = 'Средняя цена:    ' + sol['weightedAvgPrice'] + ' $'
d4 = 'Минимум:         ' + sol['lowPrice'] + ' $'
d5 = 'Максимум:        ' + sol['highPrice'] + ' $'
d6 = 'Объем в токенах: ' + sol['volume'] + ' SOL'
d7 = 'Объем в $:       ' + sol['quoteVolume'] + ' $'

e1 = 'Последняя цена:  ' + xrp['lastPrice'] + ' $'
e2 = 'Изменение цены:  ' + xrp['priceChangePercent'] + ' %'
e3 = 'Средняя цена:    ' + xrp['weightedAvgPrice'] + ' $'
e4 = 'Минимум:         ' + xrp['lowPrice'] + ' $'
e5 = 'Максимум:        ' + xrp['highPrice'] + ' $'
e6 = 'Объем в токенах: ' + xrp['volume'] + ' XRP'
e7 = 'Объем в $:       ' + xrp['quoteVolume'] + ' $'

f1 = 'Последняя цена:  ' + ltc['lastPrice'] + ' $'
f2 = 'Изменение цены:  ' + ltc['priceChangePercent'] + ' %'
f3 = 'Средняя цена:    ' + ltc['weightedAvgPrice'] + ' $'
f4 = 'Минимум:         ' + ltc['lowPrice'] + ' $'
f5 = 'Максимум:        ' + ltc['highPrice'] + ' $'
f6 = 'Объем в токенах: ' + ltc['volume'] + ' LTC'
f7 = 'Объем в $:       ' + ltc['quoteVolume'] + ' $'
