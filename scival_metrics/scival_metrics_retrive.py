# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:26:00 2018

@author: z3525552
"""
def scival_metrics(scopus_id):
    
    """Retriving SciVal default metrics using Scival API 
    it takes API file in order to get api key and scopus_id for which 
    return all default metrics displayed in Scival """
    
    import requests
    import pandas as pd
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    base_url = "http://api.elsevier.com/analytics/scival/author/metrics?"
    
    query = {'metricTypes': """ScholarlyOutput,CitationCount,hIndices,
             FieldWeightedCitationImpact,CitationsPerPublication,
		         OutputsInTopCitationPercentiles,PublicationsInTopJournalPercentiles""",
		        'byYear': 'false',
		        'yearRange': '5yrsAndCurrent',
            'authors': '%s' %(scopus_id) }  
    
    token = 'cf19ff27ef3c0d95f93c26947eb6533f'
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}

    response = requests.get(url=base_url, params=query,headers= header)
    response_data = response.json() 
    
    data = response_data['results'][0]['metrics']
    df = pd.DataFrame.from_records(data)
    
    result = df[['metricType', 'value']]
    metrics = result.fillna(0.0)
    
    return metrics

