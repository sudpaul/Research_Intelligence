# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:44:57 2019

@author: z3525552
"""
import pandas as pd
from pybliometrics.scopus import AuthorRetrieval

def journal_numberof_first_last_authorship(author_id):

    '''Input is author scopus id and get all publications 
     from Scopus database. Filter the journal publications and
     return the number of first, last authorship of the researcher
     
    Parameter
    ----------
    author_id : int or str 
                Scopus id of Author 
    
    Returns
    ----------
    first, last : obj                
               pandas dataframe object  
               number of first and last author in journals    
    ''' 
    assert isinstance(author_id, (str, int))
    
    au = AuthorRetrieval(author_id)
    publications = pd.DataFrame(au.get_document_eids(refresh=False))
    articles = publications[publications['aggregationType'] == 'Journal']
    
    first = articles[articles['author_ids'].str.startswith(author_id)]
    last = articles[articles['author_ids'].str.endswith(author_id)]
    
    n_first, n_last = len(first), len(last)
    
    return (n_first, n_last)