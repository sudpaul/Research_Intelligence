# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:22:08 2019

@author: z3525552
"""


def orcid_scopusid(ORCID):
    
    """
    Input is researher ORCID and retrive
    scopus author id from SCOPUS author retrive
    API. If ORCID is available in SCOPUS database
    return author SCOPUS ID.
    Parameters
    ----------
    ORCID : str
            Researcher ORCID
    
    
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
    
    scopus_id : str
                author SCOPUS ID   
    Raises: str
            'Not Found'
    """
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