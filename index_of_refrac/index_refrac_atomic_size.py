import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import *

############ measured data being put into various vars #################
angles_helium = np.loadtxt('min_angles.dat', dtype='float')

for i in range(np.shape(angles_helium)[0]):
    for j in range(np.shape(angles_helium)[1]):
        angles_helium[i][j] = radians(angles_helium[i][j])
#angles[0] = red
#1 = red
#2 = yellow
#3 = green
#4 = green
#etc...

angles_mercury = np.loadtxt('min_angels_mercury.dat', dtype='float')

for i in range(np.shape(angles_mercury)[0]):
    for j in range(np.shape(angles_mercury)[1]):
        angles_mercury[i][j] = radians(angles_mercury[i][j])

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

def index_of_refraction(angle, angle_error):
    n = n_air * (sin((angle+apex)/2))/(sin(apex/2))
    n_error = angle_error*(n_air/2) * (cos((angle+apex)/2))/(sin(apex/2))
    return n, n_error

def regression(x,y):
    xsquared = 0
    sumx = 0
    sumxy=0
    sumy=0
    N = len(x)
    for i in range(N):
        xsquared += x[i]**2
        sumx += x[i]
        sumxy +=x[i]*y[i]
        sumy += y[i]

    delta = (N*xsquared)-(sumx)**2
    yint = ((xsquared*sumy)-(sumx*sumxy))/delta
    slope = (N*sumxy-sumx*sumy)/delta
    sigmaysum=0
    for i in range(N):
        sigmaysum += (y[i] - yint -slope*x[i])**2
    sigmay = ((1/(N-2.0))*sigmaysum)**0.5
    sigmayint = sigmay*sqrt(xsquared/delta)
    sigmaslope = sigmay*sqrt(N/delta)
    return slope, yint, sigmaslope, sigmayint


def main():

    averages_helium = np.array([average(color) for color in angles_helium])
    stdev_helium = np.array([standard_deviation(color,average_value) for color,average_value in zip(angles_helium,averages_helium)])
    stdev_mean_helium = stdev_helium/sqrt(5)
    print ""
    print "Helium average angles"
    print averages_helium
    print "Helium 1.96*stdev(mean angles)"
    print stdev_mean_helium*1.96

    n_average = np.array([index_of_refraction(angle, error)[0] for angle, error in zip(averages_helium,stdev_mean_helium)])
    n_error = np.array([index_of_refraction(angle, error)[1] for angle, error in zip(averages_helium,stdev_mean_helium)])
    print " "
    print "n average"
    print n_average
    print "ae n average"
    print n_error*1.96
    print " "

    wavelengths = np.array([706.5,667.8,587.6,504.8,501.6,492.2,471.3])
    wavelengths = wavelengths/1000

    n_slope, n_yint, n_sigma_slope, n_sigma_yint = regression(1/(wavelengths**2), n_average)
    print "slope"
    print n_slope,n_sigma_slope
    print "yint"
    print n_yint, n_sigma_yint
    x = np.linspace(2,5.1,100)
    y = n_slope*x+n_yint
    plt.plot(x,y,'-b')
    #plt.plot(1/(wavelengths**2), n_average,'bo')
    plt.errorbar(1/(wavelengths**2),n_average,yerr=n_error,fmt="o")
    plt.xlabel("1/Wavelength^2 (1/um^2)")
    plt.ylabel("Index of refraction")
    plt.title("Index of refraction as a function of wavelength\nHelium Lamp")
    plt.show()


    averages_mercury = np.array([average(color) for color in angles_mercury])
    stdev_mercury = np.array([standard_deviation(color,average_value) for color,average_value in zip(angles_mercury,averages_mercury)])
    stdev_mean_mercury = stdev_mercury/sqrt(5)
    print ""
    print "mercury average angles"
    print averages_mercury
    print "mercury 1.96*stdev(mean angles)"
    print stdev_mean_mercury*1.96

    n_average = np.array([index_of_refraction(angle, error)[0] for angle, error in zip(averages_mercury,stdev_mean_mercury)])
    n_error = np.array([index_of_refraction(angle, error)[1] for angle, error in zip(averages_mercury,stdev_mean_mercury)])
    print " "
    print "n average"
    print n_average
    print "ae n average"
    print n_error*1.96
    print " "


    wavelengths_mercury = np.array([578,546.1,435.8,404.7])
    wavelengths_mercury = wavelengths_mercury/1000

    n_slope, n_yint, n_sigma_slope, n_sigma_yint = regression(1/(wavelengths_mercury**2), n_average)
    print "slope"
    print n_slope,n_sigma_slope*1.96
    print "yint"
    print n_yint, n_sigma_yint*1.96
    x = np.linspace(3,6.1,100)
    y = n_slope*x+n_yint
    plt.plot(x,y,'-b')
    #plt.plot(1/(wavelengths_mercury**2), n_average,'bo')
    plt.errorbar(1/(wavelengths_mercury**2),n_average,yerr=n_error,fmt="o")
    plt.xlabel("1/Wavelength^2 (1/um^2)")
    plt.ylabel("Index of refraction")
    plt.title("Index of refraction as a function of wavelength\nMercury Lamp")
    plt.show()

main()
