import feedparser

from datetime import datetime, timezone
from time import mktime
from dataclasses import dataclass
from typing import List
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


def to_rss_item(entry: any) -> RssItem:
    published_dt = datetime.fromtimestamp(mktime(entry.published_parsed)).replace(tzinfo=timezone.utc).astimezone(ZoneInfo("Europe/Amsterdam"))
    published = published_dt.strftime("%d-%m %H:%M")

    return RssItem(
        entry.title,
        entry.link,
        published,
    )


def to_rss_feed(url: str) -> RssFeed:
    d = feedparser.parse(url)
    first_entries = d.entries[:ENTRIES_PER_FEED]
    items = (to_rss_item(entry) for entry in first_entries)
    return RssFeed(
        d.feed.title,
        items,
    )
