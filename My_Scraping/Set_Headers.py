import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'zh-CN,zh;q=0.9'}

# Android
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-AL10; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.1.11 Chrome/70.0.3538.64 Mobile Safari/537.36',
#           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Language': 'zh-CN,en-CN;q=0.9,en-US;q=0.8'}

url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)

bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table', {'class': 'table-striped'}).get_text)
