import pandas as pd
import datetime
import pandas_datareader.data as web
from dateutil.relativedelta import relativedelta
import time
import queue
from yahoo_fin import stock_info as si
import numpy as np

TICKER_PROVIDER = 'yahoo'

class Hist:
    def __init__(self, df) -> None:
        self.lows = df['Low']
        self.highs = df['High']
        self.count = self.highs.count()

        def get_iqr(series):
            q1 = 0.25
            q3 = 0.75
            return series.quantile(q3) - series.quantile(q1)

        self.liqr = get_iqr(self.lows)
        self.hiqr = get_iqr(self.highs)

        self.middle = (self.lows.mode().mean() + self.highs.mode().mean()) / 2
        self.last = df['Adj Close'][-1]
        
class Bot:
    def __init__(self, stock) -> None:
        self.stock = stock
        h = self._getHist()
        self.lastPrice = 0
        self.prices = queue()

    def _getHist(self):
        length = 1
        today = datetime.date.today()
        delta = relativedelta(months=length)
        start = today - delta
        return Hist(web.DataReader(self.stock, TICKER_PROVIDER, start, today))

    def _getLive(self):
        return si.get_live_price(self.stock)

    def _log(self):
        pass

    def Start(self):
        try:
            while True:
                price = self._getLive()
                print(price)
                # print(self._getHist().__dict__)

                # prediction here...

                now = datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
                print(now)
                break
                time.sleep(60)
        except KeyboardInterrupt:
            print('\nKeyboard Interrupt')

Bot('ath.to').Start()