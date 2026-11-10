from abc import ABC, abstractmethod


class Atraccion(ABC):
    def __init__(self, nombre, capacidad):          # (1) ya no pide altura_minima
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = 0

    @abstractmethod
    def calcular_tiempo_ciclo(self):
        pass

    @abstractmethod
    def verificar_restriccion(self, altura):         # (2) ahora es abstracto
        pass

    def subir_visitantes(self, cantidad):
        if self.visitantes + cantidad <= self.capacidad:
            self.visitantes += cantidad
            return True
        return False

    def vaciar(self):
        self.visitantes = 0

    def cupos_disponibles(self):
        return self.capacidad - self.visitantes


class MontanaRusa(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):  
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 3

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima


class RuedaFortuna(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):   
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 10

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima


class Carrusel(Atraccion):
    def __init__(self, nombre, capacidad):    
        super().__init__(nombre, capacidad)

    def calcular_tiempo_ciclo(self):
        return 5

    def verificar_restriccion(self, altura):  
        return True


class Parque:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atracciones = []

    def agregar_atraccion(self, atraccion):
        self.atracciones.append(atraccion)

    def buscar_atraccion(self, nombre):
        for a in self.atracciones:
            if a.nombre.lower() == nombre.lower():
                return a
        return None

    def atracciones_disponibles(self):
        return [a for a in self.atracciones if a.cupos_disponibles() > 0]

    def tiempo_total_recorrido(self, nombres):
        total = 0
        no_encontrados = []
        for nombre in nombres:
            a = self.buscar_atraccion(nombre)
            if a:
                total += a.calcular_tiempo_ciclo()
            else:
                no_encontrados.append(nombre)
        return total, no_encontrados


def opcion_1(parque):
    print()
    for a in parque.atracciones:
        print(f"{a.nombre} ({type(a).__name__}): {a.visitantes}/{a.capacidad} visitantes, "
              f"ciclo de {a.calcular_tiempo_ciclo()} min")


def opcion_2(parque):
    print()
    disponibles = parque.atracciones_disponibles()
    if not disponibles:
        print("Ninguna atracción tiene cupo disponible.")
        return
    for a in disponibles:
        print(f"{a.nombre}: {a.cupos_disponibles()} cupo(s) disponible(s)")


def opcion_3(parque):
    a = parque.buscar_atraccion(input("Nombre de la atracción: ").strip())
    if not a:
        print("Esa atracción no existe.")
        return
    try:
        cantidad = int(input("Cantidad de visitantes: "))
    except ValueError:
        print("Debe ser un número entero.")
        return
    if a.subir_visitantes(cantidad):
        print(f"{cantidad} visitante(s) subieron a {a.nombre}.")
    else:
        print(f"No hay cupo suficiente. Cupos disponibles: {a.cupos_disponibles()}")


def opcion_4(parque):
    a = parque.buscar_atraccion(input("Nombre de la atracción: ").strip())
    if not a:
        print("Esa atracción no existe.")
        return
    a.vaciar()
    print(f"{a.nombre} fue vaciada.")


def opcion_5(parque):
    a = parque.buscar_atraccion(input("Nombre de la atracción: ").strip())
    if not a:
        print("Esa atracción no existe.")
        return
    try:
        altura = float(input("Estatura del visitante (cm): "))
    except ValueError:
        print("Debe ser un número.")
        return
    print("SÍ puede subir." if a.verificar_restriccion(altura) else "NO puede subir.")


def opcion_6(parque):
    entrada = input("Atracciones a visitar (separadas por coma): ").strip()
    if not entrada:
        print("No se ingresó ninguna atracción.")
        return
    nombres = [n.strip() for n in entrada.split(",")]
    total, no_encontrados = parque.tiempo_total_recorrido(nombres)
    print(f"Tiempo total del recorrido: {total} minutos")
    if no_encontrados:
        print(f"No se encontraron: {', '.join(no_encontrados)}")


def crear_parque_inicial():
    parque = Parque("Parque Aventura Puriscal")
    parque.agregar_atraccion(MontanaRusa("Trueno Salvaje", 8, 140))
    parque.agregar_atraccion(RuedaFortuna("Vista Central", 12, 100))
    parque.agregar_atraccion(Carrusel("Caballitos", 16))
    return parque


parque = crear_parque_inicial()
opciones = {
    "1": opcion_1, "2": opcion_2, "3": opcion_3,
    "4": opcion_4, "5": opcion_5, "6": opcion_6,
}

while True:
    print("\n=== PARQUE AVENTURA PURISCAL ===")
    print("1. Ver todas las atracciones")
    print("2. Ver atracciones con cupo disponible")
    print("3. Subir visitantes a una atracción")
    print("4. Vaciar una atracción")
    print("5. Verificar restricción de altura")
    print("6. Calcular tiempo total de un recorrido")
    print("7. Salir")

    opcion = input("\nElija una opción: ").strip()

    if opcion == "7":
        print("\n¡Gracias por visitar el Parque Aventura Puriscal!")
        break
    elif opcion in opciones:
        opciones[opcion](parque)
    else:
        print("Opción inválida.")