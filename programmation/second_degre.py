#!/usr/bin/env python3

import login
import math

def equation_solution(a,b,c):
	delta=(b**2)-(4*a*c)
	solutions=None
	if delta < 0:
		delta=-delta
	if delta > 0:
		solutions=[(-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a)]
	elif delta == 0:
		solutions=[(-b)/(2*a)]

	return solutions

def get_number(equation,start,end):
	r_nb=0
	if start != 0 and start >= end:
		r_nb=0
	elif equation[start:end].replace(' ','') == '-':
		r_nb=-1
	elif (equation[start:end].replace(' ','') == ''):
		r_nb=1
	elif (equation[start:end].replace(' ','') == '+'):
		r_nb=1
	else:
		r_nb=int(equation[start:end].replace(' ',''))

	return r_nb

login=login.Login()
equation=login.getContent('https://www.newbiecontest.org/epreuves/prog/prog6.php').split("<br />")[1].split('"')[0]
equation=equation.replace(' ','')
print(equation)

a_end=equation.find("x\\xc2\\xb2")
a=get_number(equation,0,a_end)
print("a =",a)

b_start=a_end+len("x\\xc2\\xb2")
b_end=b_start+equation[a_end+len("x\\xc2\\xb2"):].find('x')
b=get_number(equation,b_start,b_end)
print("b =",b)

c_start=b_end+len("x")
c_end=equation.find("=")
c=get_number(equation,c_start,c_end)
print("c =",c)

solutions=equation_solution(a,b,c)
solution=0

if solutions[0] > solutions[1]:
	solution=str(solutions[0])[:int(str(solutions[0]).find('.')+3)]
else:
	solution=str(solutions[1])[:int(str(solutions[1]).find('.')+3)]

print("solution =",solution)

print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr6.php?solution='+solution))
