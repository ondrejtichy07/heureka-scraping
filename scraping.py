#Python program to scrape website
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import date
from termcolor import colored
import csv
import requests
import time

URL = 'https://mysi.heureka.cz/logitech-mx-master-3-advanced-wireless-mouse-910-005710/'
r = requests.get(URL)
num = 1

soup = BeautifulSoup(r.content, 'html5lib')
value = soup.find('span', {'class': 'js-top-price'}).get_text()

res = value.replace(' Kč','')
result = res.replace(' ', '')
print(colored(result,'green'))

def print_value():
    today = date.today().strftime("%d.%m.%Y")
    name = "price_for_mx_master3.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet[f'A{num}'] = today
    sheet[f'B{num}'] = int(result)
    workbook.save(filename=name)
    time.sleep(86400)

while True:
    print_value()
    num+=1
