#!/usr/bin/env python3

import login
import subprocess

def parsing(sudoku_text):
	extremLimit=9
	sudoku_split=sudoku_text.split("<td class=")
	sudoku=[]
	data_sudoku=[[0 for x in range(0,extremLimit)] for y in range(0,extremLimit)]

	for x in range(1,len(sudoku_split)):
		sudoku.append(sudoku_split[x].split(">")[1].split("</")[0])

	beginColumn=0
	beginLine=0
	limitColumn=3
	limitLine=3

	for e in sudoku:
		if int(e) == 0:
			data_sudoku[beginLine][beginColumn]=0
		else:
			data_sudoku[beginLine][beginColumn]=int(e)

		beginColumn+=1

		if beginColumn >= limitColumn:
			beginLine+=1
			beginColumn=limitColumn-3


		if beginLine >= limitLine:
			if limitColumn >= extremLimit:
				beginColumn=0
				limitColumn=3
				beginLine=limitLine
				limitLine+=3
			else:
				beginLine=limitLine-3
				beginColumn=limitColumn
				limitColumn+=3

	return data_sudoku


login=login.Login()
sudoku=parsing(login.getContent('https://www.newbiecontest.org/epreuves/prog/progsudoku.php'))
answer=""
answer_in_url=""

# Copy all prologu file and add sudoku data
f_prolog=open('solver_sudoku.pro','r')
f_execute=open('solv_sudo.pro','w')
f_execute.write(f_prolog.read())
f_execute.write("sudokuExample(Vars) :-\n")
f_execute.write("	sudoku(\n")
f_execute.write("	[\n")

for line in range(0,len(sudoku)):
	for column in range(0,len(sudoku[line])):
		if column == 0:
			f_execute.write("	")
		f_execute.write(str(sudoku[line][column]))
		if line != int(len(sudoku))-1 or column != int(len(sudoku[line]))-1:
			f_execute.write(",")
	f_execute.write("\n")
f_execute.write('],Vars).\n')

f_prolog.close()
f_execute.close()

# Execute prolog file
subprocess.call(["chmod 744 solv_sudo.pro"],shell=True)
t=subprocess.getoutput("./solv_sudo.pro")

# Parsing the answer
for cpt in range(t.find("==================="),len(t)):
	if t[cpt] != "=" and t[cpt] != "," and t[cpt] != "|":
		if t[cpt] != "\n":
			answer+=t[cpt]

# Supress the file
subprocess.call(["rm solv_sudo.pro"],shell=True)

# Answer organisation
for cpt in range(0,len(answer),9):
	if cpt <= len(answer)-10:
		answer_in_url+=answer[cpt:cpt+9]+"-"
	else:
		answer_in_url+=answer[cpt:cpt+9]

# Send and print the answer
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifprsudoku.php?solution='+str(answer_in_url)))
