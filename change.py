def change():   
    gasto = 23.75
    pagado = 100
 
    print ("Gasto ingresado: ")
    print (f"{gasto}")
    print ("Dinero recibido: ")
    print (f"{pagado}")

    vuelto = pagado - gasto

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100 )

    print("vuelto\n")
    print("Pesos:")
    print(pesos)
    print("centavos:")
    print(centavos)

change()


# Mariano faraldo
