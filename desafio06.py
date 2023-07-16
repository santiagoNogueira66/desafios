#Faça um programaqua leia a largura e a altura da uma parede em metros, calcule a sua área e a quantidade de tinta necessária parapinta-lá, sabendo que cada litro da tinta,pinta uma área de 2m2.
altura = int(input("informe a altura da parede:"))
largura = int(input("informe a largura da parede:"))
area = largura*altura
tinta = area/2
print("sua parede tem dimensões de {}x{} e sua área é de {}m²".format(altura,largura,area))
print("a quantidade total de tinta para pintar essa parede é de: {} litros de tinta" .format(tinta))