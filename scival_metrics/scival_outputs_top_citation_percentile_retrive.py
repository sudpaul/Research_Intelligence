# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:04:53 2018

@author: z3525552
"""

def scival_top_citation_percentiles_retrive(file, author_id):
    
    ''' This function is used for SciVal matric outputs in top 
        percentile retrive. It takes API file, author id(SCOPUS_ID) as inputs 
        and return 10th percentile pulications results as list. 
        
        HTTP requestes code other than 200 return 
        the status codes. If author has not publish and no citations for the  
        publications it returns 0 and all others http requests failure return 
        -1'''
    
    
    import requests
    import pandas as pd
    pd.options.display.float_format = '{:.2f}'.format
    from elsiver_api_retrive import get_elseiver_API
    
    assert type(author_id) is str
    
    token = get_elseiver_API(file)
        
    base_url = "http://api.elsevier.com/analytics/scival/author/metrics?"
    query = {'metricTypes': 'OutputsInTopCitationPercentiles',
             'showAsFieldWeighted': 'true',
             'byYear': 'false',
             'yearRange': '5yrsAndCurrent',
             'authors': '%s' %(author_id)}

   
    header = {'Accept':'application/json', 'X-ELS-APIKey': token} 
    
    try:
        response = requests.get(url=base_url, params=query,headers= header)
        
        if not response.status_code == 200:
            
            return response.status_code
        
        else:
            try:
                response_data = response.json()
                               
                data = response_data['results'][0]['metrics'][0]['values']
                
                df = pd.DataFrame(data)                
                percentile =  df['percentage'].values 
                
                return  percentile[2]
                
            except:
                return 0
                
    except:
        return -1