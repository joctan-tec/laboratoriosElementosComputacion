"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alcia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 22-02-2022
"""
import random

print("Ejercicio #2")

cantidadCompra = int(input("Indique de cuanto fue su compra: "))
numeroAzar = random.randint(0,100)
if(numeroAzar<50):
    print("Su descuento fue de: " , cantidadCompra*0.15)

else:
    print("Su descuento fue de: " , cantidadCompra*0.20)

print("\n\nEjercicio #3")

valorX = int(input("Indique un número: "))

if(valorX%4==0):
    print("Resultado = ", valorX*valorX)
elif(valorX%4==1):
    print("Resultado = ", valorX/6)
elif(valorX%4==2):
    print("Resultado = ", valorX**0.5)
elif(valorX%4==3):
    print("Resultado = ", valorX*valorX*valorX+5)

print("\n\nEjercicio #4")


numeroParImpar = int(input("Indique un número: "))
if(numeroParImpar%2==0):
    print("El número es par")
else:
    print("El número es impar")


print("\n\nEjercicio #10")

numeroHectareas = int(input("Indique la cantidad de hectáreas del terreno a reforestar: "))
numeroMetros = numeroHectareas*10000
if(numeroMetros>1000000):
    terrenoPinos = numeroMetros*0.7
    terrenoEucalipto = numeroMetros*0.2
    terrenoCedro = numeroMetros*0.1

    print("Cantidad de Pinos: ", terrenoPinos//10*8)
    print("Cantidad de Eucalipto: ", terrenoEucalipto//15*15)
    print("Cantidad de Cedros: ", terrenoCedro//18*10)

else:
    terrenoPinos = numeroMetros*0.45
    terrenoEucalipto = numeroMetros*0.3
    terrenoCedro = numeroMetros*0.25

    print("Cantidad de Pinos: ", terrenoPinos//10*8)
    print("Cantidad de Eucalipto: ", terrenoEucalipto//15*15)
    print("Cantidad de Cedros: ", terrenoCedro//18*10)

print("\n\nEjercicio #11")

precioCarroTerreno = int(input("Indique el precio que tiene el automóvil y el terreno: "))
devaluacionCarro = int(input("Indique el porcentaje de devaluación por año: "))/100
incrementoTerreno = int(input("Indique el porcentaje de aumento por año: "))/100

if(precioCarroTerreno*devaluacionCarro*3<=precioCarroTerreno*incrementoTerreno*3/2):
    print("Puede comprar el carro")
else:
    print("Debe comprar el terreno")


print("\n\nEjercicio #13")

balanceActualTarjeta = int(input("Indique el balance actual de la tarjeta: "))
montoCompra = int(input("Indique el monto de la compra: "))
limiteCredito = int(input("Indique el limite de credito de la tarjeta: "))
porcentajeImpuestos = int(input("Indique el porcentaje de impuestos por cobrar del mes: "))/100

if(balanceActualTarjeta+montoCompra+(montoCompra*porcentajeImpuestos)<limiteCredito):
    print("Su compra ha sido exitosa, el nuevo valance de su tarjeta es: ",
     balanceActualTarjeta+montoCompra+(montoCompra*porcentajeImpuestos))
else:
    print("Su compra ha sido denegada, su balance es insuficiente")

print("\n\nEjercicio #14")

sexo = input("Indique si es hombre o mujer: ")
edad = int(input("Indique su edad: "))
if(sexo.lower()=="mujer"):
    print("Sus pulsaciones deberian ser: ", (220-edad)/10," cada 10 segundos")
elif(sexo.lower()=="hombre"):
    print("Sus pulsaciones deberian ser: ", (210-edad)/10," cada 10 segundos")
else:
    print("Sexo no existe")


print("\n\nEjercicio #16")

promedioAnterior = int(input("Indique su promedio del periodo pasado: "))

if(promedioAnterior>=70):
    print("Deberá pagar solamente: US$", 100000-100000*0.3)
else:
    print("Deberá pagar la colegiatura completa que es equivalente a: US$100000")


print("\n\nEjercicio #18")

nota = int(input("Indique la nota obtenida: "))

if(nota<5):
    print("Calificación cualitativa: Reprobado")
elif(5 < nota <7):
    print("Calificación cualitativa: Suspenso")
elif(7 < nota <8.5):
    print("Calificación cualitativa: Notable")
elif(8.5 < nota <10):
    print("Calificación cualitativa: Sobresaliente")
elif(nota==10):
    print("Calificación cualitativa: Matrícula de honor")


print("\n\nEjercicio #19")


euros = int(input("Indique la cantidad de euros: "))

if(euros//500!=0):
    print(euros//500,"billetes de 500 euros")
    euros-=euros//500*500

if(euros//200!=0):
    print(euros//200,"billetes de 200 euros")
    euros-=euros//200*200

if(euros//100!=0):
    print(euros//100,"billetes de 100 euros")
    euros-=euros//100*100

if(euros//50!=0):
    print(euros//50,"billetes de 50 euros")
    euros-=euros//50*50

if(euros//20!=0):
    print(euros//20,"billetes de 20 euros")
    euros-=euros//20*20

if(euros//10!=0):
    print(euros//10,"billetes de 10 euros")
    euros-=euros//10*10

if(euros//5!=0):
    print(euros//5,"billetes de 5 euros")
    euros-=euros//5*5

if(euros//2!=0):
    print(euros//2,"monedas de 2 euros")
    euros-=euros//2*2

if(euros!=0):
    print(euros,"monedas de 1 euro")