mi_diccionario = {
    "Deicel Fernandez": 30,
    "Daniel Espitia": 18,
    "Arianyelina Rincon": 21,
    "Brian Mendez": 10,
    "Carlos Villero": 18,
    "Damian Garcia": 13,
    "Elias Rivas": 18,
    "Fabian Cardenas": 17,
    "Franklin Vecino": 17,
    "Helyanni Rodriguez": 16,
    "Liliana Rincon": 14,
    "Maria Macias": 16,
    "Over Machado": 16,
    "Paul Moran": 14,
    "Ronald Trujillo": 12,
    "Yuliexy Dimas": 10
}
print(f"Diccionario original: {mi_diccionario}")

mi_diccionario["Deicel Fernandez"] = 17
mi_diccionario["Daniel Espitia"] = 25
mi_diccionario["Arianyelina Rincon"] = 17
mi_diccionario["Brian Mendez"] = 18
mi_diccionario["Carlos Villero"] = 21
mi_diccionario["Damian Garcia"] = 20
mi_diccionario["Elias Rivas"] = 20
mi_diccionario["Franklin Vecino"] = 20
mi_diccionario["Helyanni Rodriguez"] = 21
mi_diccionario["Liliana Rincon"] = 20
mi_diccionario["Maria Macias"] = 20
mi_diccionario["Over Machado"] = 19
mi_diccionario["Paul Moran"] = 20
mi_diccionario["Ronald Trujillo"] = 21
mi_diccionario["Yuliexy Dimas"] = 20
print(f"Diccionario original modificado: {mi_diccionario}")

for clave in mi_diccionario:
    print(f"Nombre: {clave}, Nota: {mi_diccionario[clave]}")

for valor2 in mi_diccionario.values():
    print("Nota:", valor2)
########################################################################
mi_conjunto = {1,2,3,4,5}
print("Conjunto original:",mi_conjunto)