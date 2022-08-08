#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856

import subprocess
import os

dir = "/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/analysis"

models = ["NESM3", "MIROC6", "INM-CM5-0", "GFDL-CM4", "EC-Earth3-Veg", "CESM2-WACCM"]

for model in models:
    cdo_sdii_h = "cdo -O eca_sdii pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_sdii.nc"
    cdo_sdii_f = "cdo -O eca_sdii pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_sdii.nc"

    cdo_sub = "cdo -O sub pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_sdii.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_sdii.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub.nc"
    cdo_div = "cdo -O div pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_sdii.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div.nc"

    cdo_fld = "cdo -O fldmean pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div_fldmean.nc"
    
    subprocess.check_call(cdo_sdii_h, shell=True)
    subprocess.check_call(cdo_sdii_f, shell=True)
    
    subprocess.check_call(cdo_sub, shell=True)
   
    subprocess.check_call(cdo_div, shell=True)
    

    subprocess.check_call(cdo_fld, shell=True)
    
cdo_ens_sub = "cdo -O ensmean *sdii_sub_div.nc pr_day_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div_ensmean.nc"
cdo_fldmean = "cdo -O fldmean pr_day_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div_ensmean.nc pr_day_ssp585_JJAS_remapcon_India_mask_mul_sdii_sub_div_ensmean_fldmean.nc"


subprocess.check_call(cdo_ens_sub, shell=True)
subprocess.check_call(cdo_fldmean, shell=True)