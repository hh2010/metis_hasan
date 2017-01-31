""" Project Luther - Get Stock Data from API and Webscraper """

# Need to use Selenium because Yahoo Finance data is in Javascript
from urllib.request import urlopen
import pandas as pd
import numpy as np
import re
import csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yahoo_finance import Share

ticker = ['AAPL', 'MSFT', 'XOM'] # Will need to make this read from csv

def query_sic(sym):
    ''' Scrape SIC Code (Industry Sector) '''
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + sym.upper()
    url += '&Find=Search&owner=exclude&action=getcompany'
    res = urlopen(url)
    res = res.read()
    soup = bs(res, "lxml")
    return [int(soup.find_all('a')[9].contents[0]),
            soup.p.text.split(' - ')[1].split('State location')[0]]

#  print query_sic(ticker[0])

# Scrape websites for financial data

#  chromedriver = "/Applications/chromedriver"
#  profile_url = 'http://finance.yahoo.com/quote/AAPL/profile?p=' + ticker[0] # iterate

def ceo(sym):
    ''' Scrape CEO Name and Age '''
    reut_url = urlopen('http://www.reuters.com/finance/stocks/companyOfficers?' +
                       'symbol=' + sym.upper()).read() #iterate
    soup = bs(reut_url, "lxml")

    search_str = re.compile(r'Chief Executive', re.IGNORECASE)
    found_age = soup.find('td', text=search_str)
    age = found_age.find_previous_sibling('td').find_previous_sibling('td').string
    name = found_age.parent.a.string.strip()
    name = name.replace(u'\xa0', u' ')

    a = []
    top = False
    name_low = name.lower().split(" ")
    with open('ceo_list.txt', 'r', encoding='utf-8') as f:
        csvfile = csv.reader(f)
        for i in csvfile:
            a = " ".join(i).lower().replace(u'\xa0', u' ')
            if (name_low[0] in a) and (name_low[-1] in a):
                top = True
                break
    return (name, age, top)

def anal(sym):
    ''' Calculate analyst research score '''
    reut_url = urlopen('http://www.reuters.com/finance/stocks/analyst?' +
                       'symbol=' + sym.upper()).read() #iterate
    soup = bs(reut_url, "lxml")
    rec = ['BUY', 'OUTPERFORM', 'HOLD', 'UNDERPERFORM', 'SELL']
    rec_ct = []
    for i in rec:
        search_str = re.compile(i)
        rec_ct.append(soup.find('td', text=search_str).find_next_sibling().string)
    return rec_ct

#  for i in ticker:
#      print(query_sic(i)[1])
#      print(ceo(i))

#  print("Mark Zuckerberg".split(" "))
# Pull data from Morningstar API
