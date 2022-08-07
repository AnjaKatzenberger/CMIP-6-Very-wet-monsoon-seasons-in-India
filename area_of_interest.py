#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:10:00 2022

@author: anjakatzenberger
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.patches as patches

###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856

# Python Code for producing fig S1, Supplementary Information

#### Other example from which code is derived: 
#https://towardsdatascience.com/what-is-new-in-geopandas-0-70-dda0ddc90978

#### Polygons 
# which polygon has been used for the analysis (bottom left, top left, top right, bottom, right, bottom left)
poly_used = Polygon([(67, 6), (67, 36), (98, 36), (98, 6), (67, 6)])
poly_show = Polygon([(20, -10), (20, 50), (127, 50), (127, -10), (20, -10)])

### Map
# Get world map
world = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))

# Display world map
#world.plot(color="lightgrey")

# Potentially choose countries
#countries[countries["name"] == "India"].plot(color="lightgrey",ax=ax)

# Extract framing map (world map or larger region around area of interest)
clipped = gpd.clip(world, poly_show)
#world.plot(ax=ax,color="lightgrey")

fig, ax = plt.subplots(figsize=(12,10))
clipped.plot(ax=ax, color="lightgrey")

# Create polygon of area of interest
polygon = gpd.GeoDataFrame([1], geometry=[poly_used], crs=world.crs)

#countries[countries["name"] == "India"].plot(color="lightgrey",ax=ax)
polygon.boundary.plot(ax=ax, color="red")
plt.ylabel('latitude')
plt.xlabel('longitude')
#plt.savefig('/home/anjaka/area_of_interest.pdf', bbox_inches='tight')
plt.show()
plt.close()
