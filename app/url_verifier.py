import requests


class UrlVerifier:
    @staticmethod
    def is_url_valid(protocol, url):
        try:
            req = requests.get(protocol + url)  # timeout = None
            return req.status_code == 200
        except:
            return False
