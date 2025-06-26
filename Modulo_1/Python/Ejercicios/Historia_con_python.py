#Comienzo de la historia
respuesta1 = input ("Tu amigo Guillermo y tú se encuentran de vacaciones en un yate en medio del mar, apreciando las vistas te das cuenta que hay varias islas alrededor, decides junto a Guillermo, ir a una de las islas para investigar, mientras iban de camino, notaron un olor extraño, ¡tu yate estaba echando humo!, aceleras el paso. Al llegar a la isla, revisas tu yate pero, ya no enciende. Guillermo y tú deciden sacar todo lo útil del yate, entre ellas tienen: comida(para dos dias), una bengala, ropa y un bolso. El lugar en el que se encuentran no seria visible para la bengala, asi que miran alrededor y ven una montaña, deben decidir entre subir la montaña o esperar ayuda (MONTAÑA/AYUDA): ").upper()
#Camino N°1
if respuesta1 == "MONTAÑA":
    respuesta2 = input ("Guillermo y tu fueron a la montaña, deben escalar, pero primero deber decidir que camino tomar, la derecha se ve facil pero podria tener sorpresas y la izquierda se ve un poco complicada pero podrian manejarlo (DERECHA/IZQUIERDA): ").upper()
    #Sendero N°1
    if respuesta2 == "DERECHA":
        respuesta3 = input("Deciden ir hacia la derecha, y todo iba bien de momento, hasta que se encuentran con un oso dormido, decide si rodear el oso junto con Guillermo o separarse para hacerlo (JUNTOS/SEPARADOS): ").upper()
        if respuesta3 == "SEPARADOS":
                    respuesta4 = input("Elegiste rodear separados y afortunadamente lograron cruzar sin problemas, siguen caminando y trepando, pero notas que a Guillermo se le dificulta escalar un poco, decides ayudarlo o dejar que se esfuerce (AYUDARLO/DEJARLO): ").upper()
                    #Final N°1
                    if respuesta4 == "AYUDARLO":
                        print("Elegiste ayudarlo y juntos llegaron a la cima, encendieron la bengala y al poco tiempo llego el rescate, ¡Lograron escapar!")
                        print("Juego terminado...")
                    #Final N°2
                    elif respuesta4 == "DEJARLO":
                        print("Eligiste no ayudarlo, y por un descuido Guillermo resbaló y cayó por el precipicio, sientes culpa y remordimiento pero, decides seguir adelante... lograste escapar, ¿pero a que costo?...")
                        print("Juego terminado...")

    #Sendero N°2
    elif respuesta2 == "JUNTOS":
            print("Decidiron rodear juntos, y por los nervios chocas a Guillermo por error, hacen mucho ruido y despiertan al oso, no logran ocultarse y el oso los encuentra a ambos, empiezan a correr y el oso los persigue pero... no logran escapar... Han muerto a manos del oso. : ")
            print("Juego terminado...")

#Camino N°2
elif respuesta1 == "AYUDA":
    respuesta2 = input ("Eligieron esperar ayuda, pasaba tiempo e intentaban economizar la comida, pero pronto se acabaría, al notar el problema de la comida ").upper()
    #Sendero N°1    
    if respuesta2 == "CAMBUR":
        respuesta3 = input("Elegiste cambur de nuevo, ahora debes elegir entre CAMBUR y unas UVAS: ").upper()
        if respuesta3 == "CAMBUR":
                    respuesta4 = input("Elegiste cambur, ahora elige entre CAMBUR o un CUCHILLO: ").upper()
                    #Final N°5
                    if respuesta4 == "CAMBUR":
                        print("Elegiste cambur, ganaste el juego")
                        print("Juego terminado...")
                    #Final N°6
                    elif respuesta4 == "CUCHILLO":
                        print("Eligiste cuchillo, has perdido")
                        print("Juego terminado...")

    #Sendero N°2
    elif respuesta2 == "MANZANA":
        respuesta3 = input("Elegiste manzana, ahora elige entre MANZANA o PERA: ").upper()
        #Final 7
        if respuesta3  == "MANZANA":
            print("Elegiste la manzana, ¡Has ganado!")
            print("Juego terminado...")
        #Final 8
        elif respuesta3 == "PERA":
            print("Elegiste la pera, ¡Has perdido!")
            print("Juego terminado...")
    
elif respuesta1 != "MONTAÑA" or "AYUDA":
    print("Respuesta incorrecta, ¡Intenta de nuevo!")
