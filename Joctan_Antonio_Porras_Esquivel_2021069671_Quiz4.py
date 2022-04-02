"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 30-03-2022
Quiz 4
"""

def checkLetters(string):
    for i in string:
        if not(i in "0123456789-"):
            return True
    return False

def isPair(num):
    if(num%2==0):
        return True
    return False

def printList(myList):
    for i in myList:
        print(i,end=" >> ")
    print()

def addElements():
    pairAmount = []
    stringsAmount = []
    oddAmount = []
    lessThanZeroAmount = []
    while (True):
        element = input("Digite el elemento a agregar: ")
        if(element.lower() == "salir"):
            print("Numeros pares: ",end=" ")
            printList(pairAmount)
            print("Cantidad: ", len(pairAmount))

            print("Numeros impares: ",end=" " )
            printList(oddAmount)
            print("Cantidad: ", len(oddAmount))

            print("Numeros menores a 0: ",end=" " )
            printList(lessThanZeroAmount)
            print("Cantidad: ", len(lessThanZeroAmount))

            print("Numeros de strings: ",end=" " )
            printList(stringsAmount)
            print("Cantidad: ", len(stringsAmount))
            break
        if (checkLetters(element)):
            stringsAmount.append(element)
        else:
            element = int(element)
            if(isPair(element)):
                pairAmount.append(element)
            else:
                oddAmount.append(element)
            
            if(element<0):
                lessThanZeroAmount.append(element)
            
        






#main
addElements()