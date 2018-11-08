# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:30:04 2018

@author: z3525552
"""

def alternative_theme(alternative_subjects):

    from collections import defaultdict
    result = defaultdict(set)

    themes = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'} ,
         'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'},
         'NHMA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'},
        'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
           'Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}}


    for key in themes:
        if not themes[key].isdisjoint(alternative_subjects):
           result[key] = themes[key]&alternative_subjects
      
    alternative = max(result, key=lambda k: len(result[k]))
    
    return alternative