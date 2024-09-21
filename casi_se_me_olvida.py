"""La función prueba:
es la función para crear la lista del súper, donde el usuario
podrá colocar sus artículos, haciendo su lista, posteriormente
se podrá agregar la función de listas para que se vayan guardando
los artículos y el usuario pueda ver de nuevo su lista creada,
podrá modificarla y ver las listas que había hecho anteriormente"""
def lista_antes ():
    contador=0
    entrada_salida=str(input("Ingresa N si deseas cerrar la lista, ingresa S si deseas continuar de la lista: "))
    while entrada_salida=="S":
        lista_compras=str(input("Ingresa el nombre del artículo"))
        entrada_salida=str(input("Ingresa N si deseas cerrar la lista, ingresa S si deseas continuar de la lista"))
        contador+=1
    print("Ingresa N si deseas regresar al menú principal")
"""La función precio_productos:
es la función donde el usuario, ponga un valor máximo a gastar.
Cuando se encuentre en la tienda, podrá poner el artículo, el costo y
el número a llevar del mismo, al final podrá ver cuánto
se gastó y el número de asrtículos que lleva. También se guardará en otra lista,
se podrá ver los artículos, junto con su precio y el total a gastar
del usuario."""
def precios_productos():
    monto_max=int(input("Ingresa el $monto$, máximo a gastar: "))
    numero_productos_total=int(input("Ingresa el número de artículos a comprar: "))
    entrada_salida="S"
    resultado=0
    contador=0
    print("El monto máximo a gastar es de: "+"$"+str(monto_max))
    for x in range (numero_productos_total):
        nombre_productos=str(input("Ingresa el nombre del artículo: "))
        numero_productos=int(input("¿Cuántos "+str(nombre_productos)+" vas a comprar?"))
        precio_productos=int(input("Ingresa el precio del artículo: "))
        entrada_salida=str(input("Ingresa N si deseas ver el resumen, S si deseas continuar con la lista: "))
        resultado+=(numero_productos*precio_productos)
        contador+=numero_productos
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
    print("5. Salir")
"""La función main:
Dependiendo de la selección del usuario,
podrá hacerse las diferentes funciones ya establecidas.""" 
def main():
    while True:
        menu()
        usuario=int(input("Favor de ingresar el número de acuerdo a la acción a realizar: "))
        if usuario==1:
            print("Bienvenido a la creación de tú lista de super")
            lista_antes()
        if usuario==2:
            print("En proceso de creación con listas, muchas de las funciones, aún le falta arreglos")
        if usuario==3:
            print("Bienvenido a tú lista de super en tiempo real")
            precios_productos()
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
            print("Gracias por utilizar ¡Casi se me olvida!")
            break        
main()
"""def pruebas():
    resultado=conversion_k(5)
    print(resultado)
    resultado=conversion_l(5)
    print(resultado)
pruebas()"""