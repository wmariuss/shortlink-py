class UrlParser:

    HTTP = "http://"
    HTTPS = "https://"

    @staticmethod
    def parse(url):
        if url.startswith(UrlParser.HTTP):
            return UrlParser.HTTP, url[len(UrlParser.HTTP) :]
        elif url.startswith(UrlParser.HTTPS):
            return UrlParser.HTTPS, url[len(UrlParser.HTTPS) :]
        else:
            return UrlParser.HTTP, url
