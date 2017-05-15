# -*- coding: utf-8 -*-
from sat_calcs import elv_deg, path_km, azimuth, fspl

satlong = 46    # degrees N, E
eslat = 52.06   # degrees N, E
eslong = 9.33   # degrees N, E
Fup = 6.115     # GHz

el = elv_deg(satlong, eslat, eslong)
print("Earth Station Elevation Angle\t = {:.1f}".format(el),"degrees")

slantrange = path_km(satlong, eslat, eslong)
print("Slant Path length\t\t = {:5,.0f}".format(slantrange), "km")

az = azimuth(satlong, eslat, eslong)
print("Azimuth\t\t\t\t = {:.1f}".format(az), "degrees")

fspl = fspl(Fup, slantrange)
print("Free Space Path Loss (FSPL)\t = {:3,.1f}".format(fspl), "dB")
