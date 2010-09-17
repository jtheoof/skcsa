import urllib

from api import RestAPI

class GoogleMapsGeoCodeAPI(RestAPI):

    def __init__(self, logger):
        super(GoogleMapsGeoCodeAPI, self).__init__('http://maps.google.com/maps/api/geocode/', logger)
        
    def make_api_call(self, parameters):
        end_url = u'json?'
        parameters['sensor'] = 'false'
       
        for key, value in parameters.items():
            end_url += self.encode_key_value(key, value)
        
        return self.make_request('%s%s' % (self.base_url, end_url))
        
    def get_geocode(self, street, city, country):
        address = u'%s %s %s' % (street, city, country)
        # converting explicitly to utf-8 due to bug: http://bugs.python.org/issue8136
        address = urllib.quote_plus(address.encode('utf8'))
        parameters = {
            'address': address,
        }
        
        return self.make_api_call(parameters)
