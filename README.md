# Fastfinger automátizado con Selenium

[Fast Fingers](https://10fastfingers.com)

**Fastfingers es una página web que sirve para mejorar la velocidad de escritura 
en el teclado. Ofrece una variedad de pruebas y juegos que pueden ayudar a 
los usuarios a mejorar su precisión y velocidad.

La página web tiene una interfaz simple y fácil de usar. Los usuarios pueden 
elegir entre una variedad de pruebas, incluyendo pruebas de velocidad, pruebas 
de precisión y pruebas de juegos. Las pruebas de velocidad miden la cantidad 
de palabras que un usuario puede escribir correctamente en un período de tiempo 
determinado. Las pruebas de precisión miden la cantidad de palabras que un 
usuario puede escribir correctamente sin errores. Las pruebas de juegos son 
una forma más divertida de practicar la mecanografía.**


## Instrucciones de uso

* python -m venv venv
* source/venv/bin/activate
* pip install -r requirements.txt
* python main.py



### Proceso de creación

** En el notbook se puede apreciar el proceso de creación del script, en él
se aprecia como la táctica de capturar toda la lista de palabras no funciona, 
el problema consistía en que Selenium solo reconoce las palabras visibles en la 
caja de texto. 
La primer solución a este inconveniente consitió en volver a ejecutar la capturara
de palabras una vez leída las que se mostraban en la caja, pero nuevamente surgió 
otro problema; Selenium capturaba las nuevas palabras y también las que ya se 
habían mostrado; intentar solucionar esto con un indice en la lista tampoco funcionaba 
ya que la cantidad de palabras variaba y la posición del índice también.
Solución tres, capturar palabra a palabra; esto hacía el script más lento pero funciona 
correcto **
