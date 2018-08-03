# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:17:46 2018

@author: z3525552
"""


def scival_SJR_percentile_retrive(file, author_id):
    
    ''' This function is used for SciVal matric SJR percentile retrive
        It takes API file, author id(SCOPUS_ID) as inputs and return
        ten percentile pulications in SJR journal. 
        
        HTTP requestes code other than 200 return 
        the status codes. If author has not publish in top 10 percentile in SJR  
        publications it returns 0 and all others http requests failure return 
        -1'''
    
    
    import requests
    import pandas as pd
    pd.options.display.float_format = '{:.2f}'.format
    from elsiver_api_retrive import get_elseiver_API
    
    assert type(author_id) is str
    
    token = get_elseiver_API(file)
        
    base_url = 'https://api.elsevier.com/analytics/scival/author/metrics?'
    query ='metricTypes=PublicationsInTopJournalPercentiles&yearRange=5yrs&includeSelfCitations=false&byYear=false&includedDocs=AllPublicationTypes&journalImpactType=SJR&showAsFieldWeighted=false&indexType=hIndex&authors=%s' %(author_id)
    
    url = base_url + query    
    
    header = {'Accept':'application/json', 'X-ELS-APIKey': token} 
    
    try:
        response = requests.get(url, headers=header)
        
        if not response.status_code == 200:
            
            return response.status_code
        
        else:
            try:
                response_data = response.json()
                data = response_data['results'][0]['metrics'][0]['values']   
                
                df = pd.DataFrame.from_dict(data)    
                top_10_percentile = df.iloc[2]['percentage']
                
                return top_10_percentile
                
            except:
                return 0
                
    except:
        return -1
    
   
    
   