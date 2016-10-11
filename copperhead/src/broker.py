import json
import requests
import datetime
from copperhead.src.lightstreamer import LSClient
from copperhead.src.lightstreamer import Subscription


class IGBroker(object):
    def __init__(self, identifier, password, api_key, url):
        self.identifier = identifier
        self.password = password
        self.api_key = api_key
        self.base_url = url

        # set via login call
        self.lightstreamer_endpoint = None
        self.cst_token = None;
        self.security_token = None;

    def login(self):
        payload = {'identifier': self.identifier, 'password': self.password}
        header = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': self.api_key,
        }

        response = requests.post(self.base_url + 'session', data=json.dumps(payload), headers=header)
        if response.status_code == 200:
            print('Logged in successfully')

            # set the required properties
            self.lightstreamer_endpoint = response.json()['lightstreamerEndpoint']
            self.cst_token = response.headers['CST']
            self.security_token = response.headers['X-SECURITY-TOKEN']

            print('LightStream Endpoint: ' + self.lightstreamer_endpoint)
            print('X-SECURITY-TOKEN: ' + self.security_token)
            print('CST: ' + self.cst_token)

        else:
            print('Error: Could not log in. Http code: ' + response.status_code)

    def market_search(self, search_term):

        header = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': self.api_key,
            'CST': self.cst_token,
            'X-SECURITY-TOKEN': self.security_token
        }

        response = requests.get(self.base_url + 'markets?searchTerm=' + search_term,  headers=header)
        if response.status_code == 200:
            t=0

    def market_prices(self, epic, resolution, num_points):

        header = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': self.api_key,
            'CST': self.cst_token,
            'X-SECURITY-TOKEN': self.security_token,
            'Version': 2
        }

        response = requests.get(self.base_url + 'prices/' + epic + '/' + resolution + '/' + str(num_points), headers=header)

        if response.status_code == 200:
            return response.json()['prices']
        else:
            print('Error: Could not log in. Http code: ' + response.status_code)


class IGFeed(object):

    def __init__(self, broker):
        self.broker = broker
        self.broker.login()
        self.ls_client = LSClient(broker.lightstreamer_endpoint, user=broker.identifier, password='CST-' + broker.cst_token + '|XST-' + broker.security_token)

        try:
            self.ls_client.connect()
        except Exception as e:
            print(e)

    def subscribe(self, mode, epics, fields, item_handler):

        subscription = Subscription(
            mode=mode,
            items=epics,
            fields=fields
        )

        subscription.addlistener(item_handler)
        sub_key = self.ls_client.subscribe(subscription)



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


