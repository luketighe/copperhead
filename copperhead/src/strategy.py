class StrategyBase:
    
    def __init__(self, config):
        'Strategy base class'
        self.config = config
   
    def on_bar_update(self, args, keywargs):
        'Triggered on each bar update'
        self.on_bar_update_extend()
        
    def on_bar_update_extend(self):
        'Strategy logic should override this method'
        print("Strategy not implemented")