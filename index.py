#Programa que leia um ano qualquer e diga se ele é bissexto
from datetime import date
a =int(input('Digite um ano para saber se ele é BISSEXTO. Caso queira analisar o ano atual digite 0:'))
if a ==0:
    a = date.today().year
if a % 4 ==0 and a % 100 != 0 or a % 400 ==0:
    print('Esse É um ano BISSEXTO')
else:
    print('Esse ano NÃO é BISSEXTO')