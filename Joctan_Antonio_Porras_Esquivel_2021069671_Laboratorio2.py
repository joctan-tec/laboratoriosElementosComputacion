"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 01-03-2022
Ej #3,4,7,8,10,11,12,13,16,19
"""
#Librerias
import math

#Funciones

#Ejercicio #3
def getMasaAire():
    try:
        presion = int(input("Ingrese la presion: "))
        volumen = int(input("Ingrese el volumen: "))
        temperatura = int(input("Ingrese la temperatura: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        presion = int(input("Ingrese la presion: "))
        volumen = int(input("Ingrese el volumen: "))
        temperatura = int(input("Ingrese la temperatura: "))
    print("Masa de aire: ",end="")
    return (presion*volumen)/(0.37*(temperatura+460))

#Ejercicio #4
def getPrecioArticulo():
    try:
        precioArticulo = float(input("Ingrese el precio del articulo que compró: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        precioArticulo = float(input("Ingrese el precio del articulo que compró: "))
    print("Precio del articulo con 30% de ganancia: ",end="")
    return precioArticulo+(precioArticulo*0.3)


#Ejercicio #7
def getDineroRecibidoPorDepartamento():
    try:
        presupuesto = float(input("Ingrese el presupuesto anual: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        presupuesto = float(input("Ingrese el presupuesto anual: "))
    print("Dinero de área de Ginecología: ", presupuesto*0.4)
    print("Dinero de área de Traumatología: ", presupuesto*0.3)
    print("Dinero de área de Pediatría: ", presupuesto*0.3)

#Ejercicio #8
def getPorcentajesInversiones():
    try:    
        aporteA = float(input("Ingrese el aporte A: "))
        aporteB = float(input("Ingrese el aporte B: "))
        aporteC = float(input("Ingrese el aporte C: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
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
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    return round(((9/5)*celsius+32),2)
#Ejercicio #11
def figuraCono(altura, radio):
    areaC = round(math.pi*radio*(radio+math.sqrt(radio**2+altura**2)),2)
    volumenC = round(math.pi*altura*radio**2 / 3,2)
    print("El Area de un cono circular recto   ",areaC)
    print("El Volumen de un cono circular recto   ",volumenC)



def figuraCilindro(altura, radio):
    areaC = round(2*math.pi*radio*altura + 2*math.pi*radio**2,2)
    volumenC = round(math.pi*radio**2*altura,2)
    print("El Area de un cilindro   ",areaC)
    print("El Volumen de un cilindro   ",volumenC)



def figuraPiramide(lado, altura, radio):
    apotemaPiramide = round(math.sqrt((altura**2)+(radio**2)),2)
    areaLateral = round((lado*6)*apotemaPiramide/2,2)
    areaHexa = round(((lado*6)*radio)/2,2)
    areaC = areaLateral + areaHexa
    volumenC = round((math.sqrt(3)/2)*lado**2*altura,2)
    print("El Area de una piramide   ",areaC)
    print("El Volumen de una piramide   ",volumenC)


#Ejercicio #12
def cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        lado = float(input("Ingrese el lado del cuadrado: "))
    print("Perímetro:",round((lado*4),2),"m\nArea: ",round((lado*lado),2),"m cuadrados")
#Ejercicio #13
def circulo():
    try:
        radio = float(input("Ingrese el radio del circulo: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        radio = float(input("Ingrese el radio del circulo: "))
    print("Perímetro:",round((math.pi*(radio**2)),2),"unidades de medida\nArea: ",
    round((2*math.pi*radio),2),"unidades de medida al cuadrado")
#Ejercicio #16
def rectangulo():
    try:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
    print("Perímetro:",round(((base*2)+(altura*2)),2),"m\nArea: ",
    round((base*altura),2),"m al cuadrado")

#Ejercicio #19
def biblioteca():
    try:
        cantidadLibros = int(input("Ingrese la cantidad de libros que rentó: "))
        diasRetraso = int(input("Ingrese los dias de retraso de entrega, si no tiene solo ponga un cero: "))
        isPrimeraVez = input("Ingrese un 1 si es su primera renta o un 0 si no lo es: ")
    except:
        print("ERROR: VUELVA A INGRESAR LOS DATOS")
        cantidadLibros = int(input("Ingrese la cantidad de libros que rentó: "))
        diasRetraso = int(input("Ingrese los dias de retraso de entrega, si no tiene solo ponga un cero: "))
        isPrimeraVez = input("Ingrese un 1 si es su primera renta o un 0 si no lo es: ")

    totalPagar = (cantidadLibros*500)+(diasRetraso*100*cantidadLibros)
    print("Cantidad de Libros: ",cantidadLibros,"    Total: ₡", cantidadLibros*500)
    if(diasRetraso!=0):
        print("Dias de retraso: ",diasRetraso, "   Total: ₡",diasRetraso*100*cantidadLibros)
    else:
        print("Dias de retraso: No posee")

    if(isPrimeraVez=='1'):
        totalPagar+=2000
        print("¿Es cliente nuevo? : Si     Total: ₡2000")
    else:
        print("¿Es cliente nuevo? : No")

    print("Total a pagar: ₡", totalPagar)

    

#Programa Principal

#print(getMasaAire())
#print(getPrecioArticulo())
#getDineroRecibidoPorDepartamento()
#getPorcentajesInversiones()
#print(fahrenheit())
#figuraCono(4,5)
#figuraCilindro(4,5)
#figuraPiramide(7,18,6)
#cuadrado()
#circulo()
#rectangulo()
#biblioteca()

