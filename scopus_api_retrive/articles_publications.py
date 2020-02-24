# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:42:59 2020

@author: z3525552
"""

import pandas as pd
from pybliometrics.scopus import AuthorRetrieval


def author_publication(author_id):

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
    if type(author_id)!= str:
        author = str(author_id)
    else:
        author = author_id
    au = AuthorRetrieval(author_id)
    publications = pd.DataFrame(au.get_documents(refresh=False))
    journal_publications = publications[publications['aggregationType'] == 'Journal']
    first = journal_publications[journal_publications['author_ids'].str.startswith(author)]
    last = journal_publications[journal_publications['author_ids'].str.endswith(author)]
    
    first['year'] = first['coverDate'].str[:4]
    last['year'] = last['coverDate'].str[:4]
    
    return first, last