#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:21:28 2022

@author: anjakatzenberger
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856


import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cf
from datetime import date, timedelta
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import os


def getdata(file_name):
    x = nc.Dataset(file_name)
    lon = x.variables['lon'][:]
    lat = x.variables['lat'][:]
    pr_kgms2 = x.variables['pr'][:]
    pr = pr_kgms2* 86400 # transform into mm/day
    
    time = x.variables['time'][:]
    start = date(1850,1,1) # unit of time: number of days since 1850-01-01
    dates = [start + timedelta(int(n)) for n in time] # transfers dates into more useful format
    
    return(lat,lon,dates,pr)

dir = '/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/netcdfs/pr_day_ssp585_1965-2015_India_JJAS_remapcon_mask_yearmean_timpctl_ensmean.nc'
(lat,lon,dates,pr) = getdata(dir)

fig = plt.figure()

ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cf.BORDERS)
#ax.add_feature(cf.LAND)
ax.coastlines(resolution = '50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0, color='gray', alpha=0.3, linestyle='-')
plt.imshow(pr[0][::-1], interpolation='none', extent = (67,98,6,36),cmap = cm.Blues)
gl.xlabels_top = False
gl.ylabels_bottom = True
gl.ylabels_right = False
gl.xlocator = mticker.FixedLocator([70,80,90,100])
gl.ylocator = mticker.FixedLocator([10,20,30,40])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#plt.title('1965-2015')
cbar = plt.colorbar(extend='max')
plt.clim(0,25)
cbar.set_label('mm/day')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.savefig('/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/mmm_per90_1965-2015.png', dpi = 3000)
plt.show()


dir = '/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/netcdfs/pr_day_ssp585_2050-2100_India_JJAS_remapcon_mask_yearmean_timpctl_ensmean.nc'
(lat,lon,dates,pr) = getdata(dir)

fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cf.BORDERS)
#ax.add_feature(cf.LAND)
ax.coastlines(resolution = '50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0, color='gray', alpha=0.3, linestyle='-')
plt.imshow(pr[0][::-1], interpolation='none', extent = (67,98,6,36),cmap = cm.Blues)
gl.xlabels_top = False
gl.ylabels_bottom = True
gl.ylabels_right = False
gl.xlocator = mticker.FixedLocator([70,80,90,100])
gl.ylocator = mticker.FixedLocator([10,20,30,40])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#plt.title('2050-2100')
cbar = plt.colorbar(extend='max')
plt.clim(0,25)
cbar.set_label('mm/day')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.savefig('/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/mmm_per90_2050-2100.png',dpi=3000)
plt.show()


dir = '/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/netcdfs/pr_day_ssp585_India_JJAS_remapcon_mask_yearmean_timpctl_ensmean_diff.nc'
(lat,lon,dates,pr) = getdata(dir)

fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cf.BORDERS)
#ax.add_feature(cf.LAND)
ax.coastlines(resolution = '50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0, color='gray', alpha=0.3, linestyle='-')
plt.imshow(pr[0][::-1], interpolation='none', extent = (67,98,6,36),cmap = cm.Blues)
gl.xlabels_top = False
gl.ylabels_bottom = True
gl.ylabels_right = False
gl.xlocator = mticker.FixedLocator([70,80,90,100])
gl.ylocator = mticker.FixedLocator([10,20,30,40])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#plt.title('Change between 1965-2015 and 2050-2100')
cbar = plt.colorbar(extend='max')
plt.clim(0,5)
cbar.set_label('mm/day')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.savefig('/Users/anjakatzenberger/Dokumente/01_Uni/Extremes/Figures/Per90_years/mmm_per90_diff.png',dpi=3000)
plt.show()



