from app import db, SHORTENED_LENGTH
from app.url_generator import SHA256Shortener
from app.models import UrlMapping


class UrlManager:
    class UrlManagerException(Exception):
        pass

    MAX_NUM_HASHES = 62 ** SHORTENED_LENGTH

    def __init__(self, generator=SHA256Shortener()):
        self.generator = generator

    def set_short_url(self, long_url, short_url):
        # need to ensure short url does not exist
        if not self.is_short_url_exists(short_url):
            self.__save_data(long_url, short_url)
        else:
            raise UrlManager.UrlManagerException("Short URL already exists")

    def get_short_url(self, long_url):
        # check if value exists in db
        data = UrlMapping.query.filter_by(long_url=long_url).first()
        if data is not None:
            return data.serialise()["short_url"]

        # shorten value
        short_url = self.generator.shorten(long_url)
        # check if the short url given by generator exists
        collision = True
        while collision:
            if self.is_short_url_exists(short_url):
                # short url is mapped to another long url
                self.generator.shorten(short_url)
            else:
                collision = False

        self.__save_data(long_url, short_url)
        return short_url

    def get_long_url(self, short_url):
        data = UrlMapping.query.filter_by(short_url=short_url).first()
        if data is not None:
            return data.serialise()["long_url"]

        # data does not exist
        return None

    def is_short_url_exists(self, short_url):
        data = UrlMapping.query.filter_by(short_url=short_url).first()
        return data is not None

    def delete_short_url(self, short_url):
        UrlMapping.query.filter_by(short_url=short_url).delete()
        db.session.commit()

    def __save_data(self, long_url, short_url):
        new_mapping = UrlMapping(long_url, short_url)
        db.session.add(new_mapping)
        db.session.commit()

    def get_all_previous_data(self):
        data = UrlMapping.query.all()
        return data

    def get_hash_table_usage(self):
        num_entries = len(self.get_all_previous_data())
        usage = num_entries / UrlManager.MAX_NUM_HASHES * 100
        return usage


url_manager = UrlManager()
