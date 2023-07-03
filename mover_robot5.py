# -*- coding: utf-8 -*-

# importar socket para comunicarse con el robot
import socket


import time

import math

# Centro del círculo
centro_x = -0.12114
centro_y = -0.21764
centro_z = 0.4

# Radio del círculo en metros
radio = 0.03

# Número de posiciones en el círculo
num_posiciones = 100

# Lista para almacenar las posiciones
posiciones = []

# Calcular el ángulo entre cada posición
angulo = 2 * math.pi / num_posiciones

# Generar las posiciones
for i in range(num_posiciones):
    # Calcular el ángulo actual
    theta = i * angulo

    # Calcular las coordenadas x e y usando coordenadas polares
    x = centro_x + radio * math.cos(theta)
    y = centro_y + radio * math.sin(theta)
    z = centro_z

    # Agregar la posición a la lista
    posiciones.append((x, y, z))

# Imprimir las posiciones
for posicion in posiciones:
    print(posicion)





# crear un objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# especificar la dirección IP y el puerto del robot
host = "127.0.0.1" # reemplazar con la IP real del robot
port = 30003 # puerto para enviar urscript

# conectarse al robot
s.connect((host, port))

# definir una función para enviar urscript al robot
def send_script(script):
    # codificar el script como bytes
    script = script.encode()
    # enviar el script al robot
    s.send(script)
    # recibir la respuesta del robot
    response = s.recv(1024)
    # decodificar la respuesta como texto
    # response = response.decode()
    # # imprimir la respuesta
    # print(response)

# definir una función para convertir grados a radianes
def deg2rad(deg):
    # importar el módulo math para usar pi
    import math
    # multiplicar los grados por pi/180
    rad = deg * math.pi / 180
    # devolver los radianes
    return rad

# definir la posición objetivo en metros y radianes
x = -0.12114
y = -0.21764
z = 0.40
rx = deg2rad(2.572)
ry = deg2rad(0.031)
rz = deg2rad(-0.105)

# definir la velocidad lineal deseada en m/s
v = 1

# definir la aceleración lineal deseada en m/s^2
a = 0.5

# definir el tiempo máximo de movimiento en segundos
t = 10

cont=0
# iterar sobre la lista de posiciones y asignar cada una a la variable p_target
for p_target in posiciones:
    cont=cont+1
    print(cont)
    #time.sleep(0.1)
    # crear un script urscript para mover el robot con speedl usando la posición actual como p_target
    script = f"""
def move():
  # obtener la posición actual del robot como una lista de 6 elementos
  p_actual = get_actual_tcp_pose()
  # crear una lista con la posición objetivo como una lista de 6 elementos (usando los valores de p_target)
  p_target = [{p_target[0]}, {p_target[1]}, {p_target[2]}, {rx}, {ry}, {rz}]
  # calcular el vector de velocidad lineal como la diferencia entre la posición objetivo y la actual dividida por el tiempo máximo de movimiento
  v_speed = [(p_target[0]-p_actual[0])/({t}), (p_target[1]-p_actual[1])/({t}), (p_target[2]-p_actual[2])/({t}), 0, 0, 0]
  # mover el robot con speedl usando el vector de velocidad, la aceleración y el tiempo dados
  speedl(v_speed, {a}, {t})
end

move()
"""
    # dividir el script en líneas individuales y almacenarlas en una lista
    #lines = script.split("\n")


    
    send_script(script)
        # esperar un poco antes de enviar la siguiente línea (ajustar el valor según sea necesario)
    time.sleep(0.1)


# cerrar la conexión con el robot
s.close()