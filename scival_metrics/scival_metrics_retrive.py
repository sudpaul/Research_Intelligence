# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:26:00 2018

@author: z3525552
"""

def scival_metrics(api_file, scopus_id )
    """ Retriving SciVal default metrics using Scival API
        it takes API file in order to get api key and
		scopus_id for which return all
		default metrics displayed in Scival as
		json object"""

	import requests

    base_url = "http://api.elsevier.com/analytics/scival/author/metrics?"
    query = {'metricTypes': """ScholarlyOutput,CitationCount,hIndices,
              FieldWeightedCitationImpact,CitationsPerPublication,
		      PublicationsInTopJournalPercentiles""",
		     'byYear': 'false',
		      'yearRange': '5yrsAndCurrent',
              'authors': '%s' %(scopus_id)
		    }

    with open('api_file') as f:
         token = f.read().strip()

	header = {'Accept':'application/json', 'X-ELS-APIKey': token}

    response = requests.get(url=base_url, params=query,headers= header)

   return response.json()
