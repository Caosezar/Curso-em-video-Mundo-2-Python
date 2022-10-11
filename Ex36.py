casa = float(input("Qual o valor da casa: R$ "))
sal = float(input("Qual o salário do comprador? R$ "))
anos = float(input('Em quantos anos será quitado? '))
prestacao_mensal = casa/ (anos*12)
if prestacao_mensal > ((30/100)*sal):
    print('Infelizemnte a mensalidade do financiamento é superior à 30% do seu salário, logo não será possível realizar o financiamento')
else:
    print(f'Parabéns o financiamto poderá ser realizado, o valor da mensalidade é {prestacao_mensal:.2f}')