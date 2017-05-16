# -*- coding: utf-8 -*-
from sat_calcs import elv_deg, path_km, azimuth, tilt, fspl
from itur_p838 import itur_p838

#Input 
satlong = 75.3      # degrees N, E
eslat = -33.87      # degrees N, E
eslong = 151.2      # degrees N, E
Fup = 20            # GHz

el = elv_deg(satlong, eslat, eslong)
print("Earth Station Elevation Angle\t = {:.1f}".format(el),"degrees")

slantrange = path_km(satlong, eslat, eslong)
print("Slant Path length\t\t = {:5,.0f}".format(slantrange), "km")

az = azimuth(satlong, eslat, eslong)
print("Azimuth\t\t\t\t = {:.1f}".format(az), "degrees")

poltilt = tilt(satlong, eslat, eslong)
print("Tilt Angle\t\t\t = {:.1f}".format(poltilt), "degrees")

fspl = fspl(Fup, slantrange)
print("Free Space Path Loss (FSPL)\t = {:3,.1f}".format(fspl), "dB")

RR = 51.2
tilt = 45

yr = itur_p838(Fup,el,RR,tilt)
print("Spec Atten Rain, yr \t\t = {:3,.2f}".format(yr), "dB/km")
