# Calculate Satellite Elevation Angle
#
# el = elv_deg(satlong, eslat, eslong)
#
# el = elevation angle [deg] E,N
# satlong = satellite longitude [deg] N+,S-
# eslat   = earth station latiude [deg] E+,W-
# eslong  = earth station longitude [deg] E,W-

import math

def elv_deg(satlong, eslat, eslong):

    PI = math.pi

    top = (math.cos((PI/180)*eslat)
            *math.cos((PI/180)*(eslong-satlong))
           -6378/(6378+35786)) 
    bottom = (math.sqrt(1-(math.cos((PI/180)*eslat)**2)
            *(math.cos((PI/180)*(eslong-satlong))**2)))
    el = math.atan(top/bottom) /PI*180

    return el;

