################################################################
# Copyright (C) Rocket Software 1993-2015
# Calculate the distance between two points on Earth
# assuming it is a perfect sphere
# using Haversine formula
# code borrowed from Wayne Dyck at
# http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/

import math
from decimal import *
def distanceBetweenPoints(point1, point2): 
    lat1 = Decimal(point1.lat)
    lat2 = Decimal(point2.lat)
    long1 = Decimal(point1.lng)
    long2 = Decimal(point2.lng)

    # Convert latitude and longitude to
    # spherical coordinates in radians. 
    radius = 3960 # miles

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(long2-long1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2) 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
#############################################################
