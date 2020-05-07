import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


class Content:
    """所有页面的基类"""

    def __init__(self, url, tittle, body):
        self.url = url
        self.tittle = tittle
        self.body = body

    def print(self):
        print("URL:{}".format(self.url))
        print("TITLE:{}".format(self.tittle))
        print("BODY:{}".format(self.body))


class Website:
    """网页结构"""

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def getPageCh(self, url):
        try:
            req = urlopen(url)
        except HTTPError as e:
            print(e)
            return None
        except URLError as e:
            print('server error')
            return None
        else:
            return BeautifulSoup(req, 'html.parser')

    def safeGet(self, pageObj, selector):
        selectedElements = pageObj.select(selector)
        if selectedElements is not None and len(selectedElements) > 0:
            # return '\n'.join([elem.get_txt() for elem in selectedElements])
            return selectedElements
        return ''

    def parse(self, site, url):
        """从URL提取内容"""
        bs = self.getPageCh(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


Wb = Website('Py', 'http://www.zyytlz.com',
             'span#lbNewsTitle', 'div.endText')
crawler = Crawler()
crawler.parse(Wb, 'http://www.zyytlz.com/html/party/030915092015.html')
