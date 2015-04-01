#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.conf import settings

import argparse
import json
import pprint
import sys
import urllib
import urllib2

from pyyelp.services.search import Search
from pyyelp.services.business import Business
from pyyelp.services.phone import Phone


class Yelp(object):
    """
    Example:

        yelp = Yelp(...)
    """
    API_HOST = settings.YELP_API_HOST or ''
    SEARCH_PATH = '/v2/search/'
    BUSINESS_PATH = '/v2/business/'
    PHONE_PATH = '/v2/phone_search/'

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
        
