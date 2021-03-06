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

    import math pi, cos, sqrt, atan
    
    top = (cos((pi/180)*eslat)
            *cos((pi/180)*(eslong-satlong))
           -6378/(6378+35786)) 
    bottom = (sqrt(1-(cos((pi/180)*eslat)**2)
            *(cos((pi/180)*(eslong-satlong))**2)))
    el = atan(top/bottom) /pi*180

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
   
    import math pi, cos, sqrt
                                           
    longdiffr = (eslong - satlong)/(180/pi)
    p1 = 35786*35786
    p2 = 2*6378.16*(35786 + 6378.16)
    p3 = 1 - cos(eslat/(180/pi))*cos(-longdiffr)
    slantrange = sqrt(p1 + (p2*p3))
        
    return slantrange

def azimuth(satlong,eslat,eslong):
    #
    # Calulate satellite azimuth
    #
    # esazimuth = azimuth [deg] E,S
    # satlong = satellite longitude [deg] N+,S-
    # eslat   = earth station latiude [deg] E+,W-
    # eslong  = easrth station longitude [deg] E,W-
 
    from math import pi,atan,tan,sin       

    longdiffr = (eslong - satlong)/ (180/pi)
    esazimuth = 180 + (180/pi)*atan(tan(longdiffr)/sin((eslat/(180/pi))))
    if eslat < 0:
        esazimuth = esazimuth - 180
    if esazimuth < 0:
        esazimuth = esazimuth + 360.0
        
def fspl(freq,slantrange):
    #
    # Calulate Free Space Path Loss 
    #
    # fspl = fspl [dB]
    # freq = carrier frequency GHz
    # slantrange   = slant path distance from earth station to satellite [km]

    from math import pi, log10
    
    fspl = -10*log10(0.09/freq/freq/(16*pi*pi*slantrange*1000*slantrange*1000))
   
    return fspl;
