def change():
    print("Ingresar gasto:")
    gasto = float(input())

    print("dinero recibido:")
    pagado = float(input())

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