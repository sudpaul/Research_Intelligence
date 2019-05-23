# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:52:38 2019

@author: z3525552
"""

# change the datatype to np.int of publication count 
    
# sort the data key publication count
    
# map to dictionary
    
def get_subject_docs(identifier, refresh):
    """Returns (subject area, number of documents)-tuples."""
    
    from scopus import AuthorRetrieval
    from operator import itemgetter
    
    author = AuthorRetrieval(identifier, refresh=refresh)
    docs = dict(author.classificationgroup)
    names = [(publication.area, int(docs[publication.code])) for publication in author.subject_areas]
    
    names.sort(reverse=True, key=itemgetter(1))
    
    publications = dict(names)    
    
    return publications