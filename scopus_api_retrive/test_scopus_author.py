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


if __name__ == '__main__':
    unittest.main()