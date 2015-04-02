__author__ = 'michael'

from pyyelp.pyyelp import Yelp


yelp = Yelp()
print(yelp.search(term='Starbucks', location='San Francisco'))