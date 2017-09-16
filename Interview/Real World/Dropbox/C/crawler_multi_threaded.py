import urllib2, urlparse
from bs4 import BeautifulSoup
from threading import Condition , RLock, Thread
from Queue import Queue

Lock = RLock()
NUMBER_OF_THREADS = 1
BASE_URL = 'http://localhost:9999/test.html'


class Crawler_Multi_Threaded(Thread):
    def __init__(self, crawl_queue, seen):
        self.crawl_queue = crawl_queue
        self.seen = seen
        Thread.__init__(self)

    def run(self):
        while True:
            # Wait until we get a URL
            links = self.findLinks(self.crawl_queue.get())
            print links
            for link in links:
                Lock.acquire()
                if link not in self.seen:
                    self.seen.add(link)
                    self.crawl_queue.put(link)
                    Lock.release()
                self.crawl_queue.task_done()

    def findLinks(self, link):
        crawled_urls = []
        html_page = urllib2.urlopen(link)
        soup = BeautifulSoup(html_page, "html.parser")
        for atag in soup.findAll('a'):
            lnk = atag.get('href')
            if lnk is None:
                continue
            else:
                lnk = lnk.encode('utf-8')
                if lnk.startswith('http:') or lnk.startswith('https:'):
                    crawled_urls.append(lnk)
                else:
                    crawled_urls.append(urlparse.urljoin(link, lnk) + "")

        return crawled_urls

# Thread Generation !

def Main():
    crawl_q = Queue()
    crawl_q.put(BASE_URL)
    seen = set()
    seen.add(BASE_URL)
    for i in xrange(NUMBER_OF_THREADS):
        C = Crawler_Multi_Threaded(crawl_q, seen)
        C.setDaemon(True)
        C.start()

    crawl_q.join()
    print list(seen)

Main()