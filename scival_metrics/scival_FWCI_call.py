# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:17:54 2018

@author: z3525552
"""


""" Retriving the Field Weighted Citation Impact from SciVal API"""



def get_scival_fwci(file, author_id):
    
    
    ''' This function is used for retriving SciVal matric Field weighted 
        citiations pact. It takes elseiver API file and author id(SCOPUS_ID) as
        inputs and return mean FWCI of 5 years and current year 
        exclude selfcitations journal impact SNIP. 
        
        Valid HTTP requestes code other than 200 return the 
        status codes.If http requests fail return 0''' 
    
    import requests
    import pandas as pd
    from elsiver_api_retrive import get_elseiver_API
    
    assert type(author_id) is str
    
    API = get_elseiver_API(file)
    
    base_url ='http://api.elsevier.com/analytics/scival/author/metrics?'
    query = 'metricTypes=FieldWeightedCitationImpact&yearRange=5yrsAndCurrent&includeSelfCitations=false&byYear=true&includedDocs=AllPublicationTypes&journalImpactType=SNIP&showAsFieldWeighted=false&indexType=hIndex&authors=%s' %(author_id)
    
    url = base_url + query
    
    header = {'Accept':'application/json', 'X-ELS-APIKey': API}
    
    try:
        response = requests.get(url, headers=header)
        if not response.status_code == 200:
            
            return response.status_code
        else:
       
            response_data = response.json()       
            data = response_data['results'][0]['metrics'][0]   
            
            fwci = pd.DataFrame.from_dict(data)
    
            fwci = fwci.drop(['metricType'], axis=1)    
            average_fwci = fwci['valueByYear'].mean()
            
            return average_fwci
        
    except:
          return 0
           
    
    
    