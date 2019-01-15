# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:57:33 2019

@author: z3525552
"""

from scopus_authors_retrive import scopus_author   
import pandas as pd

def author_publication(scopus_id):
    
    """Retriving Journal publication detail from Scopus 
    input scopus_id for which  return publication history
   
    Parameter
    ----------
    scopus_id : str
               Author Scopus id
    journal : obj
              pandas dataframe object         
    """
       

    researcher = scopus_author(scopus_id)
    journals = pd.DataFrame(researcher.publication_history) 
    journals.columns = ['sourcetitle','abbreviation','publication_type','issn']

    return journals      


def publication_subjects(scopus_id):
        
    """Retriving Journal publication detail from Scopus 
    input scopus_id for which  return publication history
   
    Parameter
    ----------
    scopus_id : str
               Author Scopus id
    subjects : obj
              pandas dataframe object         
    """
    
    researcher = scopus_author(scopus_id)
    
    subjects = pd.DataFrame(data=researcher.subject_areas)
    subjects.columns = ['subjects','n_documents','subject_categories','asjc_codes']
    subjects = subjects.sort_values(by=['n_documents'], ascending=False)
    
    return subjects

def get_coauthors(scopus_id):
    """Retrieves basic information about co-authors as a list of
        namedtuples in the form
        name, scopus_id, affiliation, categories
        where areas is a list of subject area codes joined by "; ".
        Note: These information will not be cached and are slow for large
        coauthor groups.
    """
    from collections import namedtuple
        # Get number of authors to search for
    res = scopus_author(scopus_id)
    data = res.get_coauthors()
        
        # Store information in namedtuples
    fields = 'surname given_name id areas affiliation_id name city country'
    coauth = namedtuple('Coauthor', fields)
    coauthors = []
        # Iterate over search results in chunks of 25 results
    count = 0
    while count < len(data):
        params = {'start': count, 'count': 25}
        res = download(url=self.coauthor_link, params=params, accept='json')
        data = loads(res.text)['search-results'].get('entry', [])
        # Extract information for each coauthor
        for entry in data:
            aff = entry.get('affiliation-current', {})
            try:
                areas = [a['$'] for a in entry.get('subject-area', [])]
            except TypeError:  # Only one subject area given
                areas = [entry['subject-area']['$']]
            new = coauth(surname=entry['preferred-name']['surname'],
                         given_name=entry['preferred-name'].get('given-name'),
                         id=entry['dc:identifier'].split(':')[-1],
                         areas='; '.join(areas),
                         affiliation_id=aff.get('affiliation-id'),
                         name=aff.get('affiliation-name'),
                         city=aff.get('affiliation-city'),
                         country=aff.get('affiliation-country'))
            coauthors.append(new)
        count += 25
    return coauthors