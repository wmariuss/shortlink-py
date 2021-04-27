from app import db


class UrlMapping(db.Model):
    __tablename__ = "short"

    url_id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255), unique=True, nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

    def __repr__(self):
        return "Long URL: {} to short URL: {}".format(self.long_url, self.short_url)

    def serialise(self):
        return {"long_url": self.long_url, "short_url": self.short_url}
