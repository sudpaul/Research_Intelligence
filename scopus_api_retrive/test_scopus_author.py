# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:19:44 2018

@author: z3525552
"""
import warnings
import unittest
from pybliometrics.scopus import AuthorRetrieval

warnings.simplefilter("always")

class TestScopusAuthor(unittest.TestCase):

    def test_author(self):
        self.assertEqual(AuthorRetrieval('7005789553', refresh=True).given_name, 'Sean')
    
    def test_date_created(self):
        self.assertEqual(AuthorRetrieval('7005789553').date_created, (2005, 12, 3))
    
    def test_orcid(self):
        self.assertEqual(AuthorRetrieval('7005789553').orcid, '0000-0001-6072-8309')
    
    def test_publication_range(self):
        self.assertEqual(AuthorRetrieval('7005789553').publication_range[0], '1985')
        self.assertTrue(int(AuthorRetrieval('7005789553').publication_range[1]) >= 2018)

if __name__ == '__main__':
    unittest.main()