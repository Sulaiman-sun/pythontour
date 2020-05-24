import asyncio
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


async def get(url):
    cli = AsyncHTTPClient()
    rsp = await cli.fetch(url)
    return rsp


async def multi_start(urls):
    # start all tasks
    tasks = [asyncio.create_task(get(url)) for url in urls]
    # wait until all tasks finish
    for task in tasks:
        body = await task
        print(body.code)


def run():
    url = 'https://www.bing.com'
    urls = [url] * 10
    asyncio.run(multi_start(urls))
    # IOLoop.current().run_sync(lambda: multi_start(urls))  # use tornado IOLoop


if __name__ == '__main__':
    run()
