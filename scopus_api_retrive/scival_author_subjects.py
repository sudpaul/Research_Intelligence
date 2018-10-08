# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:51:59 2018

@author: z3525552
"""
def author_subject_area(SCOPUS_IDs):
    
    """The function is to retrive bulk subject categories of SCOPUS author. 
    Then custom mapped to specific keywords for futher data analysis.
    
    Parameter
    ----------
    scopus_ids : list or tuple
                number of SCOPUS author id for mapping
    Return
    ----------
    df : obj
         pandas dataframe object """
    
    assert isinstance(SCOPUS_IDs, (str, int))

    
    import pandas as pd
    from scopus_authors_retrive import scopus_author
    from collections import defaultdict
    from apply_theme import main_theme
    
    scopus_id = defaultdict(list)
  
    for author in SCOPUS_IDs:
        scopus_id['SCOPUS_ID'].append(author)
       #Retriving author from SCOPUS
        au = scopus_author(author)
        subjects, documents = zip(*au.categories)
        primary_theme, result = main_theme(subjects)
        scopus_id['Name'].append(au.name)      
        scopus_id['organisation'].append(au.current_affiliation)      
        scopus_id['Main_theme'].append(primary_theme)
        scopus_id['Alternative_theme'].append(' ')
        scopus_id['Result'].append(result)
        scopus_id['Subject_category'].append(subjects)
        scopus_id['document_number'].append(documents)
    ## Add columns for each 'Theme' and tranfrom subjects to match 'Theme'   
       
    df = pd.DataFrame.from_dict(scopus_id)
    
    return df