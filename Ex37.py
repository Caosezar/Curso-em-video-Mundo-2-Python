#escreva um programa que leia um número inteiro qualquer, e peça para o usuário escolher qual será a base da conversão: 1=binário 2=octal 3=hexadecimal
from cgitb import reset

val = int(input('Digite o valor que deseja converter: '))
res = int(input('''Qual operação deseja realizar? 
1)BINÁRIO  
2)OCTAL  
3)HEXADECIMAL '''))
if res == 1:
    print(bin(val)[2:])
elif res == 2:
    print(oct(val)[2:])
elif res == 3:
    print(hex(val)[2:])
else:
    print('Invalid!!')

