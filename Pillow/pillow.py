import requests
import os
import jwt
 
url="http://172.23.21.101:8000//"
file_local="data.csv"
user="001"
# pas="no"
file_server="user"+user+".csv"
# payload={
# 	user:pas
# }
# encoded=jwt.encode(payload,"string",algorithm="HS256")

stat=os.stat(file_local).st_mtime


while 1:
	if (stat!=os.stat(file_local).st_mtime):
		r = requests.put(url+file_server, data=open(file_local, 'rb'))#,auth=encoded)
		stat=os.stat(file_local).st_mtime
		print("sent")