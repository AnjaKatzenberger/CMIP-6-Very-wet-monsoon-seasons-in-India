#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:42:26 2022

@author: anjakatzenberger
"""

import os
import subprocess
import numpy as np

###############################################################
#              USING CDOs - VERY WET MONSOON SEASONS          #
###############################################################

# After preprocessing the data including these processes:
# - cutting the periods of interest (1965-2015, 2050-2100)
# - the area of interest
# - remapping
# - masking out the ocean)
# and naming the files accordingly (note that the file names are relevant for the code below)
# we provide here a file for further data processing
# by using CDOs. 

# working directory
wd = "/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/remapcon_mask_periods"

files = os.listdir(wd)

# List of CDOs (Climate Data Operators): 
# See for more details: https://code.mpimet.mpg.de/projects/cdo/embedded/cdo.pdf

yearmean = "False"
yearpctl = "False"
daypctl = "False"
mul = "False"
gtc = "False"
timsum = "False"
sub = "False"
div = "False"
ensmean = "True" # must be calculated in extra run after preprocessing data
eq = "False"

#____________________
# Formulating CDO commands
#___________________

cdo_cmd_ens = "cdo -O ensmean"

for file in files:
    
    if yearmean == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
            
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_yearmean.nc'
            cdo_cmd = ' '.join(("cdo -O yearmean ",file, output1))
            subprocess.check_call(cdo_cmd, shell=True)
        
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask.nc'): 
            model = file.split('_')[2]

            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_yearmean.nc'
            cdo_cmd = ' '.join(("cdo -O yearmean ",file, output2))
            subprocess.check_call(cdo_cmd, shell=True)
    
    if yearpctl == "True": 
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask_yearmean.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
            
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_yearmean_timpctl.nc'
            cdo_cmd = ' '.join(("cdo -O timpctl,90 ",file, "-timmin", file, "-timmax", file, output1))
            subprocess.check_call(cdo_cmd, shell=True)
        
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask_yearmean.nc'): 
            model = file.split('_')[2]
            
            # yearmean: Mean of each year 
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_yearmean_timpctl.nc'
            cdo_cmd = ' '.join(("cdo -O timpctl,90 ",file, "-timmin", file, "-timmax", file,  output2))
            subprocess.check_call(cdo_cmd, shell=True)
    
    
    if daypctl == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
                
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_timpctl.nc'
            cdo_cmd = ' '.join(("cdo -O timpctl,90 ",file, "-timmin", file, "-timmax", file,  output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask.nc'): 
            model = file.split('_')[2]
    
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_timpctl.nc'
            cdo_cmd = ' '.join(("cdo -O timpctl,90 ",file, "-timmin", file, "-timmax", file,  output2))
            subprocess.check_call(cdo_cmd, shell=True)
            
    if mul == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
                
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_mul.nc'
            cdo_cmd = ' '.join(("cdo -O mulc,86400 ",file,  output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask.nc'): 
            model = file.split('_')[2]
    
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_mul.nc'
            cdo_cmd = ' '.join(("cdo -O mulc,86400", file,  output2))
            subprocess.check_call(cdo_cmd, shell=True)

    if gtc == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask_mul.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
                
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_ltc40.nc'
            cdo_cmd = ' '.join(("cdo -O ltc,40 ",file,  output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask_mul.nc'): 
            model = file.split('_')[2]
    
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_mul_ltc40.nc'
            cdo_cmd = ' '.join(("cdo -O ltc,40", file,  output2))
            subprocess.check_call(cdo_cmd, shell=True)

    if timsum == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
                
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum.nc'
            cdo_cmd = ' '.join(("cdo -O timsum ",file,  output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask_mul_gtc100_ltc40_eq.nc'): 
            model = file.split('_')[2]
    
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum.nc'
            cdo_cmd = ' '.join(("cdo -O timsum", file,  output2))
            subprocess.check_call(cdo_cmd, shell=True)
            
    if sub == "True":
        if file.endswith('_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
            file2 = "pr_day_" + model +"_ssp585_2050-2100_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum.nc"
            
            output1 = 'pr_day_' + model + '_ssp585_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum_sub.nc'
            cdo_cmd = ' '.join(("cdo -O sub",file2, file, output1))
            subprocess.check_call(cdo_cmd, shell=True)
            
    if div == "True":
        if file.endswith('_India_JJAS_remapcon_mask_mul_gtc100_timsum_sub.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
            file2 = "pr_day_" + model +"_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_gtc100_timsum.nc"
            
            output1 = 'pr_day_' + model + '_ssp585_India_JJAS_remapcon_mask_mul_gtc100_timsum_sub_div.nc'
            cdo_cmd = ' '.join(("cdo -O div",file, file2, output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
    if eq == "True":
        if file.endswith('_1965-2015_India_JJAS_remapcon_mask_mul_gtc10.nc') and file.startswith('pr'): 
            model = file.split('_')[2]
            file2 = "pr_day_" + model +"_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_ltc40.nc"
                
            output1 = 'pr_day_' + model + '_ssp585_1965-2015_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq.nc'
            cdo_cmd = ' '.join(("cdo -O eq ",file, file2, output1))
            subprocess.check_call(cdo_cmd, shell=True)
           
        if file.endswith('_2050-2100_India_JJAS_remapcon_mask_mul_gtc10.nc'): 
            model = file.split('_')[2]
            file2 = "pr_day_" + model +"_ssp585_2050-2100_India_JJAS_remapcon_mask_mul_ltc40.nc"
    
            output2 = 'pr_day_' + model + '_ssp585_2050-2100_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq.nc'
            cdo_cmd = ' '.join(("cdo -O eq", file,file2,  output2))
            subprocess.check_call(cdo_cmd, shell=True)          
               
            
    if ensmean == "True":
        if file.endswith('ssp585_India_JJAS_emapcon_mask_mul_gtc10_ltc40_eq_timsum_sub.nc') and file.startswith('pr'): 
            cdo_cmd_ens = ' '.join((cdo_cmd_ens, file))
            
if ensmean == "True":      
    output_ens = 'pr_day_ssp585_India_JJAS_remapcon_mask_mul_gtc10_ltc40_eq_timsum_sub_ensmean.nc'
    cdo_cmd_ens = ' '.join((cdo_cmd_ens, output_ens))
    subprocess.check_call(cdo_cmd_ens, shell=True)
    
    
#____________________
# Removing temporary files
#___________________
# In case you want to remove files that haven't been use,
# use the command:
# os.remove()


