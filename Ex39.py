#Faça um programa que com base no ano de nascimento de um jovem, informe de acordo com a sua idade 
# se ele ainda vai se alistar ao serviço militar?
# se é a hora de se alistar
# se já passou da hora de se alistar
#O programa também deve mostrar quanto tempo falta ou passou do prazo.


atualano = int(2022)
nasc = int(input('Digite aqui o ano de seu nascimento: '))
resp = atualano - nasc
dif = abs(resp - 18)
if resp <18:
    print('Ainda não é necessário o seu alistamento.')
    print(f'O seu alistamento deve ser feito em {dif} ano(s)!')
if resp == 18:
    print('O seu alistamento se faz necessário já.')
else:
    print(f'O seu alistamento deveria ter sido feito há {dif} ano(s)!')
