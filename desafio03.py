#escreva um programa que leia um valor com metros e o exiba 
#convertido em centimetros e milimetro
metros= int(input("digite um valor em metros:"))
cm = metros*100
mm = metros*1000
print("{} metros em centimetros é: {} cm".format(metros, cm))
print("{} metros em milímetros é: {} mm".format(metros, mm))