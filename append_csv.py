import sys
import csv
import json

sys.path.append("C:\\Users\\cmill_000\\Downloads\\")

airports = {}
with open( "C:\\Users\\cmill_000\\Downloads\\airports.csv", "rb" ) as theFile:
    reader = csv.DictReader( theFile )
    for line in reader:
        airports[line['iata']] = {}
        for h in line.keys():
            airports[line['iata']][h] = line[h]

carriers = {}
with open( "C:\\Users\\cmill_000\\Downloads\\mycarriers.csv", "rb" ) as theFile:
    reader = csv.DictReader( theFile )
    for line in reader:
        carriers[line['Code']] = {}
        for h in line.keys():
            carriers[line['Code']][h] = line[h]
first = 0
years = [2000,2001,2002,2003,2004,2005,2006,2007,2008]
majorcities = {"NY": ["New York"], "IL": ["Chicago"], "TX": ["Dallas","Dallas-Fort Worth","Houston","Austin"], "CA": ["Los Angeles", "San Francisco"], "GA": ["Atlanta"], "FL": ["Miami", "Orlando"], "MA": ["Boston"],"VA": ["Arlington","Chantilly"] }
daysofweek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
outstat = {}

for year in years:
    with open( "C:\\Users\\cmill_000\\Downloads\\" + str(year) + ".csv", "rb" ) as theFile:
        reader = csv.DictReader( theFile )

        for line in reader:
            if carriers.has_key(line['UniqueCarrier']) and majorcities.has_key(airports[line['Dest']]['state']) and \
                airports[line['Dest']]['city'] in majorcities[airports[line['Dest']]['state']] and \
                airports[line['Dest']]['country'] == 'USA':
            # build a list of output columns from the csv/tsv header line, and the index into
            # the data fields where that item will be in the real data
            # we're in the data now, we only want to output the columns listed in output columns with some
            # special handling for node_type of question and answer
            # perform error checking along the way in case of dirty data, we don't want to throw an error

                key = carriers[line['UniqueCarrier']]['Description'] + "_" + airports[line['Dest']]['airport'] + "_" + line['DayOfWeek'] + "_" + line['Year']
                try:
                    curDelay = int(line['ArrDelay'])
                except:
                    curDelay = 0
                if not outstat.has_key(key):
                    outstat[key] = {}
                    outstat[key]['UniqueCarrierName'] = carriers[line['UniqueCarrier']]['Description']
                    outstat[key]['Year'] = line['Year']
                    outstat[key]['DayOfWeek'] = daysofweek[int(line['DayOfWeek'])-1]
                    outstat[key]['Dest long'] = airports[line['Dest']]['long']
                    outstat[key]['Dest lat'] = airports[line['Dest']]['lat']
                    outstat[key]['Dest airport'] = airports[line['Dest']]['airport']
                    outstat[key]['TotalDelayByDay'] = curDelay
                    outstat[key]['TotalDelayByDayCount'] = 1
                else:
                    outstat[key]['TotalDelayByDay'] += curDelay
                    outstat[key]['TotalDelayByDayCount'] += 1
    outarray = []
    for key in outstat.keys():
        if outstat[key].has_key('TotalDelayByDay') and outstat[key].has_key('TotalDelayByDayCount'):
            outstat[key]['AvgArrDelay'] = outstat[key]['TotalDelayByDay'] / outstat[key]['TotalDelayByDayCount']
        outarray.append(outstat[key])
        
    with open( "C:\\Users\\cmill_000\\Downloads\\flightdelays.json", "w" ) as outFile:
        json.dump(outarray, outFile)
