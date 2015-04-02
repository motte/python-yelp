__author__ = 'michael'

from pyyelp.pyyelp import Yelp


def search_test():
    yelp = Yelp()
    print(yelp.search(term='Starbucks', location='San Francisco'))


def business_test():
    yelp = Yelp()
    print(yelp.get_business_by_id('yelp-san-francisco'))


def phone_test():
    yelp = Yelp()
    print(yelp.search_by_phone_number('8314399507'))


search_test()
business_test()
phone_test()