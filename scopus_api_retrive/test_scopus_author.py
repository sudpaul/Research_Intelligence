# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:19:44 2018

@author: z3525552
"""
import pytest
import scopus_authors_retrive 

spec = """
       scopus_id : '7005082840'
       columns: 
       - "SCOPUS_ID"
       - "name"
       - "h_index"
       - "documents_total"
       - "number_first_author"
       - "number_last_author"
       - "total_citing_papers"
       - "orcid"
       """
      

def check_schema(df, meta_columns):
    
    for col in df.columns:
        assert col in meta_columns, f'"{col}" not in metadata column spec'
    

def test_scopus_author():
    
    import yaml
    
    
    df = scopus_authors_retrive.make_dataframe(['7005082840'])
    
    metadata = yaml.load(spec)

    check_schema(df, metadata)