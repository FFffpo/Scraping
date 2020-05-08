# 进程间通讯，共同抓取
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from multiprocessing import Process, Queue
import os
import time


def task_delegator(taskQueue, urlsQueue):
    # 为每个进程初始化一个任务
    visited = ['/html/party/030915092015.html',
               '/html/student/02291L92016.html']
    taskQueue.put('/html/party/030915092015.html')
    taskQueue.put('/html/student/02291L92016.html')

    while 1:
        # 检查urlsQueue中是否有新的链接需要处理
        if not urlsQueue.empty():
            links = [link for link in urlsQueue.get() if link not in visited]
            for link in links:
                # 向taskQueue中添加链接
                taskQueue.put(link)


def getLinks(bs):
    links = bs.find('div', {'class': 'box hotlist'}).find_all(
        'a', href=re.compile('^(/html/((party)|(student))/).*'))
    return [link.attrs['href'] for link in links]


def scrap_article(taskQueue, urlsQueue):
    while 1:
        while taskQueue.empty():
            # 如果任务列表为空，停止100ms
            time.sleep(.1)
        path = taskQueue.get()
        html = urlopen('http://www.zyytlz.com{}'.format(path))
        time.sleep(4)
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.find('span', {'id': 'lbNewsTitle'}).get_text()
        print('Scraping {} in process {}'.format(title, os.getpid()))
        links = getLinks(bs)
        # 发送到委托器
        urlsQueue.put(links)


processes = []
taskQueue = Queue()
urlsQueue = Queue()
processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrap_article, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrap_article, args=(taskQueue, urlsQueue)))

if __name__ == "__main__":
    for p in processes:
        p.start()
    for p in processes:
        p.join()

# 也可以开多个爬虫，分别抓取不同部分
