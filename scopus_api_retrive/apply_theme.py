# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:54:44 2018

@author: z3525552
"""
def check_theme(theme_subject):
    
    cancer = {'Cancer Research','Oncology', 'Cancer', 'Radiation'}

    Triple_I = { 'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'}
    NCD = {'Cardiology', 'Cardiovascular Medicine', 'Endocrinology', 'Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}

    
    if not cancer.isdisjoint(theme_subject):
           return 'Cancer'
    
    elif not Triple_I.isdisjoint(theme_subject):   

          return 'Triple I'
    elif not NCD.isdisjoint(theme_subject):   

          return 'NCD'
    else:
        return None


def main_theme(subjects):
    
    d = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation'} ,
         'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'},
        'NCD' : {'Cardiology', 'Cardiovascular Medicine', 'Endocrinology', 'Diabetes and Metabolism'
            'Pulmonary and Respiratory Medicine'}}
                                                      
    
    main_subject = subjects[:5]
    alternatives = subjects[5:] 
    
    theme_subject = set(main_subject)
    theme = check_theme(theme_subject) 
    
    if theme:       
        result =  d[theme].intersection(theme_subject)
        return theme, result
    else:
        return "All/Any theme", 