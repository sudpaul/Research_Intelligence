__# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:01:27 2018

@author: z3525552
"""


def nuroscience_theme(subjects):
    
    """This is a custom function to map Scopus author subject area of 
    nuroscience to pre-defined theme
    Parameters
    ----------
    subjects : tuple
              Scopus author subject categories
    Returns
    ----------
    theme, result : tuple
                    theme is the mapping of subject sub heading to
                    aggregate higher level
                    result is a set of string which has matched to author subject
                    All/Any theme 
                   default mapping if no mactch is found"""
    data = {'NHMA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'}}
                                                      
    
        
    theme_subject = set(subjects)
    
    if not data['NHMA'].isdisjoint(theme_subject):       
        result =  data['NHMA'].intersection(theme_subject)
        return 'NHMA', result
    else :
        return 'All/Any theme', None