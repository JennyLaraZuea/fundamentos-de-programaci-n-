# Definición de una función con parámetros para saludar
def saludar(nombre, edad):
    print(f"Hola, {nombre} tienes {edad} años.")


# Función con parámetro predeterminado para el saludo
def saludar_con_saludo(nombre, edad, saludo="Hola"):
    print(f"{saludo}, {nombre} tienes {edad} años.")


# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.
    Si no se proporciona un porcentaje de descuento, por defecto es 10%.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Función para solicitar y validar la entrada de un número positivo
def solicitar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, introduce un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")


# Función principal del programa
def ejecutar_programa():
    print("Bienvenido al programa de cálculo de descuentos.")

    # Se pide el nombre y edad del usuario para saludarlo antes de iniciar el cálculo
    nombre = input("Introduce tu nombre: ")
    edad = solicitar_numero_positivo("Introduce tu edad: ")

    # Usar la función de saludo
    saludar(nombre, int(edad))  # Se usa la función de saludo básica

    # Preguntar si se desea usar un saludo personalizado
    usar_saludo_personalizado = input("¿Quieres usar un saludo personalizado? (S/N): ").strip().lower()
    if usar_saludo_personalizado == "s":
        saludo_personalizado = input("Introduce el saludo que prefieras: ")
        saludar_con_saludo(nombre, int(edad), saludo_personalizado)  # Usar el saludo personalizado
    else:
        saludar_con_saludo(nombre, int(edad))  # Usar el saludo predeterminado

    # Preguntar al usuario cuántas compras desea procesar
    num_compras = int(solicitar_numero_positivo("¿Cuántas compras has realizado?: "))

    # Lista para almacenar los detalles de todas las compras
    compras = []

    # Procesar cada compra
    for i in range(num_compras):
        print(f"\nProcesando compra {i + 1}:")

        # Solicitar el monto total de la compra
        monto = solicitar_numero_positivo("Introduce el monto total de la compra: ")

        # Preguntar al usuario si quiere usar el descuento predeterminado o personalizado
        usar_descuento_predeterminado = input(
            "¿Deseas usar el descuento predeterminado del 10%? (S/N): ").strip().lower()

        if usar_descuento_predeterminado == "s":
            descuento = calcular_descuento(monto)
            porcentaje_descuento = 10
        else:
            # Solicitar el porcentaje de descuento personalizado
            porcentaje_descuento = solicitar_numero_positivo("Introduce el porcentaje de descuento: ")
            descuento = calcular_descuento(monto, porcentaje_descuento)

        # Calcular el monto final a pagar
        monto_final = monto - descuento

        # Almacenar la compra en la lista de compras
        compras.append({
            'monto': monto,
            'porcentaje_descuento': porcentaje_descuento,
            'descuento': descuento,
            'monto_final': monto_final
        })

        # Mostrar resultados de la compra actual
        print(
            f"Compra {i + 1}: Descuento del {porcentaje_descuento}% sobre {monto} es {descuento:.2f}. Total a pagar: {monto_final:.2f}")

    # Mostrar resumen final de todas las compras
    print("\nResumen de todas las compras:")
    total_monto = 0
    total_descuentos = 0
    total_final_a_pagar = 0

    for i, compra in enumerate(compras):
        print(f"Compra {i + 1}:")
        print(f"  Monto original: {compra['monto']:.2f} €")
        print(f"  Porcentaje de descuento: {compra['porcentaje_descuento']}%")
        print(f"  Descuento aplicado: {compra['descuento']:.2f} €")
        print(f"  Total a pagar: {compra['monto_final']:.2f} €")

        # Acumular los totales
        total_monto += compra['monto']
        total_descuentos += compra['descuento']
        total_final_a_pagar += compra['monto_final']

    # Mostrar los totales generales
    print(f"\nHas realizado un total de {num_compras} compras.")
    print(f"Total antes de descuentos: {total_monto:.2f} €")
    print(f"Total descuentos aplicados: {total_descuentos:.2f} €")
    print(f"Total final a pagar: {total_final_a_pagar:.2f} €")


# Ejecutar el programa principal
ejecutar_programa()