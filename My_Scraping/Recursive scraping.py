import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import re


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

    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

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

    def parse(self, url):
        """从URL提取内容"""
        bs = self.getPageCh(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
        self.craw()

    def craw(self):
        """获取链接"""
        bs = self.getPage(self.site.url)
        targetPages = bs.find_all(
            'a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)


Wb = Website('PY', 'https://blog.csdn.net/yinyiyu/article/details/105722144?depth_1-utm_source=distribute.pc_category.none-task-blog-hot-7&request_id=&utm_source=distribute.pc_category.none-task-blog-hot-7', '.*', True,
             'h1.title-article', 'div#article-content')
crawler = Crawler(Wb)
crawler.craw()
print(crawler.visited)

# '#'匹配id//'.'匹配class
