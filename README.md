# ¡Casi se me olvida!
"¡Casi se me olvida!" es una aplicación donde antes de ir a tu supermercado favorito, podrás hacer tu lista de compras, al finalizar tú lista podrás visualizar el número de artículos a comprar. Además, podrás colocar el máximo de dinero que quisieras gastar para así poder tener un mejor registro de tus gastos. Cuando te encuentre en el supermercado, podrás registrar el costo de cada artículo para que así, la aplicación te muestre cuánto dinero estas gastando y si has llegado a tu máximo de dinero que estableciste anteriormente. De esta manera podrá aprender a organizar tú dinero y evitar gastar más de lo que se deseaba al principio. Antes de utilizar la aplicación, se recomienda que el usuario revise su casa para observar, las cosas que se necesitan comprar y la pueda colocar en la aplicación.<br>
# Contexto
Una de las cosas que pasan muchas veces cuando vamos a un supermercado es que se nos olvidan los productos que queremos comprar e incluso gastamos más de lo que teníamos esperados, por lo que está aplicación podrá ayudarte a organizarte mejor. Tener una lista de compras te ayuda a tener una mejor organización en tu vida y te evita caer en ofertas que no necesites y de esta manera solo obtener lo que realmente necesitas en tu vida. Tener una lista de compra te ayuda a comprar cosas que probablemente ya tienes en casa o cosas que no necesitas y de esta manera podrás tener todas tus cosas sin necesitar de dar doble vuelta. Otro de los beneficios es que podrás organizar calmadamente tu comida semanal y de esta manera evitar el estrés de que tengas que recordar lo que tengas que comprar. Teniendo en cuenta las cosas o comida a comprar, se evita desperdiciar comida y tenerla planificada para la semana, de esta manera tendrás toda tu casa en orden.<br>
# Instrucciones de uso 
1. Instalar la aplicación de python o algún procesador de código.<br>
2.Descargar el archivo en python así como el formato txt.<br>
2. Correr el código.<br>
3. De acuerdo a la acción que se desea relizar ingresar el número que se quiera hacer del menú.<br>
4. Seguir las insrtrucciones de lo que se pide para correr la aplicación.<br>
# Algoritmo
### Algoritmo general.<br>
### Entrada.<br>
1. Artículos a comprar.<br>
2. Monto total a gastar.<br>
3. Artículos comprados durante la tienda.<br>
4. Unidades de medida en kilogramos o libras.<br>
### Proceso.<br>
1. Preguntarle al usuario cual es su nombre.<br>
2. Imprimir la bienvenida, con el nombre del usuario ingresado.<br>
3. Mientras sea verdadero.<br>
4. Desplegar el menú con las opciones para que el ususario escoga la lista de compras que desee crear.<br>
5. Si el usuario escoge la opción 1, abrir la función instructivo, donde se desplega todas las instrucciones.<br>
6. Si usuario escoge la opción 2, imprimir la bienvenida a la función y abrir la función lista_antes para crear la lista de compras.<br>
7. Si usuario escoge la opción 3, imprimir la lista creada en la función anterior.<br>
8. Si usuario escoge la opción 4, imprimir la bienvenida, preguntar al usuario el monto máximo a gastar y número de productos a comprar, llamar la función precio_productos con los parámetros pedidos.<br>
9. Si usuario escoge la opción 5, dar la bienvenida al usuario, preguntarle al usuario cual opción quiere hacer de libras a kilogramos o de kilogramos a libras, llamar la función de libras o kilogramos dependiendo de la función escogida.<br>
10. Si usuario es igual a 6, abrir la función pruebas.<br>
11. Si usuario es igual a 7, terminar con el programa.<br>
### Salida.<br>
1. Lista de compras.<br>
2. Nueva medida de conversión de unidades.<br>
