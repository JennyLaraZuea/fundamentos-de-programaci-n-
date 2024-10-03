# Manejo de archivos en Python: Escritura y lectura de archivos de texto
# Este programa realiza dos operaciones: escribir y leer un archivo de texto llamado 'my_notes.txt'.

# Escritura de archivo de texto
# Crea un archivo llamado my_notes.txt y escribe varias líneas de notas personales.
try:
    with open('my_notes.txt', 'w') as file:  # Abre el archivo en modo escritura ('w')
        # Escribimos tres líneas de notas personales
        file.write("1. Esta es mi primera nota personal.\n")
        file.write("2. Estoy aprendiendo a manipular archivos en Python de manera eficiente.\n")
        file.write("3. Es fundamental cerrar los archivos correctamente después de usarlos.\n")
        print("Notas escritas exitosamente en my_notes.txt.")
except IOError as e:
    # Captura cualquier error de E/S durante la escritura del archivo
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Lectura de archivo de texto
# Abre el archivo my_notes.txt para leer su contenido línea por línea.
try:
    with open('my_notes.txt', 'r') as file:  # Abre el archivo en modo lectura ('r')
        print("\nContenido del archivo 'my_notes.txt':")
        # Lee y muestra el archivo línea por línea
        for line in file:
            print(line.strip())  # Muestra cada línea sin saltos de línea adicionales
except IOError as e:
    # Captura cualquier error de E/S durante la lectura del archivo
    print(f"Ocurrió un error al leer el archivo: {e}")

# El uso de la estructura 'with' asegura que los archivos se cierren automáticamente después de la operación,
# ya sea de escritura o de lectura, evitando fugas de recursos o errores posteriores.