# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:16:39 2019

@author: z3525552
"""
import pandas as pd
from scival_author_metrics import api_query
from collections import defaultdict
pd.set_option('display.float_format', lambda x: '%.3f' % x)


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
    
   
    query = {'metricTypes': """ScholarlyOutput,CitationCount,
             FieldWeightedCitationImpact""",
		        'byYear': 'false',
		        'yearRange': '5yrsAndCurrent',
            'includedDocs':'ArticlesReviews',
            'journalImpactType':'SJR',
            'authors': '%s' %(scopus_id)}  

    response = api_query(query)    
    response_data = response['results'][0]['metrics']
    metrics = {data['metricType']: data['value'] for data in response_data}
    
    
    return metrics

def articles_metrics(scopus_id, metric='PublicationsInTopJournalPercentiles'):
    
    query = {'metricTypes':'%s'%(metric),
            'yearRange':'5yrsAndCurrent',
            'includeSelfCitations':'false',
            'byYear':'false',
            'includedDocs':'ArticlesReviews',
            'journalImpactType':'SJR',
            'showAsFieldWeighted':'false',
            'indexType':'hIndex',
            'authors':'%s' %(scopus_id)}
    
    response = api_query(query)
    data = response['results'][0]['metrics'][0]['values']
    if metric== 'PublicationsInTopJournalPercentiles':
       return data[-1]['value']  

    else: 
        return data[2]['value'] 



def scival_authors(scopus_ids):

    author = defaultdict(list)
    
    for au in scopus_ids:
        author['Scopus_Id'].append(au)
        benchmark = benchmarking_metrics(au)
        author['ScholarlyOutput'].append(benchmark['ScholarlyOutput'])
        author['CitationCount'].append(benchmark['CitationCount'])
        author['FieldWeightedCitationImpact'].append(benchmark['FieldWeightedCitationImpact'])
        
        sjr_pubs = articles_metrics(au)
        author['SJR_Q1_Publications'].append(sjr_pubs) 
    
        top_pubs = articles_metrics(au,metric='OutputsInTopCitationPercentiles')
        author['Top10_Publication_Output'].append(top_pubs)
    
    df = pd.DataFrame.from_dict(author)
    
    return df