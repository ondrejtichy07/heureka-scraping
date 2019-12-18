#Python program to scrape website
from bs4 import BeautifulSoup
from datetime import date
from termcolor import colored
import xlsxwriter
import csv
import requests
import time

URL = 'https://mysi.heureka.cz/logitech-mx-master-3-advanced-wireless-mouse-910-005710/'

column_num = 1
column_date = 0
values = []
dates = []

def print_value():
    r = requests.get(URL)
    row = 0
    soup = BeautifulSoup(r.content, 'html5lib')
    value = soup.find('span', {'class': 'js-top-price'}).get_text()

    today = date.today().strftime("%d.%m.%Y")

    res = value.replace(' Kč','')
    result = res.replace(' ', '')
    print(colored(result,'green'))

    values.append(result)
    dates.append(today)

    workbook = xlsxwriter.Workbook('price_for_mx_master3.xlsx')
    worksheet = workbook.add_worksheet()

    for item in values:
        worksheet.write(row, column_num, item)
        worksheet.write(row, column_date, today)
        row += 1

    workbook.close()
    time.sleep(86400)

while True:
    print_value()