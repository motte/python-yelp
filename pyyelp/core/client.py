# -*- encoding: utf-8 -*-


import requests


from .errors import YelpError


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
        
            
