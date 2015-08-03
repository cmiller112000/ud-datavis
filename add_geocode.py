import sys
import csv
import geocoder

reader = csv.reader(sys.stdin,delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
hdrs = dict()

linenum = 0
for line in reader:
    # build a list of output columns from the csv/tsv header line, and the index into
    # the data fields where that item will be in the real data
    if (linenum == 0):
        outline = line
        idx = 0
        for h in line:
            hdrs[h] = idx
            idx =  idx + 1
        if not hdrs.has_key("Longitude"):
            hdrs["Longitude"] = len(line)
            outline.append("Longitude")
        if not hdrs.has_key("Latitude"):
            hdrs["Latitude"] = len(line)+1
            outline.append("Latitude")
            
        if (len(outline) > 1):
            writer.writerow(outline)
        linenum += 1
    else:
    # we're in the data now, we only want to output the columns listed in output columns with some
    # special handling for node_type of question and answer
    # perform error checking along the way in case of dirty data, we don't want to throw an error
        outline = line
        if (line[hdrs["City"]]  ):
            lookupstring = line[hdrs["City"]]
            if (line[hdrs["ST"]]):
                lookupstring = lookupstring + ", " + line[hdrs["ST"]]
            g = geocoder.google(lookupstring)
            if g:
                outline.append(g.lng)
                outline.append(g.lat)
                
        if (len(outline) > 1):
            writer.writerow(outline)
