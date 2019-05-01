# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:44:13 2019

@author: bfieg
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
fig=plt.figure()
class Minesweeper(object):
    count_colors = ['none','blue','green','red','darkblue','darkred','darkgreen','black','black']
    flag_vertices = np.array([[0.25,0.2],[0.25,0.8],[0.75,0.65],[0.25,0.5]])
#tiles=[]
#for i in range(10):
 #   for j in range(10):
 #     tiles.append(RegularPolygon((i+.5,j+.5),numVertices=4,radius=.5*np.sqrt(2),orientation=np.pi/4))
ax=fig.add_subplot(111,xlim=(0,10),ylim=(0,10,))
#square=RegularPolygon((.5,.5),numVertices=4, radius=.5*np.sqrt(2),orientation=np.pi/4,ec='#888888',fc='#AAAAAA')
#square2=RegularPolygon((1.5,1.5),numVertices=4, radius=.5*np.sqrt(2),orientation=np.pi/4,ec='#888888',fc='#AAAAAA')
#plt.gca().add_patch(square)
#plt.gca().add_patch(square2)
#for i in range(10):
 #   for j in range(10):
 #       square=RegularPolygon((i+.5,j+.5),numVertices=4, radius=.5*np.sqrt(2),orientation=np.pi/4,ec='#888888',fc='#AAAAAA')
  #      plt.gca().add_patch(square)
#ax.add_patch(square)
#plt.show()
squares = np.array([[RegularPolygon((i + 0.5, j + 0.5),
                                                 numVertices=4,
                                                 radius=0.5 * np.sqrt(2),
                                                 orientation=np.pi / 4,
                                                 ec='#888888',
                                                 fc='#AAAAAA')
                                  for j in range(10)]
                                 for i in range(10)])
[ax.add_patch(sq) for sq in squares.flat]
def on_click(event):
    if squares.contains_point((event.x,event.y)):
       square.set_facecolor(np.random.random(3))
       fig.canvas.draw()
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
