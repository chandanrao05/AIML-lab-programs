# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:10:34 2022

@author: chand
"""

from heuristicsearch.ao_star import AOStar

print("Graph-1")
h = {'A':1, 'B':7, 'C':12, 'D':13, 'E':5, 'F':6, 'G':5, 'H':7, 'I':2, }

graph1 ={
    'A': [[('B',1),('C',1)],[('D',1)]],
    'B': [[('E',1)],[('F',1)]],
    #'C': [[('J',1)]],
    'D': [[('G',1),('H',1)]],
    'E': [[('I', 1)]]
    
    }
graph = AOStar(graph1,h,'A')
graph.applyAOStar()