#!/usr/bin/env python3

import requests
import getpass

class Login:
	def __init__(self,user='',password=''):
		self.session=requests.session()
		self.login=dict()
		self.url='https://www.newbiecontest.org/forums/index.php?action=login2'
		self.connection(user,password)

	def connection(self,user='',password=''):
		if user == '':
			user=input("User : ")

		if password == '':
			password=getpass.getpass("Password : ")

		self.login=dict(user=user,passwrd=password)
		self.session.post(self.url,data=self.login)

	def getSession(self):
		return self.session

	def getContent(self,addr):
		return str(self.session.get(addr).content)

	def getOriginalContent(self,addr):
		return self.session.get(addr).content

	def sendAnswer(self,addr):
		return str(self.session.post(addr).content)
