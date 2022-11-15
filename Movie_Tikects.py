class usuario():

    def __init__ (self, nombre: str, ticket: str, silla: int) -> None:
        self.nombre = nombre
        self.ticket = ticket
        self.silla = silla

class ticket():

    def __init__(self, nombre_usuario: str, tipo: str, silla: int) -> None:
        self.nombre_usuario = nombre_usuario
        self.tipo = tipo
        self.silla = silla

class silla():

    def __init__(self, numero_silla = 20) -> None:
        self.numero_silla = numero_silla

class theater():

    def __init__(self) -> None:
        self.lista_usuario = []
        self.disponible_silla = []
    
    def chequear_silla(self, silla: int):
        for n in self.disponible_silla:
                if silla == self.disponible_silla(n):
                    print("la silla se encuentra ocupada")
    def generar_ticket(nombre):
        pass
    
    def registrar_usuario(self, nombre:str, silla:int):
        self.disponible_silla.append(silla)
        self.lista_usuario.append([nombre, silla])
        
    def chequear_usuarios(self):
        return self.lista_usuario