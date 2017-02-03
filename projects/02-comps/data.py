""" Project Luther - Get Stock Data from API and Webscraper """

import os
import re
import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yahoo_finance import Share
from pprint import pprint as pp

# Formatting functions
def mb(m):
    try:
        if m[-1] == "B":
            return float(m[:-1])*1000
        else:
            return float(m[:-1])
    except:
        return float(m[:-1])

def pct(m):
    try:
        if m[-1] == "%":
            return float(int(float(m[:-1])*100)/100.00)
        else:
            return float(int(float(m)*100)/100.00)
    except:
        return float(int(float(m)*100)/100.00)

def bet(m):
    try:
        return float(int(float(m)*100)/100.00)
    except:
        return float(int(float(m)*100)/100.00)

def ifna(m):
    if m=="nan":
        return 0
    else:
        return m

def intna(m):
    return int(m.replace(',',''))

def sic_format(n):
    sic_map = {(100, 999): 1, (1000, 1499): 2, (1500, 1799): 3, (1800, 1999): 4,
               (2000, 3999): 5, (4000, 4999): 6, (5000, 5199): 7, (5200, 5999): 8,
               (6000, 6799): 9, (7000, 8999): 10, (9100, 9729): 11, (9900, 9999): 12}
    for key, val in sic_map.items():
        if all([n>=key[0], n<=key[1]]):
            return val
    return 12

# SEC Scraper to Grab SIC data

def query_sic(sym):
    ''' Scrape SIC Code (Industry Sector) '''
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + sym.upper()
    url += '&Find=Search&owner=exclude&action=getcompany'
    res = urlopen(url)
    res = res.read()
    soup = bs(res, "lxml")
    sic = soup.find_all('a')[9].contents[0]
    if sic[0] == '0':
        sic = int(sic[1:])
    else:
        sic = int(sic)
    return sic_format(sic)

# Reuters BeautifulSoup Scrapers

def ceo(sym):
    ''' Scrape CEO Name and Age '''
    reut_url = urlopen('http://www.reuters.com/finance/stocks/companyOfficers?' +
                       'symbol=' + sym).read()
    soup = bs(reut_url, "lxml")

    search_str = re.compile(r'Chief Executive', re.IGNORECASE)
    found_age = soup.find('td', text=search_str)
    age = found_age.find_previous_sibling('td').find_previous_sibling('td').string
    name = found_age.parent.a.string.strip()
    name = name.replace(u'\xa0', u' ')

    a = []
    top = False
    name_low = name.lower().split(" ")
    with open('csv/ceo_list.txt', 'r', encoding='utf-8') as f:
        csvfile = csv.reader(f)
        for i in csvfile:
            a = " ".join(i).lower().replace(u'\xa0', u' ')
            if (name_low[0] in a) and (name_low[-1] in a):
                top = True
                break
    return (name, age, top)

def anal_score(sym):
    ''' Calculate analyst research score '''
    reut_url = urlopen('http://www.reuters.com/finance/stocks/analyst?' +
                       'symbol=' + sym).read() #iterate
    soup = bs(reut_url, 'lxml')
    rec = ['BUY', 'OUTPERFORM', 'HOLD', 'UNDERPERFORM', 'SELL']
    rec_ct = []
    for i in rec:
        search_str = re.compile(i)
        rec_ct.append(soup.find('td', text=search_str).find_next_sibling().string)
    score = (int(rec_ct[0])+int(rec_ct[1])-int(rec_ct[3])-int(rec_ct[4])) # HOLDs not included
    return score

def reut_fin(sym):
    ''' Scrape for Beta and Shareholder Data '''
    reut_url = urlopen('http://www.reuters.com/finance/stocks/financialHighlights?' +
                       'symbol=' + sym).read()
    soup = bs(reut_url, 'lxml')
    search_str = re.compile(r'Beta')
    try:
        beta = bet(soup.find('td', text=search_str).find_next_sibling().string)
    except:
        beta = 1
    search_str = re.compile(r'% Shares Owned')
    try:
        inst = pct(soup.find('td', text=search_str).find_next_sibling().string)
    except:
        inst = 0
    return (beta, inst)

# Scrape WSJ using BeautifulSoup
def wsj(sym):
    ''' Scrape for EBITDA, Cash Balance, and Debt '''
    wsj_url_is = urlopen('http://quotes.wsj.com/' + sym + '/financials/annual/income-statement').read()
    wsj_url_bs = urlopen('http://quotes.wsj.com/' + sym + '/financials/annual/balance-sheet').read()
    soup = bs(wsj_url_is, 'lxml')
    search_str = re.compile(r'EBITDA')
    ebitda = intna(soup.find('td', text=search_str).find_next_sibling().string)

    soup = bs(wsj_url_bs, 'lxml')
    search_str = re.compile(r'Cash &')
    cash = intna(soup.find('td', text=search_str).find_next_sibling().string)

    search_str = re.compile(r'Long-Term Debt')
    lt_debt = intna(soup.find('td', text=search_str).find_next_sibling().string)

    search_str = re.compile(r'ST Debt')
    st_debt =  intna(soup.find('td', text=search_str).find_next_sibling().string)
    debt = (lt_debt + st_debt)
    return (cash, debt, ebitda)

# Scrape WSJ using etree

def wsj2(sym):
    ''' Scrape for EBITDA, Cash Balance, and Debt '''
    wsj_url_is = 'http://quotes.wsj.com/' + sym + '/financials/annual/income-statement'
    wsj_url_bs = 'http://quotes.wsj.com/' + sym + '/financials/annual/balance-sheet'
    page_is = requests.get(wsj_url_is)
    page_bs = requests.get(wsj_url_bs)
    tree_is = html.fromstring(page_is.content)
    tree_bs = html.fromstring(page_bs.content)
    ebitda_sel = '//*[@id="cr_cashflow"]/div[2]/div/table/tbody/tr[56]/td[2]/text()'
    lt_debt_sel = '//*[@id="cr_cashflow"]/div[3]/div[2]/table/tbody/tr[19]/td[2]/text()'
    st_debt_sel = '//*[@id="cr_cashflow"]/div[3]/div[2]/table/tbody/tr[2]/td[2]/text()'
    cash_sel = '//*[@id="cr_cashflow"]/div[2]/div[2]/table/tbody/tr[3]/td[2]/text()'
    ebitda = mb(tree_is.xpath(ebitda_sel)[0])
    cash = mb(tree_bs.xpath(cash_sel)[0])
    debt = mb(tree_bs.xpath(lt_debt_sel)[0]) + mb(tree_bs.xpatch(st_debt_sel)[0])
    return (ebitda, cash, debt)

def yah(sym):
    ''' Scrape for Cash Balance (Yahoo) '''
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    key = 'http://finance.yahoo.com/quote/'+sym+'/key-statistics?p='+sym
    hold = 'http://finance.yahoo.com/quote/'+sym+'/holders?p='+sym

    # Scrape data from key statistics page
    driver.get(key)
    cash_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/' \
                + 'section/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[2]'
    debt_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/' \
                + 'section/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[3]/td[2]'
    ebitda_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/' \
                + 'section/div[2]/div[1]/div[2]/div[4]/table/tbody/tr[5]/td[2]'
    beta_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/' \
                + 'div/section/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]'

    cash = mb(driver.find_element_by_xpath(cash_sel).text)
    debt = mb(driver.find_element_by_xpath(debt_sel).text)
    ebitda = mb(driver.find_element_by_xpath(ebitda_sel).text)
    beta = bet(driver.find_element_by_xpath(beta_sel).text)

    # Scrape data from holders page
    driver.get(hold)
    inside_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/' \
                + 'section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[1]'
    inst_sel = '//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/' \
                + 'section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[1]'
    inside = pct(driver.find_element_by_xpath(inside_sel).text)
    inst = pct(driver.find_element_by_xpath(inst_sel).text)

    return (cash, debt, ebitda, beta, inside, inst)
