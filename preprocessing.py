#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856



import os
import subprocess

merge = "False"

primdir = "/p/tmp/anjaka/Extremes/CMIP6_day/PrimaryData/"

models = ["NESM3", "MIROC6", "INM-CM5-0", "GFDL-CM4", "EC-Earth3-Veg", "CESM2-WACCM"]

for model in models:
    print(model)
    dir = primdir + model + "/*" 
    
    cdo_merge = "cdo mergetime " + dir + " /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/mergetime/pr_day_" + model + "_ssp585.nc"
    
    cdo_JJAS = "cdo -selmon,6/9 -selyear,1850/2100 " + "/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/mergetime/pr_day_" + model + "_ssp585.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS.nc" 
    
    cdo_remapcon = "cdo remapcon,r360x180  /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS.nc  /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon.nc"
    
    cdo_India = "ncks -Od lon,67.0,98.0 -d lat,6.0,36.0 /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India.nc"
    
    cdo_mask = "cdo mul /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/fx_sftlf_CNRM-CM6-1-HR_masked_missval_remapcon.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask.nc"
    
    cdo_mulc = "cdo mulc,86400 /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul.nc"
    
    cdo_hist = "cdo -selyear,1965/2014 /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015.nc"
    
    cdo_fut = "cdo -selyear,2050/2099 /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul.nc /p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100.nc"
    
    
    
    if merge == "True":
        subprocess.check_call(cdo_merge, shell=True)
    
    subprocess.check_call(cdo_JJAS, shell=True)
    subprocess.check_call(cdo_remapcon, shell=True)
    subprocess.check_call(cdo_India, shell=True)
    subprocess.check_call(cdo_mask, shell = True)
    subprocess.check_call(cdo_mulc, shell = True)
    subprocess.check_call(cdo_hist, shell=True)
    subprocess.check_call(cdo_fut, shell=True)
    
    os.remove("/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS.nc")
    os.remove("/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon.nc")
    os.remove("/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India.nc")
    os.remove("/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask.nc")
    os.remove("/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/preprocessed/pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul.nc")
    