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
        status_codes = {}
        status_codes[200] = True, 'HTTP 200: OK'
        status_codes[201] = True, 'HTTP 201: Created'
        status_codes[204] = True, 'HTTP 204: Empty Response'
        status_codes[400] = False, 'HTTP 400: Bad Request'
        status_codes[401] = False, 'HTTP 401: Check WSO Credentials'
        status_codes[403] = False, 'HTTP 403: Permission denied'
        status_codes[404] = False, 'HTTP 404: Not found'
        status_codes[422] = False, 'HTTP 422: Invalid searchby Parameter'

        if status_code == expected_code:
            return True
        if status_code in status_codes:
            if self.debug:
                print(status_codes[status_code][1])
            return status_codes[status_code][0]

        print('Unknown code %s' % status_code)
        return False
