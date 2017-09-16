import urllib2, urlparse
from BeautifulSoup import BeautifulSoup

class Crawler_Single_Threaded(object):
    def __init__(self):
        self.crawl_queue = []
        self.seen = set()

    def crawl(self, base_url):
        self.crawl_queue = [base_url]
        self.seen.add(base_url)

        while len(self.crawl_queue) > 0:
            links = self.findLinks(self.crawl_queue.pop())
            for link in links:
                if link not in self.seen:
                    self.seen.add(link)
                    self.crawl_queue.append(link)
        return self.seen


    def findLinks(self, link):
        #crawled_urls = []
        html_page = urllib2.urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        for atag in soup.findAll('a'):
            lnk = atag.get('href')
            if lnk is None:
                continue
            else:
                lnk = lnk.encode('utf-8')
                if lnk.startswith('http:') or lnk.startswith('https:'):
                    #crawled_urls.append(lnk)
                    yield lnk
                else:
                    #crawled_urls.append(urlparse.urljoin(link, lnk) + "")
                    yield urlparse.urljoin(link, lnk) + ""

        #return crawled_urls

C = Crawler_Single_Threaded()
print C.crawl('http://www.google.com')
