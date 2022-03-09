"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 08-03-2022
Ej 1,2,6,9,10,13,14,17
"""

#Ejercicio #1
def solicitaNumeros0_10():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                       1                    |\n"
    "|                                            |\n"
    "··············································")
    while (True):
        try:
            numero = int(input("Digite un numero entre 0 y 10: "))
        except:
            print("ERROR: LA ENTRADA DEBE SER UN NUMERO ENTERO ENTRE 0 Y 10")
            continue
        if (0 <= numero <= 10):
            break
        else:
            print("Numero fuera de rango")
        
#Ejercicio #2
def buscaNegativo():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                       2                    |\n"
    "|                                            |\n"
    "··············································")
    mayor=0
    menor=99999999999999999999999999999999999999999
    while (True):
        try:
            numero = int(input("Digite un numero: "))
            print("Numero ingresado: ",numero)
        except:
            print("ERROR: LA ENTRADA DEBE SER UN NUMERO ENTERO")
            continue
        if(numero<0):
            print("Número mayor introducido: ", mayor)
            print("Número menor introducido: ", menor)
            print("¡¡Muchas gracias, nos vemos la próxima!!")
            break
        else:
            if(numero<menor):
                menor = numero
            
            if(numero > mayor):
                mayor = numero


        
#Ejercicio #6
def sumatoria():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                       6                    |\n"
    "|                                            |\n"
    "··············································")
    while (True):
        try:
           inicio = int(input("Digite el inicio de la sumatoria: "))
           fin = int(input("Digite el final de la sumatoria: "))
           break
        except:
            print("ERROR: LA ENTRADA DEBE SER UN NUMERO ENTERO")
            continue
    resultado=0
    while (inicio<=fin):
        resultado+=inicio
        inicio+=1
    return resultado
#Ejercicio #9
def ordenInverso():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                       9                    |\n"
    "|                                            |\n"
    "··············································")
    contador=200
    while(contador>=0):
        if (contador%2==0):
            print(contador)
        contador-=1
#Ejercicio #10
def muestraPares():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                      10                    |\n"
    "|                                            |\n"
    "··············································")
    while (True):
        try:
           fin = int(input("Digite el final del rango: "))
           break
        except:
            print("ERROR: LA ENTRADA DEBE SER UN NUMERO ENTERO")
            continue
    contador = 0
    while(contador<=fin):
        if (contador%2==0):
            print(contador)
        contador+=1
#Ejercicio #13
def escribeNumerosdel1al100():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                      13                    |\n"
    "|                                            |\n"
    "··············································")
    contador = 1
    while (contador<=100):
        if(contador%10!=0):
            print(contador,end=" ")
        else:
            print(contador)
        contador+=1
    print("Fin del programa")
    
#Ejercicio #14
def promedioCalificaciones():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                       14                   |\n"
    "|                                            |\n"
    "··············································")
    while (True):
        try:
           cantidadEstudiantes = int(input("Digite la cantidad de estudiantes: "))
           break
        except:
            print("ERROR: LA ENTRADA DEBE SER UN NUMERO ENTERO")
            continue
    contador = 0 
    sumaNotas = 0
    while (cantidadEstudiantes > contador):
        print("Digite la nota del estudiante #",contador+1,": ",end="")
        calificaciones = float(input())
        sumaNotas +=calificaciones
        contador+=1
    print("Promedio de notas: ",end="")
    return round((sumaNotas/cantidadEstudiantes),2)

#Ejercicio #17
def isTripletaPitagorica(cateto1, cateto2, hipotenusa):
    if((cateto1**2+cateto2**2)==hipotenusa**2):
        return True
    return False

def buscaTripletasPitagoricas():
    print("··············································\n"
    "|                                            |\n"
    "|               EJERCICIO NUMERO:            |\n"
    "|                                            |\n" 
    "|                  17 PARTE B                |\n"
    "|                                            |\n"
    "··············································")
    cateto1= 1
    cateto2 = 1
    hipotenusa = 1

    while(hipotenusa<=500):
        while(cateto1<=500):
            while(cateto2<=500):
                if(isTripletaPitagorica(cateto1, cateto2, hipotenusa)):
                    print("Hipotenusa: ",hipotenusa,"Cateto 1: ",cateto1, "Cateto 2: ",cateto2)
                cateto2+=1
            cateto1+=1
            cateto2=1
        hipotenusa+=1
        cateto1=1
# programa principal

solicitaNumeros0_10()
#buscaNegativo()
#print(sumatoria())
#ordenInverso()
#muestraPares()
#escribeNumerosdel1al100()
#print(promedioCalificaciones())
#buscaTripletasPitagoricas()
#isTripletaPitagorica(3,4,5)