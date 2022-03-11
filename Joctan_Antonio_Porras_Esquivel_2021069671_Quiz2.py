"""
Tecnológico de Costa Rica
Elementos de Computación
Grupo 13
Alicia Hernández
Joctan Antonio Porras Esquivel
Fecha de entrega: 09-03-2022
Quiz 2
"""
def agregaImpuestos(precio):
    return precio+(precio*0.13)+(precio*0.1)

def seleccionaServicio(servicio, tipoCLiente):
    if(servicio=='1'):
        cortePelo(tipoCLiente)
    elif(servicio=='2'):
        manicure(tipoCLiente)
    else:
        tinte(tipoCLiente)

def tinte(tipoCliente):
    if(tipoCliente=='1'):
        print("El total a pagar es: ₡",agregaImpuestos(20000))
    elif(tipoCliente=='2'):
        print("El tinte no se realiza en niños")
    else:
        print("El total a pagar es: ₡",agregaImpuestos(25000))

def manicure(tipoCliente):
    if(tipoCliente=='1'):
        print("El total a pagar es: ₡",agregaImpuestos(10000))
    elif(tipoCliente=='2'):
        print("El total a pagar es: ₡",agregaImpuestos(5000))
    else:
        print("El total a pagar es: ₡",agregaImpuestos(10000))

def cortePelo(tipoCliente):
    if(tipoCliente=='1'):
        print("El total a pagar es: ₡",agregaImpuestos(10000))
    elif(tipoCliente=='2'):
        print("El total a pagar es: ₡",agregaImpuestos(5000))
    else:
        print("El total a pagar es: ₡",agregaImpuestos(15000))

def peluqueria():
    print("1. Corte de pelo\n2. Manicure\n3. Tinte")
    opcionServicio = input("Digite la ocion deseada: ")
    print("1. Hombre\n2. Niño\n3. Mujer")
    tipoCliente = input("Digite la ocion deseada: ")
    if(opcionServicio=='1' or opcionServicio=='2' or opcionServicio=='3'):
        if(tipoCliente=='1' or tipoCliente=='2' or tipoCliente=='3'):
            seleccionaServicio(opcionServicio,tipoCliente)
            print("¡¡Muchas gracias por su preferencia!!\nHasta la próxima")
        else:
            print("ERROR: Cliente inválido")
    else:
        print("ERROR: Cliente inválido")


peluqueria()
