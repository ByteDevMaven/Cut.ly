import hashlib

class UrlShortener:
    def shorten_url(self, original_url):
        hash_value = hashlib.md5(original_url.encode()).hexdigest()[:6]
        short_url = hash_value
        return short_url