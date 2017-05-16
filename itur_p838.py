def itur_p838(f,El,RR,tilt):
    # Specific Attenuation due to rain [ITU-R P838]
    #
    # yr = itu838_Spec_Atten_Rain(f,El,RR,tilt)
    #
	 # yr = Specific Attenuation due to rain (dB/Km)
	 # f  = Frequency (GHZ) 1-400
	 # El = Elevation Angle (deg)
	 # RR = Rain rate (mm/h)
	 # tilt = polarisation tilt angle relative to horizontal (degrees) 
    #        or horizontal, 45 circular]
    
    from math import pi, cos, exp, log
  
    theta = El*(pi/180)
    tau = tilt*(pi/180)

    F  = [1, 2, 4, 6, 7, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 150, 200,
          300, 400]

    KH = [0.0000387, 0.000154, 0.00065, 0.00175, 0.00301, 0.00454, 0.0101, 0.0188, 0.0367, 0.0751, 0.124, 0.187,
              0.263, 0.35, 0.442, 0.536, 0.707, 0.851, 0.975, 1.06, 1.12, 1.18, 1.31, 1.45, 1.36, 1.32]
                        
    KV = [0.0000352, 0.000138, 0.000591, 0.00155, 0.00265, 0.00395, 0.00887, 0.0168, 0.0335, 0.0691, 0.113, 0.167,
              0.233, 0.31, 0.393, 0.479, 0.642, 0.784, 0.906, 0.999, 1.06, 1.13, 1.27, 1.42, 1.35, 1.31]
            
    AH = [0.912, 0.963, 1.121, 1.308, 1.332, 1.327, 1.276, 1.217, 1.154, 1.099, 1.061, 1.021, 0.979, 0.939,
                  0.903, 0.873, 0.826, 0.793, 0.769, 0.753, 0.743, 0.731, 0.71, 0.689, 0.688, 0.683]
            
    AV = [0.88, 0.923, 1.075, 1.265, 1.312, 1.31, 1.264, 1.2, 1.128, 1.065, 1.03, 1, 0.963, 0.929, 0.897, 0.868,
          0.824]

    if f in F:
        i = F.index(f)
        kH = KH[i]
        kV = KV[i] 
        aH = AH[i]   
        aV = AV[i] 
    
    else:
        for i in range(len(F)):
            if f <= F[i]:
                kH =  exp(log(KH[i-1]) + ((log(KH[i]) - log(KH[i-1])) /(log(F[i]) - log(F[i-1])))*(log(f) - log(F[i-1])))
                kV =  exp(log(KV[i-1]) + ((log(KV[i]) - log(KV[i-1])) /(log(F[i]) - log(F[i-1])))*(log(f) - log(F[i-1])))
                aH = (AH[i-1] + ((AH[i] - AH[i-1])/(log(F[i]) - log(F[i-1])))* (log(f) - log(F[i-1])))    
                aV = (AV[i-1] + ((AV[i] - AV[i-1])/(log(F[i]) - log(F[i-1])))* (log(f) - log(F[i-1])))
                break
            
    k = (kH + kV + (kH - kV)*pow(cos(theta),2)*cos(2*tau))/ 2.0	# (2) 
    a = (kH*aH + kV*aV + ((kH*aH - kV*aV)*pow(cos(theta),2)*cos(2*tau)))/(2.0*k) # (3) 
    yr = k*pow(RR,a)			# (1) specific attenuation (dB/km)

    return yr;


























