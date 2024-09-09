# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
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

# Función para calcular y mostrar el promedio de temperaturas de cada semana para una ciudad
def mostrar_promedios_ciudad(ciudad, ciudad_num):
    print(f"\nPromedio de temperaturas para Ciudad {ciudad_num}:")
    for i, semana in enumerate(ciudad):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {i + 1}: Promedio = {promedio:.2f}°F")

# Bucle principal del programa
while True:
    print("\nSeleccionar una ciudad:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        mostrar_promedios_ciudad(temperaturas[0], 1)
    elif opcion == "2":
        mostrar_promedios_ciudad(temperaturas[1], 2)
    elif opcion == "3":
        mostrar_promedios_ciudad(temperaturas[2], 3)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")