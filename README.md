<<<<<<< HEAD
<<<<<<< HEAD
# TP.REFLEXLABSistema de procesamiento y análisis de datos de una tarea Go/No-Go.Lee los registros de cada participante, los valida y calcula métricasde desempeño como tiempo de reacción y tasa de error.Integrantes: Bujan Alfonso, Lorenzetti Miranda, Nuñez Matilde### ### **Errores y Validaciones:***Error:* parsear\_linea (carga\_datos.py): una línea del CSV tiene menos columnas de las esperadas, o un campo no es del tipo correcto (por ejemplo, texto donde se espera un número)Manejo de Error:si la línea es inválida, la función retorna “None” y esa línea se descarta*Error:* validar\_registro (validacion\_datos.py): un registro puede tener el tiempo de reacción negativo, un ID inválido, o un resultado que no sea "correcto" o "incorrecto"Manejo de Error: la función retorna “False”  para ese registro. El programa lo cuenta como inválido pero sigue ejecutándose con el resto*Error:* calcular\_tiempo\_reaccion\_promedio (metricas.py): que no haya ningún tiempo de reacción válido (lista vacía o todos negativos)Manejo de Error: la función retorna “0” directamente para evitar una división por cero*Error:* calcular\_tasa\_error (metricas.py): que la lista de datos esté vacíaManejo de Error: la función retorna “0.0” directamente si no hay datos## **Aplicación de programación orientada a objetos*** Basándonos en la función **parsear\_linea**, que es la que representa cada linea del archivo (luego de leerlo y pasarlo a un diccionario):La podriamos dividir en dos clases: una que sea la que lee el archivo y la otra que sea la que represente cada registro.Clase LecturaArchivo: se encarga de procesar cada linea del archivo y transformarla en registros.Atributos:&#x09;- lineas&#x09;- registros Metodos: &#x09;- parsear\_linea()--> transforma cada linea en un registroClase Registro: representa una linea del archivo que ya esta convertida en datosAtributos:&#x09;- id\_participante&#x09;- trial&#x09;- estimulo&#x09;- t\_inicio&#x09;- respuesta&#x09;- tiempo\_reaccion&#x09;- resultado\_respuesta&#x09;- condicionMetodos:&#x09;- parsear\_linea() --> se pasa de una linea (que recorre y saca del archivo cargado) a un registro (y asi va haciendo con todos).\-----------------------------------------------------------------------* Basandonos en la funcion **filtrar\_por\_participantes**, la cual se encarga de seleccionar el registro de un participante especifico (el que se solicite):Se podría hacer una clase que maneje esos registros.Clase Manejo: se encarga de trabajar con los registros y aplicar el filtrado por participante. Atributos:&#x09;- registrosMétodo:&#x09;-filtrar\_por\_participantes() --> funcion que estamos usando, que como explicamos antes nos permite obtener los registros de un participante.
=======
=======
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
# TP.REFLEXLAB

Sistema de procesamiento y análisis de datos de una tarea Go/No-Go.
Lee los registros de cada participante, los valida y calcula métricas
de desempeño como tiempo de reacción y tasa de error.

Integrantes: Bujan Alfonso, Lorenzetti Miranda, Nuñez Matilde





Errores y Validaciones: 



Error: parsear\_linea (carga\_datos.py): una línea del CSV tiene menos columnas de las esperadas, o un campo no es del tipo correcto (por ejemplo, texto donde se espera un número)

Manejo de Error:si la línea es inválida, la función retorna “None” y esa línea se descarta



Error: validar\_registro (validacion\_datos.py): un registro puede tener el tiempo de reacción negativo, un ID inválido, o un resultado que no sea "correcto" o "incorrecto"

Manejo de Error: la función retorna “False”  para ese registro. El programa lo cuenta como inválido pero sigue ejecutándose con el resto



Error: calcular\_tiempo\_reaccion\_promedio (metricas.py): que no haya ningún tiempo de reacción válido (lista vacía o todos negativos)

Manejo de Error: la función retorna “0” directamente para evitar una división por cero



Error: calcular\_tasa\_error (metricas.py): que la lista de datos esté vacía

Manejo de Error: la función retorna “0.0” directamente si no hay datos

## **Aplicación de programación orientada a objetos**





* Basándonos en la función **parsear\_linea**, que es la que representa cada linea del archivo (luego de leerlo y pasarlo a un diccionario):



La podriamos dividir en dos clases: una que sea la que lee el archivo y la otra que sea la que represente cada registro.



Clase LecturaArchivo: se encarga de procesar cada linea del archivo y transformarla en registros.



Atributos:

&#x09;- lineas

&#x09;- registros 

Metodos: 

&#x09;- parsear\_linea()--> transforma cada linea en un registro



Clase Registro: representa una linea del archivo que ya esta convertida en datos



Atributos:

&#x09;- id\_participante

&#x09;- trial

&#x09;- estimulo

&#x09;- t\_inicio

&#x09;- respuesta

&#x09;- tiempo\_reaccion

&#x09;- resultado\_respuesta

&#x09;- condicion



Metodos:

&#x09;- parsear\_linea() --> se pasa de una linea (que recorre y saca del archivo cargado) a un registro (y asi va haciendo con todos).









\-----------------------------------------------------------------------







* Basandonos en la funcion **filtrar\_por\_participantes**, la cual se encarga de seleccionar el registro de un participante especifico (el que se solicite):



Se podría hacer una clase que maneje esos registros.



Clase Manejo: se encarga de trabajar con los registros y aplicar el filtrado por participante. 



Atributos:

&#x09;- registros



Método:

&#x09;-filtrar\_por\_participantes() --> funcion que estamos usando, que como explicamos antes nos permite obtener los registros de un participante.


-----------------------------------------------------------------------------------------------------------------------

La funcion_habitos.py se podria implementar con un objeto.

clase habitos: se encarga de trabajar con los habitos

atributos:

&#x09;-lista_habitos

Métodos:

&#x09;-registrar() --> funcion que le pide al usuario que cargue los habitos

&#x09;-analizar()--> funcion que indica cuantos actividades se repiten








<<<<<<< HEAD
<<<<<<< Updated upstream
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
=======
>>>>>>> b0588a1420d2948bdde92bd7f7dce1927a6f0f9c
>>>>>>> Stashed changes
=======
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
