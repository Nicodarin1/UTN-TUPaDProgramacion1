#Imprime por pantalla un hola mundo

print("hola mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
print("Escribi, tu nombre y apellido")
nombre = input ("")

print ("Hola",(nombre),"!" )

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.


print ("Ingresa tu nombre y apellido") 

Nombre = input ()

print ("Ingresa tu edad actual")

Edad = input ()

print ("Ingresa donde vivis actualmente")

LugarDeResidencia = input ()

print ("Soy",(Nombre),", tengo",(Edad),"años y vivo en", (LugarDeResidencia))

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

#Pide el radio y convierte a numero decimal

radio = float(input("Ingrese el radio de la circunferencia: "))


print ("Bien, con  el radio, se puede calcular el area y perimetro de la circunferencia")

#Calcular el area y perimetro
from math import pi
area = pi * radio ** 2

perimetro = 2 * pi * radio
print ("El Area de la circunferencia a partir del radio dado es", area,"y el perimetro es", perimetro)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = float (input("Ingrese una cantidad de segundos y sera pasada a horas en equivalencia " ) )

horas = segundos / 3600


print( "La cantidada de segundos", segundos, "pasadas en horas es ", horas )

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

#se le solicita al usuario el numero que desea saber su tabla
numero = float (input ( "Ingrese el numero para ver su tabla de multiplicacion "))

#tablas del 1 al 10 inclusive
tabladel1= print ("La tabla del uno, del numero ", numero, "es: ", 1*numero )

tabladel2= print ("La tabla del dos, del numero ", numero, "es: ", 2*numero )

tabladel3= print ("La tabla del tres, del numero ", numero, "es: ", 3*numero )

tabladel4= print ("La tabla del cuatro, del numero ", numero, "es: ", 4*numero )

tabladel5= print ("La tabla del cinco, del numero ", numero, "es: ", 5*numero )

tabladel6= print ("La tabla del seis, del numero ", numero, "es: ", 6*numero )

tabladel7= print ("La tabla del siete, del numero ", numero, "es: ", 7*numero )

tabladel8= print ("La tabla del ocho, del numero ", numero, "es: ", 8*numero )

tabladel9 = print ("La tabla del nueve, del numero ", numero, "es: ", 9*numero )

tabladel10 = print ("La tabla del diez, del numero ", numero, "es: ", 10*numero )

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#solicita al usuario dos numeros

numero1 = float(input (" Ingrese el primer numero "))
numero2 = float(input (" Ingrese el segundo numero "))


#Se realizan las cuentas de multiplicacion, division, resta, y suma

suma = print ("El resultado de la suma entre el primer y segundo numero es: " ,numero1 + numero2) 

multiplicacion = print ("El resultado de la multiplicacion entre el primer y segundo numero es: " ,numero1 * numero2) 

division = print ("El resultado de la division entre el primer y segundo numero es: " ,numero1 / numero2) 

resta = print ("El resultado de la resta entre el primer y segundo numero es: " ,numero1 - numero2) 

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = peso en kg/ altura en metros cuadrados

#Se le solicita al usuario su peso en kg, y la altura 

peso = float (input ("Ingrese su peso actual: "))
altura = float (input ("Ingrese su altura actual: ")) /100



imc = print ("Su Indice de Masa corporal es: ", (peso )/ (altura**2 ))

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =
#9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32



#Se le solicita al usuario la temperatura en grados celsius

temperatura = float(input("Ingrese la temperatura actual en °C: "))


fahrenheit = (9/5) * temperatura + 32

print("La temperatura en Fahrenheit es: ", fahrenheit)

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

#Se le solicita al usuario dos numeros, para luego sacar su promedio

numero1 = float (input ("Ingrese el primer numero: "))
numero2 = float (input ("Ingrese el segundo numero: "))


promedio = print ("El promedio de los numeros datos es: ",(numero1+numero2)/2)
