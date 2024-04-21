"""
import proyecto_final.services.IQueueService as IQueueService
queue_service = IQueueService.QueueService()  # Crear una instancia de la clase MyQueueService
queue_service.enqueue(1)  # Agregar un visitante a la cola
queue_service.enqueue(2)  # Agregar otro visitante a la cola
queue_service.enqueue(4)  # Agregar otro visitante a la cola
queue_service.enqueue(3)  # Agregar otro visitante a la cola
queue_service.size()  # Mostrar el tamaño de la cola
queue_service.dequeue()  # Retirar un visitante de la cola
queue_service.size()  # Mostrar el tamaño de la cola después de retirar un visitante
"""