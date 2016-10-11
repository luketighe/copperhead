id = 'luketighe'
pas = 'P@ssw0rd'
api = '28b4b72174d760bfb760db41f5e11a06b90f1536'
url = 'https://demo-api.ig.com/gateway/deal/'


def handler(tick):
    if tick['values']['CONS_END'] == '1':

        date = tick['values']['UTM']
        open = tick['values']['BID_OPEN']
        high = tick['values']['BID_HIGH']
        low = tick['values']['BID_LOW']
        close = tick['values']['BID_CLOSE']

        print(date + " " + open + " " + high + " " + low + " " + close)


igBroker = IGBroker(id, pas, api, url)
igStream = IGFeed(igBroker)

#igBroker.login()
igBroker.market_search('usdjpy')


igBroker.market_prices('CS.D.USDJPY.TODAY.IP', 'MINUTE_30', 90)

#igStream.subscribe('MERGE', ['CHART:CS.D.USDJPY.TODAY.IP:5MINUTE'], ['UTM', 'BID_OPEN', 'BID_HIGH', 'BID_LOW', 'BID_CLOSE', 'CONS_END'], handler)

input("{0:-^80}\n".format("HIT CR TO UNSUBSCRIBE AND DISCONNECT FROM \
LIGHTSTREAMER"))


