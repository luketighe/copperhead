from ..util import eventhook


class FeedBase(object):

    def __init__(self):
        self.onBarUpdate = eventhook.EventHook()

    def new_bar(self, bar):
        self.onBarUpdate.fire(self, bar=bar)

    def start(self):
        """override this method and call new_bar to raise onBarUpdate event"""
        print("Market data has not been implemented")


class CsvMarketData(FeedBase):

    def __init__(self):
        """init base class"""
        super(CsvMarketData, self).__init__()

    def start(self):
        """overriding the MarketData start method"""

        """iterate bars"""

        """raise call new_bar method"""
        super(CsvMarketData).new_bar(None)
