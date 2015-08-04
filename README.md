# ud-datavis
Udacity - Data Analyst Nanodegree - Project 6 - Data Visualization

# Summary
I am examining the average arrival delays by select major airlines in select major US destination cities between the years 2000-2008 by day of week.  I want to examine which days of the week experienced the most and least arrival delays.  

What I found was 2000 seemed to be the worse for arrival delays with several airlines having delays on average over 10 minutes, United being the worse with over 20 minute delays.  

From 2000 - 2003, you see a steady improvement in arrival delays, with even the worse offenders - Continental and Delta Airlines - coming in under 6 minutes on average.  Unfortunately, 2004 - 2008 saw a continual increase for all airlines except Southwest Airlines, with several airlines averaging between 10 - 18 minutes. 

From a day per week standpoint, all airlines seemed to have their lowest delay times on Tuesdays and Saturdays, and their highest delay times on Thursdays and Fridays.  Which makes sense based on the typical busy travel days matching this finding.


# Design
## Dataset - Flight Arrival and associated supplemental data

I have taken the Flight data from http://stat-computing.org/dataexpo/2009/the-data.html/ and its supplemental data (carriers.csv/airports.csv) and combined data from the 3 sources.  I then filtered down to a small subset of carriers and destination cities as listed below it.  The reason for filtering the data was due to the large dataset (over 2GB even filtered).  From performance posts I found researching dimplejs and d3js, I've seen posts saying 11MB as being excessive. Instead I pre-processed the data using the append_csv.py script and calculated the average daily arrival delay by carrier, airport, day of week and year.  I was originally working with a csv file, but in researching performance issues, found the suggestion of using a json input file to limit the parsing phase required from converting csv to a json object:

Code | Description
---- | -----------
AA | American Airlines Inc.
CO | Continental Air Lines Inc.
DL | Delta Air Lines Inc.
UA | United Air Lines Inc.
WN | Southwest Airlines Co.

State | Cities
----- | ------
"NY" | ["New York"]
"IL" | ["Chicago"]
"TX" | ["Dallas","Dallas-FtWorth","Houston","Austin"]
"CA" | ["Los Angeles", "San Francisco"]
"GA" | ["Atlanta"]
"FL" | ["Miami", "Orlando"]
"MA" | ["Boston"]
"VA" | ["Arlington","Chantilly"]


I added long/lat data as well as merged the airport and carrier name information into a single flightdelays.json file with the following fields:

Field Name | Field Description
---------- | -----------------
Dest long | longitude of destination airport
Dest lat | lat of destination airport
Dest airport | airport name of destination
ArrDelay | Arrival Delay in minutes
UniqueCarrierName | Air Carrier Name
DayOfWeek | Mon, Tues, Wed, Thu, Fri, Sat, Sun
Year | 2000 - 2008

## Data Visualization
I have developed this visualization using primarily dimple.js with some d3.js tweaks based on example visualizations from http://www.dimplejs.org, in particular the bubble chart and interactive legend examples. 

I created a dimple story board which is animated by year from 2000 - 2008.  The animation can be paused by selecting the year you want to pause on.  You can restart animation by selecting the year a second time.

I also used an interactive legend by airline carrier for filtering the data points displayed, and I also created a 'chart' to handle filtering of the aggregated data by major city airports.

### Release 1 - Issues
* How to remove "year": 1.0m type tooltip due to MeasureAxis on "Year"?
* Filter by Airport - when reactivating, does not re-include filtered data.  Any ideas why?
* Both Filter by Carrier Name and Filter by Airport - when activating and de-activating filters, both re-trigger a paused animation.  Any ideas how to stop this?

### Release 2 - Fixes
* How to remove "year": 1.0m type tooltip due to MeasureAxis on "Year"?
* Filter by Airport - when reactivating, does not re-include filtered data.  Any ideas why?
* Make Filter by Airport text/shape more consistent with the "Year" control.
* Feedback that yellow and orange series point colors are too close.  Changed 'yellow' color to light purple
* Changed bubble chart to a line chart with line markers to make day to day variance more prominent.

# Running the Data Visualization

[Run Data Visualization!](https://rawgit.com/cmiller112000/ud-datavis/master/index.html)


# Feedback
## Questions for Reviewers:

* What do you notice in the visualization?
* What questions do you have about the data?
* What relationships do you notice?
* What do you think is the main take-away from this visualization?
* Is there something you don’t understand in the graphic?

Please answer by creating an issue on my github repository following the example issue under my name:

https://github.com/cmiller112000/ud-datavis/issues/

# Resources
* http://www.d3js.org/
* http://www.dimplejs.org/
* http://stat-computing.org/dataexpo/2009/the-data.html/
* http://www.stackoverflow.com/
* http://www.udacity.com/
