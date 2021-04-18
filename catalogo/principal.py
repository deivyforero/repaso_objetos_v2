from flask import Flask, render_template
from producto import *
from cuerpos import *
from random import choice


app = Flask(__name__)

@app.route('/')
def principal():

   # prod =Producto()

    #armaorcos= ArmaOrcos()
    #escudohumanos = EscudoHumanos()
    #escudoorcos = EscudoOrcos()
    #monturahumanos = MonturaHumanos()
   # monturaorcos= MonturaOrcos()

 #   cuerpohumano = CuerpoHumano()
    armahumano= ArmaHumanos("static/imagenes/humanos/arma.png", "Humanos", "arma del humano")
    armaorco = ArmaOrcos( "static/imagenes/orcos/arma.png", "Orcos", "arma del orco")
    escudohumano = EscudoHumanos("static/imagenes/humanos/escudo.png", 'Humanos', "Escudo del humano")
    escudoorco =EscudoOrcos ("static/imagenes/orcos/escudo.png", 'Orcos', "Escudo del Orco")
    monturahumano = MonturaHumanos("static/imagenes/humanos/montura.jpg", 'Humanos', "Montura del humano")
    monturaorco =MonturaOrcos ("static/imagenes/orcos/montura.jpg", 'Orcos', "Montura del Orco")

    concretedecorarhumano = ConcreteDecorarProducto("static/imagenes/humanos/Cuerpo.jpg", "Humanos", "arma del humano", "pequeña", "grande", "fuertes", "largas", "static/imagenes/humanos/arma.png", "static/imagenes/humanos/escudo.png" , "static/imagenes/humanos/montura.jpg")
    concretedecorarorco= ConcreteDecorarProducto("static/imagenes/orcos/Cuerpo.jpg", "Orcos", "arma del Orco", "Grande", "grande", "debiles", "cortas",  "static/imagenes/orcos/arma.png", "static/imagenes/orcos/escudo.png" , "static/imagenes/orcos/montura.jpg")


   # decorarproducto= DecorarProducto("static/imagenes/humanos/arma.png", "Humanos", "arma del humano" )

 
    #cuerpoorco = CuerpoOrco()


    
    #MyComponet=ConcreteDecorator(Decorator())
  #  MyComponet=ConcreteDecorator()
    productos = []
    productos.append(armahumano)
    productos.append(armaorco)
    productos.append(escudohumano)
    productos.append(escudoorco)
    productos.append(monturahumano)
    productos.append(monturaorco)

    productosdecorados = []
    productosdecorados.append(concretedecorarhumano)
    productosdecorados.append(concretedecorarorco)

    #productos.append(MyComponet)
    
   # productos.append(cuerpoorco)

   # productos.append(armahumano)

    #productos.append(escudohumanos)
   # productos.append(escudoorcos)
   # productos.append(monturahumanos)
   # productos.append(monturaorcos)
    
    return render_template("productos.html", productos = productos, productosdecorados = productosdecorados)

if __name__ == '__main__':
    app.run(debug=True)