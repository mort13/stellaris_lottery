#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the inputfile for the distribution of the ethics and matching origins
for a list of players.
The amount of Gestalt players can be set
aswell as the number of ethiccombinations per player.
The total amount of possible ethics is 80.
The script will break if playercount * ethic per player exceeds 80.
"""

import random

players = [
    "1",
    "2",
    "3"
    ]

gestalt_num = random.randrange(0,2,1)
ethic_num = 3


"""
------------------------------------------------------------------
Only modify the following variables if you know what you are doing
------------------------------------------------------------------
"""
#Ethic axis along wich the ethic vector will be constructed
ethic_axis=[
["","Egalitarian","Fanatic Egalitarian","Fanatic Authoritarian","Authoritarian"],
["","Militarist","Fanatic Militarist","Fanatic Pacifist","Pacifist"],
["","Xenophobe","Fanatic Xenophobe","Fanatic Xenophile","Xenophile"],
#["","Competetive","Fanatic Competetive","Fanatic Cooperative","Cooperative"],
#["","Elitist","Fanatic Elitist","Fanatic Pluralist","Pluralist"],
["","Materialist","Fanatic Materialist","Fanatic Spiritualist","Spiritualist"]
#["","Industrialist","Fanatic Industrialist","Fanatic Ecologist","Ecologist"]
]

#Ethics to map onto the ethic vectors
ethics = [
    "Fanatic Egalitarian",      #0
    "Egalitarian",              #1
    "Fanatic Authoritarian",    #2
    "Authoritarian",            #3
    "Fanatic Xenophobe",        #4
    "Xenophobe",                #5
    "Fanatic Xenophile",        #6
    "Xenophile",                #7
    "Fanatic Militarist",       #8
    "Militarist",               #9
    "Fanatic Pacifist",         #10
    "Pacifist",                 #11
    "Fanatic Materialist",      #12
    "Materialist",              #13
    "Fanatic Spiritualist",     #14
    "Spiritualist",             #15
"""
    "Fanatic Competetive",      #16
    "Competetive",              #17
    "Fanatic Cooperative",      #18
    "Cooperative",              #19
    "Fanatic Elitist",          #20
    "Elitist",                  #21
    "Fanatic Pluralist",        #22
    "Pluralist",                #23
    "Fanatic Industrialist",    #24
    "Industrialist",            #25
    "Fanatic Ecologist",        #26
    "Ecologist",                #27
"""
    "Gestalt Consciousness"     #18
]

#Dictionary mapping origins to allowed ethics
origin_ethics_mapping = {
    "Prosperous Unification": ethics,
    "Galactic Doorstep": ethics,
    "Lost Colony": ethics,
    "Remnants": ethics,
    "Fruitful Partnership": ethics,
    "Mechanist": ethics[12:14],
    "Syncretic Evolution": ethics[:-1],
    "Tree of Life": ethics[-1],
    "Resource Consolidation": ethics[-1],
    "Clone Army": ethics[:-1],
    "Life-Seeded": ethics,
    "Post-Apocalyptic": ethics,
    "Calamitous Birth": ethics,
    "Common Ground": ethics[:4]+ethics[6:],
    "Hegemon": ethics[2:4]+ethics[6:-1],
    "Doomsday": ethics,
    "On the Shoulders of Giants": ethics[:-1],
    "Scion": ethics[:4]+ethics[5:-1],
    "Shattered Ring": ethics,
    "Void Dwellers": ethics,
    "Necrophage": ethics[1:6]+ethics[8:],
    "Here Be Dragons": ethics,
    "Ocean Paradise": ethics,
    "Imperial Fiefdom": ethics,
    "Progenitor Hive": ethics[-1],
    "Slingshot to the Stars": ethics,
    "Subterranean": ethics,
    "Teachers of the Shroud": ethics[14:16],
    "Knights of the Toxic God": ethics[:-1],
    "Overtuned": ethics,
    "Broken Shackles": ethics[:2]+ethics[3:5]+ethics[6:-1],
    "Payback": ethics[:-1],
    "Fear of the Dark": ethics[:-1],
    "Under One Rule": ethics[2:-1],
    "Riftworld": ethics,
    "Cybernetic Creed": ethics[14:16],
    "Synthetic Fertility": ethics[:14],
    "Arc Welders": ethics[-1],
    "Storm Chasers":ethics,
    "Primal Calling":ethics,
    "Treasure Hunters":ethics
}

