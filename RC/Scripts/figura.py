import matplotlib.pyplot as plt
import os

class  Figura:

    def create_figure( self, A, t, H, IL, TL, IP, TP, user ):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Dibujar el círculo
        circle = plt.Circle((0.5, 0.5), 0.4, edgecolor="black", facecolor="white")
        ax.add_artist(circle)

        # Dibujar las líneas internas mejoradas
        ax.plot([0.65, 0.65], [0.131, 0.87], color="blue", lw=3)  # Línea vertical
        ax.plot([0.35, 0.35], [0.131, 0.87], color="blue", lw=3)  # Línea vertical
        ax.plot([0.103, 0.348], [0.5, 0.5], color="blue", lw=3)  # Línea horizontal
        ax.plot([0.66, 0.9], [0.5, 0.5], color="blue", lw=3)  # Línea horizontal

        # Dibujar el rectángulo central
        if H != 0 or A == "Final" or A == "Inicio":
            rect = plt.Rectangle((0.35, 0.35), 0.3, 0.3, edgecolor="black", facecolor="black")
        else:
           rect = plt.Rectangle((0.35, 0.35), 0.3, 0.3, edgecolor="black", facecolor="Red")
        ax.add_artist(rect)


        # Añadir texto central
        ax.text(0.5, 0.5, A, color="white", fontsize=18, ha="center", va="center")

        # Añadir etiquetas en las áreas
        ax.text(0.5, 0.8, t, color="black", fontsize=20, ha="center")  # Parte superior
        ax.text(0.5, 0.15, H, color="black", fontsize=20, ha="center")  # Parte inferior
        ax.text(0.25, 0.33, IL, color="black", fontsize=18, ha="center", va="center")  # Izquierda
        ax.text(0.78, 0.33, TL, color="black", fontsize=18, ha="center", va="center")  # Derecha

        # Añadir etiquetas en las esquinas
        ax.text(0.25, 0.61, IP, color="black", fontsize=18, ha="center", va="center")  # Superior izquierda
        ax.text(0.78, 0.61, TP, color="black", fontsize=18, ha="center", va="center")  # Superior derecha

        # Ajustar límites y quitar ejes
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        os.makedirs(f"figuras/{user}", exist_ok=True)
        
        plt.savefig(f"figuras/{user}/{A}", format="png", dpi=300, bbox_inches="tight", transparent=True)