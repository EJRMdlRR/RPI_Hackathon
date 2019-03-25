# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
target_url = 'https://www.tripadvisor.com/Restaurants-g48739-Troy_New_York.html'
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get(target_url)
driver.maximize_window()    

soup = BeautifulSoup(driver.page_source, 'html.parser')
domain = 'https://www.tripadvisor.com'

# scrape page
next_page = '//div[@class="deckTools btm"]/div/a[1]'
check_last_page = '#EATERY_LIST_CONTENTS > div > div > div > a.pageNum.taLnk'
page_down = "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
#print(soup.select(check_last_page)[-1])
page_list = range(int(soup.select(check_last_page)[-1].get('data-page-number')))
print("Total number of page: {}".format(len(page_list)))
with open('./data/url_parser.csv', 'a') as csvfile:
    fieldnames = ['hotel_id', 'hotel_name', 'n_comment', 'rank_in_country', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    index = 0

    for p in page_list:
        hotel_blocks = []
        for i in range(1,31):
            if i == 1:
                hotel_blocks.append(soup.find('div', {"class": "listing rebrand listingIndex-{} first".format(str(i))}))
            else:
                hotel_blocks.append(soup.find('div', {"class": "listing rebrand listingIndex-{}".format(str(i))}))
        print('the number of page = {0}/{1}'.format(p+1, len(page_list)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #hotel_blocks = soup.find_all('div', {"class": "listing rebrand listingIndex-1 first"})
        #print(hotel_blocks, 'stupid')
        for element in hotel_blocks:
            index += 1
            res_name = element.find('div', {"class": "title"}).text
            #print(res_name, 'name')
            url = domain+element.find('div', {"class": "title"}).find('a').get('href')
            #print(url)
            n_comment = element.find('span', {"class": "reviewCount"}).text#, {"class": "review_count"}).text
            n_comment = re.sub('[^0-9,]', "", n_comment).replace(',','')
            #print(n_comment)
            rank_in_country = element.find('div', {"class": "popIndex rebrand popIndexDefault"}).text
            writer.writerow(
                            {
                                'hotel_id':index,
                                'hotel_name':res_name.encode("utf-8"),
                                'n_comment':n_comment,
                                'rank_in_country':rank_in_country.encode("utf-8"),
                                'url':url
                            }
                           )
        try:
            driver.execute_script(page_down)
            time.sleep(5)
            driver.find_element_by_xpath(next_page).click()
            time.sleep(8)
        except:
            print('in the end')
            
driver.quit()