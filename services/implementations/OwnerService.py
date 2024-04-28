import injector
from services.IOwnerService import IOwnerService

class OwnerService(IOwnerService):

    def __init__(self,nueva_contraseña:str,Nombre_del_dueño:str):
        super.__init__()
        self.nombre = Nombre_del_dueño
        self.contraseña = nueva_contraseña # Aqui se inicializa el dueño
        

    def entrar_como_dueño(self,contraseña_ingresada):
        if contraseña_ingresada == self.contraseña:
            return f'Has entrado al parque correctamente, {self.nombre}'
            # TO DO
        else:
            return 'Contraseña incorrecta'
    

    #Funciones iguales a las de las personas:
    def montar_en_atraccion(self,atraccion:str):
        # TO DO
        pass

    def caminar(self,hacia_donde:str):
        # TO DO
        pass

    def revisar_informacion(self,que_informacion: str):
        contraseña_ingresada = input('Para acceder a la información del parque, necesitas poner la contraseña.')
        if contraseña_ingresada == self.contraseña:
            #Aqui se necesita acceder a variables del parque de atracciones, pero todavia no hay ninguna:
            #return parque_de_atracciones.que_informacion
            # TO DO
            pass
        else:
            print('¡Esa no es la contraseña!')
        pass

    def irse_del_parque(self,contraseña:str):
        if contraseña == self.contraseña:
            return f'Hasta luego, {self.nombre}'
            # TO DO
        else:
            return 'Necesitas ingresar la contraseña correcta para irte.'
        
    def cambiar_precio(self,precio):
        # TO DO : hay que cambiar el precio del taquillero por persona
        pass

    






