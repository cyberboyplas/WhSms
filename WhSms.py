#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Algunas independencias no estan instaladas xd')
    print("Error to import 'requests' Library\ntodo : python3 -m pip install requests")
    exit()

# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']



def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """                                                  
\033[96m



.............................................................


####                            ####      ###      ###
 ####                          ####       ###      ###
  ####                        ####        ###      ###
   ####                      ####         ###      ###
    ####                    ####          ###      ###
     ####                  ####           ###      ###
      ####                ####            ############
       ####    ######    ####             ############
        ####  ###  ###  ####              ###      ###
         #######    #######               ###      ###
          #####      #####'               ###      ###



.............................................................


\033[91m By WhBeatZ        Github: https://github.com/WhBeatZ \033[96mv2.1
\033[96m                                         """
    print(logo)
    print("\n")

def Track() :
  TXTID = input("\033[96mPon la informacion del numero\n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPulsa enter para salir :(..")
  print("\nGracias por usar WhSms..")
  print("\tEspero que te sirva otra vez hacker!!\n Escribe python WhSms.py\n\tPara correrlo otra vez..")
  print("Espero que hayas conseguido lo que quieras :)...")
  exit()

clr()
banner()


while True:
	print("\033[0mHerramienta para enviar un sms de forma anonima y personalizada. La herramienta solo se puede usar una vez por dia, si la quieres usar mas veces, cambia tu ip (No lo intentes hacer mas de 2 veces con el mismo numero :)")
 
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	print("Haz tus propios mensajes :).")
	print()
	Track()
elif type == 0:
	while True:
		
		cc = input("\033[96m\tPon el codigo de pais (Sin el +, elejmplo: 34, 52) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nCodigo de pais invalido\n\t\tNormalmente, los codigos de pais suelen tener de 1 a 3 caracteres xd...\n')
		        continue
		pn = input("\033[96mPon el numero de telefono xd : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nNumero de telefono invalido xd..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nLos numeros de telefonos, contienen numeros solo xd\n')
		            continue
		receiver = '+' + numbe
		text = input("\033[96mEscribe el mensaje a enviar :) : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
		print(resp.json())
		print("Gracias por usar WhSms, mi inta: WhBeatZ :)...")
		break
		if '"completado :)" : true ' in resp.text:
		    print("\033[92m El mensaje se envio corectamente :) \033[0m")
		    input('\n\t\tPulsa Enter para continuar...')
		    banner()
		    exit()
		if '"completado" : false ' in resp.text:
		    print("\033[91m Ocurrio un problema")
		    print("\033[91m Error al enviar el Sms :c! ")
		    input('\n\t\tPulsa enter para enviar :)...')
		    banner()
		    exit()
		exit() 
