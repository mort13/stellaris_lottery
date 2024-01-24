#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import random



def create_ethic_vectors():
    vectors_1 = []
    vectors_2 = []
    for i in range(-2,3):
        for j in range(-2,3):
            for k in range(-2,3):
                for l in range(-2,3):
                    if abs(i)+abs(j)+abs(k)+abs(l) == 3:
                        if abs(i) < 2 and abs(j) < 2 and abs(k) < 2 and abs(l) < 2:
                            vectors_1.append([i,j,k,l])
                        else:
                            vectors_2.append([i,j,k,l])
    return vectors_1, vectors_2


def assign_ethics_to_vector(vectors,ethics, gestalt_num):
    ethic_vectors = [["Gestalt Consciousness","Gestalt Consciousness","Gestalt Consciousness","Gestalt Consciousness"]]*gestalt_num
    for i in range(len(vectors)):
        ethic_vectors.append([ethics[0][vectors[i][0]],
                              ethics[1][vectors[i][1]],
                              ethics[2][vectors[i][2]],
                              ethics[3][vectors[i][3]]])
    for i in range(len(ethic_vectors)):
        if ethic_vectors[i][3] == "":
            ethic_vectors[i].pop(3)
        if ethic_vectors[i][2] == "":
            ethic_vectors[i].pop(2)
        if ethic_vectors[i][1] == "":
            ethic_vectors[i].pop(1)
        if ethic_vectors[i][0] == "":
            ethic_vectors[i].pop(0)
        else:
            continue
    return ethic_vectors

def assign_ethic_to_player(list_of_players, list_of_ethics,ethic_num):
    player_ethic_pairing = [["name","ethic",[]]]*len(list_of_players)
    random.shuffle(list_of_ethics)
    for i in range(len(list_of_players)):
        player = list_of_players[i]
        player_ethic_pairing[i] = [player,[],[]]
    for i in range(len(list_of_players)*ethic_num):
        ethic = list_of_ethics[i]
        player_ethic_pairing[i%len(list_of_players)][1].append(ethic)
    return player_ethic_pairing


def assign_origins_to_players(player_ethic_pairing, list_of_origins):
    player_num = len(player_ethic_pairing)
    for i in range(len(list_of_origins)):
        if len(list_of_origins) > 0:
            ethic = player_ethic_pairing[i%player_num][1][1]
            matching_origns = [key for key, values in list_of_origins.items() if any(target in values for target in ethic)]
            if len(matching_origns)>0:
                player_ethic_pairing[i%player_num][2].append(matching_origns[0])  
                list_of_origins.pop(matching_origns[0])
        else:
            break
    
    print(list_of_origins.keys())
    print(len(list_of_origins.keys()))
    return player_ethic_pairing

def write_out(pairing_list):
    for i in range(len(pairing_list)):
        name = pairing_list[i][0]
        origins = str(pairing_list[i][2])
        f = open(name, "w")
        f.write("Hi "+name+
                "\nHier sind deine zugeteilten Ethiken:\n\n")
        for j in range(len(pairing_list[i][1])):
            ethic = str(pairing_list[i][1][j])
            f.write(ethic+"\n")
        f.write("\n\nUnd natürlich deine passenden Ursprünge:\n\n"+
                origins+
                "\n\nFalls irgendwelche Unklarheiten oder Fehler aufkommen schreibt mich gerne an.\n"+
                "Ansonsten solltet ihr nicht eure finale Wahl mir mitteilen, denn ich kenne eure Auswahl nicht.")
        