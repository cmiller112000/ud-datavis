# ud-datavis
udacity data visualization P6

# Summary
I am examining the average arrival delays by select major airlines in select major destination cities in the USA between the years 2000-2008 by day of week.  I want to examine which days of the week experienced the most and least arrival delays.  I have taken the Flight data from http://stat-computing.org/dataexpo/2009/the-data.html and its supplemental data (carriers.csv/airports.csv) combined data from the 3 sources, then filtered down to a small subset
of carriers as listed below, and cities below it.  The reason for filtering the data was due to the large dataset (over 2GB even filtered).  Instead I pre-processed the data and calculated the average daily arrival delay by carrier, airport, day of week and year:

Code	Description
AA	American Airlines Inc.
CO	Continental Air Lines Inc.
DL	Delta Air Lines Inc.
UA	United Air Lines Inc.
WN	Southwest Airlines Co.

"NY": ["New York"]
"IL": ["Chicago"]
"TX": ["Dallas","Dallas-FtWorth","Houston","Austin"]
"CA": ["Los Angeles", "San Francisco"]
"GA": ["Atlanta"]
"FL": ["Miami", "Orlando"]
"MA": ["Boston"]
"VA": ["Arlington","Chantilly"]  - Washington Dulles


I have added long/lat data as well as merged the airport and carrier name information into a single flightdelays.json file with the following fields:

Dest long - longitude of destination airport
Dest lat - lat of destination airport
Dest airport - airport name of destination
ArrDelay - Arrival Delay in minutes
UniqueCarrierName - Air Carrier Name
DayOfWeek - Mon, Tues, Wed, Thu, Fri, Sat, Sun
Year

# Design
I have developed this visualization using primarily dimple.js with some d3.js tweaks based on example visualizations from http://www.dimplejs.org, in particular the bubble chart and interactive legend examples.  I am displaying the average arrival delay in minutes for the selected airline carriers and major city airports.  The story board is animated by year from 2000 - 2008 and the airline carriers and/or major city  airports are available as data filters.

# Average Arrival Delay Visualization

https://github.com/cmiller112000/ud-datavis/index.html

# Feedback
Questions for Reviewers:

* What do you notice in the visualization?
* What questions do you have about the data?
* What relationships do you notice?
* What do you think is the main takeaway from this visualization?
* Is there something you don’t understand in the graphic?

# Resources
* http://www.d3js.org
* http://www.dimplejs.org
* http://stat-computing.org/dataexpo/2009/the-data.html
* http://www.stackoverflow.com
* http://www.udacity.com - Data Analyst Nanodegree classes and forums
