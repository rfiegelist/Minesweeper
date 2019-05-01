# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:50:51 2019

@author: bfieg
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
fig=plt.figure()
ax=fig.add_subplot(111,xlim=(0,10),ylim=(0,10,))
for i in range(10):
    for j in range(10):
        square=RegularPolygon((i+.5,j+.5),numVertices=4, radius=.5*np.sqrt(2),orientation=np.pi/4,ec='#888888',fc='#AAAAAA')
        plt.gca().add_patch(square)
ax.add_patch(square)
#plt.show()
square.set_picker(True)

def on_pick(event):
    event.artist.set_facecolor(np.random.random(3))
    fig.canvas.draw()
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()