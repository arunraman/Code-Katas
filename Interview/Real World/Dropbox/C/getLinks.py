from threading import Condition, Lock, Thread
import urllib2, urlparse
from BeautifulSoup import BeautifulSoup


class Crawler(object):

    def __init__(self, num_threads):
        self.Lock = Lock()
        self.condition_var = Condition(self.Lock)
        self.crawl_list = []
        self.seen = set()
        self.waiting_threads = 0
        self.number_of_threads = num_threads
        self.threads = []

    def main(self, starting_url):
        self.crawl_list.append(starting_url)
        self.seen.add(starting_url)

        # Start threads.
        for i in xrange(self.number_of_threads):
            thread = Thread(target=self.crawler)  # args=(self.crawl_list, self.seen, self.waiting_threads))
            thread.start()
            self.threads.append(thread)

        # Wait for all threads to finish.
        for t in self.threads:
            t.join()

        return self.seen

    def crawler(self):
        while True:
        #  Wait until we get a URL
            with self.Lock:
                self.waiting_threads += 1
                # snum_threads_waiting[0] += 1
                while len(self.crawl_list) == 0:
                # If all the threads are waiting, then we're done (no more# URLs to crawl)
                    if self.waiting_threads == self.number_of_threads:
                        self.condition_var.notify_all()
                        return
                    self.condition_var.wait()
                url = self.crawl_list.pop()
                self.waiting_threads -= 1

            # Download and parse the page.
            #links = self.get_links(url)
            links = self.findLinks(url)

            # Add new URLs to 'seen' and 'crawl_list'.
            with self.Lock:
                for link in links:
                    if link not in self.seen:
                        self.seen.add(link)
                        self.crawl_list.append(link)
                self.condition_var.notify_all()

    def findLinks(self, link):
        html_page = urllib2.urlopen(link)
        soup = BeautifulSoup(html_page)
        for atag in soup.findAll('a'):
            lnk = atag.get('href')
            if lnk is None:
                continue
            else:
                lnk = lnk.encode('utf-8')
                if lnk.startswith('http:'):# or lnk.startswith('https:'):
                    yield lnk
                else:
                    yield urlparse.urljoin(link, lnk) + ""


    # Fake get_links implementation.
    # def get_links(self, url):
    #     return ['url%d' % n for n in random.sample(range(20), random.randrange(10))]


C = Crawler(5)
#print C.main('http://localhost:9999/test.html')
print C.main('https://validator.w3.org/checklink')