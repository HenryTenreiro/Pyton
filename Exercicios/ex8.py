
#ENTRADA DE DADOS
nome = input('Nome do vendedor:')
carros_vendidos = float(input("Quantidade de carros vendidos:"))
total_de_vendas = float(input('Valor total de vendas:'))

#informação
#salario de 2.500.00
#comissão de 200
# 2% no valor total da venda


#processamento
por_vendas = carros_vendidos * 200
vendas_total = total_de_vendas * 2 / 100
salario = vendas_total + por_vendas + 2500

#saida de dados
print(f'o Vendedor {nome} Recebera um salario de {salario}$')



