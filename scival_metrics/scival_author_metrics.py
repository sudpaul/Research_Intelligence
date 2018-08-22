# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:55:38 2018

@author: z3525552
"""

def api_query(query):
    
    
    import requests
    from elsiver_api_retrive import get_elseiver_API
    
    
    key = get_elseiver_API()
    
    base_url ='http://api.elsevier.com/analytics/scival/author/metrics?'
    
    
    header = {'Accept':'application/json', 'X-ELS-APIKey': key}
    
    try:
        response = requests.get(url=base_url, params=query, headers=header)
        
        if not response.status_code == 200:
            
            return response.status_code
        else:
       
            response_data = response.json()       
            
                      
            return response_data
        
    except:
          return 0
           
    
    