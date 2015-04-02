__author__ = 'michael'


class Search(object):

    def search(self, term=None, location=None, latitude=None, longitude=None, offset=None, sort=0, category_filter=None,
               radius_filter=None, deals_filter=False, search_limit=20):
        """
        Search method that uses Yelp's Search API to retrieve releavant businesses

        For current details, refer to: https://www.yelp.com/developers/documentation/v2/search_api

        :param term: The search term(s)
        :param location: required string that has address, neighborhood, city, state or zip, optional country
        :param latitude: double geo latitude
        :param longitude: double geo longitude
        :param offset: Offset the results by this amount
        :param sort: Int sort by 0=Best matched (default), 1=Distance, 2=Highest Rated,
        :param category_filter: See https://www.yelp.com/developers/documentation/v2/all_category_list
        :param radius_filter: Int Search radius in meters
        :param deals_filter: boolean to exclusively search for businesses with deals
        :param search_limit: Int number of results to return
        :return: JSON response
        """

        url_params = {
            'term': term.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': search_limit
        }

        if latitude is not None and longitude is not None and latitude is int and longitude is int:
            url_params['cll'] = '{0},{1}'.format(latitude, longitude)

        if offset is not None:
            url_params['offset'] = offset

        if sort is 1 or sort is 2:
            url_params['sort'] = sort

        if category_filter is not None:
            url_params['category_filter'] = category_filter

        if radius_filter is not None:
            url_params['radius_filter'] = radius_filter

        if deals_filter:
            url_params['deals_filter'] = deals_filter

        return self.request(API_HOST, SEARCH_PATH, url_params=url_params)