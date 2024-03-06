# Solicitar dados ao usuário
tempo_fumando = float(input("Informe o tempo em anos que você fuma: "))
valor_maco = float(input("Informe o valor atual do maço de cigarros: "))
qtd_maco_por_dia = float(input("Informe a quantidade média de maços que você fuma por dia: "))

# Calcular montante gasto
montante = tempo_fumando * 365 * qtd_maco_por_dia * valor_maco

# Verificar o montante e exibir a mensagem correspondente
if montante < 20000:
    print("Com o valor R$ {}, você poderia ter dado entrada em um carro.".format(montante))
elif 20000 <= montante <= 50000:
    print("Com o valor R$ {}, você poderia ter comprado um carro popular usado.".format(montante))
else:
    print("Com o valor R$ {}, você poderia ter comprado um carro zero.".format(montante))