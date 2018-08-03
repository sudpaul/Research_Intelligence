# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:04:49 2018

@author: z3525552
"""

def get_elseiver_API(file_name):
    
    '''Read the Elsevier developer API key from source file
       return API Key'''
     
    
    with open(file_name) as f:
        token = f.read().strip()
    
    return token