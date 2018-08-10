from ypconnector import YappesLibrary

url = "https://testing1.apizone001.pr.yappes.com/add"
data = {
"headers": {
 "Content-Type":"application/json"
},
"queryparams":{"a":"10","b":"20"}
,
"payload": {}
}

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

token = "9c4272e8e7e09b6f701cf735cc2b66b5527f7795b637532b8ba5008328e4bea6"
getUrl = "http://localhost:8080/getdata"
postUrl = "http://localhost:8080/postdata"
putUrl = "http://localhost:8080/putdata"
deleteUrl = "http://localhost:8080/deletedata"
patchUrl = "http://localhost:8080/patchdata"


ypObj = YappesLibrary(token)
print(ypObj.get(url,data))

# print("get operation")
# ypObj.get(getUrl, getParameters)

# print("post operation")
# ypObj.post(postUrl, postParameters)

# print("put operation")
# ypObj.put(putUrl, putParameters)

# print("delete operation")
# ypObj.delete(deleteUrl, deleteParameters)

# print("patch operation")
# ypObj.patch(patchUrl, patchParameters)
