#Faça um algoritmo que leia o preço de um produto a mostra e seu novo preço com 5% de desconto.
preco = float(input("informe o preço do produto R$:"))
desconto = preco - (preco*5/100)
print("o produto que custva R${}, na promoção com de desconto 5% vai custar {}".format(preco,desconto))