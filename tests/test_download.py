from netio.g_downloader import GDownloader


def test_gdownloader():
    url = 'https://www.bing.com'
    amt = 10
    concurrence = 5
    downloader = GDownloader(concurrence)
    downloader.process([url] * amt)


if __name__ == '__main__':
    test_gdownloader()
