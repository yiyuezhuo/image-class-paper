# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 00:01:34 2018

@author: yiyuezhuo
"""

class Tag:
    def pad(self, s):
        return ' '*self.pad_length + s

class Subfigure(Tag):
    def __init__(self,
                 image_path, 
                 linewidth_p = 0.99,
                 caption = None
                 pad_length = 0):
        self.image_path = image_path
        self.linewidth_p = linewidth_p
        self.caption = caption
        self.pad_length = pad_length
    def render(self):
        header = r'\begin{subfigure}[b]{'+str(self.linewidth_p)+r'\linewidth}'
        body = r'\includegraphics[width=\linewidth]{'+self.image_path+r'}'
        caption = r'\caption{'+self.caption+'}'
        tail = r'\end{subfigure}'
        return 