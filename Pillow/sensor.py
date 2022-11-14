import time,random

numr=30
data=[]
index=0
ref=[i for i in range(34)]+[i for i in range(34,0,-1)]

def reading_from_sensor():
	global index
	time.sleep(0.1)
	index+=1
	return ref[index%(len(ref))]
file="data.csv"
open(file,"w").close()
flag=1
while flag:
	reading=reading_from_sensor()
	if (len(data)>=numr):
		with open(file,"w") as f:
			for i in data:
				f.write(str(i)+"\n")
		data=[]
	data.append(reading)