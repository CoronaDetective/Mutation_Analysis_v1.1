#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:06:01 2020

@author: tati

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nc_count_f = "/files/nc_count.txt"

nc_count = pd.read_csv(nc_count_f, sep="\t")

len_cs = len(nc_count)
varia = []

for i in range (len_cs):
    position = np.array(nc_count.loc[[i]])[0][1:]
    varia.append(sum(position)-max(position))

varias = np.array(varia, dtype=int)

plt.plot(varias,'.')
plt.savefig('/files/Variation.eps',format='eps')

pd.DataFrame(varia).to_csv('/files/Variation.txt', sep='\t', header=False)
