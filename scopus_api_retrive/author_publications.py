# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:57:33 2019

@author: z3525552
"""

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
    from scopus import ScopusAuthor
    import pandas as pd     

    researcher = ScopusAuthor(6701859739)
    journals = pd.DataFrame(researcher.publication_history) 
    journals.columns = ['sourcetitle','abbreviation','publication_type','issn']

    return journals      