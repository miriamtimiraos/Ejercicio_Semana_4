import datetime

# SUPERCLASE EMPLEADO
class Empleado:
    """Superclase Empleado"""
    def __init__(self, nif, nombre, fecha_nacimiento, sueldo_mensual):
        self.nif = nif
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.sueldo_mensual = sueldo_mensual

    # Métodos
    def comprobar_cumpleaños(self, mes):
        return bool(
            self.fecha_nacimiento.month == mes
        )  # Es como un if que comprueba si es igual y devuelve un True o un False

    def mostrar_datos(self):
        print("\nNombre: ", self.nombre)
        print("NIF: ", self.nif)
        print("Fecha de nacimiento: ", self.fecha_nacimiento)


# CLASE EMPLEADO TEMPORAL-->HEREDA DE LA SUPERCLASE EMPLEADO
class EmpleadoTemporal(Empleado):
    """Clase de Empleado Temporal"""

    tipo_empleado = "temporal"

    def __init__(self, nif, nombre, fecha_nacimiento, sueldo_mensual, fecha_alta, fecha_baja):
        super().__init__(nif, nombre, fecha_nacimiento, sueldo_mensual)
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja

    # Métodos
    def mostrar_datos(self):
        # Invocar al método de la superclase que muestra los datos generales del empleado
        super().mostrar_datos()
        # Mostrar el resto de datos que faltan
        print(f"Tipo: empleado {self.tipo_empleado}")
        print("Fecha de alta: ", self.fecha_alta)
        print("Fecha de baja: ", self.fecha_baja)
        print("Sueldo mensual: ", self.sueldo_mensual)


# CLASE EMPLEADO FIJO-->HEREDA DE LA SUPERCLASE EMPLEADO
class EmpleadoFijo(Empleado):
    """Clase de Empleado Fijo"""

    tipo_empleado = "fijo"

    def __init__(self, nif, nombre, fecha_nacimiento, sueldo_mensual, año_alta, complemento_anual):
        super().__init__(nif, nombre, fecha_nacimiento, sueldo_mensual)
        self.año_alta = año_alta
        self.complemento_anual = complemento_anual

    # Métodos
    def calculo_sueldo(self):
        return self.sueldo_mensual + ((datetime.datetime.now().year - self.año_alta) * self.complemento_anual) / 12

    def mostrar_datos(self):
        # Invocar al método de la superclase que muestra los datos generales del empleado
        super().mostrar_datos()
        # Mostrar el resto de datos que faltan
        print(f"Tipo: empleado {self.tipo_empleado}")
        print("Año de alta: ", self.año_alta)
        print("Sueldo base: ", self.sueldo_mensual)
        print("Complemento anual: ", self.complemento_anual)
        print(f"Sueldo mensual: {self.calculo_sueldo():.2f} €")
