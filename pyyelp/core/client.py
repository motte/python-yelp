# -*- encoding: utf-8 -*-

# Python libraries
import argparse
import json
import pprint
import requests
import sys
import urllib
import urllib2
import oauth2

from .errors import YelpError


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'san francisco food trucks'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credentials that are required by the user
CONSUMER_KEY = None
CONSUMER_SECRET = None
TOKEN = None
TOKEN_SECRET = None


VALID_REQUEST_ARGS = set((
    ))


class Client(object):
    """
    Client to send configured requests to Yelp API
    """

    def __init__(self, **kwargs):
        self.requester = requests.session()
        self.config = {
            'base_url': 'https://api.yelp.com/v2/'
        }
        
            
