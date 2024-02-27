import feedparser
import requests
from datetime import datetime, timezone
from time import mktime
from dataclasses import dataclass
from typing import Any, List
from zoneinfo import ZoneInfo


from .const import ENTRIES_PER_FEED


@dataclass
class RssItem:
    title: str
    link: str
    published: str


@dataclass
class RssFeed:
    title: str
    items: List[RssItem]


def to_rss_item(entry: Any) -> RssItem:
    published_dt = datetime.fromtimestamp(mktime(entry.published_parsed)).replace(tzinfo=timezone.utc).astimezone(ZoneInfo("Europe/Amsterdam"))
    published = published_dt.strftime("%d-%m %H:%M")

    return RssItem(
        entry.title,
        entry.link,
        published,
    )


def to_rss_feed(url: str) -> RssFeed:
    response = requests.get(url)

    response.raise_for_status()

    d = feedparser.parse(response.text)
    first_entries = d.entries[:ENTRIES_PER_FEED]
    items = list(to_rss_item(entry) for entry in first_entries)
    return RssFeed(
        d.feed.title,
        items,
    )
