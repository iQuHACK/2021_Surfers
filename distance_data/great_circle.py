#-----------------------------------------------------------------------
# greatcircle.py
#-----------------------------------------------------------------------

import sys
import math

def gcd(y1, x1, y2, x2):
    #https://introcs.cs.princeton.edu/python/12types/greatcircle.py.html
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)
    a = math.sin((x2-x1)/2.0) ** 2.0 \
        + (math.cos(x1) * math.cos(x2) * (math.sin((y2-y1)/2.0) ** 2.0))

    # Great circle distance in radians
    angle2 = 2.0 * math.asin(min(1.0, math.sqrt(a)))

    # Convert back to degrees.
    angle2 = math.degrees(angle2)

    # Each degree on a great circle of Earth is 60 nautical miles.
    distance2 = 60.0 * angle2

    return distance2

maine_data = [  ("23001","Androscoggin", 44.1912, -70.1707),
                ("23003","Aroostook   ", 46.8199, -68.4766),
                ("23005","Cumberland  ", 43.8133, -70.3871),
                ("23007","Franklin    ", 45.0386, -70.3980),
                ("23009","Hancock     ", 44.5770, -68.3567),
                ("23011","Kennebec    ", 44.4499, -69.7038),
                ("23013","Knox        ", 43.9970, -68.9243),
                ("23015","Lincoln     ", 44.1083, -69.5110),
                ("23017","Oxford      ", 44.4907, -70.7841),
                ("23019","Penobscot   ", 45.3231, -68.5807),
                ("23021","Piscataquis ", 45.7050, -69.3375),
                ("23023","Sagadahoc   ", 43.8171, -69.7826),
                ("23025","Somerset    ", 45.5913, -69.9999),
                ("23027","Waldo       ", 44.5107, -69.2078),
                ("23029","Washington  ", 44.9849, -67.6777),
                ("23031","York        ", 43.4133, -70.6703)]

sz = len(maine_data)
for i in range(sz):
    for j in range(sz):
        if i != j:
            dist = gcd(*maine_data[i][2:], *maine_data[j][2:])
            print(maine_data[i][0], maine_data[j][0], dist)

