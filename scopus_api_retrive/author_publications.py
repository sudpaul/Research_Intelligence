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
    journals = pd.DataFrame(researcher.publication_history) 
    journals.columns = ['sourcetitle','abbreviation','publication_type','issn']

    return journals      


def publication_subjects(scopus_id):
        
    """Retriving Journal publication detail from Scopus 
    input scopus_id for which  return publication history
   
    Parameter
    ----------
    scopus_id : str
               Author Scopus id
    subjects : obj
              pandas dataframe object         
    """
    
    researcher = scopus_author(scopus_id)
    
    subjects = pd.DataFrame(data=researcher.subject_areas)
    subjects.columns = ['subjects','n_documents','subject_categories','asjc_codes']
    subjects = subjects.sort_values(by=['n_documents'], ascending=False)
    
    return subjects

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
        
    coauthors = pd.DataFrame.from_records(data)
    coauthors.columns = ['name', 'scopus_id', 'affiliation', 'categories']
   
    return coauthors