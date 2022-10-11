#Escreva um programa que leia duas notas de um aluno e calcule sua média
#Mostrando uma mensagem final de acordo com sua média atingida
#Média abaixo de 5.0 = REPROVADO// Média entre 5.0 e 6.9 = RECUPERAÇÃO // Média 7.0 ou maior = aprovado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media <= 5.0:
    print(f'Sua média foi de {media}, sendo assim, está REPROVADO!')
elif media > 5.0 and media < 6.9:
    print(f'Sua média foi de {media}, sendo assim, está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Parabéns sua média foi de {media}, sendo assim, está APROVADO!')
    