"""Tests transport framework"""
from REST import REST
from Transport import Transport

TRANSPORT = Transport(debug=True)

# HTTP Code tests
def test_defined_response():
    """Test HTTP expected response"""
    assert TRANSPORT.check_http_response(200, 200) is True

def test_bad_response():
    """Tests unexpected response is returns as False"""
    assert TRANSPORT.check_http_response(999) is False

def test_good_http_responses():
    """Checks good responses are True"""
    demo_api = REST(url='postman-echo.com')
    for code in (200, 201, 204):
        assert TRANSPORT.check_http_response(demo_api.get("/status/%i" % code).status_code) is True

def test_bad_http_responses():
    """Checks good responses are False"""
    demo_api = REST(url='postman-echo.com')
    for code in (400, 401, 403, 404, 422):
        assert TRANSPORT.check_http_response(demo_api.get("/status/%i" % code).status_code) is False

# def test_transport_get_stops():
#     """Tests transport get stops"""
#     assert TRANSPORT.get_stops() is True
