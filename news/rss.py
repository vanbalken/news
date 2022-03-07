import feedparser

from dataclasses import dataclass
from typing import List

from .const import ENTRIES_PER_FEED


@dataclass
class RssItem:
    title: str
    link: str


@dataclass
class RssFeed:
    title: str
    items: List[RssItem]


def to_rss_item(entry: any) -> RssItem:
    return RssItem(
        entry.title,
        entry.link,
    )


def to_rss_feed(url: str) -> RssFeed:
    d = feedparser.parse(url)
    first_entries = d.entries[:ENTRIES_PER_FEED]
    items = (to_rss_item(entry) for entry in first_entries)
    return RssFeed(
        d.feed.title,
        items,
    )
