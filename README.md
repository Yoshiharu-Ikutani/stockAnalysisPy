## simple python module to get stock price data via Google finance api

## I/O
* input: code = a string to specify stock name
* input: market = a string to tell the market which the target company is in
* optional input: period = a string to tell the duration of time series
* optional input: tick = a integer value which tells data sampling time in seconds
* output: stockPrice = pandas dataframe containing stock price time series

## (usage) Get stock price data of Apple inc.
from GoogleFinance import GoogleFinance
GoogleFinance.call('AAPL', 'NASD')
