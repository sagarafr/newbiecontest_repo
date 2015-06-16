#!/usr/bin/env python3

import login
import math

def number(equation,begin,end):
	limit_start=equation.find(begin)+1

	if end == "":
		limit_end=len(equation)
	else:
		limit_end=equation.find(end)

	return int(equation[limit_start:limit_end])

login=login.Login()
equation=login.getContent('https://www.newbiecontest.org/epreuves/prog/prog4.php').split(' ')[0]
print(equation)
sqrt_nbr=number(equation,"(",")")
multi_nbr=number(equation,"*","&")
add_nbr=number(equation,"+","")
nbr=str(int(math.sqrt(sqrt_nbr)*multi_nbr**2+add_nbr))
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution='+nbr))
