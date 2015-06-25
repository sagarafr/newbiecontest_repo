#!/usr/bin/env python3

import login
import subprocess

login=login.Login()
image=login.getOriginalContent('https://www.newbiecontest.org/epreuves/prog/prog10.php')
f=open('image.png','wb')
f.write(image)
f.close()
t=subprocess.getoutput(["gocr -i image.png"])
rep=t.split('\n')[0]
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr10.php?chaine='+str(rep)))
