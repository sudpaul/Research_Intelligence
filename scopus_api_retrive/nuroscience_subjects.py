# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:01:27 2018

@author: z3525552
"""


def nuroscience_theme(subjects):
    
    d = {'NHMA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'}}
                                                      
    
        
    theme_subject = set(subjects)
    
    if not d['NHMA'].isdisjoint(theme_subject):       
        result =  d['NHMA'].intersection(theme_subject)
        return 'NHMA', result
    else :
        return 'All/Any theme', None