def crear_informacion_personal():
    """Crea un diccionario con información personal ingresada por el usuario."""
    print("Ingrese la siguiente información personal:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    profesion = input("Profesión: ")
    telefono = input("Número de teléfono: ")

    return {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "profesion": profesion,
        "telefono": telefono
    }


def modificar_dato(informacion):
    """Muestra un menú para modificar un dato específico en el diccionario."""
    print("\nSeleccione el dato que desea modificar:")
    print("1. Nombre")
    print("2. Edad")
    print("3. Ciudad")
    print("4. Profesión")
    print("5. Teléfono")

    opcion = input("Ingrese el número de la opción (1-5): ")

    if opcion == '1':
        nuevo_valor = input("Ingrese el nuevo nombre: ")
        informacion["nombre"] = nuevo_valor
    elif opcion == '2':
        nuevo_valor = input("Ingrese la nueva edad: ")
        informacion["edad"] = nuevo_valor
    elif opcion == '3':
        nuevo_valor = input("Ingrese la nueva ciudad: ")
        informacion["ciudad"] = nuevo_valor
    elif opcion == '4':
        nuevo_valor = input("Ingrese la nueva profesión: ")
        informacion["profesion"] = nuevo_valor
    elif opcion == '5':
        nuevo_valor = input("Ingrese el nuevo número de teléfono: ")
        informacion["telefono"] = nuevo_valor
    else:
        print("Opción no válida.")


def eliminar_dato(informacion, clave):
    """Elimina un dato específico del diccionario."""
    clave_normalizada = clave.lower()  # Normaliza la clave a minúsculas
    if clave_normalizada in informacion:
        del informacion[clave_normalizada]
        print(f"La clave '{clave_normalizada}' ha sido eliminada.")
    else:
        print(f"La clave '{clave}' no existe en la información.")


def imprimir_informacion(informacion):
    """Imprime la información personal de manera formateada."""
    print("\nInformación personal final:")
    for clave, valor in informacion.items():
        print(f"{clave.capitalize()}: {valor}")


# Crear el diccionario de información personal
informacion_personal = crear_informacion_personal()

# Guardar una copia de la información original para referencia
informacion_original = informacion_personal.copy()

# Modificaciones y opciones adicionales
while True:
    print("\nOpciones:")
    print("1. Modificar dato")
    print("2. Eliminar dato")
    print("3. Imprimir información")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        modificar_dato(informacion_personal)  # Modifica los datos según la opción seleccionada

    elif opcion == '2':
        # Muestra las claves disponibles al usuario
        print("Claves disponibles para eliminar: nombre, edad, ciudad, profesion, telefono")
        clave = input("Ingrese el nombre del dato que desea eliminar: ")
        eliminar_dato(informacion_personal, clave)

    elif opcion == '3':
        imprimir_informacion(informacion_personal)

    elif opcion == '4':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija de nuevo.")

# Imprimir la información original y la modificada al final
print("\nInformación original:")
imprimir_informacion(informacion_original)

print("\nInformación final después de modificaciones:")
imprimir_informacion(informacion_personal)