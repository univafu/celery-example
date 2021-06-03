from celery import Celery

from time import sleep

from tasks import task_update

print("ejecutando tarea en celery")

#ejecutamos de forma remota el metodo
#en result almacenamos el estatus de la tarea
result = task_update.delay()

#continua el control del programa sin detener el flujo
print("retomando el flujo del programa sin esperar a la finalización de la tarea")

#revisamos que la tarea no ha terminado
#imprimimos que no esta lista y esperamos 25 segundos
if not result.ready():
    print("tarea no lista, durmiendo 25 seg")
    sleep(25)

#esto debería imprimir algunas veces el mensaje de tarea no lista
while not result.ready():
    print("tarea no lista, esperando...")
    sleep(1)

#una vez que termine la tarea remota imprime un True
print(f"Tarea lista {result.ready()}")
#Con el metodo get() de result podemos obtener la data retornada por el metodo remoto
print(f"resultado: {result.get()}")
