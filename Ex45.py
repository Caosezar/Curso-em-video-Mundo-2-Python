#crie um programa que jogue joquempô com vc
from random import randrange 
print('_-_'*20)
print(str('PEDRA PAPEL TESOURA'))
print('_-_'*20)
print('1)Pedra')
print('2)Papel')
print('3)Tesoura')
player = int(input('Escolha sua jogada: '))
pc = randrange(1, 3)
print(f'Você escolheu {player} e eu escolhi {pc}')
if player == 1 and pc == 2:
    print('PAPEL GANHA DE PEDRA! te peguei, RSRSRR ')
elif player == 2 and pc == 3:
    print('AHA!! TESOURA GANHA DE PAPEL! venci, HAHAHAH')
elif player == 3 and pc == 1:
    print ('PEDRA GANHA DE TESOURA, você perdeu KKKKKKJKJK')
elif player == 2 and pc == 1:
    print('VOCÊ VENCEU UAU CÊ É O BIXÃO MEMO!')
elif player == 3 and pc ==2:
    print('VOCÊ VENCEU UAU CÊ É O BIXÃO MEMO!')
elif player == 2 and pc == 3:
    print('VOCÊ VENCEU UAU CÊ É O BIXÃO MEMO!')