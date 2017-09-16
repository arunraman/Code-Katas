import urllib2, urlparse
from bs4 import BeautifulSoup
from threading import Condition , RLock, Thread
from Queue import Queue
import random

Lock = RLock()
cv = Condition(Lock)
NUMBER_OF_THREADS = 5
BASE_URL = 'http://www.facebook.com'


class Crawler_Multi_Threaded(Thread):
    def __init__(self, crawl_queue, seen):
        self.crawl_queue = crawl_queue
        self.seen = seen
        self.num_threads_waiting = [0]
        Thread.__init__(self)

    def run(self):
        while True:
        # Wait until we get a URL
            with Lock:
                self.num_threads_waiting[0] += 1
                while not self.crawl_queue.empty():
                # If all the threads are waiting, then we're done (no more# URLs to crawl)
                    if self.num_threads_waiting[0] == NUMBER_OF_THREADS:
                        cv.notify_all()
                        self.crawl_queue.task_done()
                        return
                    cv.wait()
                url = self.crawl_queue.get()
                self.num_threads_waiting[0] -= 1

            # Download and parse the page.
            links = self.get_links(url)

            # Add new URLs to 'seen' and 'todo'.
            with Lock:
                for link in links:
                    if link not in self.seen:
                        self.seen.add(link)
                        self.crawl_queue.put(link)
                self.crawl_queue.task_done()
                cv.notify_all()

    # def findLinks(self, link):
    #     crawled_urls = []
    #     html_page = urllib2.urlopen(link)
    #     soup = BeautifulSoup(html_page)
    #     for atag in soup.findAll('a'):
    #         lnk = atag.get('href')
    #         if lnk is None:
    #             continue
    #         else:
    #             lnk = lnk.encode('utf-8')
    #             if lnk.startswith('http:') or lnk.startswith('https:'):
    #                 crawled_urls.append(lnk)
    #             else:
    #                 crawled_urls.append(urlparse.urljoin(link, lnk) + "")
    #
    #     return crawled_urls

    # Fake get_links implementation.
    def get_links(url):
        return ['url%d' % n for n in random.sample(range(20), random.randrange(10))]

# Thread Generation !

def Main():
    threads = []
    crawl_q = Queue()
    crawl_q.put('url1')
    seen = set()
    seen.add(BASE_URL)
    for i in xrange(NUMBER_OF_THREADS):
        C = Crawler_Multi_Threaded(crawl_q, seen)
        #thread = Thread(target=C)
        threads.append(C.start())

    # Wait for all threads to finish.
    for t in threads:
        t.join()

    print list(seen)

Main()