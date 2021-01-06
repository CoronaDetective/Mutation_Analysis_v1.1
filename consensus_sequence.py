#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 23:14:10 2020

@author: tati
"""

import numpy as np
import pandas as pd

# open nucleotide counter file
nc_count_f = "files/nc_count.txt"
nc_count = pd.read_csv(nc_count_f, sep="\t")
nucleotides = ["a","t","g","c","-"]

# create consensus sequence
con_seq = []
for i in range (len(nc_count)):
    position = np.array(nc_count.loc[[i]])[0][1:]   
    con_seq.append(nucleotides[np.where(position == np.amax(position))[0][0]])

# write result into file
with open("consensusSeq.txt", 'w') as outfile:
    outfile.write(">Consensus\n")
    outfile.write("".join(con_seq))
        