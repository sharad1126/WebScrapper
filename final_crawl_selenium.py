import os
import sys
import subprocess
import glob
from os import path
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class Crawler(object):
 def crawl_data(self):
  chrome_options = Options()
  chrome_options.add_argument('headless')#using headless so it doesn't opens chrome windows
  chrome_options.add_argument('--ignore-certificate-errors')
  chrome_options.add_argument('--no-sandbox')
  #chrome_options.add_argument("--window-size=1920,1080")
  # Using the crome driver file path
  desired_capabilities = DesiredCapabilities.CHROME.copy()
  desired_capabilities['acceptSslCerts'] = True
  desired_capabilities['acceptInsecureCerts'] = True
  driver = webdriver.Chrome('/Users/SharadAggrawal/Downloads/chromedriver', chrome_options=chrome_options, desired_capabilities = desired_capabilities)
  #driver.get('http://root:root@<url/ip>')
  #driver.get('<ip addresss/url>')
  driver.get('https://<ip>')
  sleep(50)
  driver.save_screenshot('<path to save>/<file name>.png')
  print driver.page_source
  #with open("out.txt", 'w') as f:
  #  print >>f, driver.page_source
  #print driver.titles
  #driver.save_screenshot('<path to save>/<file name>.png')
  #bs = BeautifulSoup(driver.page_source, 'lxml')
  #print bs.find_all('a')
  driver.quit()

if __name__ == "__main__":
 crawl = Crawler()
 crawl.crawl_data();


##converting driver result to BS and using it through html parser
# result = driver.find_element_by_class_name('profile-col-main')
# htmlText =  result.get_attribute('innerHTML')
# Here we  initialized the beautiful soup to extract data from the html

# ele = bs.select_one('.profile-props')
# currency = ele.select('.propblock-body')
# Here we printing the crawled data
# print currency[2].get_text(strip=True)
# print currency[3].get_text(strip=True)
# print currency[4].get_text(strip=True)
# print bs
#print driver.find_element_by_tag_name('body')
