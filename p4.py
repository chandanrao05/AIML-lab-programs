# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:38:16 2022

@author: chand
"""
from decisiontree.ID3Algorithm import ID3
import csv

def load_csv(filename):
    lines = csv.reader(open(filename,'r'))
    dataset = list(lines)
    headers = dataset.pop(0)
    return dataset,headers

dataset_train, headers_train = load_csv('.\p4_train.csv')
dataset_test, headers_test = load_csv('.\p4_test.csv')

id3 = ID3(dataset_train,headers_train,dataset_test,headers_test)
id3.build_tree()
id3.classify()
    