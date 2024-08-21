cant = int(input("Digite la cantidad de estudiantes: "))

i = 0

list = []

while i < cant:
    list.append(int(input("Digite su edad: ")))
    i += 1

prom = sum(list)/cant

print(f"El promedo es de {prom}")