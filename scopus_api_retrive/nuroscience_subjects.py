# -*- coding: utf-8 -*-
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
    data = {'NMHA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'}}
                                                      
    #collection of subject categories of author mapped to author subject set      
    author_subjects = set(subjects)
    #Validation for theme subjects and author main subjects is not a disjoint set
    if not data['NMHA'].isdisjoint(author_subjects):       
        #If there is intersection of the two sets, result will be the intersection set.
        result =  data['NMHA'].intersection(author_subjects)
        
        return 'NMHA', result
    else :
        return 'All/Any theme', None