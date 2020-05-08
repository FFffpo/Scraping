#import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
#import threading
import _thread
from queue import Queue
import time
import pymysql

#session = requests.Session()
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'zh-CN,zh;q=0.9'}


def storage(queue):
    conn = pymysql.connect(host='localhost', port=3306,
                           charset='utf8', user='root', passwd='Wzf04132', db='mysql')
    cur = conn.cursor()
    cur.execute('USE wiki_threads')
    while 1:
        if not queue.empty():
            article = queue.get()
            cur.execute(
                'SELECT * FROM pages WHERE path = %s', (article["path"]))
            if cur.rowcount == 0:
                print("Storing article {}".format(article["path"]))
                cur.execute('INSERT INTO pages (title,path) VALUES (%s,%s)',
                            (article["title"], article["path"]))
                conn.commit()
            else:
                print("Article already exists: {}".format(article['title']))


visited = []


def getLinks(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    links = bs.find('div', {'class': 'box hotlist'}).find_all(
        'a', href=re.compile('^(/html/((party)|(student))/).*'))
    return [link for link in links if link not in visited]


def scrap_article(thread_name, path, queue):
    visited.append(path)
    html = urlopen('http://www.zyytlz.com{}'.format(path))
    time.sleep(4)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('span', {'id': 'lbNewsTitle'}).get_text()
    print('Added {} for storage in thread {}'.format(title, thread_name))
    queue.put({"title": title, "path": path})
    links = getLinks(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        scrap_article(thread_name, newArticle, queue)


queue = Queue()

try:
    #threading.Thread(target=scrap_article, args=('Thread_1', '/html/party/030915092015.html', queue)).start()
    #threading.Thread(target=scrap_article, args=('Thread_2', '/html/student/02291L92016.html', queue)).start()
    #threading.Thread(target=storage, args=(queue)).start()
    _thread.start_new_thread(
        scrap_article, ('Thread_1', '/html/party/030915092015.html', queue,))
    _thread.start_new_thread(
        scrap_article, ('Thread_2', '/html/student/02291L92016.html', queue,))
    _thread.start_new_thread(storage, (queue,))
except:
    print('Error!')

while 1:
    pass

# 转换支持中文
# ALTER DATABASE wiki_threads CHARACTER SET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# TRUNCATE TABLE pages;清空数据表
