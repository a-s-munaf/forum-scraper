import os

from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

class UniqueURLFilter(RFPDupeFilter):
    """A dupe filter that considers each url as a unique key"""
    def __getid(self, url):
        return str(url)

    def request_seen(self, request):
        fp = self.__getid(request.url)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)
