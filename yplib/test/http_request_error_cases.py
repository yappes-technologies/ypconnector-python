from ypconnector import YappesLibrary

getParameters = {
    "headers": {"Content-Type": "application/json"},
    "queryparams": "",
    "payload": {},
}
postParameters = {
    "headers": {"Content-Type": "application/json"},
    "queryparams": "",
    "payload": "postPayLoad",
}
putParameters = {
    "headers": {"Content-Type": "application/json"},
    "queryparams": "",
    "payload": "putPayLoad",
}

token = ""
getUrl = "http://localhost:8080/getdata"
postUrl = "http://localhost:8080/postdata"
putUrl = "http://localhost:8080/putdata"


getResponseObj = {"name": "getUser", "id": "1025", "age": "22"}
addResponseObj = {"name": "addUser", "id": "1026", "age": "10"}
updateResponseObj = {"name": "updateUser", "id": "1025", "age": "22"}
ypObj = YappesLibrary(token)

# SUCCESS RESPONSES

# 200 OK
def OK():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 200, "200 OK"
    else:
        assert 2 == 1, "error"


def noContent():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 204, "204 No Content "
    else:
        assert 2 == 1, "error"


# CLIENT ERRORS
def badRequest():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 400, "400  Bad Request"
    else:
        assert 2 == 1, "error"


def unauthorizedAccess():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 401, "401 Unauthorized Access "
    else:
        assert 2 == 1, "error"


def notAcceptable():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 406, "406 Not Acceptable "
    else:
        assert 2 == 1, "error"


def notFound():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 404, "404  Not Found"
    else:
        assert 2 == 1, "error"


def Forbidden():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 403, "403  Forbidden "
    else:
        assert 2 == 1, "error"


def methodNotAllowed():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 405, "405 Method Not Allowed "
    else:
        assert 2 == 1, "error"


def unsupportedMediaType():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 415, "415 Unsupported Media Type "
    else:
        assert 2 == 1, "error"


def requestTimeout():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 408, "408  Request Timeout"
    else:
        assert 2 == 1, "error"


# SERVER ERROR
def internalServerError():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 500, "500 Internal Server Error"
    else:
        assert 2 == 1, "error"


def badGateway():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 502, "502 Bad Gateway "
    else:
        assert 2 == 1, "error"


def serviceUnavailable():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 503, "503 Service Unavailable "
    else:
        assert 2 == 1, "error"


def gatewayTimeout():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["statusCode"] == 504, "504 Gateway Timeout"
    else:
        assert 2 == 1, "error"


# success responses
OK()
noContent()
# client Error
badRequest()
unauthorizedAccess()
notAcceptable()
notFound()
Forbidden()
methodNotAllowed()
unsupportedMediaType()
requestTimeout()
# server errors
internalServerError()
badGateway()
serviceUnavailable()
gatewayTimeout()

