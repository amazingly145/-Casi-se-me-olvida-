"""La función prueba:
Podremos visualizar las funciones que se
puedan colocar números, de esta manera
podemos visualizar algunos ejemplos
de lo que saldría de la función"""
def pruebas():
    resultado=conversion_k(5)
    print(resultado)
    resultado=conversion_l(5)
    print(resultado)
"""La función lista antes:
es la función para crear la lista del súper, donde el usuario
podrá colocar sus artículos, haciendo su lista, posteriormente
se podrá agregar la función de listas para que se vayan guardando
los artículos y el usuario pueda ver de nuevo su lista creada,
podrá modificarla y ver las listas que había hecho anteriormente"""
def lista_antes (lista_compras):
    contador=0
    entrada_salida="S"
    while entrada_salida=="S":
        articulo=str(input("Ingresa el nombre del artículo: "))
        lista_compras.append((articulo))
        entrada_salida=str(input("Ingresa N si deseas cerrar la lista, ingresa S si deseas continuar de la lista: "))
        contador+=1
    return(lista_compras)
"""La función precio_productos:
es la función donde el usuario, ponga un valor máximo a gastar.
Cuando se encuentre en la tienda, podrá poner el artículo, el costo y
el número a llevar del mismo, al final podrá ver cuánto
se gastó y el número de asrtículos que lleva. También se guardará en otra lista,
se podrá ver los artículos, junto con su precio y el total a gastar
del usuario."""
def precios_productos(matriz,monto_max,numero_productos_total):
    resultado=0
    contador=0
    print("El monto máximo a gastar es de: "+"$"+str(monto_max))
    for a in range(numero_productos_total):
        producto=[]
        nombre_producto=input("Ingresa el nombre del artículo: ")
        numero_producto=int(input("¿Cuántos "+nombre_producto+ " vas a comprar? "))
        producto.append(numero_producto)
        producto.append(nombre_producto)
        precio_producto=int(input("Ingresa el precio del artículo: "))
        producto.append(precio_producto)
        matriz.append(producto)
        resultado+=(numero_producto*precio_producto)
        contador+=numero_producto
    print("---------------------Resumen de compras---------------------")
    print("número de artículos    "+"nombre productos   "+"precio de artículo   ")
    print("------------------------------------------------------------")
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
def conversion_k(n):
    kilogramo=n*2.20462
    return kilogramo
"""La función conversión_l:
está función muestra la conversión de unidades
de libra a kilogramo"""   
def conversion_l(n):
    libra=n*0.453592
    return libra
"""La función menú:
muestra las opciones que tiene el usuario
de escoger entre las opciones para la aplicación.""" 
def menu():
    print("Bienvenid@ a la aplicación ¡Casi se me olvida!")
    print("1. Crear mi lista")
    print("2. Visualzar lista")
    print("3. Ingresar productos y precios")
    print("4. Conversión de unidades de kilogramos a libras")
    print("5. Prueba")
    print("6. Salir")
"""La función main:
Dependiendo de la selección del usuario,
podrá hacerse las diferentes funciones ya establecidas.""" 
def main():
    lista_compras=[]
    matriz_principal=[]
    matriz=[]
    while True:
        menu()
        usuario=int(input("Favor de ingresar el número de acuerdo a la acción a realizar: "))
        if usuario==1:
            print("Bienvenido a la creación de tú lista de super")
            matriz_principal.append(lista_antes(lista_compras))
        if usuario==2:
            print("----Lista de compras----")
            print(matriz_principal)
        if usuario==3:
            print("Bienvenido a tú lista de super en tiempo real")
            monto_max=int(input("Ingresa el $monto$, máximo a gastar: "))
            numero_productos_total=int(input("Ingresa el número de artículos a comprar: "))
            precios_productos(matriz,monto_max,numero_productos_total)
        if usuario==4:
            print("Bienvenido a la sección de conversión de unidades")
            usuario_1=str(input("Si deseas convertir de kilogramos a libras ingresa kl, si es lo contrario ingresa lk: "))
            if usuario_1=="kl":
                o=int(input("Ingresa la unidad en kilogramos que deseas cambiar a libras: "))
                libras=conversion_k(o)
                print(str(o)+"kg es igual a: "+str(libras)+"lb")
            if usuario_1=="lk":
                p=int(input("Ingresa la unidad en libras que deseas cambiar a kilogramos: "))
                kilogramos=conversion_l(p)
                print(str(p)+"lb es igual a: "+str(kilogramos)+"kg")
        if usuario==5:
            pruebas()  
        if usuario==6:
            print("Gracias por utilizar ¡Casi se me olvida!")
            break      
main()
