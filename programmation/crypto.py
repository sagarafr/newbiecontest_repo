#!/usr/bin/env python3

import login

def caesar_decode(text,key):
	decode=''
	for i in text.lower():
		decode+=chr(ord('a')+(ord(i)-key-ord('a'))%26)

	return decode

login=login.Login()
content=login.getContent('https://www.newbiecontest.org/epreuves/prog/prog5.php')
text=content.split('\'')[1].split('\'')[0]
key=int(content.split('\'')[3])
decode=caesar_decode(text,key)
print(login.sendAnswer('https://www.newbiecontest.org/epreuves/prog/verifpr5.php?solution='+decode))
