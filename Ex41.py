#Leia a idade de um atleta e defina sua categoria de acordo com a idade do mesmo
#até 9 anos = mirim// até 14 anos = infantil// até 19 anos = junior // até 20 anos = senior// acima = master
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print(f'A categoria do atleta de idade: {idade} anos, é MIRIM.')
elif idade <= 14:
    print(f'A categoria do atleta de idade: {idade} anos, é INFANTIL')
elif idade <= 19:
    print(f'A categoria do atleta de idade: {idade} anos, é JUNIOR')
elif idade == 20:
    print(f'A categoria do atleta de idade: {idade} anos, é SENIOR')
else:
    print(f'A categoria do atleta de idade: {idade} anos, é MASTER')