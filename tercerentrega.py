import os
import pickle
import os.path
import io

class Usuario():
    def __init__(self):
        self.codigo = 0
        self.usuario = ''.ljust(100, '')
        self.clave = ''.ljust(8, '')
        self.tipo = ''.ljust(13,'')

auf = 'C:/Desktop/UTN/1ero/AyED/USUARIOS.dat'
if os.path.exists(auf):
    aul = open(auf, 'r+b')
else:
    aul = open(auf, 'w+b')

def primerMenu():
    print('''
        1- Ingresar como usuario registrado.
        2- Registrarse como cliente.
        3- Salir.
        ''')
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '1':
            print(1)
            #ingreso()
        case '2':
            registro()
        case '3':
            print("Saliendo...")


def registro():
    U = Usuario()
    ingresarDatos(U)
    while busqCli(U.usuario, U.clave): 
        ingresarDatos(U)
    ultC = sacarTam()
    U.codigo = ultC + 1
    U.tipo = 'Cliente'
    pickle.dump(U, aul)
    aul.flush()

def sacarTam():
    tamArc = os.path.getsize(aul)
    aul.seek(0)
    pickle.load(aul)
    tamReg = aul.tell()
    iterador = tamArc // tamReg
    return iterador

def ingresarDatos(x):
    x.usuario = input('Ingrese mail de usuario: ')
    while len(x.usuario) > 100:
        print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
        x.usuario = input('>>  ')

    x.clave = input('Ingrese clave de usuario: ')
    while len(x.clave) > 8:
        print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
        x.clave = input('>>  ')
    
def busqCli(x,y):
    tamArc = os.path.getsize(aul)
    aul.seek(0)
    aux = False
    while aul.tell() < tamArc and aux == False:
        reg = pickle.load(aul)
        if reg.usuario == x and reg.clave == y:
            print('Usuario existente con este usuario y clave.')
            ## agregar redireccion a ingreso
            aux = True
        elif reg.usuario == x:
            print('Usuario existente con este usuario.')
            aux = True
    return aux
     