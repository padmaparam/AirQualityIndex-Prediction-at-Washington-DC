# AirQualityIndex-Prediction-at-WashingtonDC

This project predicts airquality index in Washington DC, based on climate. 

**Data Collection**

The collection of data consists of 2 parts. First part is the collection of all climate data  and the second part is collection Of AirQuality Index data for each day.

The climate information of DC is collected from https://en.tutiempo.net/ for every day in each month from 2009 to 2019.
The data is reported by the weather station 724050(KDCA). 
<br /> <br />The features consist of:
<br /> T	Average Temperature (°C)
<br /> TM	Maximum temperature (°C)
<br />Tm	Minimum temperature (°C)
<br />SLP	Atmospheric pressure at sea level (hPa)
<br />H	Average relative humidity (%)
<br />PP	Total rainfall and / or snowmelt (mm)
<br />VV	Average visibility (Km)
<br />V	Average wind speed (Km/h)
<br />VM	Maximum sustained wind speed (Km/h)
<br />VG	Maximum speed of wind (Km/h)
<br />RA	Indicate if there was rain or drizzle (In the monthly average, total days it rained)
<br />SN	Snow indicator (In the monthly average, total days that snowed)
<br />TS	Indicates whether there storm (In the monthly average, Total days with thunderstorm)
<br />FG	Indicates whether there was fog (In the monthly average, Total days with fog)

The corresponding air quality index for each day is collected from 
https://www.epa.gov/outdoor-air-quality-data/air-data-aqi-plot

<br />**Modelling**
<br />Modelling is done with Linear Regression, Randomforest and XGBoost.Hyperparamter tuning is performed using RandomSearch.

<br />**Source code**
<br />Climate Data collection.py - The climate html data for each year is extracted from https://en.tutiempo.net/climate/ws-724050.html (specific to Washington DC) and stored in /Data/html for each year and then for each month.
<br />AQI Data Collection.ipynb - AQI data is collected for each day from https://www.epa.gov/outdoor-air-quality-data/air-data-aqi-plot.  
<br />Climate and AQI data from above 2 collections are combined based on each day as a single row and stored in airquality.csv
<br />Eash model is listed as separate file in this repository.  





