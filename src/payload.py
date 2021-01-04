import os

host = input('SET HOST > ')
port = int(input('SET PORT > '))
name = input('Payload Name > ')

try:
	r = open('template.py', 'r')
	f = open("../payload/"+name+'.py', "a")
	f.write(r.read()%(host, port))
	f.close()
except FileNotFoundError:
	os.system('mkdir ../payload')
	f = open("../payload/"+name+'.py', "a")
	f.write(code)
	f.close()