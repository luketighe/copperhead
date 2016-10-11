from copperhead.util import eventhook

class FeedBase(object):

    def __init__(self):
        self.onBarUpdate = eventhook.EventHook()

    def new_bar(self, bar):
        self.onBarUpdate.fire(self, bar=bar)

    def start(self):
        """override this method and call new_bar to raise onBarUpdate event"""
        print("Market data has not been implemented")
