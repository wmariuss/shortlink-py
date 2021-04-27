import hashlib
import base62

from app import SHORTENED_LENGTH


class SHA256Shortener:
    def shorten(self, long_url) -> str:
        hashed_url = self.__sha256(long_url)
        return base62.encode(hashed_url)[:SHORTENED_LENGTH]

    @staticmethod
    def __sha256(url) -> int:
        sha3hex = hashlib.sha256(url.encode()).hexdigest()
        return int(sha3hex, 16)
