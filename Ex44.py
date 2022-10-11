#elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
#a vista e dinheiro ou cheque=10% de desconto// à vista no cartão=5% de desconto// em até 2x no cartão= preço normal// 3x ou mais no cartão=20% de juros
from operator import mod


val = float(input('Digite o valor do produto: '))
res = int (input('Digite o número referente à sua forma de pagamento: 1)Dinheiro ou Cheque -10%!!  2)À vista cartão -5%!!  3)Em até 2x sem juros  4)Em 3x ou mais, juros de apenas 20%!'))

if res == 1:
    val = val - (val*(10/100)) 
    print(f'Desconto de 10% aplicado, novo valor: R$ {val:.2f}.')
elif res == 2:
    val = val - (val*(5/100))
    print(f'Desconto de 5% aplicado, novo valor: R$ {val:.2f}')
elif res == 3:
    print('Seu pagamento será em 2x sem Juros! ')
elif res == 4:
    val = val + (val*(20/100))
    print(f'Em 3x ou mais, serão apenas 20% de juros no cartão! novo valor: R${val:.2f}')

