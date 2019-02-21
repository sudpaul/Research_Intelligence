# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:13:28 2019

@author: z3525552
"""
#Abstract search from Scopus

import requests
import pandas as pd

def eid_authorid(eid):     
    
    with open('../elsevier_developer') as f:
                token = f.read().strip()    
    base_url =f'https://api.elsevier.com/content/abstract/eid/{eid}'
            
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
    res = requests.get(url=base_url, headers=header)
    
    response = res.json() 
        # Get authors of the abstracts
        
    data = response["abstracts-retrieval-response"]["authors"]["author"]
    scopus_id = [author['@auid'] for author in data]
     
       
    return scopus_id

