"""
CyberSecNews v1.0
CIBERSEC NEWS - Security news aggregator
Author: José Ramón López Guillén
GitHub: github.com/Sysop81

"""

from parameters import Parameters as paramHandler
from feeds import Feeds
from display_manager import Display
      
def main():
    Display.show_banner()
    params = paramHandler()    
    feeds = Feeds(params.get_date())
    feeds.load_pool_security_news()
