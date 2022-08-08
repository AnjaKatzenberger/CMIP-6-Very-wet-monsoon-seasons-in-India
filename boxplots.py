#!/usr/bin/env python3
# -*- coding: utf-8 -*-



###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856

# Create figure 04 as in publication

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
x = [0,1,2,3,4]

CESM2 =     [-224.8/50,     -190.9/50,      -108/50,      57.5/50,       16.4/50]
GFDL =      [320.9/50,      193.3/50,       68.4/50,      44.9/50,       14.1/50]
EC =        [147.1/50,      16.2/50,        36.1/50,      80/50,         14.8/50]
NESM3 =     [276.9/50,      83.4/50,        161.1/50,     32.3/50,       0.2/50]
INM =       [91.5/50,       -251.8/50,      318.3/50,     18.7/50,        6.4/50]
MIROC6 =    [113.4/50,      -2.8/50,        74.8/50,      32.4/50,          9/50]
MMM =       [115.3/50,      -23.6/50,       86.7/50,         42.4/50,        9.8/50]

ax.scatter(x, CESM2, marker = "1", label ="CESM2-WACCM", color = "darkred", s=100)
ax.scatter(x, GFDL,marker = "3", label = "GFDL-CM4",color = "darkorchid", s=100)
ax.scatter(x, EC,marker =  "2", label = "EC-Earth3-Veg", color = "mediumblue", s=100)
ax.scatter(x, NESM3,marker = "+", label = "NESM3", s=100)
ax.scatter(x, INM,marker =  "x", label = "INM-CM5-0", color = "green", s=80)
ax.scatter(x, MIROC6, marker =  "4", label = "MIROC6", color = "darkorange", s=100)

ax.scatter(x, MMM,marker = "_",color = "black", label = "Multi-Model-Mean",s=400)

ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(['wet','light','moderate','heavy','very heavy'])
ax.set_yticks([-7.5,-5,-2.5,0,2.5,5,7.5])
plt.ylabel("Change in Days per Season")
plt.axhline(0,color = "black",linewidth=0.8,linestyle = "--")

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),frameon=False)


#plt.legend()
#plt.show()
plt.savefig("/Users/anjakatzenberger/Dokumente/01_Uni/Masterarbeit/Extremes/Figures/summary_plot.pdf",bbox_inches='tight')