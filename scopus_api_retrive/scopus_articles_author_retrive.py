# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:22:52 2020

@author: z3525552
"""

def eid_authorid(SCOPUS_EID):     
    
    '''Given the journal details (SCOPUS_EID) the function returnal all authors
    name and Author Scopus_ID
    
    Parameters: str SCOPUS_EID  
               
    Returns:    dict Authors name and Author Scopus_ID
               
    '''
    from pybliometrics.scopus import AbstractRetrieval
    ab = AbstractRetrieval(SCOPUS_EID)
    
    researchers = {author.given_name+ ' '+author.surname : author.auid for author in ab.authors} 
       
    return researchers