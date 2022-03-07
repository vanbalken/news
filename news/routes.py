from flask import render_template


from flask import current_app as app
from flask import render_template
import feedparser


@app.route("/")
def home():
    urls = [
        "http://feeds.bbci.co.uk/news/rss.xml",
        "http://feeds.nos.nl/nosnieuwsalgemeen",
        "https://news.ycombinator.com/rss",
        "http://feeds.feedburner.com/tweakers/nieuws",

    ]

    dd = map(feedparser.parse, urls)
    
    return render_template("home.html", dd=dd)