# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:26:00 2018

@author: z3525552
"""

def scival_metrics(scopus_id):
    
    """Retriving SciVal default metrics using Scival API 
    input scopus_id for which  return all default metrics 
    displayed in Scival.https://www.scival.com/overview/summary
    
    Parameter
    ----------
    scopus_id : str
               Author Scopus id
    
    Returns
    -------
    metrics : obj
              pandas dataframe metricType as index
              value as column"""
    
    import pandas as pd
    from scival_author_metrics import api_query
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    assert isinstance(scopus_id, (str, int))
    
    #query for http request
    query = {'metricTypes': """ScholarlyOutput,CitationCount,hIndices,
             FieldWeightedCitationImpact,CitationsPerPublication,
		         OutputsInTopCitationPercentiles,PublicationsInTopJournalPercentiles""",
		        'byYear': 'false',
		        'yearRange': '5yrsAndCurrent',
            'authors': '%s' %(scopus_id) }  
    response = api_query(query)    
    response_data = response['results'][0]['metrics']
            
    #Making a pandas dataframe from data dictionary
    df = pd.DataFrame.from_records(response_data)
    
    # Publication metrics are CiteScore Percentile default of SciVal metrics
    
    metrics = df[['metricType', 'value']]
    #metrics = metrics.fillna(0.0)
    metrics = metrics.set_index('metricType')
    
    return metrics
    