from flask import current_app as app
from flask import render_template

from .const import URLS
from .rss import to_rss_feed


@app.route("/")
def home() -> str:
    feeds = (to_rss_feed(url) for url in URLS)
    filtered_feeds = filter(lambda r : r is not None, feeds)

    return render_template("home.html", feeds=filtered_feeds)
