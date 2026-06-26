import pickle
import os

# ==========================================
# REPRODUCCIÓN DE LAS ESTRUCTURAS (REGISTROS)
# ==========================================
class Usuario:
    def __init__(self):
        self.ID = 0
        self.Nombre = ""
        self.Plan = ""  # "Semanal" o "Mensual"
        self.Edad = 0
        self.Actividades = ""  # "Zumba", "CrossFit", "Yoga", "Gym"
        self.Asist = 0
        self.Estado_Cuota = ""

class ActividadEstructura:
    def __init__(self):
        self.Cupo_Zumba = 0
        self.Cupo_CrossFit = 0
        self.Cupo_Yoga = 0
        self.Cupo_Gym = 0

# Instancia global para controlar los cupos en memoria
Actividad = ActividadEstructura()

# ==========================================
# FUNCIÓN DE CONTROL DE ESPACIO
# ==========================================
def Hay_Espacio(x: str) -> bool:
    global Actividad
    if x == "Zumba":
        if Actividad.Cupo_Zumba < 20:
            Actividad.Cupo_Zumba += 1
            return True
        else:
            print("No hay espacio en esta actividad")
            return False
    elif x == "CrossFit":
        if Actividad.Cupo_CrossFit < 25:
            Actividad.Cupo_CrossFit += 1
            return True
        else:
            print("No hay espacio en esta actividad")
            return False
    elif x == "Yoga":
        if Actividad.Cupo_Yoga < 40:
            Actividad.Cupo_Yoga += 1
            return True
        else:
            print("No hay espacio en esta actividad")
            return False
    elif x == "Gym":
        if Actividad.Cupo_Gym < 50:
            Actividad.Cupo_Gym += 1
            return True
        else:
            print("No hay espacio en esta actividad")
            return False
    else:
        print("Actividad no reconocida")
        return False

# ==========================================
# PROCESO PRINCIPAL
# ==========================================

# Inicialización de variables globales
Asistencias = 0
Cont_Mensual = 0
Cont_Semanal = 0
Usuarios = 0
Mensual = 40000
Semanal = 10000
Sistema = True

# Nombres de los archivos físicos
ArchSal = "usuarios.dat"

# Inicializamos el archivo vacío para simular el "Crear(ArchSal)" de tu inicio
if not os.path.exists(ArchSal):
    with open(ArchSal, "wb") as f:
        pass

while Sistema:
    print("\n=== Menu Gym ===")
    print("¿Que deseas hacer?")
    print("[1] Registrar un Usuario")
    print("[2] Control de asistencia Diario")
    print("[3] Control de cuotas y pagos")
    print("[4] Estadisticas del Gym")
    print("[5] Salir")
    
    try:
        Opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    # Simulación del "Segun (Opcion) hacer"
    if Opcion == 1:
        # Se crea un nuevo objeto usuario vacío en memoria
        usuario_nuevo = Usuario()
        
        usuario_nuevo.ID = int(input("¿DNI del usuario? "))
        usuario_nuevo.Nombre = input("¿Nombre y Apellido? ")
        usuario_nuevo.Edad = int(input("¿Edad del usuario? "))
        usuario_nuevo.Plan = input("¿Que tipo de plan desea adquirir?, Mensual (40.000), Semanal (10.000): ")
        
        print("Bien, se registrará en su factura")
        
        if usuario_nuevo.Edad < 18:
            if usuario_nuevo.Plan == "Mensual":
                Pago = Mensual * 0.80
                Cont_Mensual += 1
            if usuario_nuevo.Plan == "Semanal":
                Pago = Semanal * 0.80
                Cont_Semanal += 1
        else:
            if usuario_nuevo.Plan == "Mensual":
                Cont_Mensual += 1
                Pago = Mensual
            if usuario_nuevo.Plan == "Semanal":
                Cont_Semanal += 1
                Pago = Semanal
                
        Act = input("¿A que actividad desea inscribirse? ")
        Reg_Comp = False
        
        if Hay_Espacio(Act):
            usuario_nuevo.Actividades = Act
            Reg_Comp = True
        else:
            Act = input("¿No hay espacio en esta actividad, elija otra: ")
            if Hay_Espacio(Act):
                usuario_nuevo.Actividades = Act
                Reg_Comp = True

        Confirmacion = False
        if Reg_Comp:
            print(f"Monto a pagar por parte de: {usuario_nuevo.Nombre}")
            print(f"${Pago}")
            print(f"Actividad a la que se registró: {usuario_nuevo.Actividades}")
            resp = input("¿Confirmamos pago y registro? V/F: ").upper()
            Confirmacion = True if resp == "V" else False

        if Confirmacion:
            print(f"Usuario {usuario_nuevo.Nombre} Registrado, a partir de ahora se llevará un programa de asistencias")
            usuario_nuevo.Estado_Cuota = "Al Dia"
            
            # Abrir en modo 'ab' (append binary) para añadir al final del archivo
            with open(ArchSal, "ab") as f:
                pickle.dump(usuario_nuevo, f)
                
            Usuarios += 1
            Confirmacion = False
        else:
            print("Registro Cancelado")

    elif Opcion == 2:
        id_buscar = int(input("Escriba DNI del Usuario: "))
        Encontrado = False
        
        # Leemos secuencialmente los objetos del archivo
        usuarios_actualizados = []
        if os.path.exists(ArchSal):
            with open(ArchSal, "rb") as f:
                while True:
                    try:
                        user = pickle.load(f)
                        # Procesamos el usuario si coincide y no lo encontramos antes
                        if user.ID == id_buscar and not Encontrado:
                            ue_resp = input(f"¿El Usuario es: {user.Nombre}? V/F: ").upper()
                            if ue_resp == "V":
                                Asistencias += 1
                                user.Asist += 1
                                print(f"{user.Nombre} Ahora tiene un total de: {user.Asist} Asistencias")
                                Encontrado = True
                        usuarios_actualizados.append(user)
                    except EOFError:
                        break # Fin del archivo (NFDA)
            
            # Volvemos a escribir el archivo con los cambios del usuario modificado
            with open(ArchSal, "wb") as f:
                for user in usuarios_actualizados:
                    pickle.dump(user, f)
                    
        if not Encontrado:
            print("Usuario no encontrado o no verificado.")

    elif Opcion == 3:
        id_buscar = int(input("Escriba DNI del Usuario: "))
        Encontrado = False
        usuarios_actualizados = []
        
        if os.path.exists(ArchSal):
            with open(ArchSal, "rb") as f:
                while True:
                    try:
                        user = pickle.load(f)
                        if user.ID == id_buscar and not Encontrado:
                            ue_resp = input(f"¿El Usuario es: {user.Nombre}? V/F: ").upper()
                            if ue_resp == "V":
                                print(f"El estado actual de la cuota es: {user.Estado_Cuota}")
                                Encontrado = True
                                
                                if user.Estado_Cuota == "Vencido":
                                    print("Estado: Vencido, debe abonar")
                                    cuota_resp = input("¿El Usuario abonó su cuota? V/F: ").upper()
                                    if cuota_resp == "V":
                                        if user.Plan == "Mensual":
                                            Cont_Mensual += 1
                                        if user.Plan == "Semanal":
                                            Cont_Semanal += 1
                                        user.Estado_Cuota = "Al Dia"
                                        print("Listo, Cuota del usuario al día")
                                    else:
                                        user.Estado_Cuota = "Vencido"
                                        print("Está bien, sigue con su deuda")
                                else:
                                    print("Cuota del Usuario al día")
                        usuarios_actualizados.append(user)
                    except EOFError:
                        break
            
            # Reescribimos los cambios en el archivo maestro
            with open(ArchSal, "wb") as f:
                for user in usuarios_actualizados:
                    pickle.dump(user, f)
                    
        if not Encontrado:
            print("Usuario no encontrado.")

    elif Opcion == 4:
        print("\n--- Estadisticas del Gym ---")
        print(f"Total de Usuarios registrados hoy: {Usuarios}")
        print(f"Asistencias del día: {Asistencias}")
        print(f"Total de Pagos Mensuales: {Cont_Mensual}")
        print(f"Total de Pagos Semanales: {Cont_Semanal}")

    elif Opcion == 5:
        print("Saliendo del sistema...")
        Sistema = False
    else:
        print("Opción incorrecta.")