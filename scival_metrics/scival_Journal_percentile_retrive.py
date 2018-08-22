# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:17:46 2018

@author: z3525552
"""


def scival_SJR_percentile_retrive(author_id):
    
    ''' This function is used for SciVal matric SJR percentile retrive
        It takes API file, author id(SCOPUS_ID) as inputs and return
        ten percentile pulications in SJR journal.''' 
    
    import pandas as pd
    from scival_author_metrics import api_query
    pd.options.display.float_format = '{:.2f}'.format
 
    assert type(author_id) is str
    
    query ={'metricTypes':'PublicationsInTopJournalPercentiles',
            'yearRange':'5yrs',
            'includeSelfCitations':'false',
            'byYear':'false',
            'includedDocs':'AllPublicationTypes',
            'journalImpactType':'SJR',
            'showAsFieldWeighted':'false',
            'indexType':'hIndex',
            'authors':'%s' %(author_id)}
    #HTTP request response object 
    response = api_query(query)
    data = response['results'][0]['metrics'][0]['values']   
    
    #Dataframe from the SJR percentile data dictionary            
    df = pd.DataFrame.from_dict(data)    
    top_10_percentile = df.iloc[2]['percentage']
                
    return top_10_percentile
      