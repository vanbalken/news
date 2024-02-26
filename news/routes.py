from flask import current_app as app
from flask import render_template

from .const import URLS
from .rss import to_rss_feed


@app.route("/")
def home() -> str:
    feeds = (to_rss_feed(url) for url in URLS)

    return render_template("home.html", feeds=feeds)
