# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:45:56 2018

@author: yiyuezhuo
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from PIL import Image
import numpy as np

import os


def make_jiang2king():
    fig, ax = plt.subplots(5,6,figsize=(12,10))
    #gs1 = gridspec.GridSpec(5, 6)
    #gs1.update(wspace=0.0, hspace=0.0) # set the spacing between axes. 
    
    root = 'jiang.png+king.jpg+dir'
    #for root, dirs, files in os.walk('jiang.png+king.jpg+dir'):
    #    for file in files:
    for i in range(30):
        file = f'step {i}.png'
        path = os.path.join(root, file)
        image = Image.open(path)
        arr = np.array(image)
        ax[i//6, i%6].imshow(arr)
        ax[i//6, i%6].axis('off')
    
    plt.subplots_adjust(wspace=0, hspace=0)
    
    plt.show()

def make_king2jiang():
    fig, ax = plt.subplots(6,6,figsize=(12,10))
    root = 'king.jpg+jiang.png+dir'
    
    for i in range(31):
        file = f'step {i}.png'
        path = os.path.join(root, file)
        image = Image.open(path)
        arr = np.array(image)
        ax[i//6, i%6].imshow(arr)
        ax[i//6, i%6].axis('off')
    for i in range(31,36):
        ax[i//6, i%6].axis('off')
    plt.subplots_adjust(wspace=0, hspace=0)
    
    plt.show()

x = np.random.randn(100)
y = x[:97] + x[1:98] + x[2:99] + x[3:]
plt.plot(x,label='noise')
plt.plot(y,label='shaped')
plt.legend()
plt.show()