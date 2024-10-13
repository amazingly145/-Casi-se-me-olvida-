"""La función prueba:
Podremos visualizar las funciones que se
puedan colocar números, de esta manera
podemos visualizar algunos ejemplos
de lo que saldría de la función"""
"""Caso de prueba
Entrada=
Salida=
11.0231
2.26796
1. Bienvenido a ¡casi se me olvida! Para poder utilizar la aplicación favor de leer las siguientes instrucciones:
2. Para poder ver como se utiliza 
3. Al ingresar a la aplicación podrá visualizar la sección del menú, del cual podrá hacer la acción que desea realizar.
4. Si desea crear una lista de compras, antes de dirigirse hacia su supermermercado favorito: favor de ingresar el comando "1".
5. Si desea visualizar la lista creada en el comando 1, favor de ingresar el comando 2, el cual le desplegará su lista completa.
6. Si se encuentra a su supermercado y desea tener una contabilidad de lo que está comprando, así como su precio, y el monto máximo a gastar, favor de ingresar el comando 3.
7. Si se encuentra a su supermercado y desea convertir sus unidades de libras a kilogramos o viseversa, favr de ingresar el comando 4.
8. Finalmente si desea salir de la aplicación, favor de ingresar el comando 6.
hola"""
def pruebas():
    resultado=conversion_k(5)
    print(resultado)
    resultado=conversion_l(5)
    print(resultado)
    instructivo()
    cadena="hola"
    imprimir_cadena(cadena)
"""La función imprimir_cadena:
Imprime alguna palabra a partir del número de caractéres de la misma"""
"""Caso de prueba función imprimir_cadena
Entrada=Bienvenido a la creación de tú lista de super \n
Salida=Bienvenido a la creación de tú lista de super"""
def imprimir_cadena(cadena):
    for i in range (0,len(cadena)):
        print(cadena[i], end='')
"""Caso de prueba función imprimir_cadena
Entrada=casa,ropa, vaso
Salida=[casa,ropa,vaso]"""
"""La función lista antes:
es la función para crear la lista del súper, donde el usuario
podrá colocar sus artículos, haciendo su lista, posteriormente
se podrá agregar la función de listas para que se vayan guardando
los artículos y el usuario pueda ver de nuevo su lista creada,
podrá agregarle elementos y visualizar la lista."""
def lista_antes ():
    contador=0
    lista_compras=[]
    entrada_salida="S"
    while entrada_salida=="S":
        articulo=str(input("Ingresa el nombre del artículo: ")).lower()
        lista_compras.append((articulo))
        entrada_salida=str(input("Ingresa N si deseas cerrar la lista, ingresa S si deseas continuar de la lista: "))
        contador+=1
    return(lista_compras)
"""La función instructivo:
Muestra las instrucciones de la aplicación, 
para que el usuario pueda utilizarla."""
"""Caso de prueba función instructivo
Entrada=archivo con las instrucciones
Salida=Instructivo ¡Casi se me olvida!
1. Bienvenido a ¡casi se me olvida! Para poder utilizar la aplicación favor de leer las siguientes instrucciones:
2. Para poder ver como se utiliza 
3. Al ingresar a la aplicación podrá visualizar la sección del menú, del cual podrá hacer la acción que desea realizar.
4. Si desea crear una lista de compras, antes de dirigirse hacia su supermermercado favorito: favor de ingresar el comando "1".
5. Si desea visualizar la lista creada en el comando 1, favor de ingresar el comando 2, el cual le desplegará su lista completa.
6. Si se encuentra a su supermercado y desea tener una contabilidad de lo que está comprando, así como su precio, y el monto máximo a gastar, favor de ingresar el comando 3.
7. Si se encuentra a su supermercado y desea convertir sus unidades de libras a kilogramos o viseversa, favr de ingresar el comando 4.
8. Finalmente si desea salir de la aplicación, favor de ingresar el comando 6."""
def instructivo():
    file=open("instructivo_casi_se_me_olvida.txt", "r")
    contenido=file.read()
    print(contenido)
"""La función precio_productos:
es la función donde el usuario, ponga un valor máximo a gastar.
Cuando se encuentre en la tienda, podrá poner el artículo, el costo y
el número a llevar del mismo, al final podrá ver cuánto
se gastó y el número de asrtículos que lleva. También se guardará en otra lista,
se podrá ver los artículos, junto con su precio y el total a gastar
del usuario."""
"""Caso de prueba función precio productos
Entrada=monto máximo a gastar, matriz, numero de productos total
Salida=Resumen de compras, con los montos gastados y comparación"""
def precios_productos(matriz,monto_max,numero_productos_total):
    resultado=0
    contador=0
    print("El monto máximo a gastar es de: "+"$"+str(monto_max))
    for a in range(numero_productos_total):
        producto=[]
        nombre_producto=input("Ingresa el nombre del artículo: ")
        numero_producto=int(input("¿Cuántos "+nombre_producto+ " vas a comprar? "))
        producto.append(numero_producto)
        producto.append(nombre_producto.lower())
        precio_producto=int(input("Ingresa el precio del artículo: "))
        producto.append(precio_producto)
        matriz.append(producto)
        resultado+=(numero_producto*precio_producto)
        contador+=numero_producto
    print("---------------------Resumen de compras---------------------")
    print("número de artículos    "+"nombre productos   "+"precio de artículo   ")
    cadena="------------------------------------------------------------\n"
    imprimir_cadena(cadena)
    for b in range(len(matriz)):
        for c in range(len(matriz[b])):
            print("      ",matriz[b][c],"           ", end='')
        print()
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
    if monto_max<=resultado:
        print("Te has pasado con el monto inicial de tú lista")
    else:
        print("¡Felicidades tú compra se ha mantuvido con el máximo a gastar!")
    print("Tú monto máximo era de: "+str(monto_max))
    print("La diferencia es de: "+str(resultado-monto_max))
    print("Tú monto a gastar es de: "+str(resultado))
    print("Llevas un total de: "+str(contador)+" artículos")
"""La función conversión_k:
está función muestra la conversión de unidades
de kilogramo a libra"""
"""Caso de prueba conversión k(n)
Entrada=kl, 3
Salida=6.613lb"""
def conversion_k(n):
    kilogramo=n*2.20462
    return kilogramo
"""La función conversión_l:
está función muestra la conversión de unidades
de libra a kilogramo"""
"""Caso de prueba conversión k(n)
Entrada=lk, 3
Salida=1.36077kg"""
def conversion_l(n):
    libra=n*0.453592
    return libra
"""La función imprimeMatriz(matriz):
está función imprime la matriz de la lista de compras"""
"""Caso de prueba imprimeMatriz(matriz)
Entrada=matriz_principal: planta, vaso
Salida=planta vaso"""
def imprimeMatriz(matriz):
    for c in range(0,len(matriz)):
        for d in range(0,len(matriz[c])):
            print(matriz[c][d],end=' ')
        print()
"""La función menú:
muestra las opciones que tiene el usuario
de escoger entre las opciones para la aplicación."""
"""Caso de prueba menu()
Entrada=
Salida=Menú de usuario
1. Instructivo
2. Crear/agregar elementos a mi lista
3. Visualzar lista
4. Ingresar productos y precios
5. Conversión de unidades de peso
6. Prueba
7. Salir"""
def menu():
    print("Menú de usuario")
    print("1. Instructivo")
    print("2. Crear/agregar elementos a mi lista")
    print("3. Visualzar lista")
    print("4. Ingresar productos y precios")
    print("5. Conversión de unidades de peso")
    print("6. Prueba")
    print("7. Salir")
"""La función main:
Dependiendo de la selección del usuario,
podrá hacerse las diferentes funciones ya establecidas."""
"""Caso de prueba main()
Entrada=
Salida=
Mensaje"""
def main():
    nombre=str(input("¿Cuál es tu nombre?\n"))
    print("Bienvenid@ " +nombre+ " a la aplicación ¡Casi se me olvida!")
    matriz_principal=[]
    matriz=[]
    while True:
        menu()
        usuario=int(input("Favor de ingresar el número de acuerdo a la acción a realizar: "))
        if usuario==1:
            instructivo()
        if usuario==2:
            cadena="Bienvenido a la creación de tú lista de super \n"
            imprimir_cadena(cadena)
            lista_compras=lista_antes()
            matriz_principal.append(lista_compras)
        if usuario==3:
            cadena="Tú lista de compras es la siguiente:\n"
            imprimir_cadena(cadena)
            imprimeMatriz(matriz_principal)
            #print(lista_compras)
        if usuario==4:
            cadena="Bienvenido a tú lista de super en tiempo real\n"
            imprimir_cadena(cadena)
            monto_max=int(input("Ingresa el $monto$, máximo a gastar: "))
            numero_productos_total=int(input("Ingresa el número de artículos a comprar: "))
            precios_productos(matriz,monto_max,numero_productos_total)
        if usuario==5:
            cadena="Bienvenido a la sección de conversión de unidades\n"
            imprimir_cadena(cadena)
            usuario_1=str(input("Si deseas convertir de kilogramos a libras ingresa kl, si es lo contrario ingresa lk: "))
            if usuario_1=="kl":
                o=int(input("Ingresa la unidad en kilogramos que deseas cambiar a libras: "))
                libras=conversion_k(o)
                print(str(o)+"kg es igual a: "+str(libras)+"lb")
            if usuario_1=="lk":
                p=int(input("Ingresa la unidad en libras que deseas cambiar a kilogramos: "))
                kilogramos=conversion_l(p)
                print(str(p)+"lb es igual a: "+str(kilogramos)+"kg")
        if usuario==6:
            pruebas()
        if usuario==7:
            print("Gracias "+nombre+ " por utilizar ¡Casi se me olvida!")
            break      
main()
