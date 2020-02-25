# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:06:50 2019

@author: z3525552
"""
# Generalise the new theme mapping
#Cross theme mapping keyword

#Genetics, Molecular Biology, Molecular Medicine

from pybliometrics.scopus import AuthorRetrieval
from operator import itemgetter
from collections import defaultdict

def check_theme(subjects):
    
    """The function input is SCOPUS author subjects area and it maps to medicine
    theme ASJC codes. Return the theme_subjects and map to aggregate theme result.
    
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
    
     
    result = defaultdict(int)
    
    data_set = {'Cancer Research','Oncology', 'Cancer', 'Radiation', 
                'Oncology(nursing)', 'Endocrinology',
                'General Immunology and Microbiology',
                'Immunology and Microbiology (miscellaneous)',
            'Immunology', 'Microbiology','Immunology and Allergy', 
            'Microbiology (medical)', 'Parasitology', 'Virology', 'Dermatology',
            'Allergy', 'Infectious Diseases', 'Rheumatology', 'Toxicology', 
            'Clinical Neurology','Psychiatry and Mental Health','General Neuroscience', 
            'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
            'Biological Psychiatry','Cellular and Molecular Neuroscience',
            'Cognitive Neuroscience',
            'Developmental Neuroscience', 'Neurology' ,'Psychiatry Mental Health',
            'Psychology (miscellaneous)',
            'Experimental and Cognitive Psychology', 
            'Neuropsychology and Physiological Psychology',
            'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine', 
            'Critical Care and Intensive Care Medicine',
            'Emergency Medicine','Endocrinology, Diabetes and Metabolism',
            'Pulmonary and Respiratory Medicine','Epidemiology','Family Practice',
            'Gastroenterology','Health Informatics','Health Policy','Hematology','Hepatology',
            'Internal Medicine','Nephrology', 'Ophthalmology', 'Orthopedics and Sports Medicine', 
            'Otorhinolaryngology', 'Transplantation','Urology', 'Critical Care','Respiratory Care'}
    
    
        
    theme_dict = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 
                              'Oncology(nursing)'} ,
                  'Triple I' : {'Endocrinology','General Immunology and Microbiology',
                                'Immunology and Microbiology (miscellaneous)',
                                'Immunology', 'Microbiology','Immunology and Allergy', 
                                'Microbiology (medical)','Parasitology', 'Virology', 
                                'Dermatology', 'Allergy', 'Infectious Diseases',
                                'Rheumatology', 'Toxicology'},            
                   'NMHA' : {'Clinical Neurology','Psychiatry and Mental Health', 
                             'General Neuroscience','Neuroscience (miscellaneous)' , 
                             'Behavioral Neuroscience', 'Biological Psychiatry',
                             'Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                             'Developmental Neuroscience', 'Neurology' ,'Psychiatry Mental Health',
                             'Psychology (miscellaneous)', 'Experimental and Cognitive Psychology', 
                             'Neuropsychology and Physiological Psychology'},
                             
                   'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine', 
                            'Critical Care and Intensive Care Medicine', 'Emergency Medicine',
                            'Endocrinology, Diabetes and Metabolism', 'Pulmonary and Respiratory Medicine',
                            'Epidemiology','Family Practice', 'Gastroenterology',
                            'Health Informatics','Health Policy','Hematology','Hepatology', 
                            'Internal Medicine','Nephrology', 'Ophthalmology', 
                            'Orthopedics and Sports Medicine', 'Otorhinolaryngology', 
                            'Transplantation','Urology', 'Critical Care','Respiratory Care'}}
                   
    #Filter the author publication subjects ASJC codes to UNSW med theme ASJC listed codes
    theme_subjects = {key:value for key, value in subjects.items() if key in data_set}
    #If ASJC codes are matched then mapped to the data dictionary of theme Subjects
    if theme_subjects:
        for theme, match in theme_dict.items():
            for subject in theme_subjects:
               if subject in match:
                  result[theme] += theme_subjects[subject]
        return theme_subjects, dict(result) 
    else:
        return subjects, None        
    
def theme_key(result):
    """Mapping function match the result to theme.
    
    Parameters
    ----------
    result : dict
             ASJC codes categories of Scopus author Subject areas
    Returns
    ----------
    theme1 : str
             Mapping of ASJC codes to UNSW theme
           
    alternative : dict 
             ASJC codes categories which are not mapped to theme
    """
    #The largest publications number mapped to the main theme and subset 
    #of publication is return for further analysis
    if result:
        theme1 = max(result, key=lambda k: result[k]) 
        alternative = {k:v for k, v in result.items() if k not in theme1}
        return theme1, alternative
    else:
        return result, None



def researcher_theme(SCOPUS_ID):
    
    '''Input is list/tuple of author scopus id 
     get name,subject areas attributes from 
     SCOPUS author object return a pandas dataframe.
     The attributes are as columns of the dataframe
     
    Parameter
    ----------
    SCOPUS_ID :  str or int
                 Author Scopus ID  
    Return
    ----------
    result, main: tuple
                Publication mapping and theme mapping''' 
    
    #Retriving author from SCOPUS
    
    # Retrive autor object from SCOPUS database
    au = AuthorRetrieval(SCOPUS_ID)
    docs = dict(au.classificationgroup)
    names = [(publication.area, int(docs[publication.code])) for publication in au.subject_areas]
    names.sort(reverse=True, key=itemgetter(1))
    
    publications = dict(names)    
    
    research_area, result = check_theme(publications)
    main, secondary_area = theme_key(result)
    if main: 
       alternative, all_areas = theme_key(secondary_area)
            
       return (result, main)
        
    return (result, "All_any themes")
  