"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 15-03-2022
Ej 3,5,6,8,9,21
"""

#Ejercicio #3




def deleteSpaces():
    userPhrase = input("Ingrese la frase que desea quitar los espacios: ")
    newString = ""
    deletedSpaces = 0
    for i in userPhrase:
        if(i!=" "):
            newString+=i
        else:
            deletedSpaces+=1
    print("Palabra inicial: ",userPhrase)
    print("Frase resultante: ", newString)
    print("Espacios eliminados: ", deletedSpaces)
#Ejercicio #5
def repeatName():
    userName = input("Ingrese su nombre: ")
    return (userName+" ")*100
#Ejercicio #6
def swapUpperLowerCases(string):
    newPhrase=""
    for i in string:
        if (i.isupper()):
            newPhrase += i.lower()
        else:
            newPhrase += i.upper()
    return newPhrase
#Ejercicio #8
def isLowerOrUpperCase():
    userChar = input("Ingrese un caracter: ")
    if(len(userChar)>1):
        return "ERROR: DEBE INTRODUCIR SOLO UN CARACTER"
    if(userChar in "1234567890"):
        return "No es una letra"
    if (userChar.isupper()):
        return "Es una MAYUSCULA"
    if (userChar.islower()):
        return "Es una MINUSCULA"
#Ejercicio #9
def indentifyChar():
    userChar = input("Ingrese un caracter: ")
    if(len(userChar)>1):
        return "ERROR: DEBE INTRODUCIR SOLO UN CARACTER"
    if (userChar.lower() in "aeiou"):
        if (userChar.isupper()):
            return "vocal mayuscula"
        else:
            return "vocal minuscula"
    elif(userChar.lower() in "bcdfghjklmnñpqrstvwxyz"):
        if (userChar.isupper()):
            return "consonante mayuscula"
        else:
            return "consonante minuscula"
    else:
        return "Otro tipo de caracter"
#Ejercicio #21
def countNumbers(string):
    numbers=0
    for i,j in enumerate(string):
        try:
            if (j in "1234567890" and not(string[i+1] in "1234567890")):
                numbers+=1
        except IndexError:
            if (j in "1234567890"):
                numbers+=1
    print("Cantidad de numeros: ", end="")
    return numbers


#deleteSpaces()
#print(repeatName())
#print(swapUpperLowerCases("eSTE eS solo Un EJEMPLO"))
#print(isLowerOrUpperCase())
#print(indentifyChar())
print(countNumbers("un 1, un 201 y 2 unos"))