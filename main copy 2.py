# Carpeta que permite ocultar la contraseña al ingresarla
import getpass

USUARIOS = []

def cargaU(arr):
    us = []
    us.append(1) 
    us.append("admin@shopping.com") 
    us.append("12345") 
    us.append("administrador") 
    arr.append(us)
    us = []
    us.append(4) 
    us.append("localA@shopping.com") 
    us.append("AAAA1111") 
    us.append("dueño") 
    arr.append(us)    
    us = []
    us.append(6) 
    us.append("localB@shopping.com") 
    us.append("BBBB2222") 
    us.append("dueño") 
    arr.append(us)
    us = []
    us.append(9) 
    us.append("unCliente@shopping.com") 
    us.append("33xx33") 
    us.append("cliente") 
    arr.append(us)
    us = []
    us.append(10) 
    us.append("1") 
    us.append("2") 
    us.append("administrador") 
    arr.append(us)
    
# Declaración de contadores de rubros, y de auxiliares para la validación de usuario  
intentos = 1
aux = 0
tdc = ""
codu = 0
locales = [[0, 0, 0, 0, 0, 0]]*50
c = 0
ind = 0
perf = 0
com = 0   

for i in range(50):
    locales[i] = [[i + 1, 0, 0, 0, 0, 0]]
   
cargaU(USUARIOS)

def separacion():
    print('-----------------------------------------------------------------------------------------')
   
def ordenadoC(N, filas, ref, col):
    for i in range(0, filas-1):
        for j in range(i+1, filas):
            if N[i][ref] > N[j][ref]:
                for k in range(col):
                    aux = N[i][k]
                    N[i][k] = N[j][k]
                    N[j][k] = aux    
    return N

def ordenadoD(N, filas, ref, col):
    for i in range(0, filas-1):
        for j in range(i+1, filas):
            if N[i][ref] < N[j][ref]:
                for k in range(col):
                    aux = N[i][k]
                    N[i][k] = N[j][k]
                    N[j][k] = aux    
    return N
   
# Respuesta ante ingreso de datos de usuario
def validacion():
    global tdc, codU
    usuario_ingresado = input("Usuario: ") 
    contrasena_ingresada = input('Contraseña: ')
    auxU = False
    auxC = False
    aux = False
   
    for user in USUARIOS:
        if user[1] == usuario_ingresado:
            auxU = True
        if user[2] == contrasena_ingresada:
            auxC = True
        if user[1] == usuario_ingresado and user[2] == contrasena_ingresada:
            tdc = user[3]
            codU = user[0] 
            return True
            
    if auxU == False and auxC == True:
        print("Usuario")
    elif auxU == True and auxC == False:
        print("Contra")
    if auxU == False and auxC == False:
        print("Todo mal")

    
    if aux == False: return False 
    
validado = validacion()
   
# Validación de datos de usuario con variables auxiliares
while intentos != 3:
    print(intentos)
    if validado:
        aux = 1
        intentos = 3
    else:    
        intentos = intentos + 1
        validado = validacion()
        print(validado)
    if intentos == 3 and aux == 0:
        print("Fuera de intentos!")
                  
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
            x = input("Seguir: ").lower()
            if x != "Si":
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
    
def buscarLocalD(x,y,z,m):
    loc = ordenadoC(x, y, z, m)
    cod = int(input("Código de negocio a modificar: "))
    aux = False
    com = 1
    fin = y
    while com < fin or aux:
        med = (com + fin) // 2
        if loc[med][z] == cod:
            aux = True
        elif loc[med][z] > cod:
            fin = med - 1
        else:
            com = med + 1
    if aux:
        print(loc[med])
    else:
        print("No")
            
    
    
# Procedure que permite al admin administrar nuevos locales
def gestionDeLocales():
        global locales, c, ind, perf, com
        print('''
            a) Crear locales.
            b) Modificar local.
            c) Eliminar local.
            d) Mapa de locales.
            e) Volver.
        ''')
        eleccion = input("Seleccione una opción: ")
        while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd' and eleccion != 'e':
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
        match eleccion:
            case 'a':
                verlos = input("Desea ver los locales ya cargados? Si/No: ")
                if verlos == "si":
                    print("Todos los locales: ")
                    for l in range(c):
                        print(locales[l])
                nombre = input("Ingrese el nombre del nuevo local: ")
                for i in range(c):
                    if nombre == locales[i][1]:
                        nombre = input("Ese nombre ya existe, ingrese el nombre de nuevo: ")  
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
                        rubro = "Indumentaria."
                        ind = ind + 1
                    case "b":
                        rubro = "Perfumería."
                        perf = perf + 1                                        
                    case "c":
                        rubro = "Gastronomía."
                        com = com + 1
                locales[c] = [c+1, nombre, ubicacion, rubro, codU] 
                separacion()
                maxMinLocales(c)
                c = c + 1
                locales = ordenadoC(locales, c, 1, 5) 
                menuPrincipalAdmin()
            case 'b': 
                buscarLocalD(locales, c, 0, 5)
                verlos = input("Desea ver los locales ya cargados? Si/No")
                if verlos == "si":
                    print("Todos los locales: ")
                    for l in locales: 
                        print(l)
                locales = ordenadoD(locales, c, 1) 
                menuPrincipalAdmin()
            case 'c': 
                verlos = input("Desea ver los locales ya cargados? Si/No")
                locales = ordenadoD(locales, c, 1, 5) 
                while verlos != "si" or verlos != "Si" or verlos !="No" or verlos != "no":
                    if verlos == "si":
                        print("Todos los locales: ")
                        for l in range(0, c): 
                            print(locales[l])
                        print(l)
                print("En construcción...")
                menuPrincipalAdmin()
            case 'd': 
                verlos = input("Desea ver los locales ya cargados? Si/No")
                while verlos != "si" or verlos != "Si" or verlos !="No" or verlos != "no":
                    if verlos == "si":
                        print("Todos los locales: ")
                        for l in range(0, c): 
                            print(locales[l])
                menuPrincipalAdmin()
            case 'e':
                print("Volviendo... ")
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
            menuPrincipalAdmin()    

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
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '0':
            print("Saliendo.")
        case '1':
            print("En construcción...")
            menuPrincipalDue()
        case '2':
            print("En construcción...")
            menuPrincipalDue()
        case '3':
            print("En construcción...")
            menuPrincipalDue()

def menuPrincipalCli():
    print('''
        1- Registrarme.
        2- Buscar descuentos en locales.
        3- Solicitar descuento.
        4- Ver novedades.
        0- Salir.
    ''')
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '0':
            print("Saliendo.")
        case '1':
            print("En construcción...")
            menuPrincipalCli()
        case '2':
            print("En construcción...")
            menuPrincipalCli()
        case '3':
            print("En construcción...")
            menuPrincipalCli()
        case '4':
            print("En construcción...")
            menuPrincipalCli()
    
# Qué rubro tiene más y menos locales    
def maxMinLocales(x):
    global ind, perf, com
    r = [[1, ind], [2, perf], [3, com]]
    r = ordenadoD(r, 3, 1, 2)
    for i in range(c+1):
        print(locales[i])
    separacion()
    for i in range(len(r)):
        match r[i][0]:
            case 1:
                print("Indumentaria: ", str(ind))
            case 2:
                print("Perfumería: ", str(perf))
            case 3:
                print("Gastronomía: ", str(com))
                
    separacion()
                
if aux == 1:
    print("Bienvenido "+tdc+"!")
    match tdc:
        case "administrador":
            menuPrincipalAdmin()
        case "cliente":
            menuPrincipalDue()
        case "dueño":
            menuPrincipalCli()