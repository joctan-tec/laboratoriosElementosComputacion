"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 02-04-2022
Tarea Programada
"""


def askForStudentScores():
    containerScores = 0
    highiestScore = 0
    lowestScore = 100
    counterOfEvaluations = 0
    while (True):
        try:
            amountScores = int(input("Indique la cantidad de evaluaciones a promediar: "))
            if(amountScores<1):
                input("Error: el valor debe ser un numero entero mayor a 0 \nPresione ENTER para continuar")
            else:
                break
        except:
            input("Error: el valor debe ser un numero entero mayor a 0 \nPresione ENTER para continuar")
    for i in range(amountScores):
        while (True):
            try:
                score = float(input("Indique la nota obtenida: "))
                if(0<=score<=100):
                    break
                else:
                    input("Error: el valor debe ser un numero entre 0 y 100 \nPresione ENTER para continuar")
            except:
                input("Error: el valor debe ser un numero entre 0 y 100 \nPresione ENTER para continuar")
        containerScores += score
        counterOfEvaluations +=1
        if(score > highiestScore):
            highiestScore = score
        if(score < lowestScore):
            lowestScore = score
    print("El promedio de las notas del estudiante es: ",containerScores/amountScores)
    input("Presione ENTER para continuar")
    #Return Format
    #(Sum of student scores, highiest Score of student, lowest score of student, amount of evaluations)
    return containerScores, highiestScore, lowestScore, counterOfEvaluations

def calculateAverages():
    amountOfStudentsEvaluated = 0
    highiestScore = 0
    lowestScore = 100
    containerScores = 0
    counterOfEvaluations = 0
    while (True):
        print("··············································\n"
            "|                                            |\n"
            "|              Menu Principal                |\n"
            "|                                            |\n"
            "|        1. Promediar Estudiante             |\n"
            "|        0. Salir                            |\n"
            "|                                            |\n"
            "··············································")
        option = input("Digite la opcion que desea realizar: ")
        if (option=='0'):
            print("Estudiantes Promediados: ", amountOfStudentsEvaluated)
            print("Promedio de todas las evaluaciones: ", containerScores/counterOfEvaluations)
            print("Nota más alta: ", highiestScore)
            print("Nota más baja: ", lowestScore)
            break
        elif(option=='1'):
            results = askForStudentScores()
            containerScores += results[0]
            if(results[1] > highiestScore):
                highiestScore = results[1]
            if(results[2] < lowestScore):
                lowestScore = results[2]
            amountOfStudentsEvaluated +=1
            counterOfEvaluations += results[3]


#main

calculateAverages()
