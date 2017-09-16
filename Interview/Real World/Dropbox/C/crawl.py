from HTMLParser import HTMLParser
import urlparse
import urllib2
import Queue
from threading import Thread, Lock


#START_URL = 'http://localhost:9999/test.html'
START_URL = 'http://www.google.com'
#MAX_DEPTH = 1
NUM_THREADS = 5

debug = True
print_lock = Lock()

class CrawlRequest:
    def __init__(self, url):
        self.url = url
        #self.level = level

class CrawlResult:
    def __init__(self, url, data, html = False):
        self.url = url
        #self.level = level
        self.data = data
        self.html = html

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.urls = list()

    def handle_starttag(self, tag, attrs):
        url = None
        if tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    url = value
                    break
        elif tag == 'img':
            for key, value in attrs:
                if key == 'src':
                    url = value
                    break
        if url is not None:
            url = urlparse.urljoin(self.base_url, url)
            url = urlparse.urldefrag(url)[0]  # remove fragment
            url = url.rstrip('/')
            self.urls.append(url)

    def run(self, data):
        self.feed(data)
        return self.urls


class CrawlThread(Thread):
    def __init__(self, in_queue, out_queue):
        super(CrawlThread, self).__init__()
        self.in_queue = in_queue    # queue of CrawlRequest
        self.out_queue = out_queue  # queue of CrawlResult

    def run(self):
        while True:
            request = self.in_queue.get()
            url = request.url
            if url is None: # command to stop the thread
                self.in_queue.task_done()
                break
            if debug:
                with print_lock: print self.name, "- START", url
            try:
                response = urllib2.urlopen(url)
            except urllib2.URLError:
                if debug:
                    with print_lock: print self.name, "- FAIL ", url
                self.out_queue.put(CrawlResult(url, None))  # no data
            else:
                try:
                    html = response.headers['content-type'][:9] == 'text/html'
                except KeyError:
                    html = True  # ???
                data = response.read()
                self.out_queue.put(CrawlResult(url, data, html))
                if debug:
                    with print_lock: print self.name, "- END  ", url
            self.in_queue.task_done()
        if debug:
            with print_lock: print self.name, "stopped"


class Crawler():
    def __init__(self, start_url, num_threads=NUM_THREADS):
        self.num_threads = num_threads
        self.urls = Queue.Queue()
        self.urls.put(CrawlRequest(start_url))
        self.contents = Queue.Queue()
        self.seen = set()
        self.seen.add(start_url)
        self.errors = dict()
        self.counter = 1

    def run(self):
        threads = [CrawlThread(self.urls, self.contents) for _ in range(self.num_threads)]
        for t in threads:
            t.setDaemon(True)
            t.start()

        while self.counter > 0:
            result = self.contents.get()
            self.counter -= 1
            with print_lock:
                print "MainThrd - RCVD ", result.url, \
                                   "[", len(result.data) if result.data is not None else 0, "]"
                if result.data is not None:
                    if result.html:
                        parser = LinkParser(result.url)
                        for url in parser.run(result.data):
                            if url not in self.seen:
                                self.seen.add(url)
                                self.urls.put(CrawlRequest(url))
                                self.counter += 1
                else:  # some error
                    self.errors[result.url] = "Could not access"
            self.contents.task_done()

        for t in threads:
           self.urls.put(CrawlRequest(None))  # command to stop the thread

        for t in threads:
            t.join()  # wait for threads to stop

        return self.seen


if __name__ == "__main__":
    crawler = Crawler(START_URL)
    print len(list(crawler.run()))
    #errors = crawler.run()
    #print '*'*10, "Errors", '*'*10
    #for url, error in sorted(errors.iteritems()):
    #    print url, "->", error