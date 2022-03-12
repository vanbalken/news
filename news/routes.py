from flask import current_app as app
from flask import render_template, request
from flask_restful import Resource, Api

from .const import URLS
from .models import db, Feed
from .rss import to_rss_feed


class FeedList(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        url = json_data["url"]

        feed = Feed(url)
        db.session.add(feed)
        db.session.commit()

        return {}


@app.route("/")
def home():
    feeds = (to_rss_feed(url) for url in URLS)

    return render_template("home.html", feeds=feeds)


api = Api(app)
api.add_resource(FeedList, "/feeds")        
