    #Faça um algoritmo qua leia o salário de um Funcionário e mostre seu novo salário, com 15% de aumento
sal = float(input("informe o salario atual:"))
aumento = sal + (sal*15/100)
print("o salario antes do aumento era de {}, após o aumento foi para: {:.2f}".format(sal,aumento))