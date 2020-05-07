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


def getLinks(articleUrl):
    html = urlopen('http://www.zyytlz.com'+articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    try:
        title = bs.find('span', {'id': 'lbNewsTitle'}).get_text()
        content = bs.find('div', {'class': 'ep-info'}).get_text()
    except:
        title = 'None'
        content = 'Error'

    store(title, content)
    founded = bs.find('div', {'class': 'box hotlist'}).find_all(
        'a', href=re.compile('^(/html/party/).*'))
    html.close()
    return founded


times = 0
links = getLinks('/html/party/030915092015.html')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        time.sleep(2)
        links = getLinks(newArticle)
        times += 1
        if times > 20:
            break
finally:
    cur.close()
    conn.close()
