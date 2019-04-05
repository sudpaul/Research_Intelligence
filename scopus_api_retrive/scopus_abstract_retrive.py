# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:13:28 2019

@author: z3525552
"""
#Abstract search from Scopus

import requests



def publication_retrive(eid):
    
    #with open('../elsevier_developer') as f:
               # token = f.read().strip()    
    base_url =f'https://api.elsevier.com/content/abstract/eid/{eid}'
            
    header = {'Accept':'application/json', 'X-ELS-APIKey': 'cf19ff27ef3c0d95f93c26947eb6533f'}
    res = requests.get(url=base_url, headers=header)
    
    response = res.json() 
        
    return response





def eid_authorid(eid):     
    
    res_obj = publication_retrive(eid)
    # Get authors of the abstracts    
    data = res_obj["abstracts-retrieval-response"]["authors"]["author"]
    auth_id = {author['ce:surname']:author['@auid'] for author in data}
     
       
    return auth_id

#To do generalise abstract retrive to get funding agency from dois/eids/pubmed_id
    

def eid_grants(eid):
    
    res_obj = publication_retrive(eid)
    funding = res_obj["abstracts-retrieval-response"]["item"]["xocs:meta"]["xocs:funding-list"]["xocs:funding"]
    
    grants = {}
    for fund in funding:
        grants[fund["xocs:funding-id"]]= fund["xocs:funding-agency"]
    
    return grants