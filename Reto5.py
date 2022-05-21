def agregar(tabla):
    registro=input().split()
    clave=int(registro[0])
    datos=[registro[1], float(registro[2]), int(registro[3])]
    if clave in tabla.keys():
        Error = True    #bandera
    else:
        tabla[clave]=datos
        Error = False
    return(tabla, Error)

def borrar(tabla):
    reg=input().split()
    reg[0]=int(reg[0])
    if reg[0] in tabla.keys():
        tabla.pop(reg[0])
        Error = False   
    else:
        Error = True    #bandera
    return(tabla, Error)

def actualizar(tabla):
    registro=input().split()
    clave=int(registro[0])
    datos=[registro[1], float(registro[2]), int(registro[3])]
    if clave in tabla.keys():
        tabla[clave]=[]
        tabla[clave]=datos
        Error = False   
    else:
        Error = True    #bandera
    return(tabla, Error)

def promedio(tabla):
    suma=0
    for i in tabla:
        suma += tabla[i][1]
    promedio =suma/len(tabla)
    return (round(promedio,1))

def valor_inventario(tabla):
    suma=0
    for i in tabla:
        suma += tabla[i][1]*tabla[i][2]
    return (round(suma,1))

def mayor(tabla):
    valor=[]
    for i in tabla:
        if i <= len(tabla)+1:
            valor.append(tabla[i][1])
    x=max(valor)
    for j in tabla:
        if not x == tabla[j][1]:
            w=False
        else:
            w=True  #Bandera
            break
    if w == True:
        printlinemax=(tabla[j][0]) 
        return (printlinemax)

def menor(tabla):
    valor=[]
    for i in tabla:
        if i <= len(tabla)+1:
            valor.append(tabla[i][1])
    x=min(valor)
    for j in tabla:
        if not x == tabla[j][1]:
            w=False
        else:
            w=True  #Bandera
            break
    if w == True:
        printlinemin=(tabla[j][0])
        return (printlinemin)
    
productos = {
    1:['Manzanas', 9000.0, 65],
    2:['Limones', 2300.0, 15],
    3:['Peras', 2500.0, 38],
    4:['Arandanos', 9300.0, 55],
    5:['Tomates', 2100.0, 42],
    6:['Fresas', 4100.0, 33],
    7:['Helado', 4500.0, 41],
    8:['Galletas', 500.0, 833],
    9:['Chocolates', 3500.0, 806],
    10:['Jamon', 17000.0, 10], 
}

funcion=input()
if funcion == 'AGREGAR':
    tabla, falla = agregar(productos)
elif funcion == 'BORRAR':
    tabla, falla = borrar(productos)
elif funcion == 'ACTUALIZAR':
    tabla, falla = actualizar(productos)

maximo=mayor(productos)
minimo=menor(productos)
prom=promedio(productos)
valor_total=valor_inventario(productos)

if falla:
    print('ERROR')
else:
    print(maximo, minimo, prom, valor_total)