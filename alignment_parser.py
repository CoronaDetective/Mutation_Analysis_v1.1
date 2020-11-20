#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:50:33 2020

@author: tatiana
https://www.ncbi.nlm.nih.gov/projects/msaviewer/ alighment  viewer
"""
import numpy as np
import os

from Bio import SeqIO

path = os.getcwd() + "/align_online.aln"
  
def count_nucleo (fseq):
    """    
    Parameters
    ----------
    fseq : str
        sequence

    Returns
    -------
    counter : npy array
        counts how many nucleotides in presented sequence.
        [a,t,g,c,-]
    """
    counter = np.array([0,0,0,0,0]) 
    
    nucleotides = {'a':[1, 0, 0, 0, 0], 't':[0, 1, 0, 0, 0], 'g':[0, 0, 1, 0, 0], 
               'c':[0, 0, 0, 1, 0], '-':[0, 0, 0, 0, 1], 'w':[0.5, 0.5, 0, 0, 0],
               'y':[0, 0.5, 0, 0.5, 0], 'r':[0, 0, 0, 0, 1], 'n':[0.25, 0.25, 0.25, 0.25, 0],
               'k':[0, 0.5, 0.5, 0, 0], 's':[0, 0, 0.5, 0.5, 0], 'm':[0.5, 0, 0, 0.5, 0],
               'b':[0, 0.33, 0.33, 0.33, 0],'d':[0.33, 0.33, 0.33, 0, 0], 
               'h':[0.33, 0.33, 0, 0.33, 0],'v':[0.33, 0, 0.33, 0.33, 0]}     
         
    for x in fseq:
        counter = counter + np.array(nucleotides[x])
  
    return counter
#%%
nucleotide_number = 0
nucleotides = {}
        
records = list(SeqIO.parse(handle, "clustal")
for record in records:
    nucleotide_number += 1
    nucleotides[nucleotide_number] = count_nucleo(record.seq)
    
#%%
with open("files/nc_count.txt", 'w') as outfile:
        outfile.write("Nt\tA\tT\tG\tC\t-\n")
        for i in range(nucleotide_number-1):
            current_string = str(i+1) + "\t" + str(nucleotides[i+1][0]) + "\t" + str(nucleotides[i+1][1]) + "\t" + str(nucleotides[i+1][2]) + "\t" + str(nucleotides[i+1][3]) + "\t" + str(nucleotides[i+1][4])+ "\n"
            outfile.write(current_string)
            