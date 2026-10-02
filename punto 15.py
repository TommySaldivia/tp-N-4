import lista

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} (Nvl: {self.nivel} | Tipo: {self.tipo}/{self.subtipo})"

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = [lista]  

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        
    def __str__(self):
        return f"Entrenador: {self.nombre} | Torneos: {self.torneos_ganados} | Victorias: {self.batallas_ganadas} | Derrotas: {self.batallas_perdidas}"

# ==========================================
# Funciones 
# ==========================================

# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(lista_entrenadores, nombre_entrenador):
    for entrenador in lista_entrenadores:
        if entrenador.nombre == nombre_entrenador:
            print(f"[*] {nombre_entrenador} tiene {len(entrenador.pokemons)} Pokémons.")
            return
    print(f"[-] Entrenador {nombre_entrenador} no encontrado.")

# b. Listar los entrenadores que hayan ganado más de tres torneos
def mas_de_tres_torneos(lista_entrenadores):
    print("[*] Entrenadores con más de 3 torneos ganados:")
    for entrenador in lista_entrenadores:
        if entrenador.torneos_ganados > 3:
            print(f"    - {entrenador.nombre} ({entrenador.torneos_ganados} torneos)")

# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def mejor_pokemon_del_mejor_entrenador(lista_entrenadores):
    if not lista_entrenadores:
        return
    
    # entrenador con más torneos
    mejor_entrenador = max(lista_entrenadores, key=lambda e: e.torneos_ganados)
    
    if mejor_entrenador.pokemons:
        mejor_pokemon = max(mejor_entrenador.pokemons, key=lambda p: p.nivel)
        print(f"[*] Mejor entrenador: {mejor_entrenador.nombre} | Su Pokémon de mayor nivel: {mejor_pokemon.nombre} (Nvl {mejor_pokemon.nivel})")
    else:
        print(f"[*] El mejor entrenador es {mejor_entrenador.nombre} pero no tiene Pokémons.")

# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(lista_entrenadores, nombre_entrenador):
    for entrenador in lista_entrenadores:
        if entrenador.nombre == nombre_entrenador:
            print(f"[*] Datos de {entrenador}")
            print("    Pokémons:")
            for p in entrenador.pokemons:
                print(f"      - {p}")
            return

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%
def porcentaje_victorias_alto(lista_entrenadores):
    print("[*] Entrenadores con más del 79% de victorias:")
    for entrenador in lista_entrenadores:
        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        if total_batallas > 0:
            porcentaje = (entrenador.batallas_ganadas / total_batallas) * 100
            if porcentaje > 79:
                print(f"    - {entrenador.nombre} ({porcentaje:.2f}% de victorias)")

# f. Entrenadores que tengan Pokémons de tipo Fuego/Planta o Agua/Volador (tipo y subtipo)
def entrenadores_tipos_especificos(lista_entrenadores):
    print("[*] Entrenadores con Pokémons Fuego/Planta o Agua/Volador:")
    entrenadores_encontrados = set() # Usamos un set para no repetir al entrenador si tiene varios
    
    for entrenador in lista_entrenadores:
        for p in entrenador.pokemons:
            fuego_planta = (p.tipo.lower() == "fuego" and p.subtipo.lower() == "planta")
            agua_volador = (p.tipo.lower() == "agua" and p.subtipo.lower() == "volador")
            
            if fuego_planta or agua_volador:
                entrenadores_encontrados.add(entrenador.nombre)
                
    for nombre in entrenadores_encontrados:
        print(f"    - {nombre}")

# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(lista_entrenadores, nombre_entrenador):
    for entrenador in lista_entrenadores:
        if entrenador.nombre == nombre_entrenador:
            if not entrenador.pokemons:
                print(f"[*] {nombre_entrenador} no tiene Pokémons para calcular el promedio.")
                return
            suma_niveles = sum(p.nivel for p in entrenador.pokemons)
            promedio = suma_niveles / len(entrenador.pokemons)
            print(f"[*] Promedio de nivel de Pokémons de {nombre_entrenador}: {promedio:.2f}")
            return

# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def cuantos_tienen_pokemon(lista_entrenadores, nombre_pokemon):
    cantidad = 0
    for entrenador in lista_entrenadores:
        if any(p.nombre.lower() == nombre_pokemon.lower() for p in entrenador.pokemons):
            cantidad += 1
    print(f"[*] {cantidad} entrenador(es) tienen a {nombre_pokemon}.")

# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_pokemons_repetidos(lista_entrenadores):
    print("[*] Entrenadores con Pokémons repetidos:")
    for entrenador in lista_entrenadores:
        nombres_pokemons = [p.nombre for p in entrenador.pokemons]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            print(f"    - {entrenador.nombre}")

# j. Determinar los entrenadores que tengan: Tyrantrum, Terrakion o Wingull
def entrenadores_con_buscados(lista_entrenadores):
    buscados = ["tyrantrum", "terrakion", "wingull"]
    print("[*] Entrenadores con Tyrantrum, Terrakion o Wingull:")
    encontrados = set()
    
    for entrenador in lista_entrenadores:
        for p in entrenador.pokemons:
            if p.nombre.lower() in buscados:
                encontrados.add(entrenador.nombre)
                
    for nombre in encontrados:
        print(f"    - {nombre}")

# k. Determinar si un entrenador X tiene al Pokémon Y y mostrar datos de ambos
def consultar_entrenador_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in lista_entrenadores:
        if entrenador.nombre.lower() == nombre_entrenador.lower():
            for p in entrenador.pokemons:
                if p.nombre.lower() == nombre_pokemon.lower():
                    print(f"[*] ¡Coincidencia encontrada!")
                    print(f"    - {entrenador}")
                    print(f"    - Pokémon: {p}")
                    return
            print(f"[-] {nombre_entrenador} no tiene a {nombre_pokemon}.")
            return
    print(f"[-] Entrenador {nombre_entrenador} no encontrado.")