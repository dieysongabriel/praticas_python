

listaPrecos  = [490, 795, 1250, 3800, 510, 8370]

imposto = []

for preco in listaPrecos:
    if preco > 1000:
        imposto.append(preco * 0.5);

print(imposto);

#Usando list comprehension

listaPrecos2  = [490, 795, 1700, 5500, 510, 8400]

imposto2 = [x * 0.5 for x in listaPrecos2 if x > 1000]

print(imposto2);