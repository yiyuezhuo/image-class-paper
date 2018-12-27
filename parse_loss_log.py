# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:16:33 2018

@author: yiyuezhuo
"""

def parse(fname):
    #with open('loss_log.txt') as f:
    #    lines = f.readlines()
    with open(fname) as f:
        lines = f.readlines()
    
    records= []
    for line in lines:
        if len(line) == 0 or line[0] == '=':
            continue
        p = line.replace('(','').replace(')','').replace(',','').replace(':',"")
        ps = p.split(' ')
        record = {}
        for i in range(0,len(ps)-1,2): # ignore \n
            key,value = ps[i],ps[i+1]
            if key in {'epoch','iters'}:
                value = int(value)
            else:
                value = float(value)
            record[key] = value
        records.append(record)
        
    keys = ['D_A','G_A','cycle_A','idt_A','D_B','G_B','cycle_B','idt_B']
    lists = {key:[] for key in keys}
    for record in records:
        for key in keys:
            lists[key].append(record[key])
    
    return lists

lists = parse('loss_log.txt')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(lists['D_A'])