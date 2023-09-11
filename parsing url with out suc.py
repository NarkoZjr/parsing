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


html = get_html('URL')
# print(html)
bs = BeautifulSoup(html, 'lxml')
name_title = bs.find("span", class_='mw-page-title-main').get_text()
print(name_title)

# resp = requests.get(url)
# print(resp)
