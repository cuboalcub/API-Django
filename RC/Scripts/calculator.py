import json
from .nodo import Nodo

def nodos_en_orden(data):

    data = json.load(data)

    # Obtener las actividades
    valores = data["actividades"]

    # Crear los nodos usando un diccionario por comprensión
    nodos = {k: Nodo(v["pert"], k) for k, v in valores.items()}
    nodos["Inicio"] = Nodo(0, "Inicio")
    nodos["Final"] = Nodo(0, "Final")

    # Paso 1: Calcular tiempos tempranos (IP y TP)
    for key, value in valores.items():
        if not value["precedentes"]:  
            nodos[key].actualizar_IP(0)
        else:
            for p in value["precedentes"]:  
                nodos[key].actualizar_IP(nodos[p].TP)

    # Identificar los nodos con sucesores
    con_sucesores = []
    for key, value in valores.items():
        precedentes = value["precedentes"] 
        if precedentes:
            for p in precedentes:
                con_sucesores.append(p)
    con_sucesores = list(set(con_sucesores))  # Eliminar duplicados

    # Conectar los nodos sin sucesores al nodo "Final"
    for key in valores.keys():
        if key not in con_sucesores:
            nodos["Final"].actualizar_IP(nodos[key].TP)
            nodos["Final"].actualizar_TL(nodos["Final"].TP)
            nodos[key].actualizar_TL(nodos["Final"].IL)

    # Crear un diccionario de sucesores
    sucesores = {key: [] for key in nodos.keys()}


    # Llenar el diccionario de sucesores basado en los precedentes
    for key, value in valores.items():
        for precedente in value["precedentes"]:
            sucesores[precedente].append(key)

    # Paso 2: Calcular tiempos tardíos (TL e IL) recorriendo desde el nodo "Final" hacia atrás
    for key in list(valores.keys())[::-1]:  # Recorrido inverso
        if key in sucesores and sucesores[key]:  
                min_IL = min(nodos[sucesor].IL for sucesor in sucesores[key])
                nodos[key].actualizar_TL(min_IL)
        else:
            nodos[key].actualizar_TL(nodos["Final"].IL)

