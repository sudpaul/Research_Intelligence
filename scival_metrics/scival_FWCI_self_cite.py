# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:08:27 2018

@author: z3525552
"""

def get_scival_fwci_selfcite(author_id):
    
    
    ''' This function is used for retriving SciVal matric Field weighted 
        citiations impact. Input author id(SCOPUS_ID) 
        return FWCI of the author including selfcitations and 
        journal impact type CiteScore. '''
        
    
    from scival_author_metrics import api_query
        
    assert type(author_id) is str
    
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
  