# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:26:00 2018

@author: z3525552
"""

def scival_metrics(filepath, scopus_id):
    
    """Retriving SciVal default metrics using Scival API 
    it takes API file in order to get api key and scopus_id for which 
    return all default metrics displayed in Scival """
    
    import requests
    import pandas as pd
    from elsiver_api_retrive import get_elseiver_API
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    assert isinstance(scopus_id, (str, int))
    
    #SciVal base URL for author metrics retrive
    base_url = "http://api.elsevier.com/analytics/scival/author/metrics?"
    
    #query for http request
    query = {'metricTypes': """ScholarlyOutput,CitationCount,hIndices,
             FieldWeightedCitationImpact,CitationsPerPublication,
		         OutputsInTopCitationPercentiles,PublicationsInTopJournalPercentiles""",
		        'byYear': 'false',
		        'yearRange': '5yrsAndCurrent',
            'authors': '%s' %(scopus_id) }  
    
    token = token = get_elseiver_API(filepath)
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}

    try:
        response = requests.get(url=base_url, params=query,headers= header)
        #http request response object for status code
        if not response.status_code == 200:
        
            return response.status_code
        
        else:
            #Respose json data
            response_data = response.json()    
            data = response_data['results'][0]['metrics']
            
            #Making a pandas dataframe from data dictionary
            df = pd.DataFrame.from_records(data)
    
            result = df[['metricType', 'value']]
            metrics = result.fillna(0.0)
    
            return metrics
    except:
         return "HTTP requestes fail"