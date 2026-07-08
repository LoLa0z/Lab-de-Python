Sistema de Gestión de Gimnasio

Trabajo Final Integrador - Algoritmos

Integrantes del grupo


Florentin Lautaro Nicolas
Caroprese Franchesco
Echenique Lautaro Daniel
Barrios Leonel


Comisión

k1.1

Link de video tutorial de Youtube:
https://youtu.be/r7_39qt78Ss

Descripción general del sistema

Este sistema permite administrar un gimnasio desde la consola. Fue desarrollado en Python
y permite gestionar socios, actividades, cuotas y asistencias.

El programa se maneja a través de un menú principal con las siguientes opciones:


Registrar un usuario: se cargan sus datos (DNI, nombre, edad, plan y actividad).
El sistema valida que el DNI no esté repetido, que los campos no queden vacíos y
que haya cupo disponible en la actividad elegida. Si el usuario es menor de 18 años,
se le aplica un 20% de descuento sobre el plan.
Control de asistencia diaria: se busca al usuario por DNI y se le suma una
asistencia si se confirma su identidad.
Control de cuotas y pagos: se consulta el estado de la cuota de un usuario
(Al día / Vencido) y permite actualizarlo si abona.
Estadísticas del gimnasio: muestra la cantidad de usuarios registrados,
asistencias del día y pagos mensuales/semanales realizados durante la ejecución.
Salir: cierra el sistema.


Los usuarios se guardan en un archivo (usuarios.dat) usando la librería pickle,
por lo que los datos de los socios quedan almacenados aunque se cierre el programa.
Las estadísticas de la opción 4, en cambio, se reinician cada vez que se vuelve a
ejecutar el programa, ya que se llevan en variables en memoria y no en el archivo.

Actividades y cupos disponibles

ActividadCupo máximoZumba20CrossFit25Yoga40Gym50

Planes disponibles


Mensual: $40.000
Semanal: $10.000
Menores de 18 años tienen un 20% de descuento sobre el valor del plan.


Instrucciones de ejecución


Tener instalado Python 3.
Clonar este repositorio:


   git clone [URL DEL REPOSITORIO]


Ubicarse en la carpeta del proyecto y ejecutar:


   python gym.py


Seguir las opciones que aparecen en el menú.


No se necesita instalar ninguna librería adicional, ya que solo se usan módulos
propios de Python (pickle y os).

Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó Claude IA.
como herramienta de apoyo.

¿Para qué se usó?


Para revisar el código en busca de errores de sintaxis y para entender cómo usar la librería pickle.



¿Cómo se usó?


Se le mostró el código ya escrito por el grupo y se le pidió que señale errores o partes a mejorar, sin que reescriba el sistema completo


Todos los integrantes del grupo revisaron y entendieron el código final antes de
la entrega, pudiendo explicar y justificar cada una de las decisiones tomadas.

Estructura del código


Usuario: clase que representa los datos de cada socio del gimnasio.
ActividadEstructura: clase que lleva el control de los cupos ocupados por actividad.
Funciones de validación: obtener_entero, obtener_texto_no_vacio, obtener_plan,
obtener_actividad, dni_ya_registrado.
Hay_Espacio: controla si hay cupo disponible en una actividad.
Bloque principal: menú con bucle while y estructura if/elif/else para manejar
cada opción.
