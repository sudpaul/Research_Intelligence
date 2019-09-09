# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:44:57 2019

@author: z3525552
"""
import pandas as pd
from scopus import AuthorRetrieval

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
    
    author = str(author_id)
    au = AuthorRetrieval(author_id)
    eids = pd.DataFrame(au.get_documents())
    articles = eids[eids['aggregationType'] == 'Journal']
    first = articles[articles['author_ids'].str.startswith(author)]
    last = articles[articles['author_ids'].str.endswith(author)]
    
    return (first, last)