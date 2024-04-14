from services.iqueueservice import IQueueService

class QueueService(IQueueService):  

    def __init__(self):
        super().__init__()  # Llama al constructor de la clase IQueueService

    def vacio(self):
        return len(self.visitants) <= 0
    
    def enqueue(self, visitor_id: int) -> None:
        """Agrega un visitante a la cola."""
        self.visitants.append(visitor_id)
        print("El visitante ha sido agregado a la fila")
        self.n_can += 1

    def dequeue(self) -> int:
        """Retira el primer visitante de la cola."""
        if self.vacio() == True:
             print("La fila está vacía")
        else:
            self.visitants.pop(0)
            print("El primer visitante ha sido retirado de la fila")
            self.n_can -= 1

    def size(self) -> int:
        """Devuelve el número total de visitantes en la cola."""
        if self.n_can > 0:
             print("En total han participado en la atracción " + str(self.n_can) + " participantes")
        else:
             print("No hay participantes en la fila")

