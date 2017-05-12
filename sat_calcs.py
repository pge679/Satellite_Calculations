def elv_deg(satlong, eslat, eslong):
    #
    # Calculate Satellite Elevation Angle
    #
    # el = elv_deg(satlong, eslat, eslong)
    #
    # el = elevation angle [deg] E,N
    # satlong = satellite longitude [deg] N+,S-
    # eslat   = earth station latiude [deg] E+,W-
    # eslong  = earth station longitude [deg] E,W-

    import math
    
    pi = math.pi

    top = (math.cos((pi/180)*eslat)
            *math.cos((pi/180)*(eslong-satlong))
           -6378/(6378+35786)) 
    bottom = (math.sqrt(1-(math.cos((pi/180)*eslat)**2)
            *(math.cos((pi/180)*(eslong-satlong))**2)))
    el = math.atan(top/bottom) /pi*180

    return el;

def path_km(satlong,eslat,eslong):
    #
    # Calculate satellite slant path range 
    #
    # slantrange = path_km(satlong, eslat, eslong)
    #
    # slantrange = slant range [km]
    # satlong = satellite longitude [deg] N+,S-
    # eslat   = earth station latiude [deg] E+,W-
    # eslong  = easrth station longitude [deg] E,W-
   
    import math
                                           
    pi = math.pi
    
    longdiffr = (eslong - satlong)/(180/pi)
    p1 = 35786*35786
    p2 = 2*6378.16*(35786 + 6378.16)
    p3 = 1 - math.cos(eslat/(180/pi))*math.cos(-longdiffr)
    slantrange = math.sqrt(p1 + (p2*p3))
        
    return slantrange
        
        

