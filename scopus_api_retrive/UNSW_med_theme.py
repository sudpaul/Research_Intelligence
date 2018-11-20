# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:14:07 2018

@author: z3525552
"""
def scopus_author(scopus_id):
    
    '''Helper function to invoke the Scopus Author from SCOPUS database
     download the author contenets and retrun author object
    
    Parameter
    ----------
    scopus_id : str or int
    
    Return
    ----------
    author : Scopus Author object'''
    
    assert isinstance(scopus_id, (str, int))
    
    from scopus import ScopusAuthor
    
    # Retrive autor object from SCOPUS database
    author = ScopusAuthor(scopus_id)
    
    return author


def check_theme(subjects):
    
    """The fuction input is SCOPUS author subjects area and it maps to medicine
    theme ASJC. Return the theme_subjects and map to aggregate theme result.
    
    Parameters
    ----------
    subjects : dict
               Subject categories of Scopus author Subject areas
    Returns
    ----------
    theme_subjects : dict
                     Mapping of the ASJC codes of SCOPUS subjects to theme_subjects
           
    result : dict 
             aggregate result of the theme mapping       
    """ 
    
    from collections import defaultdict
    result = defaultdict(int)
    
    data_set = {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)',
            'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
            'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
            'Rheumatology', 'Toxicology', 'Clinical Neurology','Psychiatry and Mental Health', 
            'General Neuroscience', 'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
            'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
            'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
            'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology',
            'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
            'Endocrinology, Diabetes and Metabolism','Pulmonary and Respiratory Medicine'}
    
        
    theme_dict = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'} ,
                  'Triple I' : {'Endocrinology','Immunology and Microbiology','Immunology', 'Microbiology',
                  'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
                  'Rheumatology', 'Toxicology'},            
                   'NHMA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Phychiatric Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'},
                   'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine',
                        'Endocrinology, Diabetes and Metabolism','Pulmonary and Respiratory Medicine'}}    
   
    theme_subjects = {key:value for key, value in subjects.items() if key in data_set}
    
    for theme, match in theme_dict.items():
        for subject in theme_subjects:
            if subject in match:
               result[theme] += theme_subjects[subject]

    return theme_subjects, result 
            

