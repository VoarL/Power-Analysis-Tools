from datetime import datetime
import math
import cmath
import numpy as np

# Globals
# ------------------
pi = math.pi

def transformer_primary_terminal_voltage_given_delivered_power():
    #Ex: The transformer delivers 20 kW at 0.8 power factor (lagging) to a load on the lowvoltage side.
    #Calculate the primary terminal voltage
    r1 = 0.16 #ohm
    r2 = 0.04 #ohm
    rc = 270 #ohm
    x1 = 0.32 #ohm
    x2 = 0.08 #ohm
    xm = 100 #ohm

    power_delivered = 20e3 #w
    power_factor = 0.8 #pf, lagging
    a = 2 # turns ratio
    
    transformer_rated_power = 25e3 #va
    load_voltage = 220
    primary_rated_voltage = load_voltage / a #v

    #refer everything to primary side to calculte the new primary voltage
    i2 = power_delivered / load_voltage / power_factor * cmath.exp(1j*(-1)*math.acos(power_factor))
    v2_prime = a * load_voltage
    i2_prime = i2 / a
    r2_prime = a*a*r2
    x2_prime = a*a*x2
    e1 = v2_prime + i2_prime *(r2_prime + 1j*x2_prime)

    ic = e1/rc
    im = e1/1j/xm
    ie = ic + im
    i1 = ie + i2_prime
    v1 = e1 + i1*(r1+1j*x1)

    r , phi = cmath.polar(v1)
    print ("The new primary terminal voltage is: ", r, "V ", phi*180/pi, "degrees")
    
def main():
    transformer_primary_terminal_voltage_given_delivered_power()
    
if __name__ == '__main__':
    main()
