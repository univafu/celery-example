from celery import Celery
from celery.utils.threads import default_socket_timeout
from decouple import config

from time import sleep

CELERY_URL = config('CELERY_URL', default="redis://127.0.0.1:6379/0")
CELERY_BACKEND = config('CELERY_BACKEND', default='redis://127.0.0.1')

app = Celery('tasks', backend=CELERY_BACKEND, broker=CELERY_URL)

@app.task
def task_update():
  sleep(30)
  print("Tarea ejecutada despues de 30 segundos")
  
  #agregamos un return para almacenar la respuesta
  # y obtenerla en nuestro programa principal
  return "Tarea ejecutada despues de 30 segundos"
