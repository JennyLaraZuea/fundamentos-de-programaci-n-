# Datos de temperaturas: 3 ciudades durante 4 semanas (en Fahrenheit)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(temp_f):
    return (5/9) * (temp_f - 32)

# Función para calcular el promedio de temperaturas en Celsius durante un periodo de tiempo (semanas)
def calcular_promedio_temperaturas(temperaturas, ciudad_num, semana_inicio, semana_fin):
    ciudad = temperaturas[ciudad_num - 1]  # Selecciona la ciudad basada en el número ingresado
    suma_total = 0
    dias_totales = 0

    # Itera sobre el rango de semanas especificado
    for i in range(semana_inicio - 1, semana_fin):
        semana = ciudad[i]
        for dia in semana:
            suma_total += fahrenheit_a_celsius(dia['temp'])  # Suma las temperaturas convertidas a Celsius
            dias_totales += 1  # Cuenta los días

    promedio_general = suma_total / dias_totales if dias_totales else 0
    return promedio_general

# Bucle principal del programa
while True:
    print("\nSeleccionar una ciudad para calcular su promedio de temperaturas:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. Salir")

    opcion = input("Ingrese el número de la ciudad: ")

    if opcion in ["1", "2", "3"]:
        ciudad_num = int(opcion)

        # Solicita el período de tiempo
        semana_inicio = int(input(f"Ingrese la semana de inicio (1-4) para la Ciudad {ciudad_num}: "))
        semana_fin = int(input(f"Ingrese la semana de fin (1-4) para la Ciudad {ciudad_num}: "))

        if semana_inicio >= 1 and semana_fin <= 4 and semana_inicio <= semana_fin:
            promedio = calcular_promedio_temperaturas(temperaturas, ciudad_num, semana_inicio, semana_fin)
            print(f"\nEl promedio de temperaturas en grados Celsius para la Ciudad {ciudad_num} desde la semana {semana_inicio} "
                  f"hasta la semana {semana_fin} es: {promedio:.2f}°C")
        else:
            print("Rango de semanas inválido. Inténtelo de nuevo.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")