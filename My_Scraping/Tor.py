import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

# 在使用Selenium和driver时，只需要在前面加上
# service_args=['--proxy=localhost:9150','--proxy-type=socks5']
