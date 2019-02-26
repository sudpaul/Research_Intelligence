# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:44:21 2018

@author: z3525552
"""

def doi_edi(doi):    
    ''' This function is used to change SCOPUS DOI to EDI number
    
    Parameters
    ----------
    doi : str 
          Scopus' Document Object Identifier 
    
    
    Return
    -------
    edi : str
          Scopus’ Electronic Identifier'''      
    import requests
    
    with open('../elsevier_developer') as f:
                token = f.read().strip()    
    
    
    base_url ='http://api.elsevier.com/content/search/scopus?query=%s'%(doi)
    
    
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
    
    try:
        response = requests.get(url=base_url, headers=header)
        
        if not response.status_code == 200:
            
            return response.status_code
        else:
       
            response_data = response.json()       
            eid = response_data['search-results']['entry'][0]['eid']
                      
            return eid
        
    except:
          return 0
           