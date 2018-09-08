from abc import ABC, abstractmethod
from Consts import RES_ETAG
import re


class CacheItem():
    def __init__(self, etag, response, headers, **kwargs):
        self.response = response
        self.headers = headers
        self.etag = etag


class RequesterCache(ABC):

    def __init__(self, size=None):
        self._cache = {}

    def lookup(self, url):
        return self._cache.get(url)

    def _construct_item(self, url, responseHeaders, output, item=CacheItem):
        if RES_ETAG in responseHeaders:
            etag_rgx = re.compile(r'"[^"]+"')
            etag = etag_rgx.search(responseHeaders[RES_ETAG])
            if etag:
                return item(etag.group(), output, responseHeaders, url=url)
        return None


    @abstractmethod
    def insert(self, url, responseHeaders, output):
        pass


class AggressiveCache(RequesterCache):
    def insert(self, url, responseHeaders, output):
        self._cache[url] = self._construct_item(url, responseHeaders, output)


class ClockCache(RequesterCache):

    class ClockItem(CacheItem):
        def __init__(self, etag, response, headers, **kwargs):
            super().__init__(etag, response, headers)
            self._dirty = True
            self._url = kwargs.get('url')

    def __init__(self, size=30):
        self._cache = [None] * size
        self._current = 0
        self._size = size

    def insert(self, url, responseHeaders, output):
        inserted = False
        while (not inserted):
            curr = self._cache[self._current]
            if (curr is None or not curr._dirty):
                self._cache[self._current] = self._construct_item(url, responseHeaders, output, self.ClockItem)
                inserted = True
            else:
                curr._dirty = False
            self._current = (self._current + 1) % self._size

    def lookup(self, url):
        curr = self._cache[self._current]
        if curr is not None and curr._url == url:
            curr._dirty = True
            return curr
        start = self._current
        self._current = (self._current + 1) % self._size
        while (start != self._current):
            curr = self._cache[self._current]
            if (curr is not None):
                if (curr._url == url):
                    return curr
                else:
                    curr._dirty = False
            self._current = (self._current + 1) % self._size
        return None
