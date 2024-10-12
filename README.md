# ¡Casi se me olvida!
"¡Casi se me olvida!" es una aplicación donde antes de ir a tu supermercado favorito, podrás hacer tu lista de compras, al finalizar tú lista podrás visualizar el número de artículos a comprar. Además, podrás colocar el máximo de dinero que quisieras gastar para así poder tener un mejor registro de tus gastos. Cuando te encuentre en el supermercado, podrás registrar el costo de cada artículo para que así, la aplicación te muestre cuánto dinero estas gastando y si has llegado a tu máximo de dinero que estableciste anteriormente.
# Contexto
Una de las cosas que pasan muchas veces cuando vamos a un supermercado es que se nos olvidan los productos que queremos comprar e incluso gastamos más de lo que teníamos esperados, por lo que está aplicación podrá ayudarte a organizarte mejor. Tener una lista de compras te ayuda a tener una mejor organización en tu vida y te evita caer en ofertas que no necesites y de esta manera solo obtener lo que necesitas. Tener una lista de compra te ayuda a comprar cosas que probablemente ya tienes en casa o cosas que no necesitas y de esta manera podrás tener todas tus cosas sin necesitar de dar doble vuelta. Otro de los benneficios es que podrás organizar calamadamente tu comida semanal y de esta manera evitar el estrés de que tengas que recordar lo que tengas que comprar.
# Algoritmo
Algoritmo general.<br>
Entrada.<br>
1.Artículos a comprar.<br>
2.Monto total a gastar.<br>
3.Artículos comprados durante la tienda.<br>
4.Unidades de medida en kilogramos o libras.<br>
Proceso.<br>
1.Preguntarle al usuario cual es su nombre.<br>
2.Imprimir la bienvenida, con el nombre del usuario ingresado.<br>
3.Mientras sea verdadero.<br>
4.Desplegar el menú con las opciones para que el ususario escoga la lista de compras que desee crear.<br>
5.Si el usuario escoge la opción 1, abrir la función instructivo, donde se desplega todas las instrucciones.<br>
6.Si usuario escoge la opción 2, imprimir la bienvenida a la función y abrir la función lista_antes para crear la lista de compras.<br>
7.Si usuario escoge la opción 3, imprimir la lista creada en la función anterior.<br>
8.Si usuario escoge la opción 4, imprimir la bienvenida, preguntar al usuario el monto máximo a gastar y número de productos a comprar, llamar la función precio_productos con los parámetros pedidos.<br>
9.Si usuario escoge la opción 5, dar la bienvenida al usuario, preguntarle al usuario cual opción quiere hacer de libras a kilogramos o de kilogramos a libras, llamar la función de libras o kilogramos dependiendo de la función escogida.<br>
10.Si usuario es igual a 6, abrir la función pruebas.<br>
11. Si usuario es igual a 7, terminar con el programa.<br>
Salida:
1.Lista de compras.<br>
2.Nueva medida de conversión de unidades.<br>
Entrada:
1. La opción que ingrese el usuario.
Proceso:
1. Mientras True
2. Imprimir la función menú.
3. usuario es igual a lo que ingrese el usuario de las opciones del menú
4. si usuario es igual a uno:
5. imprimir bienvenido a la función crear listas
6. correr la función prueba.
7. si usuario es igual a dos:
5. imprimir en proceso de creación
6. si usuario es igual a tres:
5. imprimir bienvenido a tu lista de super en tiempo real
6. correr la función precio_productos.
7. si usuario es igual a cuatro:
5. imprimir bienvenido a la sección de convrsión de unidades
6. usuario_1 es igual a lo que ingrese el usuario kl o lk.
7. si usuario_1 es igual a kl
8. o=el valor numérico que ingrese el usuario
9. llamar la función conversión_k
10. imprimir resultado
11.  si usuario_1 es igual a lk
8. p=el valor numérico que ingrese el usuario
9. llamar la función conversión_l
10. imprimir resultado
12. si usuario es igual a 5
13. imprimir gracias por utilizar la aplicación casi se me olvida, vuelva pronto
14. break
15. Salida:
16. Mensaje dependiendo la función
       
Entrada:
1.Artículo.
2.Cantidad del artículo.
3.Monto máximo deseado a gastar.
Proceso:
1.Preguntar el monto máximo que la persona desea gastar.
2.Preguntar por el artículo que van a comprar.
3.Ir sumando todos los artículo que la persona quiera comprar.
4.Agregar una función donde el usuario pueda quitar el artículo ya comprado.
5.Mostrar el monto que desea gastar.
6.Al final preguntar el monto gastado y compararlo con el monto antes dicho.
Salida:
1.Lista de compras.
2.Monto gastado
3.Monto previsto.

