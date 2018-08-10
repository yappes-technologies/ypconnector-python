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
deleteParameters = {
    "headers": {"Content-Type": "application/json"},
    "queryparams": "",
    "payload": "deletePayLoad",
}
patchParameters = {
    "headers": {"Content-Type": "application/json"},
    "queryparams": "",
    "payload": "patchPayLoad",
}


token = ""
getUrl = "http://localhost:8080/getdata"
postUrl = "http://localhost:8080/postdata"
putUrl = "http://localhost:8080/putdata"
deleteUrl = "http://localhost:8080/deletedata"
patchUrl = "http://localhost:8080/patchdata"

getResponseObj = {"name": "getUser", "id": "1025", "age": "22"}
addResponseObj = {"name": "addUser", "id": "1026", "age": "10"}
updateResponseObj = {"name": "updateUser", "id": "1025", "age": "22"}
deleteResponseObj = {"name": "deleteUser", "id": "1025", "age": "22"}
patchResponseObj = {"name": "patchUser", "id": "1025", "age": "22"}
ypObj = YappesLibrary(token)

# GET OPERATION ASSERTION TEST
def getOperation():
    connection = ypObj.get(getUrl, getParameters)
    if connection is not None:
        assert connection["body"] == str(getResponseObj), "GET Operation Test"
    else:
        assert 2 == 1, "error"


# POST OPERATION ASSERTION TEST
def postOperation():
    connection = ypObj.post(postUrl, postParameters)
    if connection is not None:
        assert connection["body"] == str(addResponseObj), "POST Operation Test"
    else:
        assert 2 == 1, "error"


# PUT OPERATION ASSERTION TEST
def putOperation():
    connection = ypObj.put(putUrl, putParameters)
    if connection is not None:
        assert connection["body"] == str(updateResponseObj), "PUT Operation Test"
    else:
        assert 2 == 1, "error"
# DELETE OPERATION ASSERTION TEST        
def deleteOperation():
    connection = ypObj.delete(deleteUrl, deleteParameters)
    if connection is not None:
        assert connection["body"] == str(deleteResponseObj), "DELETE Operation Test"
    else:
        assert 2 == 1, "error"
# PATCH OPERATION ASSERTION TEST        
def patchOperation():
    connection = ypObj.patch(patchUrl, patchParameters)
    if connection is not None:
        assert connection["body"] == str(patchResponseObj), "PATCH Operation Test"
    else:
        assert 2 == 1, "error"

getOperation()
postOperation()
putOperation()
deleteOperation()
patchOperation()