# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:08:27 2018

@author: z3525552
"""

def get_scival_fwci_selfcite(author_id):
    
    ''' This function is used for retriving SciVal 
        Field weighted citation impact with selfcitations
        input is author id (SCOPUS_ID).
        Return FWCI Journal impact type is CiteScore.
        
    Parameter
    ----------
    author_id : str or int
                Author Scopus Id 
    
    Return
    -------
    mean_fwci : float   
                FWCI for 5 years and current
    ''' 
    
    from scival_author_metrics import api_query
        
    assert isinstance(author_id, (str, int))
    
    query = {'metricTypes' :'FieldWeightedCitationImpact',
             'yearRange' : '5yrsAndCurrent',
             'includeSelfCitations':'true',
             'byYear':'false',
             'includedDocs':'AllPublicationTypes',
             'journalImpactType':'CiteScore',
             'showAsFieldWeighted':'true',
             'indexType':'hIndex',
             'authors': '%s' %(author_id)}
    
    #HTTP request response object        
    response = api_query(query)      
    
    #FWCI data frame from data dictionary         
    fwci = response['results'][0]['metrics'][0]['value']             
       
                     
    return fwci
  