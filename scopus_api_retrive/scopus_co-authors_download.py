# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:15:17 2018

@author: z3525552
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of IEDriverServer
#dir = os.path.dirname(__file__)
driver = webdriver.Chrome(executable_path="C:/Users/z3525552/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://www.scopus.com/authid/detail.url?authorId=6603573607')

co_authors = driver.find_element_by_id('coAuthLi')
co_authors.click()

overview = driver.find_element_by_link_text('View co-author overview')
overview.click()

export = driver.find_element_by_id("export_results")
export.click()

csv_export = driver.find_element_by_class_name("radio")
csv_export.click()

#result = driver.find_element_by_tag_name("button")
#result.click()

driver.close()



#<button class="btn btn-primary btn-sm pull-right dropdownActionButton exportButton" type="button"><span class="btnText">Export</span></button>

#test xpath //*[@id="export_results-data"]/span[2]/span/button[2]/span 