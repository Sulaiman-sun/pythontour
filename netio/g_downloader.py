from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()
import requests
from functools import partial


class GDownloader:

    def __init__(self, concurrence, headers=None):
        self.pool = Pool(concurrence)
        self.session = requests.session()
        self.headers = headers

    def process(self, urls):
        self.pool.map(partial(self.download, headers=self.headers), urls)
        self.pool.join()

    def download(self, url, headers=None, method='GET'):
        rsp = self.session.request(method=method, url=url, headers=headers)
        self.save(rsp.content)

    def save(self, data):
        pass
