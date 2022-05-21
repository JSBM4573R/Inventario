# Inventario

Reto 5 Python - Desarrollo de un programa que realiza una gestion tipo Crud a un inventario de una tienda de productos.

Descripcion del Reto:
### Entrada
Cada uno de los casos de prueba estara compuesto por dos lineas. La primera linea estara formada por una cadena de texto que identifica la operacion a realizar. En este caso las operaciones validas son:ACTUALIZAR, BORRAR y AGREGAR.<br>
La segunda linea estara formada por 4 valores (Codigo, nombre, precio, inventario) que representan el producto sobre el cual se quiere realizar la operacion. En el caso de la operacion ACTUALIZAR la segunad linea debe contener el Codigo y los nuevos valores del producto.En el caso de la operacion de BORRAR se deben especificar todos los atributos del caso de producto a eliminar.
<br>
### Salida
La salida estara representada por una unica linea formada por cuatro valores: Nombre del producto con el precio mayor, nombre del producto con el precio menor, el promedio de los precios del inventario y el valor total del inventario.
<br>
### Casos de prueba
Entrada:<br>
AGREGAR <br> 11 Melón 70 13<br>
BORRAR <br> 10 Jamón 15000 10<br>
ACTUALIZAR <br> 7 Helado 65000 11<br>
BORRAR <br> 14 Maíz 4500 12<br>
<br>
Salida:<br>
Jamón Melón 4897.3 8857410.0<br>
Galletas Arandanos 4088.9 8686500.0<br>
Helado Galletas 11430.0 9387000.0<br>
ERROR<br>
