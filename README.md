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

### Final Release - Fixes
* Premature animation triggering after selecting/deselecting Carrier or Airport filters
* Changed y-axis to originate from zero instead of allowing them to go negative
* Changed y-axis so scale remains constant to eliminate the constant moving of the axis grids
* Changed y-axis markings to increments of 5 to reduce ticks
* Updated data point tooltip text to make labels more friendly
* Removed x-axis title, since day of way names are obvious
* Repositioned airport selector under carrier filter to keep it from getting hidden
* Changed references to 'cities' to 'airports'
* Moved descriptive text to below the chart, and made it part of the javascript instead of html body so it displays at same time as chart
* Increased font/shape size of year selectors
* Increased opacity percent of 'on' condition of airport filter to make selection/deselection more clear
* Instead of removing tooltip on circle datapoints, I increased the frame refresh delay to allow tooltip display to last a little longer
* Changed wording of 'select airports' to 'selected airports' in title and text

### Release 2 - Fixes
* How to remove "year": 1.0m type tooltip due to MeasureAxis on "Year"?
* Filter by Airport - when reactivating, does not re-include filtered data.  Any ideas why?
* Make Filter by Airport text/shape more consistent with the "Year" control.
* Feedback that yellow and orange series point colors are too close.  Changed 'yellow' color to light purple
* Changed bubble chart to a line chart with line markers to make day to day variance more prominent.

### Release 1 - Issues
* How to remove "year": 1.0m type tooltip due to MeasureAxis on "Year"?
* Filter by Airport - when reactivating, does not re-include filtered data.  Any ideas why?
* Both Filter by Carrier Name and Filter by Airport - when activating and de-activating filters, both re-trigger a paused animation.  Any ideas how to stop this?

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


## Release 2 Responses
### Charlie1d
<p>
Hi @cheryl_592988902, thanks for posting your latest version. I've taken a look and so I'll post a few thoughts on here to encourage more discussion! I hope you don't mind that I've not posted on GitHub.
</p>

* Some things I like
 * the use of coloured lines to represent airlines and connecting the dots so you can see a 'profile of a typical week'
 * the interesting pattern over the week -- I had no idea that there was a consistent pattern of delays!
 * the user instructions, so I know what to do to interact with the plot

* Some things I like less
 * The way that the y-axis moves between years. This is really distracting for me, I can't make any comparison between years.
 * In a few places, the tooltips and axis labels names are unpolished: "AvgArrDelay" and "DayOfWeek" look like variable names rather than user-facing labels.
 * The fact that the animation starts and continues by default unless I stop it.

* Some more ideas
 * I'd be interested in seeing the pattern in arrival delays over the whole period -- I don't feel this is currently conveyed by the animation. Perhaps another plot (average delay over the years for each airline?) or small multiples would convey this information?
 * I think there might be too many variables involved. Day of the week, year, airline, airport combinations, delay times are all encoded here. I'm not particularly likely to stumble across a particularly interesting airport or airline without a bit of guidance of what to look for. Is your main aim to show patterns of delays through the years or through the week? Is there anything specific you're hoping to show about a certain airline or airport?

### andrew_37796816420h
<p>Hi @cheryl_592988902, I agree with the comments from @Charlie. In addition
</p>
<p>
Nice chart!!
</p>
* ** Like **
 * Interactive choices
 * Open circle points - they act like hinges

* Like Less

 * The vertical axis movement from negative values - I guess that is arriving ahead of schedule. I think it would be ok treat this as zero because it is infrequent and your chart is one of "delays" and it begs an explanation
strongly agree scale of the y axis -should not change - then the story of increasing delays from year to year will be more apparent
 * The x axis ticks are distracting because they break the vertical alignment of the day of week label an the aligned points.
your airport selector gets hidden with a more narrow browser width. Perhaps place it under the carrier filter
 * The title says "cities" but the data is for "airports"
try it without the horizontal grid .. I don't think the actual measurements are important. This may make the whole chart feel simpler and may make the animation feel more fluid
 * try it with fewer y axis markings (greater intervals) - perhaps five minutes will be a more natural/intuitive increment

Great!!!

### Yohann16h
<p>
Hi @cheryl_592988902,
</p>
<p>
Nice chart, the design is very good as well as the different transitions
</p>
* What I like :

 * The animation and transitions (including the one when removing an airline)
 * The message being shared

* What I like less :
 * I would probably put the explanation text below the graph instead
 * The y-axis constantly changing, it's difficult to compare between years
 * Negative y-values, you should put a minimum to 0
 * The selection for the years and airports are fairly small, hence it's not always clear where I am at a specific time. You would probably want to increase the difference of shade when selecting an airport
 * You may want to remove the circle tooltip while the animation is running as it goes away very quickly as the graph changes.
 * In the title I would say "selected" instead of "select"

* Questions
 * What do you notice in the visualization?
  * A smooth transition between years

 * What questions do you have about the data?
  * How it was collected and how outliers are being handled (cancelled flights etc..)

 * What relationships do you notice?
  * Saturday being the best performer in terms of arriving on time
Tuesday seems to go on and off across years
  * Southwest Airlines seems to have worked hard on their delays, going from a below average airline to a champion across the years

 * What do you think is the main takeaway from this visualization?
  * There's a lot of focus on Saturday instead of other weekdays for performance of airlines

 * Is there something you don’t understand in the graphic?
  * The negative values even though I understand that it is flights arriving before scheduled time but it's still odd

<p>
I hope this helps !
</p>
<p>
Kind Regards,
</p>
<p>
Yohann
</p>

## Release 1 Responses

### Shirley McAdams
* What do you notice in the visualization?
 * Delay times arriving flights
* What questions do you have about the data?
 * After clicking on some airlines and then trying to retrieve  them,it was not possible
* What relationships do you notice?
 * It appears Monday, Thursday & Friday have on average most delays
* What do you think is the main take-away from this visualization?
 * Make plans to fly Tuesday, Wednesday or Sunday
* Is there something you don’t understand in the graphic?
 * It is  pretty self explanatory
   
#### Response
regarding the disappearing data, fixed that and will be providing a new release later today or tomorrow.

### Cara Miller
* What do you notice in the visualization?
 * The large jump between going above the x axis and then it dropping downing into the negatives.  And the way that the shifts are any where from small to large.
* What questions do you have about the data?
 * What makes the difference between delay arrival time and why do the years really matter?
* What relationships do you notice?
 * The way that the orange dots seem to stay in the same base arrangement even with the large change in the minutes.
* What do you think is the main take-away from this visualization?
 * Just how much of a delay there are over the years for the different major airlines.
* Is there something you don’t understand in the graphic?
 * Not really.

* Any Additions Comments:
 * make the colors of the graph a little more differing because the pastel colors are to similar in saturation.

#### Response
new version is hopefully much clearer (changed the bubble chart to a line chart with line markers), hopefully this will make the day to day relationships more clear. Regarding the yellow dots remaining in same spot, if you notice, the scale changes from year to year, that may be why it appears they are remaining the same. As for the purpose of the year over year, it makes it possible to see improvement and/or degradation in arrival times over time.

as for the yellow/orange color being too close, I changed the yellow to a light purple, so hopefully its easier to distinguish the different lines.

### Alan McAdams
* What do you notice in the visualization?
 * When filtered by airline, the airline dots (info) disappears from graph and when airline re-clicked it does not reappear. If all airlines are clicked the graph goes blank and stays blank, have to refresh screen to bring back data.

 * Sometimes after picking a year or airport the visualization starts scrolling again when should stay paused?

* What questions do you have about the data? 
 * None, really. It is presented clearly

* What relationships do you notice?
 * Southwest airlines started to take delays seriously in 2005 and has best showing in the list at most destinations in the following years,

* What do you think is the main take-away from this visualization?
 * Fly Southwest

* Is there something you don’t understand in the graphic?
 * It is difficult to tell which Airport is being represented in the graph because when you click the airport it stays highlighted even when the next airport is picked.
Maybe graph titles which change with selections picked to show what airport and year is being shown??

* Any Additions Comments:
 * Very interesting!

#### Response
Thanks Alan, good feedback! I have a new version I will be uploading later today or tomorrow (waiting for feedback from class peers). This new version fixes the disappearing data issue, and makes the airport filter clearer and easier to read. I also changed the bubble graph to a line graph with line markers so that the day to day differences are more obvious. I liked the bouncing balls, but it didn't make that relationship very clear.

I haven't figured out how to keep the animation paused when filtering by carrier or airport yet, still working to figure out how to do that.

### JoAnna McAdams
* What do you notice in the visualization?

 * I first noticed how much easier it was to detect trends when the years flow automatically across. Not having to take my eyes off the data or trend pattern to click on different years gave a better appreciation for gaps in info. To go back and single out a year is also simple to do.

* What questions do you have about the data?
 * How to keep raw data integrity in check - i.e.: one time meaning a plane pulls away from the gate, or actually takes off?

* What relationships do you notice?

 * It appears to mostly remain consistently inconsistent.

* What do you think is the main take-away from this visualization?

 * Very smart, easy to read way to interpret what would normally be a very cumbersome data set. Very good to market / prove on time capabilities to consumer, or investors.

* Is there something you don’t understand in the graphic?

 * Per airport numbers were a little confusing, but that may be my system may not meet requirements.

* Any Additions Comments:

 * Very exciting to check this out!

#### Response
Thanks Joey! good feedback.

I have a new release coming later today or tomorrow that fixes the airport selector and a few other issues (like disappearing data). Hopefully that will make it clearer. While I liked the look of the bubble chart, I changed it to a line chart with line markers. It makes the day to day relationships much clearer.

Re: "How to keep raw data integrity in check - i.e.: one time meaning a plane pulls away from the gate, or actually takes off?"

I'm not clear on what you are asking? The raw data I based this on had multiple 'delay' timings and some (but limited) cause indicators. However, the data set itself, even filtering down to just these carriers and airports was till almost 2GB, and would never load in the browser using the tools I've been given. So I decided to just concentrate on the average arrival delay, thinking from a consumer standpoint, that is what most people would care about. I definitely see where the airlines or regulation industry would care much more on drilling down on specific causes. Is that what you were referring to?

#### Follow-up Response

Yes, that is what I was referring to, and it was more industry related, but given each airline had their own criteria for the definition of on time... Well, what can you do to control that?

I am really impressed with how you tamed THAT MUCH data in one file. Very nice!

# Resources
* http://www.d3js.org/
* http://www.dimplejs.org/
* http://stat-computing.org/dataexpo/2009/the-data.html/
* http://www.stackoverflow.com/
* http://www.udacity.com/
