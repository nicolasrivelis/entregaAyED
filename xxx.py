c = []
for i in range(10):
    c.append([0, i])
print(c)

def buscarLocalD(x, y):
    cod = int(input("Código de negocio a modificar: "))
    com = 0
    fin = len(x) - 1
    while com <= fin:
        med = (com + fin) // 2
        if x[med][y] == cod:
            print(med, x[med])
            return True
        elif x[med][y] > cod:
            fin = med - 1
        else:
            com = med + 1
    return False
        
print(buscarLocalD(c, 1))