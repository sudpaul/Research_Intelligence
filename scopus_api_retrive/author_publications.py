# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:57:33 2019

@author: z3525552
"""

from scopus_authors_retrive import scopus_author   
import pandas as pd

def author_publication(scopus_id):
    
    """Retriving Journal publication detail from Scopus 
    input scopus_id for which  return publication history
   
    Parameter
    ----------
    scopus_id : str
               Author Scopus id
    journal : obj
              pandas dataframe object         
    """
    researcher = scopus_author(scopus_id)
    journals = pd.DataFrame(researcher.journal_history) 
    
    return journals      

def get_coauthors(scopus_id):
    """Retrieves basic information about co-authors as a list of
        namedtuples in the form
        name, scopus_id, affiliation, categories
        where areas is a list of subject area codes joined by "; ".
        Note: These information will not be cached and are slow for large
        coauthor groups.
    """
   
        # Get number of authors to search for
    res = scopus_author(scopus_id)
    data = res.get_coauthors()
    coauthors = pd.DataFrame(data)
       
    return coauthors