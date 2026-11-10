
nombres = {
    "E": "Entrada",
    "C": "Exposición de ciencias",
    "J": "Zona de juegos",
    "R": "Robótica",
    "T": "Talleres",
    "S": "Salida",
}

nodos = ["E", "C", "J", "R", "T", "S"]


conexiones = [
    ("E", "C"), ("E", "J"),
    ("C", "R"), ("C", "T"),
    ("J", "S"), ("R", "S"),
    ("T", "S"),
]


mapa = {nodo: [] for nodo in nodos}
for a, b in conexiones:
    mapa[a].append(b)
    mapa[b].append(a)


def construir_matriz(mapa, nodos):
    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]   
    for nodo, vecinos in mapa.items():
        i = nodos.index(nodo)
        for vecino in vecinos:
            j = nodos.index(vecino)
            matriz[i][j] = 1
    return matriz


def dfs_recursivo(mapa, inicio):
    visitados = set()
    orden = []

    def visitar(nodo):
        visitados.add(nodo)        
        orden.append(nodo)
        for vecino in mapa[nodo]:
            if vecino not in visitados:
                visitar(vecino)

    visitar(inicio)
    return orden


def dfs_iterativo(mapa, inicio):
    visitados = set()
    orden = []
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        if nodo in visitados:      
            continue
        visitados.add(nodo)
        orden.append(nodo)

        for vecino in reversed(mapa[nodo]):
            if vecino not in visitados:
                pila.append(vecino)
    return orden


def pedir_nodo(mensaje):
    
    nodo = input(mensaje).strip().upper()
    if nodo not in mapa:
        print("Ese espacio no existe en el mapa.")
        return None
    return nodo


matriz = construir_matriz(mapa, nodos)

while True:
    print("\n=== MAPA DE LA FERIA CIENTÍFICA ===")
    print("1. Ver conexiones de un espacio")
    print("2. Ver matriz de adyacencia")
    print("3. Recorrer con DFS recursivo")
    print("4. Recorrer con DFS iterativo")
    print("5. Consultar si hay un pasillo directo")
    print("6. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        nodo = pedir_nodo("Espacio: ")
        if nodo is not None:
            vecinos = ", ".join(mapa[nodo])
            print(f"{nodo} · {nombres[nodo]} se conecta con: {vecinos}")

    elif opcion == "2":
        print("  " + " ".join(nodos))
        for i, nodo in enumerate(nodos):
            print(nodo + " " + " ".join(str(x) for x in matriz[i]))

    elif opcion == "3":
        inicio = pedir_nodo("Nodo inicial: ")
        if inicio is not None:
            print("DFS recursivo: " + " -> ".join(dfs_recursivo(mapa, inicio)))

    elif opcion == "4":
        inicio = pedir_nodo("Nodo inicial: ")
        if inicio is not None:
            print("DFS iterativo: " + " -> ".join(dfs_iterativo(mapa, inicio)))

    elif opcion == "5":
        origen = pedir_nodo("Origen: ")
        if origen is None:
            continue
        destino = pedir_nodo("Destino: ")
        if destino is None:
            continue
        i = nodos.index(origen)
        j = nodos.index(destino)
        if matriz[i][j] == 1:
            print(f"Sí existe un pasillo directo entre {origen} y {destino}.")
        else:
            print(f"No existe un pasillo directo entre {origen} y {destino}.")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")