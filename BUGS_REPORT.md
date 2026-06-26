# BUGS IDENTIFICADOS EN import pickle.py

## 🔴 BUG #1: Variable `Pago` no definida (CRÍTICO)
**Ubicación:** Líneas 104-117 (Opción 1 - Registrar Usuario)

**Problema:** Si el usuario ingresa un Plan que NO sea "Mensual" ni "Semanal", la variable `Pago` nunca se asigna. Luego en línea 123 (`print(f"${Pago}")`) causa `UnboundLocalError`.

**Ejemplo de error:**
```
Usuario ingresa: "Premium" (plan inválido)
Error: UnboundLocalError: local variable 'Pago' referenced before assignment
```

**Solución:**
```python
usuario_nuevo.Plan = input("¿Que tipo de plan desea adquirir?, Mensual (40.000), Semanal (10.000): ").strip()

# Validar que sea un plan válido
while usuario_nuevo.Plan not in ["Mensual", "Semanal"]:
    print("Plan inválido. Ingrese 'Mensual' o 'Semanal'")
    usuario_nuevo.Plan = input("¿Que tipo de plan desea adquirir?: ").strip()

if usuario_nuevo.Edad < 18:
    Pago = Mensual * 0.80 if usuario_nuevo.Plan == "Mensual" else Semanal * 0.80
else:
    Pago = Mensual if usuario_nuevo.Plan == "Mensual" else Semanal
```

---

## 🔴 BUG #2: Datos vacíos en campos de texto (CRÍTICO)
**Ubicación:** Líneas 98-104

**Problema:** Si el usuario presiona Enter sin escribir en campos como "Nombre" o "Plan", se crean registros con datos vacíos. Esto no genera error, pero contamina la base de datos.

**Ejemplo:**
```
¿Nombre y Apellido? [usuario presiona Enter]
→ Se registra Usuario con Nombre = ""
```

**Solución:**
```python
usuario_nuevo.Nombre = input("¿Nombre y Apellido? ").strip()
while not usuario_nuevo.Nombre:
    print("El nombre no puede estar vacío")
    usuario_nuevo.Nombre = input("¿Nombre y Apellido? ").strip()

usuario_nuevo.Plan = input("¿Que tipo de plan desea adquirir?, Mensual (40.000), Semanal (10.000): ").strip()
while usuario_nuevo.Plan not in ["Mensual", "Semanal"]:
    print("Plan inválido. Ingrese 'Mensual' o 'Semanal'")
    usuario_nuevo.Plan = input("¿Que tipo de plan desea adquirir?: ").strip()
```

---

## 🔴 BUG #3: Entrada de números sin validación (CRÍTICO)
**Ubicación:** Líneas 98, 99, 102

**Problema:** Si el usuario ingresa texto en lugar de números en DNI o Edad, el programa colapsa.

**Ejemplo de error:**
```
¿DNI del usuario? abc
ValueError: invalid literal for int() with base 10: 'abc'
```

**Solución:**
```python
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

usuario_nuevo.ID = obtener_entero("¿DNI del usuario? ")
usuario_nuevo.Edad = obtener_entero("¿Edad del usuario? ")
```

---

## 🔴 BUG #4: Actividad no validada (CRÍTICO)
**Ubicación:** Líneas 118-131

**Problema:** Si el usuario ingresa una actividad que no existe ("Pilates", "Natación", etc.), se pasa a `Hay_Espacio()` que devuelve False sin registrar la actividad. Pero el usuario puede dejar vacía o ingresar algo inválido.

**Ejemplo:**
```
¿A que actividad desea inscribirse? Pilates
→ La función Hay_Espacio() no reconoce "Pilates"
→ Imprime "Actividad no reconocida" y pide otra
→ Si deja vacío: se registra con Actividades = ""
```

**Solución:**
```python
actividades_validas = ["Zumba", "CrossFit", "Yoga", "Gym"]

Act = input("¿A que actividad desea inscribirse? (Zumba/CrossFit/Yoga/Gym): ").strip()
while Act not in actividades_validas:
    print(f"Actividad inválida. Opciones: {', '.join(actividades_validas)}")
    Act = input("¿A que actividad desea inscribirse?: ").strip()

Reg_Comp = False
if Hay_Espacio(Act):
    usuario_nuevo.Actividades = Act
    Reg_Comp = True
```

---

## 🟡 BUG #5: Búsqueda de usuario con datos inválidos
**Ubicación:** Líneas 157, 198 (Opciones 2 y 3)

**Problema:** Similar a Bug #3, si el usuario no ingresa un número en DNI causa ValueError.

**Solución:**
```python
try:
    id_buscar = int(input("Escriba DNI del Usuario: "))
except ValueError:
    print("DNI inválido. Ingrese un número.")
    continue
```

---

## 🟡 BUG #6: Comparación de strings sensible a mayúsculas
**Ubicación:** Líneas 102, 118, etc.

**Problema:** Si el usuario ingresa "mensual" (minúscula) en lugar de "Mensual", la validación fallará.

**Solución:** Usar `.lower()` o `.upper()` para normalizar:
```python
usuario_nuevo.Plan = input("¿Plan? ").strip().capitalize()
Act = input("¿Actividad? ").strip().capitalize()
```

---

## RESUMEN DE PRIORIDADES

| Prioridad | Bug | Impacto |
|-----------|-----|---------|
| 🔴 CRÍTICA | Variable `Pago` no definida | Crash del programa |
| 🔴 CRÍTICA | Validación de números | Crash al entrada inválida |
| 🔴 CRÍTICA | Campos vacíos sin validación | Datos corruptos |
| 🔴 CRÍTICA | Actividades no validadas | Registros inválidos |
| 🟡 IMPORTANTE | Búsqueda sin validación DNI | Crash en opciones 2 y 3 |
| 🟡 IMPORTANTE | Sensibilidad mayúsculas | Validaciones falsas |

