<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# TP.REFLEXLAB

Sistema de procesamiento y análisis de datos de una tarea Go/No-Go.
Lee los registros de cada participante, los valida y calcula métricas
de desempeño como tiempo de reacción y tasa de error.

Integrantes: Bujan Alfonso, Lorenzetti Miranda, Nuñez Matilde



### 

### **Errores y Validaciones:**



*Error:* parsear\_linea (carga\_datos.py): una línea del CSV tiene menos columnas de las esperadas, o un campo no es del tipo correcto (por ejemplo, texto donde se espera un número)

Manejo de Error:si la línea es inválida, la función retorna “None” y esa línea se descarta



*Error:* validar\_registro (validacion\_datos.py): un registro puede tener el tiempo de reacción negativo, un ID inválido, o un resultado que no sea "correcto" o "incorrecto"

Manejo de Error: la función retorna “False”  para ese registro. El programa lo cuenta como inválido pero sigue ejecutándose con el resto



*Error:* calcular\_tiempo\_reaccion\_promedio (metricas.py): que no haya ningún tiempo de reacción válido (lista vacía o todos negativos)

Manejo de Error: la función retorna “0” directamente para evitar una división por cero



*Error:* calcular\_tasa\_error (metricas.py): que la lista de datos esté vacía

Manejo de Error: la función retorna “0.0” directamente si no hay datos









## **Aplicación de programación orientada a objetos**





* Basándonos en la función **parsear\_linea**, que es la que representa cada linea del archivo (luego de leerlo y pasarlo a un diccionario):



La podriamos dividir en dos clases: una que sea la que lee el archivo y la otra que sea la que represente cada registro.



Clase LecturaArchivo: se encarga de procesar cada linea del archivo y transformarla en registros.



Atributos:

&#x09;- lineas

&#x09;- registros 

Metodos: 

parsear\_linea()--> transforma cada linea en un registro



Clase Registro: representa una linea del archivo que ya esta convertida en datos



Atributos:
id\_participante
 trial
estimulo
t\_inicio
respuesta
tiempo\_reacción
resultado\_respuesta
condicion



Metodos:

parsear\_linea() --> se pasa de una linea (que recorre y saca del archivo cargado) a un registro (y asi va haciendo con todos).









\-----------------------------------------------------------------------







* Basandonos en la funcion **filtrar\_por\_participantes**, la cual se encarga de seleccionar el registro de un participante especifico (el que se solicite):



Se podría hacer una clase que maneje esos registros.



Clase Manejo: se encarga de trabajar con los registros y aplicar el filtrado por participante. 



Atributos:

&#x09;- registros



Método:

&#x09;-filtrar\_por\_participantes() --> funcion que estamos usando, que como explicamos antes nos permite obtener los registros de un participante.






























=======
=======
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
=======
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
=======
>>>>>>> 12e4338e0685533ac98978509ce10b631bfbd183
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


## **Aplicación de PANDAS**

* Basándonos en la función **parsear\_linea**, que es la que representa cada linea del archivo (luego de leerlo y pasarlo a un diccionario):

Podríamos usar la librería Pandas dentro de la clase LecturaArchivo porque el archivo tiene datos organizados en filas y columnas. Usaríamos un objeto de tipo DataFrame porque en el archivo cada fila representa un registro y cada columna representa un atributo. 

Dentro de la función leer_archivo utilizariamos pd.read_csv() porque el archivo se encuentra en formato csv. El resultado se almacenaria en un DataFrame y ahi se podria acceder facilmente a los datos por las filas y las columnas. 
Cada fila del DataFrame representaria un registro como: 
- id_participante
- trial
- estimulo
- t_inicio
- respuesta
- tiempo_reaccion
- resultado_respuesta 
- condicion

Para el acceso a los datos se podrían utilizar series para trabajar con columnas individuales. 


* Basandonos en la funcion **filtrar\_por\_participantes**, la cual se encarga de seleccionar el registro de un participante especifico (el que se solicite):

Se podría aplicar un DataFrame para reemplazar los registros como lista y que ahora los registros sean el DataFrame. 

En el método filtrar_por_participantes se podría usar filtrado directo de pandas en vez de recorrer con un for, se haría filtrado por columna. 
Resultado: se devolvería otro DataFrame filtrado. 

Ademas se podrían usar series, mas que nada para comparar la columna de id_participantes. Es para generar la condición de filtrado. 


* Basandonos en la funcion_habitos.py, que es la que se encarga de registrar los habitos diarios de una persona:
  Se podria implementar la lbireria Pandas para organizar los habitos ingresados por el usuario en un estructura de tipo DataFrame.
  La funcion lo que hace es almacenar cada habito dentro de una lista llamada lista_habitos, despues gracias al DataFrame se podrian transformar esos datos en una tabla, donde cada fila representa un habito registrado por el usuario. El resultado se almacaneria como DataFrame y se podria acceder asi a los habitos registrados en filas y en columnas.
  Importante entender que la columna "habitos"puede contener todos los habitos ingresados por el usuario, y asi de esa forma permite analizar mejor los datos o buscar habitos especificos o incluso contar las actividades que esten repetidas.
  
* Basándonos en la función validar_datos, la cual se encarga de leer el archivo CSV línea por línea y descartar las líneas inválidas:
  Se podría aplicar un DataFrame para reemplazar la apertura manual del archivo con open() y el recorrido con while.
  En lugar de eso, se usaría pd.read_csv() para cargar todos los datos directamente en un DataFrame.


--------------------------------------------------------------------
## Guía de Ejecución de la Interfaz Web

Este proyecto incluye una interfaz web desarrollada con Streamlit para la visualización y análisis de los datos del laboratorio.

### Instalación de dependencias

Ejecutar en la terminal:

pip install -r requirements.txt

### Ejecución de la interfaz

Desde la raíz del repositorio ejecutar:

streamlit run app.py

### Funcionamiento

La interfaz permite:

- Cargar archivos CSV mediante un componente interactivo.
- Validar registros automáticamente y mostrar errores. 
- Visualizar una vista previa de los datos procesados.
- Mostrar indicadores clave de desempeño (KPIs).
- Filtrar información por participante.
- Visualizar gráficos generados a partir de los datos.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< Updated upstream
