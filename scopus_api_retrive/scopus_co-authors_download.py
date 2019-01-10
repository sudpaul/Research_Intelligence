# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:15:17 2018

@author: z3525552
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = 'https://www.scopus.com/authid/detail.url?authorId='

scopus_id = input('Please enter author SCOPUS Id ')
#scopus_url from base_url and SCOPUS author ID
url = link+scopus_id

try:
   driver = webdriver.Chrome(executable_path="C:/Users/z3525552/Downloads/chromedriver_win32/chromedriver.exe")
   driver.get(url)
   driver.implicitly_wait(5)
   #Html Id on the author page
   co_authors = driver.find_element_by_id('coAuthLi')
   co_authors.click()
   #Html text of co-author overiew for an author
   overview = driver.find_element_by_link_text('View co-author overview')
   overview.click()
   driver.implicitly_wait(2)
   #html id for exporting the result
   export = driver.find_element_by_id("export_results")
   export.click()
   driver.implicitly_wait(2)
   #Class name for first radio button option for CSV download
   csv_export = driver.find_element_by_class_name("radio")
   csv_export.click()
   driver.implicitly_wait(1)
   #Final css selector for exporting the result 
   result = driver.find_element_by_css_selector("button.btn.btn-primary.btn-sm.pull-right.dropdownActionButton.exportButton") 
   result.click()
    
finally:
        driver.close()





