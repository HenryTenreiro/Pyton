
#dados de entrada
produto = input('Diga qual o seu produto aqui: ')
valor = float(input('qual o valor de seu produto: '))

#Processamento
desconto = 10 * valor / 100
total = valor - desconto


#saida de dados
print(f'o seu produto {produto} está com 10% então')
print(f'seu produto sai por {total}')



