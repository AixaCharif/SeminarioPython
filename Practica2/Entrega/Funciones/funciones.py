#total_games es igual al total de partidos jugados en la temporada

total_games = 25

#Genera la nueva estructura con los datos de cada jugador

def inciso_a ():
    names = "Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, Francsica, FEDERICO, Fernanda, GONZALO, Nancy"
    goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
    goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
    assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

    names = names.split (", ")
    jugadores = []

    for index in range(len(names)):
        jugadores.append({"Nombre": names[index], "Goles a favor": goals[index], "Goles evitados": goals_avoided[index], "Asistencias": assists[index]})
    return jugadores



#Busca el máximo goleador del equipo con función max 

def inciso_b (jugadores):
    goleador = max(jugadores, key=lambda x: x["Goles a favor"])
    return goleador ["Nombre"], goleador ["Goles a favor"]



#Busca el jugador más influyente del equipo con función max

def inciso_c (jugadores):
    jugador_influyente = max(jugadores, key= lambda x: x["Goles a favor"] * 1.5 + x["Goles evitados"] * 1.25 + x["Asistencias"] * 1)
    
    return jugador_influyente["Nombre"] 



#Calcula el promedio de goles por partido del equipo completo con función sum

def inciso_d (jugadores):
    total_goals = sum(jugador["Goles a favor"] for jugador in jugadores)
    return (total_goals / total_games)



#Calcula el promedio de goles por partido del maximo goleador/a

def inciso_e (goals_max):
    return (goals_max / total_games)
