# Carpeta que permite ocultar la contraseña al ingresarla
import getpass
#import numpy as np

USUARIOS = []
    
# Declaración de contadores de rubros, y de auxiliares para la validación de usuario
ind = 0
perf = 0
com = 0   
intentos = 1
aux = 0
contador = 0
locales = []

def separacion():
    print('-----------------------------------------------------------------------------------------')
   
def ordenado(N, filas, c):
    for i in range(0, filas-1):
        for j in range(i+1, filas):
            if N[i][c] < N[j][c]:
                for k in range(5):
                    aux = N[i][k]
                    N[i][k] = N[j][k]
                    N[j][k] = aux    

# Respuesta ante ingreso de datos de usuario
def validacion():
    global contador
    carga(USUARIOS)
    usuario_ingresado = input("Usuario: ") 
    contrasena_ingresada = getpass.getpass(prompt='Contraseña: ')
    auxU = False
    auxC = False
   
    for user in USUARIOS:
        if user[1] == usuario_ingresado:
            auxU = True
        if user[2] == contrasena_ingresada:
            auxC = True
        if user[1] == usuario_ingresado and user[2] == contrasena_ingresada:
            return True
        else: 
            contador = contador + 1
            return False
            
    if auxU == False and auxC == True:
        print("Usuario")
    elif auxU == True and auxC == False:
        print("Contra")
    if auxU == False and auxC == False:
        print("Todo mal")

validado = validacion()
    
# Validación de datos de usuario con variables auxiliares
while intentos != 3:
    if validado:
        aux = 1
        intentos = 3
    else:    
        intentos = intentos + 1
        validado = validacion()
    if intentos == 3:
        print("Muchas gracias!")
                
# Qué rubro tiene más y menos locales
def maxMinLocales():
    if ind > perf and ind > com:
        print('Indumentaria es el rubro con más locales, con un total de',ind)
    elif perf > ind and perf > com:
        print('Perfumería es el rubro con más locales, con un total de',perf)
    elif com > perf and com > ind:
        print('Gastronomía es el rubro con más locales, con un total de',com)
    elif ind == perf and perf == com:
        print("Todos los rubros tienen la misma cantidad de locales, con un total de", ind)
    elif ind == perf and ind > com:
        print('Indumentaria y perfumería son los rubros con más locales, con un total de', perf)
    elif ind == com and ind > perf:
        print('Indumentaria y gastronomía son los rubros con más locales, con un total de', ind)
    elif perf == com and perf > ind:
        print('Perfumería y gastronomía son los rubros con más locales, con un total de', perf)

    if ind < perf and ind < com:
        print('Indumentaria es el rubro con menos locales, con un total de',ind)
        separacion()
    elif perf < ind and perf < com:
        print('Perfumería es el rubro con menos locales, con un total de',perf)
        separacion()
    elif com < perf and com < ind:
        print('Gastronomía es el rubro con menos locales, con un total de',com)
        separacion()
    elif ind == perf and ind < com:
        print('Indumentaria y perfumería son los rubros con menos locales, con un total de', perf)
        separacion()
    elif ind == com and ind < perf:
        print('Indumentaria y gastronomía son los rubros con menos locales, con un total de', ind)
        separacion()
    elif perf == com and perf < ind:
        print('Perfumería y gastronomía son los rubros con menos locales, con un total de', perf)
        separacion()

# Menu Principal donde usuario puede hacer lo que quiera
def menuPrincipalAdmin():
    print('''
        1- Gestión de locales.
        2- Crear cuenta de dueños de locales.
        3- Aprobar/Denegar solicitudes de cuentas.
        4- Gestión de novedades.
        5- Reporte de utilización de descuentos.
        0- Salir.
        ''')
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4' and eleccion != '5' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '0':
            print("Saliendo.")
        case '1':
            gestionDeLocales()
        case '2':
            print("En construcción...")
            menuPrincipalAdmin() 
        case '3':
            print("En construcción...")
            menuPrincipalAdmin()
        case '4':
            gestionDeNovedades()
        case '5':
            print("En construcción...")
            menuPrincipalAdmin()


# Procedure que permite al admin administrar nuevos locales
def gestionDeLocales():
        global ind         
        global perf        
        global com         
        print('''
            a) Crear locales.
            b) Modificar local.
            c) Eliminar local.
            d) Mapa de locales.
            e) Volver.
        ''')
        eleccion = input("Seleccione una opción: ")
        while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd':
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
        match eleccion:
            case 'a':
                verlos = input("Desea ver los locales ya cargados? Si/No")
                if verlos == "Si":
                    for l in locales: 
                        print(l)
                nombre = input("Ingrese el nombre del nuevo local: ")
                ubicacion = input("Ingrese la ubicación: ")
                print('''
                      a- Indumentaria.
                      b- Perfumería.
                      c- Gastronomía.
                      ''')
                rubro = input("Seleccione a que rubro pertenece el local: ").lower()
                while rubro != 'a' and rubro != 'b' and rubro != 'c' and rubro != 'indumentaria' and rubro != 'perfumeria' and rubro != 'gastronomia':
                    print('Selección no válida.')
                    rubro = input("Seleccione a que rubro pertenece el local: ")                  
                match rubro:
                    case "a":
                        ind = ind + 1
                    case "indumentaria":
                        ind = ind + 1
                    case "b":
                        perf = perf + 1
                    case "perfumeria":  
                        perf = perf + 1
                    case "c":  
                        com = com + 1
                    case "gastronomia":
                        com = com + 1
                locales.append([nombre, ubicacion, rubro, contador])
                locales = ordenado(locales, 50, 2)
                separacion()
                maxMinLocales()
                menuPrincipalAdmin()
            case 'b': 
                verlos = input("Desea ver los locales ya cargados? Si/No")
                if verlos == "Si":
                    for l in locales: 
                        print(l)                
                print("En construcción...")
                menuPrincipalAdmin()
            case 'c':
                verlos = input("Desea ver los locales ya cargados? Si/No")
                if verlos == "Si":
                    for l in locales: 
                        print(l)
                print("En construcción...")
                menuPrincipalAdmin()
            case 'd':
                verlos = input("Desea ver los locales ya cargados? Si/No")
                if verlos == "Si":
                    for l in locales: 
                        print(l)
                menuPrincipalAdmin()
 
# Procedure que permite al admin administrar novedades, en construcción 
def gestionDeNovedades():
    print('''
          a- Crear novedades.
          b- Modificar novedades.
          c- Eliminar novedades.
          d- Ver reporte de novedades.
          e- Volver''')
    eleccion = input("Seleccione una opción: ")
    while eleccion != 'a' or eleccion != 'b' or eleccion != 'c' or eleccion != 'd' or eleccion != 'e':
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
    match eleccion:    
        case 'a':
            print('En construcción...')
            gestionDeNovedades()
        case 'b':
            print("En construcción...")
            gestionDeNovedades()
        case 'c':
            print("En construcción...")
            gestionDeNovedades()
        case 'd':
            print("En construcción...")
            gestionDeNovedades()
        case 'e':
            menuPrincipal()    

def menuPrincipalDue():
    print('''
        1- Gestión de Descuentos.
          a) Crear descuento para mi local
          b) Modificar descuento de mi local
          c) Eliminar descuento de mi local
          d) Volver
        2- Aceptar / Rechazar pedido de descuento.
        3- Reporte de uso de descuentos.
        0- Salir.
    ''')
    
def menuPrincipalCli():
    print('''
        1- Registrarme.
        2- Buscar descuentos en locales.
        3- Solicitar descuento.
        4- Ver novedades.
        0- Salir.
    ''')
            
if aux == 1:
    print("Bienvenido!")
    tdc = USUARIOS[contador][3]
    match tdc:
        case 0:
            menuPrincipalAdmin()
        case 1:
            menuPrincipalDue()
        case 2:
            menuPrincipalCli()
        case 3:
            print("")
