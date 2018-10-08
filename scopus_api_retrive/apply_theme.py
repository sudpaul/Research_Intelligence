# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:54:44 2018

@author: z3525552
"""

def check_theme(theme_subject):
    """Helper function which can help to identify scopus subject catgories set is
      a disjoint set of author subject catgories.
     
    Parameter
    ----------
    theme_subject : str
                  Three main subject categories of Scopus author Subject areas
    Return
    ----------
    theme : str
           Mapping of the theme name
           
    nomatch : None """ 
    
    cancer = {'Cancer Research','Oncology', 'Cancer', 'Radiation'}

    Triple_I = { 'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'}
    
    if not cancer.isdisjoint(theme_subject):
           return 'Cancer'
    
    if not Triple_I.isdisjoint(theme_subject):   

          return 'Triple I'
    else:
        return None


def main_theme(subjects):
    """This is a custom function to map Scopus author subject categories to 
    pre-defined theme
    
    Parameter
    ----------
    subjects : tuple
              Scopus author subject categories
    Return
    ----------
    theme, result : tuple
                    theme is the mapping of subject sub heading
                    result is a set of string which has matched to author subject
                    All/Any theme 
                   default mapping if no mactch is found
    """                       
    d = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation'} ,
         'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 
                       'Microbiology','Parasitology', 'Virology', 'Dermatology', 
                       'Allergy', 'Infectious Diseases','Rheumatology',
                       'Toxicology'}}
    main_subject1, main_subject2, main_subject3, *alternatives = subjects 
     
    theme_subject = {main_subject1, main_subject2, main_subject3}
    theme = check_theme(theme_subject) 
    
    if theme:       
        result =  d[theme].intersection(theme_subject)
        return theme, result
    else:
        return "All/Any theme"