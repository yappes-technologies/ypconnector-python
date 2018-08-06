import http.client
import json
from urllib.parse import urlparse
import urllib.request
import sys
import json
import requests

responseSchema = {"headers": "", "statusCode": "", "statusMessage": "", "body": ""}


class YappesLibrary:
    def __init__(self, token):
        self.xyappeskey = token

    # get operation
    def get(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "get",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            if parameters["queryparams"] != "":
                URL = apiUrl + "?" + parameters["queryparams"]
            else:
                URL = apiUrl
            conn = requests.get(
                URL, data=json.dumps(parameters["payload"]), headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            print(responseSchema)
            return responseSchema
        except:
            print(sys.exc_info())

    # post operation
    def post(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "POST",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            if parameters["queryparams"] != "":
                URL = apiUrl + "?" + parameters["queryparams"]
            else:
                URL = apiUrl

            conn = requests.post(
                URL, data=json.dumps(parameters["payload"]), headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            print(responseSchema)
            return responseSchema
        except:
            print(sys.exc_info())

    # put operation
    def put(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "PUT",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            if parameters["queryparams"] != "":
                URL = apiUrl + "?" + parameters["queryparams"]
            else:
                URL = apiUrl

            conn = requests.put(
                URL, data=json.dumps(parameters["payload"]), headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            print(responseSchema)
            return responseSchema
        except:
            print(sys.exc_info())

