"""A module to get data from NSW Transport"""
import json
from REST import REST

class Transport():
    """Framework for NSW Transport API"""
    def __init__(self, debug=False):
        self.debug = debug

    def get_stops(self):
        """Get the PT stops in the area"""
        with open('api_key.json') as json_file:
            api_key = json.load(json_file)['api_key']

        # Set headers
        headers = {'Accept': 'application/json', 'Authorization': 'apikey %s' % api_key}

        # Create instance of configured REST
        rest = REST(url='api.transport.nsw.gov.au', debug=self.debug, headers=headers)

        # URL to get
        url = "/v1/tp/departure_mon?outputFormat=rapidJSON&coordOutputFormat=EPSG%3A4326&mode=direct&type_dm=stop&name_dm=10111010&itdDate=20161001&itdTime=1200&departureMonitorMacro=true&TfNSWDM=true&version=10.2.1.42"

        response = rest.get(url)

        # Check response was good
        self.check_http_response(response.status_code)

        print(response.text)

        return True

    # Check HTTP codes for common errors
    # Allow specifying an expected code for custom use
    def check_http_response(self, status_code, expected_code=None):
        """Checks if response is a expected or a known good response"""
        if status_code == expected_code:
            return True
        elif status_code == 200:
            if self.debug:
                print('HTTP 200\nOK')
            return True
        elif status_code == 201:
            if self.debug:
                print('HTTP 201\nCreated')
            return True
        elif status_code == 204:
            if self.debug:
                print('HTTP 204\nEmpty response')
            return True
        elif status_code == 400:
            if self.debug:
                print('HTTP 400\nBad request')
            return False
        elif status_code == 401:
            print('HTTP 401\nCheck Authorisation')
            return False
        elif status_code == 403:
            print('HTTP 403\nPermission denied, check AW permissions')
            return False
        elif status_code == 404:
            print('HTTP 404\nNot found')
            return False
        elif status_code == 422:
            print('HTTP 422\nInvalid SearchBy Parameter')
            return False
        else:
            print('Unknown code %s' % status_code)
            return False
