import random
import time

# Generar nombres de alumnos
alumnos = [f"Alumno{i}" for i in range(1, 501)]

# Generar nombres de materias
materias = [f"Materia{i}" for i in range(1, 7)]

# Generar calificaciones aleatorias para los alumnos en cada materia
def generar_matriz_alumnos_materias(alumnos, materias):
    matriz = [[random.randint(0, 100) for _ in materias] for _ in alumnos]
    return matriz

# Buscar alumno y materia
def buscar_calificacion(matriz, alumno_index, materia_index):
    return matriz[alumno_index][materia_index]

# Prueba con la primera forma (alumnos en filas, materias en columnas)
def forma1(alumnos, materias):
    matriz = generar_matriz_alumnos_materias(alumnos, materias)
    
    start_time = time.time()
    calificacion = buscar_calificacion(matriz, 320, 4)  # Alumnos indexado desde 0 (321 -> 320, Materia 5 -> 4)
    end_time = time.time()

    print(f"Forma 1: Calificación del Alumno 321 en Materia 5: {calificacion}")
    print(f"Tiempo de búsqueda (Forma 1): {end_time - start_time} segundos")

# Prueba con la segunda forma (materias en filas, alumnos en columnas)
def forma2(alumnos, materias):
    matriz = generar_matriz_alumnos_materias(materias, alumnos)
    
    start_time = time.time()
    calificacion = buscar_calificacion(matriz, 4, 320)  # Materia 5 -> 4, Alumno 321 -> 320
    end_time = time.time()

    print(f"Forma 2: Calificación del Alumno 321 en Materia 5: {calificacion}")
    print(f"Tiempo de búsqueda (Forma 2): {end_time - start_time} segundos")

# Probar con diferentes tamaños de datos
def probar_con_tamanos(diferentes_tamanos_alumnos, diferentes_tamanos_materias):
    for tamano_alumnos in diferentes_tamanos_alumnos:
        for tamano_materias in diferentes_tamanos_materias:
            print(f"\nProbando con {tamano_alumnos} alumnos y {tamano_materias} materias...")
            
            # Actualizar listas
            alumnos_test = [f"Alumno{i}" for i in range(1, tamano_alumnos + 1)]
            materias_test = [f"Materia{i}" for i in range(1, tamano_materias + 1)]
            
            print("---- Forma 1 ----")
            forma1(alumnos_test, materias_test)
            
            print("---- Forma 2 ----")
            forma2(alumnos_test, materias_test)

# Ejecución con diferentes tamaños de datos
diferentes_tamanos_alumnos = [1000, 10000, 100000]
diferentes_tamanos_materias = [100, 500, 10000]

probar_con_tamanos(diferentes_tamanos_alumnos, diferentes_tamanos_materias)
