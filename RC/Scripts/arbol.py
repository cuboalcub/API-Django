import os
import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from .figura import Figura
from .calculator import nodos_en_orden  
from datetime import datetime
from .fire import subir_imagen_usuario_a_firebase

class Arbol:

    def __init__(self,data,user) :
        self.data = data
        self.user = user
        
        data = json.load(data)


        G = nx.DiGraph()

        # Crear nodos especiales "Inicio" y "Final"
        inicio = "Inicio"
        final = "Final"
        G.add_node(inicio)
        G.add_node(final)

        # Figura personalizada (de tu importación)
        figura = Figura()

        # Crear nodos y bordes
        sin_precedentes = []

        # Asumimos que `nodos_en_orden` devuelve una estructura ordenada de nodos
        nodos = nodos_en_orden(self.data)

        # Crear nodos con figura personalizada
        for nodo, obj in nodos.items():
            figura.create_figure(
                nodo,
                obj.tiempo,
                obj.h,
                obj.IL,
                obj.TL,
                obj.IP,
                obj.TP
            )

        # Agregar nodos y relaciones del JSON
        for k, v in data["actividades"].items():
            G.add_node(k)
            if not v["precedentes"]:
                sin_precedentes.append(k)
            for p in v["precedentes"]:
                G.add_edge(p, k)

        # Conectar "Inicio" con nodos sin precedentes
        for actividad in sin_precedentes:
            G.add_edge(inicio, actividad)

        # Identificar nodos finales (sin sucesores)
        con_sucesores = []
        for key, value in data["actividades"].items():
            for p in value["precedentes"]:
                con_sucesores.append(p)
        con_sucesores = list(set(con_sucesores))

        for key in data["actividades"].keys():
            if key not in con_sucesores:
                G.add_edge(key, final)

        
        # Diccionario de imágenes para nodos
        imagenes = os.listdir("figuras")

        imagenes= {k:f"{self.user}/{v}" for k,v in imagenes}

        # Parámetro de escala para las imágenes (ajusta este valor para cambiar el tamaño)
        scale_factor = 0.05  # Menor valor hará la imagen más pequeña

        # Dibujar el grafo
        plt.figure(figsize=(12, 8))
        pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot", args="-Grankdir=LR")

        # Dibujar bordes
        nx.draw_networkx_edges(G, pos, arrows=True)

        # Añadir imágenes en nodos
        ax = plt.gca()
        for nodo, (x, y) in pos.items():
            if nodo in imagenes:  # Si el nodo tiene imagen asociada
                img = mpimg.imread(imagenes[nodo])  # Cargar la imagen
                # Ajustar la escala con zoom
                img_box = OffsetImage(img, zoom=scale_factor)  # Cambiar el zoom para redimensionar
                img_artist = AnnotationBbox(img_box, (x, y), frameon=False)
                ax.add_artist(img_artist)
            else:  # Nodos sin imágenes
                ax.text(x, y, nodo, fontsize=10, ha="center", va="center", bbox=dict(facecolor="lightblue", edgecolor="black", boxstyle="circle"))

        # Ajustar límites del gráfico
        ax.set_xlim(min(x for x, y in pos.values()) - 50, max(x for x, y in pos.values()) + 50)
        ax.set_ylim(min(y for x, y in pos.values()) - 50, max(y for x, y in pos.values()) + 50)
        plt.axis("off")

        # Guardar el grafo con imágenes como PNG
        plt.close()
        fecha_hora_actual = datetime.now()

        # Formatea la fecha y hora
        fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y_%H:%M:%S")

        plt.savefig(f"figuras/{self.user}/{fecha_hora_formateada}.png", format="png", dpi=300, bbox_inches="tight", transparent=True)
        url = subir_imagen_usuario_a_firebase(self.user, f"figuras/{self.user}/{fecha_hora_formateada}.png")
        os.remove(f"figuras/{self.user}")
        
        return url
