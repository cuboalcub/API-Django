class Nodo:
    def __init__(self, tiempo, nombre):
        self.nombre = nombre  # Nombre del nodo
        self.tiempo = tiempo  # Duración o tiempo asociado al nodo
        self.IL = 0  # Inicio más tardío
        self.TL = 0 # Término más tardío
        self.IP = 0  # Inicio más temprano
        self.TP = 0  # Término más temprano
        self.h = 0   # Holgura (Slack)

    # Método para actualizar el inicio más temprano
    def actualizar_IP(self, tiempo):
        self.IP = max(self.IP, tiempo)
        self.calcular_TP()

    # Calcular el término más temprano
    def calcular_TP(self):
        self.TP = self.IP + self.tiempo

    # Actualizar el término más tardío
    def actualizar_TL(self, tiempo):
        if self.nombre == "Final":
            self.TL = max(self.TL, tiempo)
            self.calcular_IL()
            self.calcular_H()
        else:
            self.TL = max(self.TL, tiempo)
            self.calcular_IL()
            self.calcular_H()

    # Calcular el inicio más tardío
    def calcular_IL(self):
        self.IL = self.TL - self.tiempo

    # Calcular la holgura
    def calcular_H(self):
        self.h = self.TL - self.TP
