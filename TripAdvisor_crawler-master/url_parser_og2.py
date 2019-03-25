# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import json
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
with open('./data/url_parser.txt', 'a') as jsonfile:
    fieldnames = ['hotel_id', 'hotel_name', 'n_comment', 'rank_in_country', 'url']
    writer = json.dump(fieldnames, jsonfile)
    #writer.writeheader()
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
        for element in hotel_blocks:
            index += 1
            res_name = element.find('div', {"class": "title"}).text.strip()
            print("rest:", res_name)
            url = domain+element.find('div', {"class": "title"}).find('a').get('href')
            print(url)
            rating = None
            r = 50
            while rating == None and r > 0:
                rating = element.find('span',{"class": "ui_bubble_rating bubble_{}".format(r)})
                r -= 5
            rating = rating.get('alt')
            rating = float(rating.replace(' of 5 bubbles',''))
            print('rating:',rating)
            if rating >= 4 or rating <=2:
                print('rating:',rating)
                json.dump({'hotel_id':index,'hotel_name':res_name.encode("utf-8"),'rating':rating,'url':url}, jsonfile)
        try:
            driver.execute_script(page_down)
            time.sleep(5)
            driver.find_element_by_xpath(next_page).click()
            time.sleep(8)
        except:
            print('in the end')
            
driver.quit()

