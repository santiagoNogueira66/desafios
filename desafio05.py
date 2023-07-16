#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar Considare US$:1,OO = R$3,27
dinheiro = float(input("informe o saldo atual:"))
print("com o valor de {}, você pode comprar {:.2f}, dolares".format(dinheiro,dinheiro/3.27))