# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:55:38 2018

@author: z3525552
"""

def api_query(query):
    
    """
    It takes http query as input 
    detail specifications 
    https://dev.elsevier.com/scival.html

    return response_data 

    Parameters
    ----------
    query : str
            scival author metrics query
    
    Returns
    -------
    status_code : int
                  400 : Invalid Request 
                  401 : Authentication Error
                  403 : Authorization/Entitlements Error
                  405 : Invalid HTTP Method
                  406 : Invalid Mime Type
                  429 : Quota Exceeded
                  500 : Generic Error
    
    response_data : dict
                  response data dictionary 
    
    Raises: int    
            0 : http request fail
    """
    import requests
    from elseiver_api_retrive import get_elseiver_API
    
    key = get_elseiver_API('../elsevier_developer')
    
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
           
    
    