# EJEMPLO 2. OPERACIONES MATEMÁTICAS

# IMPORTAR UNA LIBRERÍA O BIBLIOTECA DE FUNCIONES MATEMÁTICAS DE PYTHON
import math

# ENTRADAS DE DATOS
''' Declarar o crear variables '''
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))

# PROCESOS (Operaciones o Cálculos Matemáticos y/o Lógicos)
suma = número_1 + número_2
resta = número_1 - número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1	% número_2

# SALIDA DE DATOS
print("La suma es =", round(suma, 2))
print("La suma es = " + str(suma)) # CONCATENACIÓN (Unión o cuando juntas dos o más textos)
# CASTEO: Convetir un tipo de dato en otro tipo de dato
print(f"La suma es = {suma}") # Interpolación de Textos F (Formatear)

print("La potencia_1 de num1 a la num2 es =", potencia_1)
print("La potencia_2 de num1 a la num2 es =", potencia_2)
