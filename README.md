# CMIP-6-Very-wet-monsoon-seasons-in-India

CODES FOR FIGURES OF PUBLICATION
Katzenberger et al. (2022): Intensification of Very Wet Monsoon Seasons in India Under Global Warming
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022GL098856

In the following, an overview of the underlying codes for the figures in the manuscript (A) and Supplementary Information (B) is given. The author of all listed codes is Anja Katzenberger. The preprocessing was done with preprocessing.py.

(A) MANUSCRIPT-FIGURES

FIG01: General increase from mean annual summer rainfall [mm/day] of the Indian monsoon toward wetter years between the historical (1965–2015) and the future period (2050–2100) in the Indian monsoon region under unabated climate change (SSP5-8.5).
-> data_analysis_GRL.py

FIG02a: Increase of very wet Indian summer monsoon (ISM) seasons (JJAS) in the 21st century under unabated climate change (SSP5-8.5).
-> data_analysis_GRL.py

FIG02b&c: Increase of very wet Indian summer monsoon (ISM) seasons (JJAS) in the 21st century under unabated climate change (SSP5-8.5).
-> percentiles_fig.py

FIG03: Increase in the number of very wet Indian summer monsoon (ISM) seasons by the second half of the 21st century in comparison to 1965–2015 in the Indian monsoon region under sustainable development (SSP1-2.6), modest mitigation (SSP2-4.5) and unabated climate change (SSP5-8.5).
-> Other


FIG04a-d: Change in (a.) wet days (>0.1 mm) and days with (b.) light (10 mm > x > 0.1 mm), (c.) moderate (10 mm > x > 40 mm) and (d.) heavy (>40 mm) rainfall between 1965–2015 and 2050–2100 under SSP5-8.5.
-> wetdays_fig.py, wetdays_CDO.py, lightdays_fig.py, lightdays_CDO.py, moderatedays_fig.py, moderatedays_CDO.py, heavydays_fig.py, heavydays_CDO.py

FIG04e:  In (e.) the results for the single models as well as the multi-model mean are summarized (mean from monsoon region).
-> boxplots.py




(B) SUPPLEMENTARY INFORMATION - FIGURES
FIGS1: Deﬁnition of Indian monsoon region (longitude 67 ◦ - 98 ◦ E; latitude 6 ◦ - 36 ◦ N)
-> area_of_interest.py

FIGS2: Increase in very wet seasons during the Indian monsoon between 1965-2015 and 2050-2100 as a function of global mean temperature (GMT; K) under unabated climate change (SSP5-8.5).
-> data_analysis_GRL.py

FIGS3: Change in wet days (> 0.1mm) per season between 1965-2015 and 2050-2100 under unabated climate change (SSP5-8.5) for the six models with best monsoon performance in the past.
-> wetdays_fig.py, wetdays_CDO.py

FIGS4: Change in in days with light (10mm> x > 0.1mm), moderate (10mm> x > 40mm) and heavy (40mm>) rainfall per season between 1965-2015 and 2050-2100 under unabated climate change (SSP5-8.5) for the six models with best monsoon performance in the past.
-> lightdays_fig.py, lightdays_CDO.py, moderatedays_fig.py, moderatedays_CDO.py, heavydays_fig.py, heavydays_CDO.py

FIGS5: Change in Simple Daily Intensity Index (SDII) between 1965-2015 and 2050-2100 under unabated climate change (SSP5-8.5) for the six models with best monsoon performance in the past (right) and their multi-model mean (left).
-> SDII_fig.py, SDII_CDO.py
