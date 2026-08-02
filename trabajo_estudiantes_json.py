import json
import os   

while True:
    print("REGISTRO DE ESTUDIANTES")
    print("1. Ingresar estudiante")
    print("2. Consultar promedio de un estudiante")
    print("3. mostrar todo los estudiantes")
    print("0. salir")
    opciones=input("selecciona una opcion: ").strip()
    if opciones == "0":
        print("saliendo del programa")
        break
    elif opciones == "1":
        nombre=input("ingrese el nombre del estudiante: ").strip()
        calificaciones = []
        for i in range(1,4):
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificación {i} (0-100): "))
                    if 0 <= calificacion <= 100:
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 0 y 100. Intente nuevamente.")
                except ValueError:
                    print(" Entrada inválida. Por favor, ingrese un número válido.")
        
        estudiantes = []
        if os.path.exists("estudiantes.json"):
            try:
                with open("estudiantes.json", "r", encoding="utf-8") as archivo_json:
                    estudiantes = json.load(archivo_json)
            except (json.JSONDecodeError, FileNotFoundError):
                estudiantes = []
        
        nuevo_estudiante = {
            "nombre": nombre,
            "calificaciones": calificaciones
        }
        estudiantes.append(nuevo_estudiante)
        
        with open("estudiantes.json", "w", encoding="utf-8") as archivo_json:
            json.dump(estudiantes, archivo_json, indent=4, ensure_ascii=False)
            
        print(f"Estudiante '{nombre}' guardado exitosamente en 'estudiantes.json'.")
    elif opciones == "2":
        nombre_buscar = input("Ingrese el nombre del estudiante a consultar: ").strip()
        try:
            with open("estudiantes.json", "r", encoding="utf-8") as archivo_json:
                estudiantes = json.load(archivo_json)
        except (FileNotFoundError, json.JSONDecodeError):
            print(" No hay estudiantes registrados en el sistema.")
            continue

        encontrado = False
        for est in estudiantes:
            if est["nombre"].lower() == nombre_buscar.lower():
                notas = est["calificaciones"]
                promedio = sum(notas) / len(notas)
                print(f"\n Estudiante: {est['nombre']}")
                print(f"   Calificaciones: {notas}")
                print(f"   Promedio: {promedio:.2f}")
                encontrado = True
                break

        if not encontrado:
            print(f" No se encontró al estudiante '{nombre_buscar}'.")
    elif opciones == "3":
        try:
            with open("estudiantes.json", "r", encoding="utf-8") as archivo_json:
                estudiantes = json.load(archivo_json)
        except (FileNotFoundError, json.JSONDecodeError):
            print(" No hay estudiantes registrados en el sistema.")
            continue

        if not estudiantes:
            print(" No hay estudiantes registrados en el sistema.")
        else:
            print("\n--- LISTA DE TODOS LOS ESTUDIANTES ---")
            for est in estudiantes:
                print(f" Nombre: {est['nombre']}, Calificaciones: {est['calificaciones']}")
