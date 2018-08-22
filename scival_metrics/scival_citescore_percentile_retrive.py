# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:04:53 2018

@author: z3525552
"""

def scival_citescore_percentile_retrive(author_id):
    
    ''' This function is used for SciVal matric CiteScore percentile retrive
        It takes API file, author id(SCOPUS_ID) as inputs and return
        1st,5th, and 10th percentile pulications results as list. '''
            
    import pandas as pd
    from scival_author_metrics import api_query
    pd.options.display.float_format = '{:.2f}'.format
    
    assert type(author_id) is str
    
    query = {'metricTypes': 'FieldWeightedCitationImpact,PublicationsInTopJournalPercentiles',
             'byYear': 'false','yearRange': '5yrsAndCurrent',
              'authors': '%s' %(author_id)}

    #HTTP request response object
    response = api_query(query)
    # Retriving only 1,5 and 10th percentile publication values                          
    *data, _ = response['results'][0]['metrics'][1]['values']
    
    #Data frame from data dictioanry and only values are return         
    df = pd.DataFrame(data)                
    percentile =  df['percentage'].values 
                
    return  percentile
          