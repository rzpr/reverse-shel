import os
import time

r = '\033[91m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'

baner = f"""

   {y}╭━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮
   {y}┃╭━╮┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱┃┃  
   {y}┃╰━╯┣━━┳╮╭┳━━┫╰━┳━━┫┃  {y}coded by : {r}Rezzaapr
   {y}┃╭╮╭┫┃━┫╰╯┃━━┫╭╮┃┃━┫┃  {y}github : {r}github.com/rezzaapr
   {y}┃┃┃╰┫┃━╋╮╭╋━━┃┃┃┃┃━┫╰╮
   {y}╰╯╰━┻━━╯╰╯╰━━┻╯╰┻━━┻━╯
    {y}</>{r}Reverse Shell{y}</>
          {r}Termux

 {y}[1] {r}Create Payload
 {y}[2] {r}Start Server
 {y}[3] {r}Exit
"""
os.system('clear')
print(baner)

payloa = f"""

{y}╭━━━╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮╱╱╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃╱╱┃╭━╮┃╱╱╱╱╱╱╭╯╰╮╱╭╯╰╮
┃╰━╯┣━━┳╮╱╭┫┃╭━━┳━━┳━╯┃╱╱┃┃╱╰╋━┳━━┳━┻╮╭╋━┻╮╭╋━━┳━╮
┃╭━━┫╭╮┃┃╱┃┃┃┃╭╮┃╭╮┃╭╮┣━━┫┃╱╭┫╭┫┃━┫╭╮┃┃┃┃━┫┃┃╭╮┃╭╯
┃┃╱╱┃╭╮┃╰━╯┃╰┫╰╯┃╭╮┃╰╯┣━━┫╰━╯┃┃┃┃━┫╭╮┃╰┫┃━┫╰┫╰╯┃┃
╰╯╱╱╰╯╰┻━╮╭┻━┻━━┻╯╰┻━━╯╱╱╰━━━┻╯╰━━┻╯╰┻━┻━━┻━┻━━┻╯
╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╰━━╯
"""
while True:
	def create():
		os.system('clear')
		print(payloa)
		print('==========')
		host = input('SET HOST > ')
		print('==========')
		port = int(input('SET PORT > '))
		print('==========')
		name = input('Payload Name > ')
		print('==========')

		try:
			r = open('src/template.py', 'r')
			f = open("payload/"+name+'.py', "a")
			f.write(r.read()%(host, port))
			f.close()
			print('Payload Berhasill Dibuat Di payload/'+name+'.py')
			input('\n\nTekan Enter Untuk Kembali')
			os.system('clear')
			print(baner)
		except FileNotFoundError:
			os.system('mkdir payload')
			f = open("payload/"+name+'.py', "a")
			r = open('src/template.py', 'r')
			f.write(r.read()%(host, port))
			f.close()
			print('Payload Berhasill Dibuat Di payload/'+name+'.py')
			input('\n\nTekan Enter Untuk Kembali')
			os.system('clear')
			print(baner)
	
	def start():
		os.system('clear')
		print("Listening...")
		time.sleep(1)
		os.system('python3 src/server.py')


	if __name__ == '__main__':
		try:
			inp = input("Choice > ")
		except KeyboardInterrupt:
			break
		if inp == '1':
			create()
		elif inp == '2':
			try:
				start()
			except KeyboardInterrupt:
				print('Stopping Server....')
				time.sleep(1)
				os.system('clear')
				print(baner)
		elif inp == '3':
			break
			print('Bye Bye')
		elif inp != '1' or inp != '2' or inp != '3':
			print('Command Not Found')
