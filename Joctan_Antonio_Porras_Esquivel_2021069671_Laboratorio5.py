"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 22-03-2022
Ej #3,4,5,6,13
"""



def isNumbers(string):
    for i in string:
        if (i not in "0123456789.-"):
            return False
    return True

def fillListWithNumbers(myType):
    myList = []
    while (True):
        print("Para terminar digite una S")
        num = input("Ingrese un numero: ").lower()
        if(not isNumbers(num)):
            if(num=="s"):
                break
        else:
            myList.append(myType(num))
    return myList


def swapNegativeTozero(myList):
    for j,i in enumerate(myList):
        if (i<0):
            myList[j] = 0


def separateList(myList):
    oddList=[]
    for i in myList:
        if(i%2!=0):
            oddList.append(i)
    return oddList

#Ejercicio #3
def changeNegativeToZero():
    myList = fillListWithNumbers(float)
    swapNegativeTozero(myList)
    return myList
#Ejercicio #4
def generateOddList():
    myList = fillListWithNumbers(float)
    print("Lista original = ",myList)
    print("Lista de impares = ",separateList(myList))
#Ejercicio #5
def pairOddIndex():
    myList = fillListWithNumbers(float)
    oddNumbers = []
    pairNumbers = []
    for j,i in enumerate(myList):
        if (j%2==0):
            pairNumbers.append(i)
        else:
            oddNumbers.append(i)
    print("Lista original = ",myList)
    print("Lista de indices impares = ",oddNumbers)
    print("Lista de indices pares = ",pairNumbers)
#Ejercicio #6
def repetedWords():
    while True:
        try:
            limit = int(input("Cuantas palabras va a ingresar: "))
            if(0 < limit < 11):
                break
            print("ERROR: DEBE SER UN NUMERO ENTERO MAYOR A 0 Y MENOR A 11")
        except:
            print("ERROR: DEBE SER UN NUMERO ENTERO MAYOR A 0 Y MENOR A 11")
    myList = []
    counter = 0
    while (counter < limit):
        word = input("Ingrese la palabra: ")
        if(word not in myList):
            myList.append(word)
            counter+=1
    print(myList)
#Ejercicio #13
def isProductInStock(myList, product):
    for i in myList:
        if (i[0]==product):
            return True
    return False        
def consulta(myList, product):
    for i in myList:
        if (i[0]==product):
            print("Producto: ",product, "--------   Cantidad: ",i[1])
            input("Presione ENTER para continuar")
            return 0
    print("ATENCIÓN: No hay en bodega ningun producto del tipo: ", product)
    input("Presione ENTER para continuar")


def modificarProducto(product, amount, myList, action):
    if(action==1):
        if(isProductInStock(myList,product)):
            for i in myList:
                if (i[0]==product):
                    i[1] = i[1]+amount
        else:
            myList.append([product,amount])
    else:
        if(isProductInStock(myList,product)):
            for i in myList:
                if (i[0]==product):
                    if(i[1]>=amount):
                        i[1] = i[1]-amount
                    else:
                        print("ERROR: No hay suficientes productos de tipo:", product)
        else:
            myList.append([product,amount])
    
    input("Presione ENTER para continuar")

def printStock(myList):
    for i in myList:
        print("Producto: ",i[0], "---------        Cantidad: ",i[1])

def pulperia():
    myList = []
    while True:
        print("··············································\n"
        "|                                            |\n"
        "|                 Pulperia:                  |\n"
        "|                                            |\n"
        "|              Menu Principal                |\n"
        "|                                            |\n"
        "|        1. Consulta                         |\n"
        "|        2. Agregar Productos                |\n"
        "|        3. Vender Productos                 |\n"
        "|        0. Salir                            |\n"
        "|                                            |\n"
        "|                                            |\n"
        "··············································")
        option = input("Ingrese la opción que desea: ")

        if (option=='1'):
            product = input("Digite el producto que desea consultar: ")
            consulta(myList,product)
        elif (option=='2'):
            product = input("Digite el producto que desea agregar: ")
            while True:
                try:
                    amount = int(input("Digite la cantidad de productos que va a agregar: "))
                    if(amount<1):
                        print("ERROR: Debe ser un numero entero mayor a 0")
                        continue
                    break
                except:
                    print("ERROR: Debe ser un numero entero mayor a 0")
            modificarProducto(product,amount,myList,1)
        elif (option=='3'):
            product = input("Digite el producto que desea vender: ")
            while True:
                try:
                    amount = int(input("Digite la cantidad de productos que va a vender: "))
                    if(amount<1):
                        print("ERROR: Debe ser un numero entero mayor a 0")
                        continue
                    break
                except:
                    print("ERROR: Debe ser un numero entero mayor a 0")
            modificarProducto(product,amount,myList,0)
        elif (option=='0'):
            printStock(myList)
            break



#main

#print(changeNegativeToZero())
#generateOddList()
#pairOddIndex()
#repetedWords()
#pulperia()