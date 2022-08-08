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
    pr = pr_kgms2/50 # transform into %
    
    time = x.variables['time'][:]
    start = date(1850,1,1) # unit of time: number of days since 1850-01-01
    dates = [start + timedelta(int(n)) for n in time] # transfers dates into more useful format
    
    return(lat,lon,dates,pr)

dir = "/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/analysis"

files = os.listdir(dir)

for file in files: 
    if file.endswith("gtc10_ltc40_eq_timsum_sub.nc") or file.endswith("gtc10_ltc40_eq_timsum_sub_ensmean.nc"):
    #if file.endswith("gtc10_ltc40_eq_timsum_sub_ensmean.nc"):
              
            (lat,lon,dates,pr) = getdata(dir + '/' + file)
            model = file.split('_')[2]
            if model == "ssp585":
                model = "ensmean"
            
            fig = plt.figure()
            
            ax = plt.axes(projection=ccrs.PlateCarree())
            ax.add_feature(cf.BORDERS)
            #ax.add_feature(cf.LAND)
            ax.coastlines(resolution = '50m')
            gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0, color='gray', alpha=0.3, linestyle='-')
            plt.imshow(pr[0][::-1], interpolation='none', extent = (67,98,6,36),cmap = cm.RdBu)
            
            gl.xlabels_top = False
            gl.ylabels_bottom = True
            gl.ylabels_right = False
            gl.xlocator = mticker.FixedLocator([70,80,90,100])
            gl.ylocator = mticker.FixedLocator([10,20,30,40])
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
            
            plt.title(model)
            
            cbar = plt.colorbar(extend='both')
            plt.clim(-14,14)
            cbar.set_label('Days')
            
            plt.xlabel('latitude')
            plt.ylabel('longitude')
            
            
            plt.savefig('/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/figures/moderatedays_' +model + '_2.png', dpi = 800,bbox_inches='tight')
            plt.show()
    





