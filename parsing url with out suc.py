import random
import time
from multiprocessing import Pool
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint




def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # print(headers)
    res = requests.get(url, timeout=30, headers=headers)
    # print(ua.random)
    if res.status_code == 200:
        print('OK!')
    else:
        print('Boo!')
    return res.text
#
html = get_html('https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%98%D0%BB%D1%8C%D0%B8%D1%87')
# print(html)
bs = BeautifulSoup(html, 'lxml')
name_title = bs.find("span", class_='mw-page-title-main').get_text()
print(name_title)



# resp = requests.get(url)
# print(resp)