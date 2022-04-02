"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 29-03-2022
Ejercicios #1,3,5,6
"""

def createMatrix():
    while (True):
        try:
            size = int(input("Indique el tamaño que va a tener la matriz: "))
            if(size<2):
                input("Error: el valor debe ser un numero entero mayor a 1")
            else:
                break
        except:
            input("Error: el valor debe ser un numero entero mayor a 1")
    matrix = []
    
    for i in range(size):
        row = []
        for j in range(size):
            while (True):
                try:
                    number = int(input("Ingrese un numero: "))
                    if(size<2):
                        print("Error: el valor debe ser un numero entero mayor a 1")
                    else:
                        row.append(number)
                        break
                except:
                    print("Error: el valor debe ser un numero entero")
        matrix.append(row)
        row = []
    return matrix

def count(num):
    num = abs(num)
    if(num==0):
        return 1
    digits = 0
    while (num !=0):
        num//=10
        digits+=1
    return digits

def showMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" "*(4-count(j)))
        print()
    
def readMatrix(row,colum):
    matrix = []
    
    for i in range(row):
        row = []
        for j in range(colum):
            while (True):
                try:
                    number = int(input("Ingrese un numero: "))
                    row.append(number)
                    break
                except:
                    print("Error: el valor debe ser un numero entero")
        matrix.append(row)
        row = []
    return matrix
    


#Ejercicios #1
def matrixT():
    matrix = createMatrix()
    sizeMatrix = len(matrix)
    showMatrix(matrix)
    print("\nTriangular Superior")
    for i,colum in enumerate(matrix):
        for j,row in enumerate(colum):
            if(j>=i):
                print(row,end=" "*(4-count(row)))
            else:
                print(0,end="   ")
        print()
    print("\nTriangular Inferior")
    for i,colum in enumerate(matrix):
        for j,row in enumerate(colum):
            if(j<=i):
                print(row,end=" "*(4-count(row)))
            else:
                print(0,end="   ")
        print()

#Ejercicios #3
def fillMatrixWithIndex():
    matrix = []
    for i in range(7):
        row = []
        for j in range(4):
            row.append(i+j)
        matrix.append(row)
        row = []
    showMatrix(matrix)
#Ejercicios #5
def identifyMatrix():
    while (True):
        try:
            size = int(input("Indique el tamaño que va a tener la matriz: "))
            if(size<2):
                input("Error: el valor debe ser un numero entero mayor a 1")
            else:
                break
        except:
            input("Error: el valor debe ser un numero entero mayor a 1")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if(j==i):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
        row = []
    showMatrix(matrix)
#Ejercicios #6
def addSubtractMatrix():
    while (True):
        try:
            row = int(input("Indique el numero de filas: "))
            colum = int(input("Indique el numero de columnas: "))
            if(row<2 or colum <2):
                input("Error: el valor debe ser un numero entero mayor a 1")
            else:
                break
        except:
            input("Error: el valor debe ser un numero entero mayor a 1")
    print("Digite los numeros de la primer matriz")
    matrix1 = readMatrix(row,colum)
    print("Digite los numeros de la segunda matriz")
    matrix2 = readMatrix(row,colum)

    newMatrixSum = []
    newMatrixSubs = []
    for m,i in enumerate(matrix1):
        newRow = []
        for j,k in enumerate(i):
            newRow.append(k+matrix2[m][j])
        newMatrixSum.append(newRow)
        
    print("\nSuma de matrices\n")
    showMatrix(newMatrixSum)

    for m,i in enumerate(matrix1):
        newRow = []
        for j,k in enumerate(i):
            newRow.append(k-matrix2[m][j])
        newMatrixSubs.append(newRow)
    print("\nResta de matrices\n")
    showMatrix(newMatrixSubs)
    

#main
#matrixT()
#fillMatrixWithIndex()
#identifyMatrix()
#addSubtractMatrix()