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


ypObj = YappesLibrary(token)

print("post operation")
ypObj.post(postUrl, postParameters)

print("put operation")
ypObj.put(putUrl, putParameters)

print("get operation")
ypObj.get(getUrl, getParameters)
