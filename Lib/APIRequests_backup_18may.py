"""
This file contains common methods to execute APIs.
"""

import requests
import json
from LoggerUtils import LoggerUtils

class APIRequests:

    def __init__(self, base_url, req_timeout=10):
        self.base_url = base_url
        self.timeout = req_timeout
        self.logger = LoggerUtils.set_log()

    def execute_api_request(self, request_type, endpoint, data, header):
        """
        Method to execute given requests (GET, POST, PUT, DELETE).
        :param request_type: request type that want to execute
        :param endpoint: API endpoint
        :param data: API data
        :param header: API header
        :return: status_code: API status code
                response: API returned response
        """
        response, status_code = "", ""
        try:
            URL = self.base_url + endpoint
            if request_type == "GET":
                response = requests.get(url=URL, timeout=self.timeout)
            elif request_type == "POST":
                response = requests.post(url=URL, headers=header, data=data, timeout=self.timeout)
            elif request_type == "PUT":
                response = requests.put(url=URL, headers=header, data=data, timeout=self.timeout)
            elif request_type == "DELETE":
                response = requests.delete(url=URL, timeout=self.timeout)
            else:
                response = "Invalid request type found"
            status_code = response.status_code
            response = response.json()
        except requests.exceptions.HTTPError as exhttp:
            response = exhttp
        except requests.exceptions.ConnectionError as exconn:
            response = exconn
        except requests.exceptions.Timeout as extimeout:
            response = extimeout
        except requests.exceptions.RequestException as exreq:
            response = exreq
        except Exception as ex:
            response = "Exception raised during execution of {} request, exception is : {}".format(request_type, ex)
        return status_code, response

    def get_request(self, endpoint):
        """
        Method to execute GET request.
        :param endpoint: API endpoint
        :return status_code: API status code
                response: API returned response
        """
        self.logger("Inside get_request method")
        URL = self.base_url + endpoint
        response, status_code = "", ""
        try:
            response = requests.get(url=URL, timeout=self.timeout)
            status_code = response.status_code
            response = response.json()
        except Exception as ex:
            response = "Exception raised during execution of GET request, exception is : {}".format(ex)
            print(response)

        return status_code, response

    def post_request(self, endpoint, data, headers):
        """
        Method to execute POST request.
        :param endpoint: API endpoint
        :param data: API data
        :param headers: API header
        :return: status_code: API status code
                response: API returned response
        """
        URL = self.base_url + endpoint
        response, status_code = "", ""
        try:
            response = requests.post(url=URL, headers=headers, data=data, timeout=self.timeout)
            status_code = response.status_code
            response = response.json()
        except Exception as ex:
            response = "Exception raised during execution of POST request, exception is : {}".format(ex)
            print(response)

        return status_code, response

    def put_request(self, endpoint, data, headers):
        """
        Method to execute PUT request.
        :param endpoint: API endpoint
        :param data: API data
        :param headers: API header
        :return: status_code: API status code
                response: API returned response
        """
        URL = self.base_url + endpoint
        response, status_code = "", ""
        try:
            response = requests.put(url=URL, headers=headers, data=data, timeout=self.timeout)
            status_code = response.status_code
            response = response.json()
        except Exception as ex:
            response = "Exception raised during execution of PUT request, exception is : {}".format(ex)
            print(response)

        return status_code, response

    def delete_request(self, endpoint):
        """
        Method to execute DELETE request.
        :param endpoint: API endpoint
        :return: status_code: API status code
                response: Empty string on success else error message.
        """
        print("Inside delete_request")
        URL = self.base_url + endpoint
        response, status_code = "", ""
        try:
            response = requests.delete(url=URL, timeout=self.timeout)
            status_code = response.status_code
        except Exception as ex:
            response = "Exception raised during execution of DELETE request, exception is : {}".format(ex)
            print(response)

        return status_code, response
