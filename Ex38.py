#escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma das seguintes frases
#O primeiro valor é maior/ O segundo valor é maior/Não existe valor maior, ambos são iguais
print('-'*40)
print('COMPARADOR DE NÚMEROS [MENOR/MAIOR]')
print('-'*40)
n1 = int(input('Digite um o primeiro valor para comparação: '))
n2 = int(input('Digite o segundo valor para comparação: '))
if n1 > n2:
    print(f'O maior valor é {n1}')
elif n2 > n1:
    print(f'O maior valor é {n2}')
else:
    print('Não há valor maior ou menor, ambos os valores são iguais. ')