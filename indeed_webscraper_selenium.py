from bs4 import BeautifulSoup
from lxml import etree as et
from csv import writer
import time
from time import sleep
import pandas as pd
from random import randint
import threading
from concurrent.futures import ThreadPoolExecutor, wait
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


option= webdriver.ChromeOptions()
option.add_argument("--incognito") # scrawl in the undercover

# Define job and location search keywords
job_search_keyword = ['Data+Scientist', 'Business+Analyst', 'Data+Engineer', 
                      'Python+Developer', 'Full+Stack+Developer', 
                      'Machine+Learning+Engineer']

# Locations
location_search_keyword = ['Berlin', 'Dortmund', 'Kassel']

# Finding location, position, radius=35 miles, sort by date and starting page
paginaton_url = 'https://www.indeed.com/jobs?q={}&l={}&radius=35&filter=0&sort=date&start={}'

#print(paginaton_url)

start = time.time()


job_='Data+Engineer'
location='Washington'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                         options=option)


driver.get(paginaton_url.format(job_,location,0))

# t = ScrapeThread(url_)
# t.start()

sleep(randint(2, 6))

#p=driver.find_element(By.CLASS_NAME,'jobsearch-JobCountAndSortPane-jobCount').text

# Max number of pages for this search! There is a caveat described soon
#max_iter_pgs=int(p.split(' ')[0])//15 


driver.quit() # Closing the browser we opened


end = time.time()

