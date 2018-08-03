# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:35:35 2018

@author: Sudipta Paul
"""

def scopus_author(scopus_id):
    
    '''Helper function to invoke the Scopus Author from SCOPUS database
     download the author contenets and retrun author object'''
    
    assert isinstance(scopus_id, (str, int))
    
    from scopus import ScopusAuthor
    
    author = ScopusAuthor(scopus_id)
    
    return author



def make_dataframe(authors_scopus_ids):
    
   '''Input is list/tuple of author scopus id 
     get name, h-index, total documents and other attributes from 
     SCOPUS author object return a pandas dataframe.
     The attributes are as columns of the dataframe'''
    
   assert isinstance(authors_scopus_ids,(list, tuple)) 
    
   import pandas as pd
   from collections import defaultdict
   
   scopus_id = defaultdict(list)
  
   
   for author in authors_scopus_ids:
       
       scopus_id['SCOPUS_ID'].append(author)
       
       au = scopus_author(author)    
       name = au.firstname +' ' + au.lastname
       
       scopus_id['name'].append(name)
       scopus_id['h_index'].append(au.hindex)
       scopus_id['documents_total'].append(au.ndocuments)
       scopus_id['number_first_author'].append(au.n_first_author_papers(refresh=False))
       scopus_id['number_last_author'].append(au.n_last_author_papers(refresh=False))
       scopus_id['total_citing_papers'].append(au.ncited_by)
      
       
       scopus_id['orcid'].append(au.orcid)
       
   df = pd.DataFrame.from_dict(scopus_id)
   
   return df