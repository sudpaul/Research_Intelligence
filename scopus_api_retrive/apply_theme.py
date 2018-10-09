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
    
    #Subject heading of SCOPUS is theme data dictionary
    
    cancer = {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'}

    triple_I = { 'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'}
    ncd = {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
           'Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}
    #Theme subject and SCOPUS subject heading is a disjoint set then no mapping 
    #otherwise return matching theme 
    
    if not cancer.isdisjoint(theme_subject):
           return 'Cancer'
    
    elif not triple_I.isdisjoint(theme_subject):   

          return 'Triple I'
    elif not ncd.isdisjoint(theme_subject):   

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
    #Subject heading of SCOPUS is theme data dictionary. 
    #Lookup table for set intersection
    d = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'} ,
         'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'},
        'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
           'Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}}
                                                      
    #Five main subjects of researchers publications
    main_subject = subjects[:5]
    #Placeholders for alternatives theme mapping
    alternatives = subjects[5:] 
    #Five main subjects of researchers publications
    #Authhor main subjects set 
    theme_subject = set(main_subject)
    #Validation for theme subjects and author main subjects is not a disjoint set
    theme = check_theme(theme_subject) 
    #If there is intersection of the two sets, result will be the intersection set.
    if theme:       
        result =  d[theme].intersection(theme_subject)
        return theme, result
    #Otherwise researcher is All/Any theme
    else:
        return "All/Any theme", None