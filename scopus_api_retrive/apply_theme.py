# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:54:44 2018

@author: z3525552
"""
def check_theme(theme_subject):
    
    """Helper function which can help to identify scopus subject catgories set is
      a disjoint set of author subject catgories.
     
    Parameters
    ----------
    theme_subject : str
                  Five main subject categories of Scopus author Subject areas
    Returns
    ----------
    theme : str
           Mapping of the theme name
           
    nomatch : None """ 
    
    
    
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
    
    """This is a custom function to map Scopus author subject categories to 
    pre-defined theme
    Parameters
    ----------
    subjects : tuple
              Scopus author subject categories
    Returns
    ----------
    theme, result : tuple
                    theme is the mapping of subject sub heading
                    result is a set of string which has matched to author subject
                    All/Any theme 
                   default mapping if no mactch is found
    """               
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
        return "All/Any theme", None