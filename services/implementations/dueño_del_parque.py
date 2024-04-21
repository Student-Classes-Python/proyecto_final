import injector
from abc import ABC, abstractmethod

# Definición de la interfaz
class IEntityService(ABC):

    ## Ejemplos de la clase IEntityService(yo no la hago)
    @abstractmethod
    def hacer_algo(self):
        pass

# Implementación de la interfaz del dueño
class IOwnerService(IEntityService):

    super.__init__()
    #Entrar y verificar que es el dueño
    @abstractmethod
    def entrar_como_dueño(self,contraseña_ingresada):
        pass
    
    
    @abstractmethod
    def montar_en_atraccion(self,atraccion:str):
        pass

    #Acceder a informacion del parque como las personas que han entrado o el dinero recaudado
    @abstractmethod
    def revisar_informacion(self,que_informacion: str):
        pass

    #Irse del parque (como cerrar sesion)
    @abstractmethod
    def irse_del_parque(self,contraseña:str):
        pass

    @abstractmethod
    def caminar(self,hacia_donde:str):
        pass

class OwnerService(IOwnerService):

    def __init__(self,nueva_contraseña:str,Nombre_del_dueño:str):
        super.__init__()
        self.nombre = Nombre_del_dueño
        self.contraseña = nueva_contraseña # Aqui se inicializa el dueño
        

    def entrar_como_dueño(self,contraseña_ingresada):
        if contraseña_ingresada == self.contraseña:
            return f'Has entrado al parque correctamente, {self.nombre}'
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
        #Aqui se necesita acceder a variables del parque de atracciones, pero todavia no hay ninguna:
        #return parque_de_atracciones.que_informacion
        pass

    def irse_del_parque(self,contraseña:str):
        if contraseña == self.contraseña:
            return f'Hasta luego, {self.nombre}'
        else:
            return 'Necesitas ingresar la contraseña correcta para irte.'






