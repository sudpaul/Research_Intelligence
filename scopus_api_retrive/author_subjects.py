# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:52:38 2019

@author: z3525552

Upgrade scopus from 0.8 to 1.6 deprecated support ScopusAuthor and
introduction of new class AuthorRetieval
"""
def get_subject_docs(identifier):
    
    """
    Parameter
    ----------
    identifier : str or int
    
    Returns
    ----------
    
    publication: dict
                subject area dict key and value number of documents.
    """
    
    from scopus_authors_retrive import scopus_author
    from operator import itemgetter
    
    author = scopus_author(identifier)
    # publication number mapping to ASJC code dictionary
    docs = dict(author.classificationgroup)
    #Retrive the names and number of publication from author subject areas
    names = [(publication.area, int(docs[publication.code])) for publication in author.subject_areas]
      
    # sort the data key publication count
    names.sort(reverse=True, key=itemgetter(1))
    
    publications = dict(names)    
    
    return publications