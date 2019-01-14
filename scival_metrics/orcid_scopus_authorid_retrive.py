# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:22:08 2019

@author: z3525552
"""


def orcid_scopusid(ORCID):
    
    import requests
        
    with open('../elsevier_developer') as f:
            token = f.read().strip()
    
    
        
    base_url ='https://api.elsevier.com/content/author/orcid/{orcid}'.format(orcid=ORCID)
        
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
        
    try:
        response = requests.get(url=base_url, headers=header)
        
        if not response.status_code == 200:
            
           return response.status_code
    
        response_data = response.json()       
        result = response_data['author-retrieval-response'][0]['coredata']                      
        _, scopus_id = result['dc:identifier'].split(':')
        return scopus_id
        
    except:
        return 'Not Found'