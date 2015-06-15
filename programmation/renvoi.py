#!/usr/bin/env python3

import login

login=login.Login()
rep=login.getContent('https://www.newbiecontest.org/epreuves/prog/prog1.php')
nbr=rep.split(':')[1].split('\'')[0]
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution='+nbr))
