#!/usr/bin/env python3

import login
import math

def number(login,addr):
	rep=login.getContent(addr)

	return int(rep.split(':')[1].split('\'')[0])

login=login.Login()
nbr_a=number(login,'https://www.newbiecontest.org/epreuves/prog/prog3_1.php')
nbr_b=number(login,'https://www.newbiecontest.org/epreuves/prog/prog3_2.php')
nbr=str(int(math.sqrt(nbr_a)*nbr_b))
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr3.php?solution='+nbr))
