"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 29-03-2022
Ejercicios #1,4
"""
import random

# Ejercicio 1
def searchNames():
    while (True):
        try:
            size = int(input("Indique la cantidad de nombres que va a insertar: "))
            if(size<0):
                return 0
            else:
                break
        except:
            input("Debe indicar un valor numerico, Digite ENTER para continuar")
    namesList = []
    for i in range(size):
        print(i+1,'. ')
        namesList.append((i+1,input("Ingrese un nombre: ")))

    while (True):
        print("··············································\n"
        "|                                            |\n"
        "|                                            |\n"
        "|              Menu Principal                |\n"
        "|                                            |\n"
        "|        1. Buscar Nombre                    |\n"
        "|        0. Salir                            |\n"
        "|                                            |\n"
        "|                                            |\n"
        "··············································")
        option = input("Digite la opcion que desea realizar: ")

        if(option=='0'):
            break
        elif(option =='1'):
            while (True):
                try:
                    position = int(input("Indique la posicion del nombre: "))
                    break
                except:
                    input("ERRROR: DEBE DIGITAR UN NUMERO ENTERO MAYOR A 0")
            if(size<1):
                input("ERRROR: DEBE DIGITAR UN NUMERO ENTERO MAYOR A 0")
                continue
            if(0<position<=len(namesList)):
                print("El nombre en la posicion ",position," es: ", namesList[position-1][1])
            else:
                print("el nombre no existe")

# Ejercicio 4

def searchMax(myList):
    currentMax = 0
    for i in myList:
        if(i>currentMax):
            currentMax = i
    return currentMax

def searchMin(myList):
    currentMin = 111
    for i in myList:
        if(i<currentMin):
            currentMin = i
    return currentMin

def average(myList):
    container = 0
    for i in myList:
        container+=i
    return container/100

def median(myList):
    myList.sort()
    print(myList)
    return myList[49]+myList[50]/2


def generateRandoms():
    myList = []
    for i in range(100):
        myList.append(random.randint(1,100))
    return (searchMax(myList), searchMin(myList),average(myList),median(myList))

def callGenerateRandoms():
    data = generateRandoms()
    print("Numero Mayor: ", data[0])
    print("Numero Menor: ", data[1])
    print("Promedio de numeros: ", data[2])
    print("Mediana: ", data[3])


#main

#searchNames()
#callGenerateRandoms()



    
    

    
