
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

def PromedioRecursivo(n):
    if n == 0:
        return 0
    nota = float(input(f"Ingrese nota del curso {n}:\t"))
    return nota + PromedioRecursivo(n - 1)

def Procesar(contTotalEst, contAlto, contBajo, acumPromedios):
    while True:
        nombre = input("Ingrese nombre del estudiante:\t")
        numCursos = int(input("Ingrese número de cursos:\t"))

        sumaNotas = PromedioRecursivo(numCursos)
        promedio = sumaNotas / numCursos

        bono = 0
        if promedio >= 18:
            bono = 1
        elif promedio >= 16:
            bono = 0.5

        promedioFinal = promedio + bono

        contTotalEst = contTotalEst + 1
        acumPromedios = acumPromedios + promedioFinal

        if promedioFinal >= 17:
            contAlto = contAlto + 1
        if promedioFinal < 12:
            contBajo = contBajo + 1

        print("\n======= REPORTE DEL ESTUDIANTE =======")
        print("Nombre:", nombre)
        print("Promedio:", round(promedio, 2))
        print("Bonificación:", bono)
        print("Promedio Final:", round(promedioFinal, 2))

        rpta = input("\n¿Desea ingresar otro estudiante? (S/N): ")
        rpta = rpta.upper()
        if rpta != "S":
            salir = True
        else:
            salir = False

        if salir == True:
            break

    return [contTotalEst, contAlto, contBajo, acumPromedios]

def Reportar(contTotalEst, contAlto, contBajo, acumPromedios):
    print("\n======= REPORTE GENERAL =======")
    print("Total Estudiantes:", contTotalEst)
    print("Estudiantes con rendimiento alto:", contAlto)
    print("Estudiantes con rendimiento bajo:", contBajo)
    print("Suma total de promedios:", round(acumPromedios, 2))

    if contTotalEst > 0:
        print("Promedio general del grupo:", round(acumPromedios / contTotalEst, 2))
    else:
        print("No hay datos para calcular promedio.")

Ejecutar() 
