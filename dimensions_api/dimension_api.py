# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 12:03:57 2018

@author: z3525552
"""
query = '''search grants where (start_year in [2013:2018] and funders.acronym="NHMRC")
           return funders[name + acronym + country_name]
           return active_year aggregate funding''' 



def api_query(query):
    
    """
    It takes http query as input 
    detail specifications 
    https://dev.elsevier.com/scival.html

    return response_data 

    Parameters
    ----------
    query : str
            dsl query
    
    Returns
    -------
    status_code : int
                  400 : Invalid Request 
                
    
    response_data : dict
                  response data dictionary 
    
    Raises: int    
            0 : http request fail
    """
    import requests
        
    with open('../dimensions_user') as f:
        contents = f.read().strip().split(',')
        username = contents[0]
        password = contents[1]


    login = {'username': username,
            'password': password
            }
        
    try:
        resp = requests.post('https://app.dimensions.ai/api/auth.json', json=login)
        headers = {'Authorization': "JWT " + resp.json()['token'] }
        
        if not resp.status_code == 200:
            
            return resp.status_code
        else:
       
            response = requests.post('https://app.dimensions.ai/api/dsl.json',
                                 data=query,headers=headers)
            response_data = response.json()                              
            return response_data
        
    except:
          return 0
