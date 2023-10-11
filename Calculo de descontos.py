ganha_hora=float(input('digite quanto voçê ganha por hora de trabalho:'))
horas_trabalho=int(input('digite a quantidade de horas rabalhadas no mês:'))


salario_bruto=ganha_hora * horas_trabalho
inss= (8*salario_bruto)/100
GPS= (9*salario_bruto)/100
descontos = inss + GPS
salario_liquido = salario_bruto - descontos
print()
print("-----------Salario-------")
print("salario_bruto.............:R$%.2f" %(salario_bruto))
print("inss......................:R$%.2f" %(inss))
print("GPS.......................:R$%.2f" %(GPS))
print("salario_liquido...........:R$%.2f" %(salario_liquido))
print()
