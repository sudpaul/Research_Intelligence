# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:04:49 2018

@author: z3525552
"""

def get_elseiver_API(filepath ='../elsevier_developer'):
    
    '''Read the Elsevier developer API key from source file
       return API Key
    
    Parameters
    ----------
    filepath : str
               API file location
    
    Returns
    -------
    token : str
            API key string
    ''' 
    
    with open(filepath) as f:
        token = f.read().strip()
    
    return token