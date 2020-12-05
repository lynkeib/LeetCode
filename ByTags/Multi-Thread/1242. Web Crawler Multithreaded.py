# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from concurrent import futures


class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        hostname = lambda url: url.split("/")[2]
        seen = set([startUrl])

        with futures.ThreadPoolExecutor() as executor:
            tasks = [executor.submit(htmlParser.getUrls, startUrl)]
            while tasks:
                finished = tasks.pop(0).result()
                for url in finished:
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        return list(seen)


from Queue import Queue
from threading import Lock
from concurrent import futures


class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        hostname = lambda url: url.split("/")[2]
        seen = set([startUrl])
        queue = Queue()
        lock = Lock()

        def worker():
            try:
                while True:
                    url = queue.get(timeout=0.015)
                    for url in htmlParser.getUrls(url):
                        lock.acquire()
                        if url not in seen and hostname(startUrl) == hostname(url):
                            seen.add(url)
                            queue.put(url)
                        lock.release()
                    queue.task_done()
            except:
                pass

        queue.put(startUrl)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            for _ in range(8):
                executor.submit(worker)

        return list(seen)

