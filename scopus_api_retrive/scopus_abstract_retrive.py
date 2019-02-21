# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:13:28 2019

@author: z3525552
"""
#Abstract search from Scopus

import requests
import pandas as pd

     
with open('../elsevier_developer') as f:
            token = f.read().strip()    
base_url ='https://api.elsevier.com/content/abstract/eid/2-s2.0-85012915011'
        
header = {'Accept':'application/json', 'X-ELS-APIKey': token}

res = requests.get(url=base_url, headers=header)

response = res.json() 


# Get authors of the abstracts

data = pd.DataFrame.from_records(response['abstracts-retrieval-response']['authors']['author'])



df =  data[['ce:surname','@auid']]

df = df.rename(columns={'@auid': 'Scopus_id', 'ce:surname': 'Surname'})