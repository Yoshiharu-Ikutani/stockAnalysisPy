# -*- coding: utf-8 -*-
from GoogleFinance import GoogleFinance

# example : JPN index
NI225 = GoogleFinance.call('NI225', 'INDEXNIKKEI') # 日経平均株価
TOPIX = GoogleFinance.call('TOPIX500', 'INDEXTOPIX') # 東証株価指数
# example : U.S. index
DOW     = GoogleFinance.call('.DJI', 'INDEXDJX')
NASDAQ  = GoogleFinance.call('.IXIC', 'INDEXNASDAQ')
# example : currency
USDJPY = GoogleFinance.call('USDJPY', 'CURRENCY') # 米ドル -> 円
BTCJPY = GoogleFinance.call('BTCJPY', 'CURRENCY') # BTC -> 円
