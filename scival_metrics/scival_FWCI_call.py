# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:17:54 2018

@author: z3525552
"""

def get_scival_fwci(author_id):
    
    ''' This function is used for retriving SciVal 
        Field weighted citation impact exclude selfcitations
        input is author id (SCOPUS_ID).
        Return mean FWCI.
        
    Parameter
    ----------
    author_id : str or int
                Author Scopus Id 
    
    Return
    -------
    mean_fwci : float   
                mean FWCI for 5 years and current
    ''' 
               
    import pandas as pd
    from scival_author_metrics import api_query  
    
    assert isinstance(author_id, (str, int))
    #FWCI for last years and 5 years and current year exclude selfcitations and journal impact type SNIP
    query = {'metricTypes':'FieldWeightedCitationImpact',
             'yearRange' : '5yrsAndCurrent',
             'includeSelfCitations':'false',
             'byYear':'true',
             'includedDocs':'AllPublicationTypes',
             'journalImpactType':'SNIP',
             'showAsFieldWeighted':'false',
             'indexType':'hIndex',
              'authors':'%s' %(author_id)}
   
    #HTTP response object from request       
    response = api_query(query)
    data = response['results'][0]['metrics'][0]   
    
    #Dataframe from the data dictionary and calculating mean from the values      
    fwci = pd.DataFrame.from_dict(data)
    fwci = fwci.drop(['metricType'], axis=1)    
    mean_fwci = fwci.mean()        
            
    return mean_fwci
 
           
    
    
    