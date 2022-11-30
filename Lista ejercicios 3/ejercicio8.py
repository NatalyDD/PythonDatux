texto = "Python es uno de los lenguajes de programación dinámicos más populares\
que existen entre los que se encuentran Java, Javascript, Go y C.\
Aunque es considerado a menudo como un lenguaje 'scripting', es realmente un\
lenguaje de propósito general. En la actualidad, Python es usado para todo,\
desde simples 'scripts', hasta grandes servidores web que proveen servicio\
ininterrumpido 24x7. Es utilizado para la programación de interfaces gráficas\
y bases de datos, programación web tanto en el cliente como en el servidor\
(véase Django o Flask) y 'testing' de aplicaciones"

def busca ():
    import re
    busqueda = re.search("python",texto.lower())
    if busqueda:
        print("La palabra buscada existe en el texto")
    else:
        print("No se encontraron coincidencias en el texto con la palabra ingresada")



