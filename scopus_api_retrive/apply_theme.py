# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:54:44 2018

@author: z3525552
"""
from author_subjects import get_subject_docs

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
    
    
    data = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'}, 
            'Triple I' : { 'Endocrinology','General Immunology and Microbiology',
                'Immunology and Microbiology (miscellaneous)','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Immunology and Allergy',
             'Infectious Diseases', 'Microbiology (medical)','Rheumatology', 'Toxicology'},
             'NMHA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'},                                                    
           'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
           'Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}}
    #Theme subject and SCOPUS subject heading is a disjoint set then no mapping 
    #otherwise return matching theme 
    
    for key in data:
        if not data[key].isdisjoint(theme_subject):
               return key
    else:
        return None


def main_theme(subjects):
    """This is a custom function to map Scopus author subject categories to 
      pre-defined theme
    Parameters
    ----------
    subjects : list
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
    data = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'} ,
         'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
             'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
             'Rheumatology', 'Toxicology'},
         'NMHA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'},
        'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
           'Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine'}}
                                                      
    #Five main subjects of researchers publications
    main_subject = subjects[:5]
    #Placeholders for alternatives theme mapping
    alternatives = subjects[5:] 
    #Five main subjects of researchers publications
    #Authhor main subjects set 
    author_subjects = set(main_subject)
    #Validation for theme subjects and author main subjects is not a disjoint set
    theme = check_theme(author_subjects) 
    #If there is intersection of the two sets, result will be the intersection set.
    if theme:       
        result =  data[theme].intersection(author_subjects)
        return theme, result
    #Otherwise researcher is All/Any theme
    else:
        return "All/Any theme", None