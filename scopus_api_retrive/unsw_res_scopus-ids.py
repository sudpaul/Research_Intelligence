# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:35:52 2019

@author: z3525552
"""
import pandas as pd
import numpy as np
import requests
from scopus_authors_retrive import scopus_author

publication = pd.read_excel('data/UNSW SPHERE data SWSR CRM 20180726 v3.xlsx', sheet_name='Publications', encoding='utf-8')
missing_scopus = pd.read_csv('data/medicine_missing_scopus-ids.csv')

columns = ['ID', 'CONTACT_SURNAME', 'CONTACT_FIRST_NAME','SCHOOL','Scopus_id']

df = publication.loc[publication['CONTACT_ID'].isin(missing_scopus['ID'])]

data = missing_scopus[columns]
data['publication_score'] = 0.0


def eid_authorid(eid):     
    
    with open('../elsevier_developer') as f:
                token = f.read().strip()    
    base_url =f'https://api.elsevier.com/content/abstract/eid/{eid}'
            
    header = {'Accept':'application/json', 'X-ELS-APIKey': token}
    res = requests.get(url=base_url, headers=header)
    
    response = res.json() 
        # Get authors of the abstracts
        
    data = response["abstracts-retrieval-response"]["authors"]["author"]
    auth_id = {author['ce:surname']:author['@auid'] for author in data}
     
       
    return auth_id


for author, _ in df.groupby('CONTACT_SURNAME'):
    researcher = df.loc[(df['CONTACT_SURNAME']==author)&(df['TYPE']=='Journal article')]
    eids = researcher['SCOPUS_ID'].tolist()
    scopus_eids = [str(eid) for eid in eids if eid is not np.nan]
    row = {'Author': author, 'eids': scopus_eids}
    
    #finding the author scopus id from co-authors list of the publication
    #Evoke the scival abstract api get co-authors from eid_authorid function
    try:
        researchers = eid_authorid(row['eids'][0])
        author_scopus_id = researchers[row['Author']]
        #Call Scopus Author API and get pbulications EIDs match to authors
        au = scopus_author(author_scopus_id)
    
    
        #Retrive all publications of the retive author
        pubs = au.get_document_eids()
    #Get the subset which match to SCOPUS database and Central publication repos
        match_publications = set(pubs).intersection(row['eids'])
    
    #Validation scores for the authors
        match_score = len(match_publications)/len(row['eids'])
    
        data.loc[data['CONTACT_SURNAME']==author,'Scopus_id'] = author_scopus_id
        data.loc[data['CONTACT_SURNAME']==author,'publication_score'] = match_score 
    except:
        continue
    
    
data.to_csv('data/medicine_scopus_ids.csv', index=False)    