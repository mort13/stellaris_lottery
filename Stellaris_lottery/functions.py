#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import random
import itertools

def create_ethic_vectors(ethic_axis, ethic_points):
    points = [-2,-1,0,1,2]
    vectors = list(itertools.product(points, repeat=len(ethic_axis)))
    filtered_vectors = [vector for vector in vectors if sum(abs(component) for component in vector) == ethic_points
]
    return filtered_vectors


def assign_ethics_to_vector(all_vectors, ethic_axis, gestalt_num):
    ethic_vectors = [["Gestalt Consciousness"]]*gestalt_num
    for vector in range(len(all_vectors)):
        ethics = []
        for value in range(len(all_vectors[vector])):
                if all_vectors[vector][value] !=0:
                    ethic = ethic_axis[value][all_vectors[vector][value]]
                    ethics.append(ethic)
        ethic_vectors.append(ethics)
    return ethic_vectors


def assign_ethic_to_player(list_of_players, list_of_ethics, ethic_num, gestalt_num):
    player_ethic_pairing = [0]*len(list_of_players)
    list_of_ethics_wo_gestalt = list_of_ethics[gestalt_num:]
    random.shuffle(list_of_ethics_wo_gestalt)
    list_of_ethics[gestalt_num:] = list_of_ethics_wo_gestalt
    random.shuffle(list_of_players)
    for i in range(len(list_of_players)):
        player = list_of_players[i]
        player_ethic_pairing[i] = [player,["ethics"],[]]
    for i in range(len(list_of_players)*ethic_num):
        ethic = list_of_ethics[i]
        if ethic not in player_ethic_pairing[i%len(list_of_players)][1]:
            player_ethic_pairing[i%len(list_of_players)][1].append(ethic)
    return player_ethic_pairing



def assign_origins_to_players(player_ethic_pairing, list_of_origins):
    player_num = len(player_ethic_pairing)
    i=0
    while len(list_of_origins) > 0 and i < 10000:
        ethic = player_ethic_pairing[i%player_num][1][1]
        matching_origns = [key for key, values in list_of_origins.items() if any(target in values for target in ethic)]
        if len(matching_origns)>0:
            player_ethic_pairing[i%player_num][2].append(matching_origns[0])  
            list_of_origins.pop(matching_origns[0])
        i+=1
    
    print(list_of_origins.keys())
    print(len(list_of_origins.keys()))
    return player_ethic_pairing

def assign_origins_to_players_old(player_ethic_pairing, list_of_origins):
    player_num = len(player_ethic_pairing)
    for i in range(len(list_of_origins)):
        if len(list_of_origins) > 0:
            ethic = player_ethic_pairing[i%player_num][1][1]
            matching_origns = [key for key, values in list_of_origins.items() if any(target in values for target in ethic)]
            if len(matching_origns)>0:
                player_ethic_pairing[i%player_num][2].append(matching_origns[0])  
                list_of_origins.pop(matching_origns[0])

    
    print(list_of_origins.keys())
    print(len(list_of_origins.keys()))
    return player_ethic_pairing

def write_out(pairing_list):
    for i in range(len(pairing_list)):
        name = pairing_list[i][0]
        origins = str(pairing_list[i][2])
        f = open("Tickets/"+name, "w")
        f.write("Hi "+name+
                "\nHier sind deine zugeteilten Ethiken:\n\n")
        for j in range(len(pairing_list[i][1])):
            ethic = str(pairing_list[i][1][j])
            f.write(ethic+"\n")
        f.write("\n\nUnd natürlich deine passenden Ursprünge:\n\n"+
                origins+
                "\n\nFalls irgendwelche Unklarheiten oder Fehler aufkommen schreibt mich gerne an.\n"+
                "Ansonsten solltet ihr nicht eure finale Wahl mir mitteilen, denn ich kenne eure Auswahl nicht.")
        