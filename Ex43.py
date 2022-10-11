#desenvolva uma lógica que leia o peso e a altura de uma pessoa , calcule seu IMC de acordo com a tabela
#abaixo de 18.5 ABAIXO DO PESO// entre 18.5 e 25 PESO IDEAL// entre 25 e 30 SOBREPESO// entre 30 e 40 OBESIDADE// acima de 40 OBESIDADE MÓRBIDA
#peso / altura**2
peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua Altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu imc é de {imc}, e você está ABAIXO DO PESO')
elif imc <= 25:
    print(f'Seu imc é de {imc}, e você está IDEAL')
elif imc <= 30:
    print(f'Seu imc é de {imc}, e você está SOBREPESO')
elif imc <= 40:
    print(f'Seu imc é de {imc}, e você está em OBESIDADE')
elif imc > 40:
    print(f'Seu imc é de {imc}, e você está em OBESIDADE MÓRBIDA')
