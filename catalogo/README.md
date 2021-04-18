# Readme Catalogos	
Deivy Alexander Forero Castañeda
Codigo 20211099027

Jorge Armando Sanchez Garcia
Codigo 20211099037

Se realiza la adaptación del ejercicio utilizando el patrón de diseño Decorate que consiste en 
Añadir en tiempo de ejecución nuevas funcionalidades a un objeto (wrapper), para tal fin utilizamos 
la siguiente metodologia

1. Hemos trabajado solo con las clases productos y principal
2. Hemos decidido decorar los cuerpos de los humanos y los orcos con los escudos, armas y monturas  correspondientes a cada uno
3. En una tabla hemos presentado los productos y en la siguiente tabla 2 filas una de humanos y otra de orcos con sus respectivas decoraciones
4. en la clase producto hemos redefinido las clases 
ArmaHumanos(), ArmaOrcos(), EscudoHumanos(), EscudoOrcos(), MonturaOrcos(), MonturaHumanos() (herencias de la clase producto para que reciban parametros de "imagen, grupo y descripción" 
5. se define una clase DecorarProducto que servira para decorar los productos y contiene los mismos parametros de las clases nombradas en el punto 4
6. se define la clase ConcreteDecorarProducto la cual hereda de la clase DecorarProducto, la cual servira para construir el objeto decorado (productos vs cuerpos), se define un constructor que permitirá recibir los atributos de la clase DecorarProducto que son  "imagen, grupo y descripción" 
7. en el programa principal se invoca la clase ConcreteDecorarProducto y recibe los parametros necesarios para 
construir el orco y el humano con las respectivas decoraciones
8. se ajusta la plantilla productos.html para que reciba el objeto con las decoraciones
