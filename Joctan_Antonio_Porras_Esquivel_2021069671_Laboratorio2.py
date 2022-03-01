"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 
Ej #3,4,7,8,10,11,12,13,16,19
"""
#Librerias
import math

#Funciones

#Ejercicio #3
def getMasaAire():
    presion = int(input("Ingrese la presion: "))
    volumen = int(input("Ingrese el volumen: "))
    temperatura = int(input("Ingrese la temperatura: "))
    print("Masa de aire: ",end="")
    return (presion*volumen)/(0.37*(temperatura+460))

#Ejercicio #4
def getPrecioArticulo():
    precioArticulo = float(input("Ingrese el precio del articulo que compró: "))
    print("Precio del articulo con 30% de ganancia: ",end="")
    return precioArticulo+(precioArticulo*0.3)


#Ejercicio #7
def getDineroRecibidoPorDepartamento():
    presupuesto = float(input("Ingrese el presupuesto anual: "))
    print("Dinero de área de Ginecología: ", presupuesto*0.4)
    print("Dinero de área de Traumatología: ", presupuesto*0.3)
    print("Dinero de área de Pediatría: ", presupuesto*0.3)

#Ejercicio #8
def getPorcentajesInversiones():    
    aporteA = float(input("Ingrese el aporte A: "))
    aporteB = float(input("Ingrese el aporte B: "))
    aporteC = float(input("Ingrese el aporte C: "))
    total= aporteA+aporteB+aporteC
    print("Total de Inversiones: ",total)
    print("El aporte A corresponde a: ",aporteA, " Representa un ", round((aporteA/total*100),2) ,"% del total")
    print("El aporte A corresponde a: ",aporteB, " Representa un ", round((aporteB/total*100),2) ,"% del total")
    print("El aporte A corresponde a: ",aporteC, " Representa un ", round((aporteC/total*100),2) ,"% del total")

#Ejercicio #10
def fahrenheit():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    return round(((9/5)*celsius+32),2)
#Ejercicio #11

#Ejercicio #12
def cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    print("Perímetro:",round((lado*4),2),"m\nArea: ",round((lado*lado),2),"m cuadrados")
#Ejercicio #13
def circulo():
    radio = float(input("Ingrese el radio del circulo: "))
    print("Perímetro:",round((math.pi*(radio**2)),2),"unidades de medida\nArea: ",
    round((2*math.pi*radio),2),"unidades de medida al cuadrado")
#Ejercicio #16

#Ejercicio #19



#Programa Principal
#print(getMasaAire())
#print(getPrecioArticulo())
#getDineroRecibidoPorDepartamento()
#getPorcentajesInversiones()
#print(fahrenheit())
#cuadrado()
circulo()