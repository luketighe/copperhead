from util.eventhook import EventHook

class MarketDataSubscriber():
    
    def __init__(self, config):
        self.onBarUpdate = EventHook()
        
    def __subscribe__(self):
        self.onBarUpdate.fire(self, None)