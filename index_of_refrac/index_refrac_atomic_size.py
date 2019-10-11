import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import *

############ measured data being put into various vars #################
angles_helium = np.loadtxt('min_angles.dat', dtype='float')
#angles[0] = yellow
#1 = red
#2 = green
#3 = blue
#4 = violet
n_air = 1.000293
apex = radians(45)
#########################################################################


def average(data_set):
    sum = 0
    for val in data_set:
        sum = sum + val
    average = sum/np.size(data_set)
    return average

def standard_deviation(data_set,average):
    sum = 0
    for val in data_set:
        sum = sum + (val-average) ** 2

    standard_deviation = (sum/(np.size(data_set)-1))**(.5)
    return standard_deviation

def index_of_refraction(angle):
    angle = radians(angle)
    return n_air * (sin((angle+apex)/2))/(sin(apex/2))


def main():

    averages_helium = np.array([average(color) for color in angles_helium])
    stdev_helium = np.array([standard_deviation(color,average_value) for color,average_value in zip(angles_helium,averages_helium)])
    print ""
    print "Helium average angles"
    print averages_helium
    print "Helium 1.96*stdev(mean angles)"
    print stdev_helium/sqrt(5)*1.96
    print " "

    n_average = np.array([index_of_refraction(angle) for angle in averages_helium])
    print " "
    print "n average"
    print n_average
    print "stdev n average"
    print " "

main()
