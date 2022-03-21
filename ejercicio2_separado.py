# Ejercicio 2
# Importar la fecha actual
import datetime
import re

from clases_ej3 import EmpleadoFijo, EmpleadoTemporal

# Función de comprobación de fecha
def comprobacion_fecha(fecha):
    dia, mes, año = fecha.split("/")
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    flag_error = False
    try:
        fecha = datetime.datetime(año, mes, dia).date()
    except ValueError:
        flag_error = True
        print("Fecha introducida errónea")

    return flag_error, fecha


# Función de comprobación de DNI
def comprobacion_DNI(nif):
    flag_error = False
    diccionario_dni = {
        0: "T",
        1: "R",
        2: "W",
        3: "A",
        4: "G",
        5: "M",
        6: "Y",
        7: "F",
        8: "P",
        9: "D",
        10: "X",
        11: "B",
        12: "N",
        13: "J",
        14: "Z",
        15: "S",
        16: "Q",
        17: "V",
        18: "H",
        19: "L",
        20: "C",
        21: "K",
        22: "E",
    }
    p = re.compile("^[0-9]{8}[a-zA-Z]$")  # Dar el formato al DNI
    if p.match(nif):
        # Comprobar si la letra corresponde con el número del DNI
        numeros_nif = int(nif[:8])
        letra_nif = numeros_nif % 23  # Con % obtenemos el resto de la división
        if nif[8] != diccionario_dni[letra_nif]:
            print("Error de formato en el nif.")
            flag_error = True
    else:
        print("Error de formato en el nif.")
        flag_error = True

    return flag_error


# Función para añadir un empleado
def añadir_empleado(diccionario):
    print("\nIntroduce los datos del empleado.\n")
    # Tipo de empleado
    tipo = input("Tipo de empleado (fijo/temporal): ")
    while not ((tipo=="fijo" or tipo=="temporal")): #Es lo mismo que decir si no es temporal o fijo
        tipo = input(
            "Error al introducir el tipo de empleado. Por favor, indique de nuevo el tipo de empleado (fijo/temporal): "
        )
    # Nombre y DNI
    nombre = input("Introduce el nombre del empleado (nombre y apellidos): ")
    nif = input("Introduce el nif: ")
    flag = comprobacion_DNI(nif)
    while flag:
        nif = input("Introduce el nif: ")
        flag = comprobacion_DNI(nif)
    # Fecha de nacimiento con comprobación
    fecha_nacimiento = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
    flag, fecha_nacimiento = comprobacion_fecha(fecha_nacimiento)
    while flag:
        fecha_nacimiento = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
        flag, fecha_nacimiento = comprobacion_fecha(fecha_nacimiento)
    # Para solicitar el resto de datos se diferencia entre empleados fijos o temporales
    if tipo == "temporal":
        # EMPLEADO TEMPORAL
        sueldo_mensual = int(input("Introduce el sueldo mensual: "))
        while sueldo_mensual <= 0:
            sueldo_mensual = int(input("Error al introducir el dato.\nIntroduce el sueldo mensual: "))
        fecha_alta = input("Introduce la fecha de alta (dd/mm/aaaa): ")
        flag, fecha_alta = comprobacion_fecha(fecha_alta)
        while flag:
            fecha_alta = input("Introduce la fecha de alta (dd/mm/aaaa): ")
            flag, fecha_alta = comprobacion_fecha(fecha_alta)
        fecha_baja = input("Introduce la fecha de baja (dd/mm/aaaa): ")
        flag, fecha_baja = comprobacion_fecha(fecha_baja)
        while flag:
            fecha_baja = input("Introduce la fecha de baja (dd/mm/aaaa): ")
            flag, fecha_baja = comprobacion_fecha(fecha_baja)
        diccionario[nif] = EmpleadoTemporal(nif, nombre, fecha_nacimiento, sueldo_mensual, fecha_alta, fecha_baja)
    else:
        # EMPLEADO FIJO
        sueldo_mensual = int(input("Introduce el sueldo base mensual: "))
        while sueldo_mensual <= 0:
            sueldo_mensual = int(input("Error al introducir el dato.\nIntroduce el sueldo base mensual: "))
        año_alta = int(input("Introduce el año de alta en la empresa: "))
        while año_alta <= 0:
            año_alta = int(input("Error al introducir el dato.\nIntroduce el año de alta en la empresa: "))
        complemento_anual = int(input("Introduce el complemento anual: "))
        while complemento_anual < 0:
            complemento_anual = int(input("Error al introducir el dato.\nIntroduce el complemento anual: "))
        diccionario[nif] = EmpleadoFijo(nif, nombre, fecha_nacimiento, sueldo_mensual, año_alta, complemento_anual)

    return diccionario


# Función para eliminar un empleado
def eliminar_empleado(diccionario):
    nif = input("Introduce el nif del empleado que quieras borrar: ")
    if nif in diccionario:
        del diccionario[nif]
        print(f"El empleado con nif {nif} se ha eliminado correctamente.")
    else:
        print(f"El empleado con nif {nif} no figura en la base de datos del sistema.")
    return diccionario


# Función para mostrar los empleados
def lista_empleados(diccionario):
    for x in diccionario.values():
        print(f"{x.nif} {x.nombre} - {x.tipo_empleado}")


# def detalle_de_un_empleado ():
def detalle_de_un_empleado(diccionario):
    nif = input("Introduce el NIF del empleado: ")
    if nif in diccionario:
        diccionario[nif].mostrar_datos()
    else:
        print(f"El empleado con nif {nif} no figura en la base de datos")


# Función de gestión de la opción de indicar los empleados que es su cumpleaños
def empleados_cumpleaños(diccionario):
    mes = int(input("Introduce un mes (1-12): "))
    while (mes < 1) or (mes > 12):
        mes = int(input("Error, dato fuera de rango.\nIntroduce un mes (1-12): "))

    print("Están de cumpleaños:\n")

    for x in diccionario.values():
        if x.comprobar_cumpleaños(mes):
            print(f"{x.nombre}, {x.fecha_nacimiento}")


# Función de control e impresión del menú de slección
def menu():
    # Mostrar las opciones
    print(
        """Menú de opciones:
(1) Añadir empleado
(2) Borrar empleado
(3) Mostrar lista de empleados
(4) Mostrar detalle de un empleado
(5) Mostrar empleados cumpleaños
(6) Terminar"""
    )
    # Solicitar opcion seleccionada
    opcion = int(input("\nElige una opción: "))
    # Comprobar la opción
    while (opcion < 1) or (opcion > 6):
        opcion = int(input("Error, la opción indicada no está disponible.\nElige de nuevo una opción: "))
    return opcion


# Main
def main():
    # Diccionario vacío inicial de los empleados
    empleados = {}
    # Pedir una opción
    opcion = menu()
    while opcion != 6:  # Mientras no se seleccione terminar se sigue ejecutando el proceso
        if opcion == 1:
            empleados = añadir_empleado(empleados)
        elif opcion == 2:
            empleados = eliminar_empleado(empleados)
        elif opcion == 3:
            lista_empleados(empleados)
        elif opcion == 4:
            detalle_de_un_empleado(empleados)
        elif opcion == 5:
            empleados_cumpleaños(empleados)
        opcion = menu()  # Solicitar de nuevo una opción


if __name__ == "__main__":
    main()
