#!/bin/bash
#Programado por cyberbpyplas
#Todos los derechos reservados ®
#No me hago responsable del mal uso que le puedan dar a esta herramienta

#colores :D

blanco="\e[1;37m"
cyan="\e[1;36m"
lila="\e[1;35m"
verde="\e[1;32m"
amarillo="\e[1;33m"
rojo="\e[1;31m"

#codigo

banner () {
clear
echo -e "$lila ---------------------------------------------"
echo -e "$blanco   __          ___      _____"
echo -e "$cyan   \ \        / / |    / ____|"
echo -e "$verde    \ \  /\  / /| |__ | (___  _ __ ___  ___"
echo -e "$blanco     \ \/  \/ / | '_ \ \___ \| '_   _ \/ __|"
echo -e "$verde      \  /\  /  | | | |____) | | | | | \__ \ "
echo -e "$cyan       \/  \/   |_| |_|_____/|_| |_| |_|___/"
echo
echo -e "$amarillo     Programado por$blanco Cyberboyplas$amarillo  Insta:$blanco "
echo -e "$lila ---------------------------------------------"
}


menuprincipal() {
echo
echo -e "$rojo------------------------------------------------------------------------------"
echo -e "$amarillo-$blanco Escribe el numero al que quieras enviar el sms, $lila($verde Ejemplo: +5213342510790$lila )"
echo -e "$rojo------------------------------------------------------------------------------"
echo

echo -e -n "$amarillo--->$blanco "
read numero
echo
echo -e "$rojo-----------------------------------------------------------------------------------"
echo -e "$amarillo-$blanco Escribe el mensage, $lila($verde Ejemplo: Mi Insta $lila )"
echo -e "$rojo-----------------------------------------------------------------------------------"
echo
echo -e -n "$amarillo--->$blanco "
read mensage
comilla="'"

echo -e "$amarillo"

       curl -X POST https://textbelt.com/text \
       --data-urlencode phone=$comilla$numero$comilla \
       --data-urlencode message=$mensage \
       -d key=textbelt
       
       
       
sleep 1
echo
echo -e "$rojo Gracias por usar Whsms :D"
sleep 3 
}


banner
menuprincipal
