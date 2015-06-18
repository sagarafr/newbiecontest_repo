#!/usr/bin/env python3

import login

def data_split(data,condition,value):
	r_data={}
	split_data=data.split("<td>")
	
	for i in range(1,len(split_data)-1,2):
		result=split_data[i+1].split("</td")[0]
		if result == condition:
			result=value

		r_data[split_data[i].split("</td")[0]]=result

	return r_data

login=login.Login()
content=login.getContent("https://www.newbiecontest.org/epreuves/prog/prog9/epreuve9.php")
all_data=content.split("\\n\\n")[3]
proc_data=content.split("\\n\\n")[4]

ram_data=all_data.split("\\n<br><br>\\n")[1]
pc_data=all_data.split("\\n<br><br>\\n")[0]

name=[]
proc=[]
ram=[]
proc_price=data_split(proc_data,"N\\'existe plus ;)",0)
ram_price=data_split(ram_data,"Trop ch\\xc3\\xa8re ;)",float("inf"))

data=pc_data.split(". ")
for d in data:
	if d != '':
		tmp=d.split(" a ")
		name.append(tmp[0])
		proc.append(tmp[1].split(" et ")[0].split("un processeur de ")[1])
		ram.append(tmp[1].split(" et ")[1].split("dispose de ")[1])

max_price=0
max_name=""
for cpt in range(0,len(name)-1):
	tmp_max=int(proc_price[proc[cpt]])+int(ram_price[ram[cpt]])
	if max_price < tmp_max:
		max_price=tmp_max
		max_name=name[cpt]

print(login.sendAnswer('http://www.newbiecontest.org/epreuves/prog/prog9/verifpr9.php?prenom='+max_name+'&prix='+str(max_price)))
