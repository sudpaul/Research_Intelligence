# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:22:08 2019

@author: z3525552
"""

import requests
    
key = 'cf19ff27ef3c0d95f93c26947eb6533f'
    
base_url ='https://api.elsevier.com/content/author/orcid/0000-0002-3612-8298'
    
header = {'Accept':'application/json', 'X-ELS-APIKey': key}
    
try:
    response = requests.get(url=base_url, headers=header)
    
    if not response.status_code == 200:
        
        response.status_code
    else:
   
        response_data = response.json()       
        result = response_data['author-retrieval-response'][0]['coredata']                      
        response_data
    
except:
       0