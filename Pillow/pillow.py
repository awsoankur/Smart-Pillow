import requests
import os
 
url="http://172.23.72.72:8000//"
file_local="data.csv"
user="001"
file_server="user"+user+".csv"

stat=os.stat(file_local).st_mtime


while 1:
	if (stat!=os.stat(file_local).st_mtime):
		r = requests.put(url+file_server, data=open(file_local, 'rb'))#, headers=headers, auth=('username', 'pass'))
		stat=os.stat(file_local).st_mtime
		print("sent")