#This script uses AdaFurit Library to measure temp
#!/usr/bin/python

import sys
import Adafruit_DHT
import math




def get_frost_point_c(t_air_c, dew_point_c):
    """Compute the frost point in degrees Celsius
    :param t_air_c: current ambient temperature in degrees Celsius
    :type t_air_c: float
    :param dew_point_c: current dew point in degrees Celsius
    :type dew_point_c: float
    :return: the frost point in degrees Celsius
    :rtype: float
    """
    dew_point_k = 273.15 + dew_point_c
    t_air_k = 273.15 + t_air_c
    frost_point_k = dew_point_k - t_air_k + 2671.02 / ((2954.61 / t_air_k) + 2.193665 * math.log(t_air_k) - 13.3448)
    return frost_point_k - 273.15


def get_dew_point_c(t_air_c, rel_humidity):
    """Compute the dew point in degrees Celsius
    :param t_air_c: current ambient temperature in degrees Celsius
    :type t_air_c: float
    :param rel_humidity: relative humidity in %
    :type rel_humidity: float
    :return: the dew point in degrees Celsius
    :rtype: float
    """
    A = 17.27
    B = 237.7
    alpha = ((A * t_air_c) / (B + t_air_c)) + math.log(rel_humidity/100.0)
    return (B * alpha) / (A - alpha)


while True:

    rh, t = Adafruit_DHT.read_retry(11, 4)
    #temperature = temperature * 9/5.0 + 32
    dw = get_dew_point_c(t,rh)
    fp= get_frost_point_c(t,dw)
    print 'TEMP (c): {0:0.1f} C HUMIDITY: {1:0.1f} % DEW POINT: {2:0.1f} FROST POINT {3:0.1f}'.format(t,rh,dw,fp)








