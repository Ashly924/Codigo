
def Ejecutar():
    contTotalEst = 0
    contAlto = 0
    contBajo = 0
    acumPromedios = 0

    while True:
        print("========= MENÚ OPCIONES =========")
        print("1. Procesar")
        print("2. Reportar")
        print("3. Salir")

        while True:
            op = int(input("Ingrese opción de menú:\t"))
            if op < 1 or op > 3:
                print("ERROR. Vuelva a ingresar")
            else:
                break

        match op:
            case 1:
                datos = Procesar(contTotalEst, contAlto, contBajo, acumPromedios)
                contTotalEst = datos[0]
                contAlto = datos[1]
                contBajo = datos[2]
                acumPromedios = datos[3]
            case 2:
                Reportar(contTotalEst, contAlto, contBajo, acumPromedios) 