def Ejecutar():
    ContadorDeEstudiantes = 0
    ContadorPromediosAltos = 0
    ContadorPromediosBajos = 0
    PromediosFinales = 0

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
                datos = Procesar(ContadorDeEstudiantes, ContadorPromediosAltos, ContadorPromediosBajos, PromediosFinales)
                ContadorDeEstudiantes = datos[0]
                ContadorPromediosAltos = datos[1]
                ContadorPromediosBajos = datos[2]
                PromediosFinales = datos[3]
            case 2:
                Reportar(ContadorDeEstudiantes, ContadorPromediosAltos, ContadorPromediosBajos, PromediosFinales)
            case 3:
                while True:
                    rpta = input("¿Desea salir del programa? (S/N): ").upper()
                    if rpta == "S":
                        salir = True
                        break
                    elif rpta == "N":
                        salir = False
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

def Procesar(ContadorDeEstudiantes, ContadorPromediosAltos, ContadorPromediosBajos, PromediosFinales):
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

        ContadorDeEstudiantes = ContadorDeEstudiantes + 1
        PromediosFinales = PromediosFinales + promedioFinal

        if promedioFinal >= 17:
            ContadorPromediosAltos = ContadorPromediosAltos + 1
        if promedioFinal < 12:
            ContadorPromediosBajos = ContadorPromediosBajos + 1

        print("\n======= REPORTE DEL ESTUDIANTE =======")
        print("Nombre:", nombre)
        print("Promedio:", round(promedio, 2))
        print("Bonificación:", bono)
        print("Promedio Final:", round(promedioFinal, 2))

        while True:
            rpta = input("\n¿Desea ingresar otro estudiante? (S/N): ").upper()
            if rpta == "S":
                salir = False
                break
            elif rpta == "N":
                salir = True
                break
            else:
                print("ERROR. Ingrese solo 'S' o 'N'.")

        if salir == True:
            break

    return [ContadorDeEstudiantes, ContadorPromediosAltos, ContadorPromediosBajos, PromediosFinales]

def Reportar(ContadorDeEstudiantes, ContadorPromediosAltos, ContadorPromediosBajos, PromediosFinales):
    print("\n======= REPORTE GENERAL =======")
    print("Total Estudiantes:", ContadorDeEstudiantes)
    print("Estudiantes con rendimiento alto:", ContadorPromediosAltos)
    print("Estudiantes con rendimiento bajo:", ContadorPromediosBajos)
    print("Suma total de promedios:", round(PromediosFinales, 2))

    if ContadorDeEstudiantes > 0:
        print("Promedio general del grupo:", round(PromediosFinales / ContadorDeEstudiantes, 2))
    else:
        print("No hay datos para calcular promedio.")

Ejecutar()
