import asyncio
from asyncio import Queue
import aiohttp


class AsyncDownloader:

    def __init__(self, concurrence=10, headers=None):
        self.queue = Queue(concurrence)
        self.headers = headers
        self.concurrence = concurrence

    async def push_task(self, urls):
        for idx, url in enumerate(urls):
            await self.queue.put((idx, url))
            print(f"pushed {idx}")

    async def worker(self):
        async with aiohttp.ClientSession() as session:
            while True:
                # print('worker start')
                idx, url = await self.queue.get()
                # print(f'{idx} start')
                rsp = await self.download(session=session, url=url, headers=self.headers)
                await self.save(rsp)
                self.queue.task_done()

    async def process(self, urls):
        tasks = asyncio.create_task(self.push_task(urls))
        workers = [asyncio.create_task(self.worker()) for _ in range(self.concurrence)]
        await tasks
        await self.queue.join()
        for worker in workers:
            worker.cancel()

    @staticmethod
    async def download(session, url, headers=None, method='GET'):
        async with session.request(method=method, url=url, headers=headers) as rsp:
            data = await rsp.text()
        return data

    async def save(self, data):
        pass


async def main():
    url = 'https://www.bing.com'
    downloader = AsyncDownloader(concurrence=10)
    await downloader.process(urls=[url] * 20)


if __name__ == '__main__':
    asyncio.run(main())
