# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:38:31 2018

@author: z3525552
"""

def save_excel(df, filename, sheetname):
    
    '''This helper function takes input dataframe, name of the excel file,
    sheetname and save the file as specified in the directory 
    print out the status''' 
    import pandas as pd
    
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,sheetname, index=False, encoding='utf-8')
    writer.save()
    
    return "Your Excel file is ready!"