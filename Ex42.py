#Só irá existir um triângulo se: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 + s2 > abs(s3) and s2 + s3 > abs(s1) and s3 + s1 > abs(s2):
    print('Estas medidas podem formar um triângulo. ')    
    if s1 == s2 and s2 == s3:
        print('Este é um triângulo EQUILÁTERO pois possui todos os seus lados iguais.')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('Este é um triângulo ISÓCELES pois possui dois lados iguais.')
    elif s1 != s2 and s2 != s3 and s3 != s1:
        print('Este triângulo é ESCALENO pois possui todos os lados diferentes entre si.')
else:
    print('Estas medidas não formam um triângulo. ')

