#punto 6

import lista

class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return f"Nombre: {self.nombre} | Año: {self.anio_aparicion} | Casa: {self.casa_comic} | Bio: {self.biografia}"

# ==========================================
# Funciones 
# ================================

# a. Eliminar el nodo que contiene la información de Linterna Verde
def eliminar_heroe(lista, nombre_a_eliminar):
    for i in range(len(lista)):
        if lista[i].nombre == nombre_a_eliminar:
            lista.pop(i)
            print(f"[-] {nombre_a_eliminar} eliminado de la lista.")
            return
    print(f"No se encontró a {nombre_a_eliminar}.")

# b. Mostrar el año de aparición de Wolverine
def mostrar_anio_aparicion(lista, nombre):
    for heroe in lista:
        if heroe.nombre == nombre:
            print(f"[*] Año de aparición de {nombre}: {heroe.anio_aparicion}")
            return

# c. Cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista, nombre, nueva_casa):
    for heroe in lista:
        if heroe.nombre == nombre:
            heroe.casa_comic = nueva_casa
            print(f"[*] La casa de {nombre} fue cambiada a {nueva_casa}.")
            return

# d. Mostrar el nombre de aquellos superhéroes que en su biografía menciona "traje" o "armadura"
def buscar_palabras_en_biografia(lista):
    print("[*] Superhéroes con 'traje' o 'armadura' en su biografía:")
    for heroe in lista:
        bio = heroe.biografia.lower() # Convertimos a minúsculas para evitar problemas de mayúsculas
        if "traje" in bio or "armadura" in bio:
            print(f"    - {heroe.nombre}")

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def mostrar_anteriores_a(lista, anio_limite):
    print(f"[*] Superhéroes que aparecieron antes de {anio_limite}:")
    for heroe in lista:
        if heroe.anio_aparicion < anio_limite:
            print(f"    - {heroe.nombre} ({heroe.casa_comic})")

# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def mostrar_casas_especificas(lista):
    nombres_buscados = ["Capitana Marvel", "Mujer Maravilla"]
    print("[*] Casas de superhéroes específicos:")
    for heroe in lista:
        if heroe.nombre in nombres_buscados:
            print(f"    - {heroe.nombre} pertenece a {heroe.casa_comic}")

# g. Mostrar toda la información de Flash y Star-Lord
def mostrar_info_especifica(lista):
    nombres_buscados = ["Flash", "Star-Lord"]
    print("[*] Información detallada:")
    for heroe in lista:
        if heroe.nombre in nombres_buscados:
            print(f"    - {heroe}")

# h. Listar los superhéroes que comienzan con la letra B, M y S
def listar_por_iniciales(lista):
    iniciales = ('B', 'M', 'S')
    print("[*] Superhéroes que comienzan con B, M y S:")
    for heroe in lista:
        if heroe.nombre.upper().startswith(iniciales):
            print(f"    - {heroe.nombre}")

# i. Determinar cuántos superhéroes hay de cada casa de comic
def contar_por_casa(lista):
    conteo = {"Marvel": 0, "DC": 0}
    for heroe in lista:
        # Se verifica si la casa existe en el diccionario para sumar 1
        if heroe.casa_comic in conteo:
            conteo[heroe.casa_comic] += 1
        else:
            conteo[heroe.casa_comic] = 1
    
    print("[*] Cantidad por casa de cómic:")
    for casa, cantidad in conteo.items():
        print(f"    - {casa}: {cantidad}")