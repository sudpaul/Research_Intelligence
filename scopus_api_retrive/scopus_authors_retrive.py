# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:35:35 2018

@author: Sudipta Paul
"""

def scopus_author(scopus_id):
    
    '''Helper function to invoke the Scopus Author from SCOPUS database
     download the author contenets and retrun author object
    
    Parameter
    ----------
    scopus_id : str or int
    
    Return
    ----------
    author : Scopus Author object'''
    
    assert isinstance(scopus_id, (str, int))
    
    from scopus import AuthorRetrieval
    
    # Retrive autor object from SCOPUS database
    author = AuthorRetrieval(scopus_id)
    
    return author



def make_dataframe(authors_scopus_ids):
    
   '''Input is list/tuple of author scopus id 
     get name, h-index, total documents and other attributes from 
     SCOPUS author object return a pandas dataframe.
     The attributes are as columns of the dataframe
     
    Parameter
    ----------
    scopus_ids : list or tuple 
    
    Returns
    ----------
    df : Pandas dataframe'''  
    
   assert isinstance(authors_scopus_ids,(list, tuple)) 
    
   import pandas as pd
   from collections import defaultdict
   
   #Default dictionary of Scopus ID for author attributes lookup
   scopus_id = defaultdict(list)
  
   
   for author in authors_scopus_ids:
       
       scopus_id['SCOPUS_ID'].append(author)
       #Retriving author from SCOPUS
       au = scopus_author(author)    
       firstname, surname = au.given_name, au.surname
       author = firstname + ' ' + surname
       #Retriving attributies from author 
       scopus_id['name'].append(author)
       scopus_id['h_index'].append(au.h_index)
       scopus_id['documents_total'].append(au.document_count)
       #scopus_id['number_first_author'].append(au.n_first_author_papers(refresh=False))
       #scopus_id['number_last_author'].append(au.n_last_author_papers(refresh=False))
       scopus_id['total_citing_papers'].append(au.cited_by_count)
      
       
       scopus_id['orcid'].append(au.orcid)
   #Making dataframe for further analysis    
   df = pd.DataFrame.from_dict(scopus_id)
   
   return df