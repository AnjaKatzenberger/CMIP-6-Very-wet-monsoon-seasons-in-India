#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################
#       DATA ANALYSIS - VERY WET MONSOON SEASONS IN INDIA     #
#      RESULTS PUBLISHED IN GEOPHYSICAL RESEARCH LETTERS      #
#                    Code by Anja Katzenberger                #
###############################################################  
#Link to publication: 
#https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856

# Wet days: more than 0.1mm

import subprocess
import os

dir = "/p/tmp/anjaka/Extremes/CMIP6_day/SecondaryData/analysis"

models = ["NESM3", "MIROC6", "INM-CM5-0", "GFDL-CM4", "EC-Earth3-Veg", "CESM2-WACCM"]

for model in models:
    cdo_gtc_h = "cdo -O gtc,0.1 pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1.nc"
    cdo_gtc_f = "cdo -O gtc,0.1 pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_gtc0.1.nc"

    cdo_timsum_h = "cdo -O timsum  pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1.nc  pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1_timsum.nc"
    cdo_timsum_f = "cdo -O timsum  pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_gtc0.1.nc  pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_gtc0.1_timsum.nc"
    
    cdo_sub = "cdo -O sub pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_gtc0.1_timsum.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1_timsum.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub.nc"
    cdo_div = "cdo -O div pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1_timsum.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_div.nc"
    
    cdo_fld = "cdo -O fldmean pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub.nc pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_fldmean.nc"
        
    subprocess.check_call(cdo_gtc_h, shell=True)
    subprocess.check_call(cdo_gtc_f, shell=True)
    subprocess.check_call(cdo_timsum_h, shell=True)
    subprocess.check_call(cdo_timsum_f, shell=True)
    subprocess.check_call(cdo_sub, shell=True)
    subprocess.check_call(cdo_div, shell=True)
    subprocess.check_call(cdo_fld, shell = True)
    
    os.remove("pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_1965-2015_gtc0.1.nc")
    os.remove("pr_day_" + model + "_ssp585_JJAS_remapcon_India_mask_mul_2050-2100_gtc0.1.nc")

cdo_ens_div = "cdo -O ensmean *gtc0.1_timsum_sub_div.nc pr_day_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_div_ensmean.nc"
cdo_ens_sub = "cdo -O ensmean *gtc0.1_timsum_sub.nc pr_day_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_ensmean.nc"
cdo_fldmean = "cdo -O fldmean pr_day_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_ensmean.nc pr_day_ssp585_JJAS_remapcon_India_mask_mul_gtc0.1_timsum_sub_ensmean_fldmean.nc"

subprocess.check_call(cdo_ens_div, shell=True)
subprocess.check_call(cdo_ens_sub, shell=True)
subprocess.check_call(cdo_fldmean, shell=True)