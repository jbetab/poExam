# Funciones para un gestor de tareas

def mostrar_menu():
    print("Bienvenido al Gestor de Tareas")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Salir")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for idx, tarea in enumerate(tareas, start=1):
            print(f"{idx}. {tarea}")

def agregar_tarea(tareas, nueva_tarea):
    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")

def completar_tarea(tareas, indice):
    if indice >= 0 and indice < len(tareas):
        tarea_completada = tareas.pop(indice)
        print(f"Tarea '{tarea_completada}' completada.")
    else:
        print("Índice de tarea inválido.")

def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            nueva_tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(tareas, nueva_tarea)
        elif opcion == "3":
            indice = int(input("Ingrese el índice de la tarea completada: ")) - 1
            completar_tarea(tareas, indice)
        elif opcion == "4":
            print("Gracias por usar el Gestor de Tareas.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
