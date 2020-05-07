from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
import socket
import time

html = urlopen("https://wjx.seu.edu.cn/2020/0426/c21084a325835/page.htm")
bs = BeautifulSoup(html, 'html.parser')
title = bs.find('h1', {'class': 'arti_title'}).get_text()
content = bs.find('span', {'class': 'arti_update'}).get_text()
founded = bs.find('li', {'class': 'list_item i1'}).find_all(
    'a', href=re.compile('^(/2020/0(5|4)).*'))
print(title)
print(content)
print(founded)
html.close()
