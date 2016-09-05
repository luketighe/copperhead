from src.market_data import MarketData    
   
        
class Composer():
    
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
        self.marketDataSubscriber.start()
