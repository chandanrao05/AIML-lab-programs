# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:12:58 2022

@author: chand
"""

from conceptlearning.CandidateEliminationAlgorithm import CandidateElimination
import csv

with open('./p3.csv') as csvFile:
    data = [tuple(line) for line in csv.reader(csvFile)]
    
ce = CandidateElimination(data)
ce.candidate_elimination()
    