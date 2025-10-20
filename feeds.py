import json
import feedparser
from colors import Colors
from display_manager import Display
from datetime import datetime
from dateutil import parser
from xlsx_handler import XLSXHandler
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map

class Feeds:

    _FILE_NAME = "FeedJSON.json"
    _BASE_DIR = Path(__file__).resolve().parent
    _FEEDS_PATH = _BASE_DIR / "feed_json" / _FILE_NAME
    _MODE = "r"
    _ENCODING ="utf-8"
    _ENTRY_LIMIT = 20
    _POOL_MAX_WORKERS = 10

    # Constructor
    def __init__(self,_iDate):
        self.iDate = _iDate
        self.xlsxhandler = XLSXHandler()
        self.data = self.load_feed_url()

    # Load Feeds url.
    def load_feed_url(self):
        with open(self._FEEDS_PATH,self._MODE, encoding = self._ENCODING) as f:
            return json.load(f) 

    # Show feed with thread pool executor
    def load_pool_security_news(self):
        # Build arguments   
        args_list = [(site, rss_url) for site, rss_url in self.data.items()]

        # Using a map and ThreadPoolExecutor to extract news with workers shown a progress bar
        futures = thread_map(
            lambda args: self.get_news_from_site(*args),
            args_list,
            max_workers=self._POOL_MAX_WORKERS,
            desc=Colors.print_color_text("Global process",Colors.MAGENTA)
        )

        # Build xlsx
        Display.show_info(f"\nThe program is generating the XLSX file.",Colors.YELLOW)
        for result in tqdm(futures,
                           desc="Writing data"):
            if result["data"]:
                for entry in result["data"]:
                    # Adding entry to local XLS
                    self.xlsxhandler.add_news(entry)    
        
        #Build url links and show info
        self.xlsxhandler.build_url_link() 
        Display.show_info("The program finished successfully.",Colors.GREEN)       

    # Build and show news
    def get_news_from_site(self,site, rss_url): 
        site_dic ={
            "site":site,
            "data":[]
        }
        
        # Parse the feed
        feed = feedparser.parse(rss_url)

        if not feed.entries: 
            return site_dic
        
        for entry in tqdm(feed.entries[:self._ENTRY_LIMIT],
                          desc=Colors.print_color_text(site,Colors.GREY),
                          dynamic_ncols=True,
                          leave=True):
            if hasattr(entry, "published"):
                published = parser.parse(entry.published).date()

                if(published >= self.iDate):
                    soup = BeautifulSoup(entry.summary[:200],"html.parser")
                    site_dic["data"].append({
                        "title": entry.title,
                        "link" : entry.link,
                        "published": entry.published,
                        "published_date": parser.parse(entry.published).strftime("%d/%m/%Y"),
                        "summary": f"{soup.get_text(separator=" ", strip=True)[:80]}..."
                    })

        return site_dic
                               