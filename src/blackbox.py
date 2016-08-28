class Config():
    
    def __init(self):
        'Config class'
    
class Strategy():
    
    def __init__(self, config):
        'Strategy base class'
        self.config = config
   
    def on_bar_update(self, args, keywargs):
        'Triggered on each bar update'
        self.on_bar_update_extend()
        
    def on_bar_update_extend(self):
        'Strategy logic should override this method'
        print("Strategy not implemented")
        
class MarketDataSubscriber():
    
    def __init__(self, config):
        self.onBarUpdate = EventHook()
        
    def __subscribe__(self):
        self.onBarUpdate.fire(self, None)
    
        
class StrategyComposer():
    
    def __init__(self, strategy, marketDataSubscriber):
        'Will compose the strategy'
        if strategy is None:
            raise TypeError                   

        if marketDataSubscriber is None:
            raise TypeError        
        
        self.marketDataSubscriber = marketDataSubscriber        
        
        'subscribe to the market data'
        self.marketDataSubscriber.onBarUpdate += strategy.on_bar_update()
        
    def start(self):
        'Subscribe etc'

class EventHook(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def clearObjectHandlers(self, inObject):
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler