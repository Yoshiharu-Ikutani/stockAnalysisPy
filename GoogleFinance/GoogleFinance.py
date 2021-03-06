### module to get stock price data via Google finance api
# input: code = a string to specify stock name
# input: market = a string to tell the market which the target company is in
# optional input: period = a string to tell the duration of time series
# optional input: tick = a integer value which tells data sampling time in seconds
# output: stockPrice = pandas dataframe containing stock price time series
### (usage) Get stock price data of Apple inc.
# from GoogleFinance import GoogleFinance
# GoogleFinance.call('AAPL', 'NASD')
import pandas as pd
from time import time
from datetime import datetime, timedelta
import requests
import re
import csv
def call(code, market, period = '1Y', tick = 86400):
    # set parameters
    dType   = 'd,c,o,h,l,v'
    lsat_date = int(time())

    # set base url
    BASE = 'https://www.google.com/finance/getprices'
    URL  = BASE + '?q=' + code + '&x=' + market + '&p=' + period + '&f' + dType + '&ts' + str(lsat_date)

    # get data
    rowData = requests.get(URL).content.splitlines()
    if len(rowData) < 10:
        return -1   # fail to get data

    # get colnames
    idx = [ i for i, item in enumerate(rowData) if re.search( 'COLUMNS*' , item ) ]
    colnames = rowData[idx[0]]
    colnames = colnames.split('=')[1].split(',')

    # remove header info
    idx = [ i for i, item in enumerate(rowData) if re.search( 'TIMEZONE*' , item ) ]
    contents    = rowData[idx[0]+1:]
    regex       = re.compile(r'TIMEZONE.*')
    contents    = filter(lambda i: not regex.search(i), contents)

    # create datastore
    stockPrice  = pd.DataFrame()

    # re-define time data
    timeSet = [ i for i, item in enumerate(contents) if re.search( '^a.*' , item ) ]
    timeSet.append(len(contents))
    for i in range(0, len(timeSet)-1):
        # convert str to dataframe
        data    = contents[timeSet[i]:timeSet[i+1]]
        dcsv    = csv.reader(data)
        dlist   = list(dcsv)
        stockData = pd.DataFrame(dlist)
        stockData.columns = [colnames]
        # string to datetime
        tUnix = stockData.DATE[0]
        tUnix = tUnix.split('a')[1]
        startDate = datetime.fromtimestamp(int(tUnix)).date()
        # re-define date info
        stockData.DATE[0] = 0
        daySeries = stockData.DATE
        date = []
        for day in daySeries:
            date.append(startDate + timedelta(days=int(day)))
        stockData['date'] = date
        del stockData['DATE']
        # concatenate stockdata
        stockPrice = pd.concat([stockPrice, stockData])
        stockPrice = stockPrice[['date', 'OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUME']]

    return stockPrice

