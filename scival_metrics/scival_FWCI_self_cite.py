# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:08:27 2018

@author: z3525552
"""

def get_scival_fwci_selfcite(file, author_id):
    
    
    ''' This function is used for retriving SciVal matric Field weighted 
        citiations impact. It takes elseiver API file and author id(SCOPUS_ID) 
        as inputs. Return FWCI of the author including selfcitations and 
        journal impact type CiteScore. 
        
        Valid HTTP requestes code other than 200 return the 
        status codes.If http requests fail return 0''' 
    
    import requests
    from elsiver_api_retrive import get_elseiver_API
    
    assert type(author_id) is str
    
    API = get_elseiver_API(file)
    
    base_url ='http://api.elsevier.com/analytics/scival/author/metrics?'
    query = 'metricTypes=FieldWeightedCitationImpact&yearRange=5yrsAndCurrent&includeSelfCitations=true&byYear=false&includedDocs=AllPublicationTypes&journalImpactType=CiteScore&showAsFieldWeighted=true&indexType=hIndex&authors=%s' %(author_id)
    
    url = base_url + query
    
    header = {'Accept':'application/json', 'X-ELS-APIKey': API}
    
    try:
        response = requests.get(url, headers=header)
        if not response.status_code == 200:
            
            return response.status_code
        else:
       
            response_data = response.json()       
             
            fwci = response_data['results'][0]['metrics'][0]['value']             
       
                      
            return fwci
        
    except:
          return 0