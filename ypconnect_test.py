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


ypObj = YappesLibrary(token)

print("post operation")
ypObj.post(postUrl, postParameters)

print("put operation")
ypObj.put(putUrl, putParameters)

print("get operation")
ypObj.get(getUrl, getParameters)

print("delete operation")
ypObj.delete(deleteUrl, deleteParameters)

print("patch operation")
ypObj.patch(patchUrl, patchParameters)
