from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Feed(db.Model):
    __tablename__ = "feed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, url: str):
        self.url = url


    def __repr__(self) -> str:
        return f"{self.url}"
