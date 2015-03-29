Pyyelp
=======

Pyyelp is a python wrapper for the **Yelp API v2**

`Yelp API v2 docs <https://www.yelp.com/developers/documentation>`

Fast install
-------
::
   pip install pyyelp2

Fase example
-------
::
   from pyyelp import Yelp
   yelp = Yelp(oauth_consumer_key='', oauth_token='', oauth_signature='')

   search_result = yelp.search(term='foo store', lat='', lon='')

TODO
-------
- Authentication
- Search API
- Business API
- Phone Search API
- Errors

Contribute
-------
1. Fork the `repo <https://github.com/motte/python-yelp>`_
2. Test the code thoroughly
3. Code with `pep8 <http://www.python.org/dev/peps/pep-0008/>`_ rules
4. Pull request

Tests
-------
Unit test setup to come.
