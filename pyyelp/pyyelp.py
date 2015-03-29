#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pyyelp.services.search import Search


class Yelp(object):
    """
    Example:

        yelp = Yelp(...)
    """


    def __init__(self, **config):
        self._search_results = Search(**config)
        self._business_results = Business(**config)
        self._phone_results = Phone(**config)


    @property
    def search_results(self):
        """
        :ref:`Search service <Search service>`
        """
        return self._search_results


    @property
    def business_results(self):
        return self._business_results


    @property
    def phone_results(self):
        return self._phone_results
        
