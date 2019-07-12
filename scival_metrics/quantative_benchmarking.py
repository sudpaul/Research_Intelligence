# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:16:39 2019

@author: z3525552
"""


def benchmarking_metrics(scopus_id):
    
    """Retriving SciVal publication metrics using Scival API 
    input scopus_id for which  return all metrics  defined in the query
   
    
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
    query = {'metricTypes': """ScholarlyOutput,CitationCount,
             FieldWeightedCitationImpact,
		         OutputsInTopCitationPercentiles,PublicationsInTopJournalPercentiles""",
		        'byYear': 'false',
		        'yearRange': '5yrsAndCurrent',
            'includedDocs':'ArticlesReviews',
            'journalImpactType':'SJR',
            'authors': '%s' %(scopus_id)}  

    response = api_query(query)    


    response_data = response['results'][0]['metrics']       
    
    df = pd.DataFrame.from_records(response_data)
    
    # Publication metrics are CiteScore Percentile default of SciVal metrics
    
    metrics = df[['metricType', 'value']]
    #metrics = metrics.fillna(0.0)
    metrics = metrics.set_index('metricType')
    
    return metrics
    