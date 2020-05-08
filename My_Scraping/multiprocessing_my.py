from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

from multiprocessing import Process
import os
import time

visited = []


def getLinks(bs):
    print('Getting links in {}'.format(os.getpid()))
    links = bs.find('div', {'class': 'box hotlist'}).find_all(
        'a', href=re.compile('^(/html/((party)|(student))/).*'))
    return [link for link in links if link not in visited]


def scrap_article(path):
    visited.append(path)
    html = urlopen('http://www.zyytlz.com{}'.format(path))
    time.sleep(4)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('span', {'id': 'lbNewsTitle'}).get_text()
    print('Scraping {} in process {}'.format(title, os.getpid()))
    links = getLinks(bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        scrap_article(newArticle)


processes = []
processes.append(Process(target=scrap_article,
                         args=('/html/party/030915092015.html',)))
processes.append(Process(target=scrap_article,
                         args=('/html/student/02291L92016.html',)))

if __name__ == "__main__":
    for p in processes:
        p.start()
    for p in processes:
        p.join()
