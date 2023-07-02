from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:\Videos\Ecucation videos\[FreeCourseSite.com] Udemy - Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023\TEST_WORK\chromedriver'
# define 'driver' variable
driver = webdriver.Chrome(path)
# open Google Chrome with chromedriver
driver.get(website)