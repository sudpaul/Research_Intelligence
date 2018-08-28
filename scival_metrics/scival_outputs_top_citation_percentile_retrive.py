# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:04:53 2018

@author: z3525552
"""

def scival_top_citation_percentiles_retrive(author_id):
    
    ''' This function retrive SciVal matric outputs in top 
        percentile. Input is author id(SCOPUS_ID) 
        and return output in top 10th percentile cited. 
        
    Parameter
    ----------
    author_id : str or int
                Author Scopus Id 
    
    Return
    -------
    percentile : float   
                 Top 10th percentile cited
    ''' 
 
    import pandas as pd
    from scival_author_metrics import api_query
    pd.options.display.float_format = '{:.2f}'.format
    
    assert  isinstance(author_id, (str, int))
        
    query = {'metricTypes': 'OutputsInTopCitationPercentiles',
             'showAsFieldWeighted': 'true',
             'byYear': 'false',
             'yearRange': '5yrsAndCurrent',
             'authors': '%s' %(author_id)}
    
    #HTTP response from request
    response = api_query(query)                        
    data = response['results'][0]['metrics'][0]['values']
    
    #Dataframe from the top citiation percentiles data             
    df = pd.DataFrame(data)                
    percentile =  df['percentage'].values 
                
    return  percentile[2]
      