from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
import socket
import time

socket.setdefaulttimeout(15)

conn = pymysql.connect(host='localhost', port=3306, charset='utf8',
                       user='root', passwd='Wzf04132', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute(
        'INSERT INTO pages (title,content) VALUES ("%s","%s")', (title, content))
    cur.connection.commit()


websites = set(
    'https://www.nytimes.com/2020/05/01/health/coronavirus-vaccine-supplies.html')


def getLinks(articleUrl):
    try:
        html = urlopen(articleUrl)
    except:
        html = urlopen(
            'https://www.nytimes.com/2020/05/01/health/coronavirus-vaccine-supplies.html')

    bs = BeautifulSoup(html, 'html.parser')

    try:
        title = bs.find('h1').get_text()
        content = bs.find('p', {'id': 'article-summary'}).get_text()
    except:
        title = None
        content = None

    store(title, content)

    founded = bs.find_all(
        'a', href=re.compile('(nytimes\.com/2020).*(\.html)$'))
    html.close()
    return founded


times = 0
links = getLinks(
    'https://www.nytimes.com/2020/05/01/health/coronavirus-vaccine-supplies.html')

try:
    while len(links) > 0:
        for link in links:
            newArticle = link.attrs['href']
            if newArticle not in websites:
                websites.add(newArticle)
                print(newArticle)

                time.sleep(1)
                links = getLinks(newArticle)
                times += 1
                if times > 30:
                    break
finally:
    cur.close()
    conn.close()
