
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
            case 3:
                while True:
                    rpta = input("¿Desea salir del programa? (S/N): ")
                    rpta = rpta.upper()
                    if rpta == "S":
                        salir = True
                    else:
                        salir = False

                    if rpta == "S" or rpta == "N":
                        break
                    else:
                        print("ERROR. Vuelva a ingresar")
                if salir == True:
                    break
