## GoogleFinance
Simple python module to get stock price data via Google finance api

## I/O
* input: code = a string to specify stock name
* input: market = a string to tell the market which the target company is in
* optional input: period = a string to tell the duration of time series
* optional input: tick = a integer value which tells data sampling time in seconds
* output: stockPrice = pandas dataframe containing stock price time series

## (usage) Get stock price data of Apple inc.

```
from GoogleFinance import GoogleFinance
GoogleFinance.call('AAPL', 'NASD')
```

## installation

```
$ git clone git@github.com:Yoshiharu-Ikutani/stockAnalysisPy.git
$ cd /path/to/stockAnalysisPy
$ pip install -r requirements.txt
```

## Demo

```
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

```