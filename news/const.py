__version__ = "0.1.0"

URLS = [
    "http://feeds.nos.nl/nosnieuwsalgemeen",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://www.nu.nl/rss/Algemeen",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://news.ycombinator.com/rss",
    "http://feeds.feedburner.com/tweakers/nieuws",
    # "https://www.reddit.com/r/all/top.rss", # Getting 429 too many requests, probably need API key
]
ENTRIES_PER_FEED = 10
