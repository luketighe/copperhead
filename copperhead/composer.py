
        
class Composer:
    
    def __init__(self, strategy, feed):
        """Will compose the strategy"""
        if strategy is None:
            raise TypeError                   

        if feed is None:
            raise TypeError        
        
        self.feed = feed
        
        'subscribe to the market data'
        self.feed.onBarUpdate += strategy.on_bar_update()
        
    def start(self):
        """Subscribe etc"""
        self.feed.start()
