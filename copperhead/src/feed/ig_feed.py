from copperhead.src.feed.feed_base import FeedBase


class IGFeed(FeedBase):

    def __init__(self, ig_rest, ig_streaming):
        """init base class"""
        super(IGFeed, self).__init__()

        self.ig_rest = ig_rest
        self.ig_streaming = ig_streaming


    def start(self):
        """overriding the MarketData start method"""

        """iterate bars"""

        """raise call new_bar method"""
        super(IGFeed).new_bar(None)
