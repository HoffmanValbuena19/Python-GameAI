#comentario de una linea
"comentario de varias lineas"

#Tipos de datos
#Enteros    
a = 1
#Flotantes
b = 1.0
#Cadenas
c = "Hola"
#Booleanos
d = True
#Listas
e = [1,2,3]
#Tuplas
f = (1,2,3)
#Diccionarios
g = {"a":1,"b":2,"c":3}
#Conjuntos
h = {1,2,3}

#Operadores
#Aritmeticos
#Suma
a + b
#Resta
a - b
#Multiplicacion
a * b
#Division
a / b
#Modulo
a % b
#Potencia
a ** b
#Division entera
a // b

#Relacionales
#Igualdad
a == b
#Desigualdad
a != b
#Mayor que
a > b
#Menor que
a < b
#Mayor o igual que
a >= b
#Menor o igual que
a <= b  

#Logicos
#Negacion
not a == b
#Conjuncion
a == b and a > b



#Ejercicios de practica 1

#Escribe un programa que muestre por pantalla la frase "¡Hola mundo!".
#Solucion
print("¡Hola mundo!") 

#ejercio 2 
#escribir un programa quer almacene el nombre de una persona en una variable, y luego muestre por pantalla el mensaje "Hola <nombre>!".

#Solucion

nombre = "Juan"
print("Hola " + nombre + "!")

#ejercio 3
#escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla en lineas distintas} el nombre del usuario tantas veces como el numero introducido.

#Solucion

nombre = input("¿Cual es tu nombre? ")

#ejercio 4

#escribir un programa que muestre por pantalla el resultADO DE LA SIGUIENTE OPERACION 3+2/2*5
#solucion
print(3+2/2*5)

#ejercio 5
#escribir un programa que pregunte al usuario por el numero de horas trabajadas y el coste por hora. Despues debe mostrar por pantalla la paga que le corresponde.

#Solucion

horas = input("¿Cuantas horas trabajaste? ")
costo = input("¿Cual es el costo por hora? ")
print("Tu paga es: " + str(int(horas) * int(costo)))

#ejercio 6
#escribir un programa que lea un entero positivo, n, introducido por el usuario y despues muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = n * (n + 1) / 2
#solucion