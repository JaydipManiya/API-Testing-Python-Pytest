"""
Here, we are going to use https://reqres.in sample server to run different requests methods.
You can find more details on https://reqres.in/ .

Command to run all tests: pytest -vs Test\test_requests.py
Command to run all tests and generate pytest html report: pytest -vs --capture sys Test\test_requests.py --html=report.html
"""

import json
import pytest
import Lib.APIRequests as ApiReq
from Lib.LoggerUtils import set_logger

# Global defines
BASE_URL = "https://reqres.in"


@pytest.fixture(scope="class")
def class_fixture(request):
    """
    Class fixture to initialize APIRequests instance. This fixture will execute once before class execution.
    """
    print("Execute class_fixture")
    request.cls.req_obj=ApiReq.APIRequests(base_url=BASE_URL)
    request.cls.logger = set_logger(__name__)
    return


@pytest.mark.usefixtures("class_fixture")
class TestRequestsMethods(object):

    def test_execute_get_method(self):
        """
        Method to execute GET request and verify returned status code and response.
        """
        self.logger.info("Execute GET request test")
        print("Execute GET request test")
        endpoint = '/api/users/2'
        status_code, response = self.req_obj.execute_api_request(request_type=ApiReq.GET_METHOD, endpoint=endpoint)
        print("Response code is: {}".format(status_code))
        print("Response is: {}".format(response))

        assert status_code == 200, "Expected status code is : {} but received status code : {}".format(200, status_code)
        assert response["support"]["url"] == "https://reqres.in/#support-heading", "Received unexpected URL in response"
        assert response["data"]["first_name"] != "", "Received empty first_name in response"

    def test_execute_post_request(self):
        """
        Method to execute POST request and verify returned status code and response.
        """
        print("Execute POST request test")
        data = {"name": "morpheus", "job": "leader"}
        endpoint = '/api/users'

        status_code, response = self.req_obj.execute_api_request(request_type=ApiReq.POST_METHOD, endpoint=endpoint,
                                                                 data=json.dumps(data))
        print("Response is: {}".format(response))
        assert status_code == 201, "Expected status code is : {0} but received status code : {1}".format(200, status_code)
        assert response["name"] == "morpheus", "Received invalid name in response. response is : {0}, " \
                                               "expected name is : {1}".format(response, "morpheus")
        assert response["job"] == "leader", "Received invalid job in response. response is : {0}, " \
                                            "expected job is : {1}".format(response, "leader")

    def test_execute_put_request(self):
        """
        Method to execute PUT request and verify returned status code and response.
        """
        print("Execute PUT request test")
        endpoint = '/api/users/2'
        data = {"name": "morpheus", "job": "zion resident"}
        status_code, response = self.req_obj.execute_api_request(request_type=ApiReq.PUT_METHOD, endpoint=endpoint,
                                                                 data=json.dumps(data))
        print("PUT Response is: {}".format(response))
        assert status_code == 200, "Expected status code is : {} but received status code : {}".format(200, status_code)
        assert response["job"] == "zion resident", "Job is not updated. Returned response is : {}".format(response)

    def test_execute_delete_request(self):
        """
        Method to execute DELETE request and verify returned status code and response.
        """
        print("Execute DELETE request test")
        endpoint = '/api/users/2'
        status_code, response = self.req_obj.execute_api_request(request_type=ApiReq.DELETE_METHOD, endpoint=endpoint)
        print("Response is: {}".format(response))
        assert status_code == 204, "Expected status code is : {} but received status code : {}".format(204, status_code)

