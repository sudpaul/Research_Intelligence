# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:13:28 2019

@author: z3525552
"""
#Abstract search from Scopus

import requests


def eid_authorid(eid):     
    with open('../elsevier_developer') as f:
         token = f.read().strip()    
    base_url =f'https://api.elsevier.com/content/abstract/eid/{eid}'
            
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
    res = requests.get(url=base_url, headers=header)
    
    # Get authors of the abstracts
    response = res.json()     
    data = response["abstracts-retrieval-response"]["authors"]["author"]
    auth_id = {author['ce:surname']:author['@auid'] for author in data}
     
       
    return auth_id

#To do generalise abstract retrive to get funding agency from dois/eids/pubmed_id
    

def eid_grants(eid):
    
    with open('../elsevier_developer') as f:
         token = f.read().strip()
    base_url =f'https://api.elsevier.com/content/abstract/eid/{eid}'
            
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
    res = requests.get(url=base_url, headers=header)
    response = res.json() 
    funding = response["abstracts-retrieval-response"]["item"]["xocs:meta"]["xocs:funding-list"]["xocs:funding"]
    
    grants = {fund["xocs:funding-id"]: fund["xocs:funding-agency"] for fund in funding}
    
    return grants