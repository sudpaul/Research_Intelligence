# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:14:07 2018

@author: z3525552
"""
def scopus_author(scopus_id):
    
    '''Helper function to invoke the Scopus Author from SCOPUS database
     download the author contents and return author object
    
    Parameter
    ----------
    scopus_id : str or int
    
    Return
    ----------
    author : Scopus Author object'''
    
    assert isinstance(scopus_id, (str, int))
    
    from pybliometrics.scopus import AuthorRetrieval
    
    # Retrive autor object from SCOPUS database
    author = AuthorRetrieval(scopus_id)
    
    return author


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
    
    from collections import defaultdict
    result = defaultdict(int)
    
    data_set = {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)',
            'Endocrinology','General Immunology and Microbiology','Immunology and Microbiology (miscellaneous)',
            'Immunology', 'Microbiology','Immunology and Allergy', 'Microbiology (medical)',
            'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
            'Rheumatology', 'Toxicology', 'Clinical Neurology','Psychiatry and Mental Health', 
            'General Neuroscience', 'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
            'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
            'Developmental Neuroscience', 'Neurology' ,'Psychiatry Mental Health','Psychology (miscellaneous)',
            'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology',
            'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine', 'Critical Care and Intensive Care Medicine',
            'Emergency Medicine','Endocrinology, Diabetes and Metabolism','Pulmonary and Respiratory Medicine','Epidemiology','Family Practice',
            'Gastroenterology','Health Informatics','Health Policy','Hematology','Hepatology', 'Internal Medicine','Nephrology', 'Ophthalmology',
            'Orthopedics and Sports Medicine', 'Otorhinolaryngology', 'Transplantation','Urology', 'Critical Care','Respiratory Care'}
    
        
    theme_dict = {'Cancer' : {'Cancer Research','Oncology', 'Cancer', 'Radiation', 'Oncology(nursing)'} ,
                  'Triple I' : {'Endocrinology','General Immunology and Microbiology','Immunology and Microbiology (miscellaneous)',
                                'Immunology', 'Microbiology','Immunology and Allergy', 'Microbiology (medical)',
                  'Parasitology', 'Virology', 'Dermatology', 'Allergy', 'Infectious Diseases',
                  'Rheumatology', 'Toxicology'},            
                   'NMHA' : {'Clinical Neurology','Psychiatry and Mental Health', 'General Neuroscience',
                   'Neuroscience (miscellaneous)' , 'Behavioral Neuroscience', 
                   'Biological Psychiatry','Cellular and Molecular Neuroscience','Cognitive Neuroscience',
                   'Developmental Neuroscience', 'Neurology' ,'Psychiatry Mental Health','Psychology (miscellaneous)',
                   'Experimental and Cognitive Psychology', 'Neuropsychology and Physiological Psychology'},
                   'NCD' : {'Cardiology', 'Cardiovascular Medicine','Cardiology and Cardiovascular Medicine', 
                            'Critical Care and Intensive Care Medicine', 'Emergency Medicine','Endocrinology, Diabetes and Metabolism',
                            'Pulmonary and Respiratory Medicine','Epidemiology','Family Practice', 'Gastroenterology',
                            'Health Informatics','Health Policy','Hematology','Hepatology', 'Internal Medicine','Nephrology', 
                            'Ophthalmology', 'Orthopedics and Sports Medicine', 'Otorhinolaryngology', 'Transplantation','Urology', 
                            'Critical Care','Respiratory Care'}}    
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

def author_subject_area(SCOPUS_IDs):
    
    '''Input is list/tuple of author scopus id 
     get name,subject areas attributes from 
     SCOPUS author object return a pandas dataframe.
     The attributes are as columns of the dataframe
     
    Parameter
    ----------
    scopus_ids : list or tuple 
                 Author Scopus IDs  
    Return
    ----------
    df        : Obj
                Pandas dataframe''' 
    
    import pandas as pd
    from collections import defaultdict
    from operator import itemgetter
    
    assert isinstance(SCOPUS_IDs,(list, tuple))
    
    scopus_id = defaultdict(list)
  
    for author in SCOPUS_IDs:
        scopus_id['SCOPUS_ID'].append(author)
       #Retriving author from SCOPUS
        au = scopus_author(author)
        docs = dict(au.classificationgroup)
        #Retrive the names and number of publication from author subject areas
        names = [(publication.area, int(docs[publication.code])) for publication in au.subject_areas]
        # sort the data key publication count
        names.sort(reverse=True, key=itemgetter(1))
        publications = dict(names) 
        research_area, result = check_theme(publications)
        scopus_id['Name'].append(au.given_name)      
        scopus_id['Subjects_area'].append(research_area)
        scopus_id['Result'].append(result)
        main, secondary_area = theme_key(result)
        if main: 
            alternative, all_areas = theme_key(secondary_area)
            scopus_id['Main_theme'].append(main)
            scopus_id['Alternative_theme'].append(alternative)
        else:
            scopus_id['Main_theme'].append("All/Any")
            scopus_id['Alternative_theme'].append("All_any themes")
    ## Add columns for each 'Theme' and transfrom subjects to match 'Theme'   
       
    dataframe = pd.DataFrame.from_dict(scopus_id)
    
    return dataframe