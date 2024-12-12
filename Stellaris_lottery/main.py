#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np

import functions
import names

gestalt = names.gestalt_num


vectors = functions.create_ethic_vectors(names.ethic_axis,5)
print(len(vectors))
ethic_vectors = functions.assign_ethics_to_vector(vectors, names.ethic_axis,gestalt)

ethic_pairing = functions.assign_ethic_to_player(names.players, ethic_vectors,names.ethic_num,gestalt)

ethic_origin_pairing = functions.assign_origins_to_players(ethic_pairing, names.origin_ethics_mapping)

functions.write_out(ethic_origin_pairing)

