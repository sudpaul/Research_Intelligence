# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:17:46 2018

@author: z3525552
"""


def scival_SJR_percentile_retrive(author_id):
    
    ''' This function retrives SciVal matric SJR top ten percentile.
        input is author id(SCOPUS_ID) and return ten percentile 
        exclude selfcitations pulications in SJR journal.
        
    Parameter
    ----------
    author_id : str or int
                Author Scopus Id 
    
    Return
    -------
    top_10_percentile : float   
                ten percentile publication in SJR journal
    ''' 
        
    import pandas as pd
    from scival_author_metrics import api_query
    pd.options.display.float_format = '{:.2f}'.format
 
    assert  isinstance(author_id, (str, int))
    
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
    # Get the publication percentile from the data frmae 
    # If the nubmer is needed change dataframe column name to value
    top_10_percentile = df.iloc[2]['percentage']
                
    return top_10_percentile
      