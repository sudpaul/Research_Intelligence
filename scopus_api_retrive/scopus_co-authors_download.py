# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:15:17 2018

@author: z3525552
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = 'https://www.scopus.com/authid/detail.url?authorId='

scopus_id = input('Please enter author SCOPUS Id')
url = link+scopus_id

try:
   driver = webdriver.Chrome(executable_path="C:/Users/z3525552/Downloads/chromedriver_win32/chromedriver.exe")
   driver.get(url)
   driver.implicitly_wait(5)

   co_authors = driver.find_element_by_id('coAuthLi')
   co_authors.click()
   
   overview = driver.find_element_by_link_text('View co-author overview')
   overview.click()
   driver.implicitly_wait(2)

   export = driver.find_element_by_id("export_results")
   export.click()
   driver.implicitly_wait(2)

   csv_export = driver.find_element_by_class_name("radio")
   csv_export.click()
   driver.implicitly_wait(1)

   result = driver.find_element_by_css_selector("button.btn.btn-primary.btn-sm.pull-right.dropdownActionButton.exportButton") 
   result.click()
    
finally:
        driver.close()





