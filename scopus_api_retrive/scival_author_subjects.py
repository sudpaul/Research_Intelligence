# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:51:59 2018

@author: z3525552
"""


def author_subject_area(SCOPUS_IDs):
    
    import pandas as pd
    from scopus_authors_retrive import scopus_author
    from collections import defaultdict
    
    scopus_id = defaultdict(list)
  
   
    for author in SCOPUS_IDs:
       
       scopus_id['SCOPUS_ID'].append(author)
       #Retriving author from SCOPUS
       au = scopus_author(author)
       
       scopus_id['Name'].append(au.name)
       subjects, documents = zip(*au.categories)
       
       scopus_id['subject_categorties'].append(subjects)
       scopus_id['document_number'].append(documents)
    ## Add columns for each 'Theme' and tranfrom subjects to match 'Theme'   
       
       
       
    df = pd.DataFrame.from_dict(scopus_id)
    
    
    
    return df