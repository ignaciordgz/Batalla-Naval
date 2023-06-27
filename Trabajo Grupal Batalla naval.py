import random  #Importamos esta librería que utilizaremos más adelante para localizar los barcos aleatoriamente.
import string  #Importamos librería string para que transforme los enteros dados en "tamaño" a letras del abecedario en mayusculas y lo guarda en la variable "letras" como lista.
import math    # Importamos librería math para poder utilizar la funcion ceil, la cual redondea el numero hacia el siguiente entero, esto lo utilizaremos para los Turnos.

# Funcion crear Tablero

def crear_tablero(tamaño):  # Creamos funcion para armar el tablero con el parámetro (tamaño)
    tablero = []  # Creamos lista vacía
    
    letras = list(string.ascii_uppercase[:tamaño])   # Mencionado anteriormente en import string
    
    if tamaño >= 3 and tamaño <= 10 :       # Condicional que actua si se ingresa un numero correcto de dimensiones
        print("\n- - - - Batalla Naval - - - - ")
        
        print(" "," ".join(letras))     # Se utiliza la funcion .join() para concatenar las letras dejando un espacio, el primer espacio vacío es para que el tablero quede lo más simétrico posible 
        
        for i in range(0,tamaño):    # Estructura for para agregar a la lista del tablero "-" cuantas veces sea ingresado en tamaño
            tablero.append(["-"]*tamaño)

        for i, fila in enumerate(tablero, start=1):    # Estructura for con clase enumerate(), esto es para que el indice empiece desde 1, para imprimir las filas del tablero, tambien concatenadas con la función .join()
            print(i, " ".join(fila))     
    
    else:   # Otro condicional, si no se ingresa un numero correcto de dimensiones, surgirá un Error
        raise ValueError("INGRESE UN NUMERO CORRECTO ENTRE 3 y 10")
    
    return tablero

# Funcion Ubicar barcos aleatoriamente

def ubicar_enemigos(tamaño, barcos): # Creamos función con el tamaño del tablero y el numero de barcos ingresados como parametros
    barcos_aleatorios = []           # Creamos lista vacía para agregar las tuplas de las coordenadas
    
    while len(barcos_aleatorios) < barcos:   # Estructura while, hasta que no se agregen las coordenadas a la lista y el largo sea igual a la cantidad de barcos ingresados no termina
        fila_aleatoria = random.randint(0, tamaño-1)          # Se guarda un valor random fila aleatoria en cada iteracion
        columna_aleatoria = random.randint(0, tamaño-1)       # Se guarda un valor random columna aleatoria en cada iteracion
        filas_columnas = fila_aleatoria,columna_aleatoria     # Se crea una tupla con los valores
    
        if filas_columnas not in barcos_aleatorios:           # Condicional para que no se repitan las tuplas y generar errores
            barcos_aleatorios.append(filas_columnas)           # Se agrega a la lista con los valores de los barcos aleatorios ya creados
    
    return barcos_aleatorios

# Funcion de Disparos

def disparo(tablero, tamaño, columna, fila, barcos_aleatorios):  # Creamos función para los disparos con tablero,tamaño,fila,columna y las tuplas de las posiciones de los barcos como parametros
    letras = string.ascii_uppercase         # Mencionado en import string
    
    columna_indice = letras.index(columna.upper())      # Transformamos la letra de la columna a mayuscula y luego al numero del indice del abecedario al que pertenece
    
    if fila > tamaño:      # Condicional
        return "Fila seleccionada incorrecta, no está dentro del rango del tablero"
    elif columna_indice >= tamaño:
        return "Columna seleccionada incorrecta, no está dentro del rango del tablero"
    
    fila_indice = fila - 1

    if (fila_indice, columna_indice) in barcos_aleatorios:    # Condicional, si la tupla del indice de fila y columna estan en la tupla de los barcos aleatorios generados hace lo siguiente
        print(True)                                         # Imprime True si está
        tablero[fila_indice][columna_indice] = "X"       # Cambia el guion de la coordenada a una X
        barcos_aleatorios.remove((fila_indice, columna_indice))         # Elimina la tupla de las coordenadas ingresadas de la lista
    elif tablero[fila_indice][columna_indice] == "-":            # Otro condicional, si la coordenada es un guion
        print(False)                                        # Imprime False
        tablero[fila_indice][columna_indice] = "o"         # Cambia el guion de la coordenada a una o
    else:                           
        print("¡Ya disparaste en este lugar!")            # Imprime ya disparaste en este lugar
    
    print(" "," ".join(letras[:tamaño]))           # Imprime las letras del abecedario en base al tamaño ingresado
    
    for i, fila in enumerate(tablero, start=1):    # Estructura for con funcion enumerate(), esto es para que el indice del tablero(columnas) empiecen desde 1, para imprimir las filas del tablero, tambien concatenadas con la función .join()
        print(i, " ".join(fila)) 


tamaño = int(input("Ingrese las dimensiones del tablero [3-10]: "))
tablero = crear_tablero(tamaño)

## CONFIGURACIONES DEL JUEGO

# Cantidad de Barcos

bandera_booleana = False           # Creamos bandera booleana
barcos = int(input("Ingrese la cantidad de barcos enemigos : "))         # Preguntamos al usuario con un input(), el valor se guarda en "barcos"
while bandera_booleana == False:     # Estructura de control while utilizando la bandera booleana creada anteriormente
    if barcos > tamaño :      # Condicional
        barcos = int(input("Ingrese una cantidad de barcos correcta : "))     # Hasta que no se ingrese una cantidad de barcos menor o igual a la raíz cuadrada del total de casillas del tablero seguira preguntando
    if barcos <= tamaño:
        print(f"Has ingresado {barcos} barcos en el tablero ")        # Utilizamos f-string
        bandera_booleana = True          # Una vez ingresado una cantidad correcta, finaliza el while cambiando el valor de la bandera booleana

barcos_aleatorios = ubicar_enemigos(tamaño,barcos)

# Dificultad

dificultad=input("Ingrese la dificultad : (Facil, Intermedio, Dificil) : ")    # Input donde se lee la dificultad a ingresar y se guarda en la variable "dificultad"
Turnos=0           # Turnos o disparos del juego
if dificultad.lower() == "facil":  # Condicional, con la funcion lower() para que lo ingresado sea siempre en minuscula
    Turnos=tamaño*tamaño*0.7          # La variable turnos toma el valor de 70% de las dimensiones del tablero
    print(f"Tienes {math.ceil(Turnos)} disparos")       # F-string, donde utilizamos math.ceil para redondearlo al siguiente entero
elif dificultad.lower() == "intermedio":    # Otro condicional
    Turnos=tamaño*tamaño*0.5         # En este caso la variable turnos toma el 50% de las dimensiones del tablero
    print(f"Tienes {math.ceil(Turnos)} disparos")       # F-string, donde utilizamos math.ceil para redondearlo al siguiente entero 
elif dificultad.lower()== "dificil":         # Otro condicional
    Turnos=tamaño*tamaño*0.3              # En este caso la variable turnos toma el 30% de las dimensiones del tablero
    print(f"Tienes {math.ceil(Turnos)} disparos")        # F-string, donde utilizamos math.ceil para redondearlo al siguiente entero
else:
    raise ValueError("Dificultad ingresada incorrecta, INGRESE FACIL, INTERMEDIO O DIFICIL")

turnos_resultados = math.ceil(Turnos)    # Guardamos el numero de turnos para luego imprimirlos en los resultados
    
# Turnos

secuencia_disparos = []  # Creamos lista vacía para guardar las secuencias de disparos efectuados, luego las imprimiremos en resultados
while Turnos > 0:            # Utilizamos estructura while, mientras que tengas turnos puedes Ingresar las coordenadas a disparar
    columna_letra = str(input("Ingrese la columna (letra) la cual quieres disparar (0 para salir): "))
    secuencia_disparos.append(columna_letra.upper())  # Guardamos la columna en la lista
    
    if columna_letra == "0":     # Si ingresaste 0, termina el programa
        break
    
    fila = int(input("Ingrese la fila (numero) para disparar: "))       # Ingresa la fila a disparar
    secuencia_disparos.append(fila)        # Se ingresa el numero de la fila en la lista
     
    Turnos=Turnos-1    # Se te resta un turno
    disparo(tablero, tamaño, columna_letra, fila, barcos_aleatorios)    # Llamamos a la funcion de disparo

    if len(barcos_aleatorios) == 0:      # Condicional, si ya destruiste todos los barcos
        print("¡Felicitaciones, has ganado!")        # Imprimimos que ganaste 
        break
    elif Turnos < 0 and len(barcos_aleatorios) != 0:    # Otro condicional, si te quedaste sin disparos y no destruiste todos los barcos
        print("¡Te has quedado sin disparos!")          # Imprimimos que te quedaste sin disparos
        break

## RESULTADOS DE LA PARTIDA

print("--------------------")
print("Resultados")
print("--------------------")
print(f"Disparos Efectuados : {turnos_resultados}")
print(f"Enemigos Acertados : {barcos-len(barcos_aleatorios)}")
print(f"Secuencia de disparos efectuados : {tuple(secuencia_disparos)}")