# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:21:08 2018

@author: z3525552
"""

def scopus_affiliation(affiliation_id):
    
    '''Helper function to invoke the Scopus Affiliation from SCOPUS database
     download basic information on registered affiliations in affliation object
   
    Parameter
    ----------
    affiliation_id: str or int
                  Scopus affiliations: Org profiles and Non-Org profiles 
                  Scopus start with a 6 (6XXXXXXX) Affiliations is Org profiles   
                  Non-Org profiles start with a 1 (1XXXXXXXX) 
    Return     
    ----------
    affliation : obj
                Scopus Affliation object'''
    
    assert isinstance(affiliation_id, (str, int))
    
    from scopus import ScopusAffiliation
    
    # Retrive Affiliation object from SCOPUS database
    affiliation = ScopusAffiliation(affiliation_id) 
    print(affiliation) 
    
    return affiliation
