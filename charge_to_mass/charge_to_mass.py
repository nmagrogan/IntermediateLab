import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import *

############ measured data being put into various vars #################

##### Data and constants #####
mu_naught = 4*pi*10**-7
N_coils = 130
coil_rad = 100/(2*pi) #cm
coil_rad = coil_rad/100 #m
coil_rad = 0.15
coil_rad_uncert = 0.005

method1_current = 1.585 #A
method2_potential = 344.5 #V
method3_potential = 163 #V

current_uncertainty = 0.05 #A

radius_uncert = 0.05/100
voltage_uncert = 1


### Measured data from files####
method1_potentials = np.loadtxt('method1_potentials.dat', dtype='float') #V
method1_radii = np.loadtxt('method1_diameters.dat', dtype='float') #cm
method1_radii = method1_radii/100

fastest_electron_radii = method1_radii[0]


method2_currents = np.loadtxt('method2_currents.dat', dtype='float') #V
method2_diameters = np.loadtxt('method2_diameters.dat', dtype='float')
method2_radii = method2_diameters/100

method3_currents = np.loadtxt('method3_currents.dat', dtype='float') #V
method3_diameters = np.loadtxt('method3_diameters.dat', dtype='float')
method3_radii = method3_diameters/100



#########################################################################


def average(data_set, data_set_uncertainty):
    sum = 0
    sum2 = 0
    for i in range(len(data_set)):
        sum = sum + data_set[i]
        sum2 += data_set_uncertainty[i]**2
    average = sum/np.size(data_set)
    average_uncertainty = sqrt(sum2 / np.size(data_set))
    return average, average_uncertainty

def standard_deviation(data_set,average):
    sum = 0
    for val in data_set:
        sum = sum + (val-average) ** 2

    standard_deviation = (sum/(np.size(data_set)-1))**(.5)
    return standard_deviation

def weighted_average(data,uncertainty):
    sum_t = 0
    sum_b = 0
    for i in range(len(data)):
        sum_t += (1/uncertainty[i]**2)*data[i]
        sum_b += (1/uncertainty[i]**2)

    weighted_avg = sum_t/sum_b
    weighted_ave_uncertainty = 1/sqrt(sum_b)
    return weighted_avg,weighted_ave_uncertainty


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


def magnetic_field(I):
    B = (8.0/sqrt(125.0))*(mu_naught*N_coils*I/coil_rad)
    dbdr = (8.0/sqrt(125.0))*(-1)*(mu_naught*N_coils*I/coil_rad**2)
    dbdi = (8.0/sqrt(125.0))*(mu_naught*N_coils/coil_rad)
    B_uncertainty = np.sqrt((dbdr*coil_rad_uncert)**2 + (dbdi*current_uncertainty)**2 )
    return B, B_uncertainty

def ratio(B,V,r, b_uncert):
    em = (2*V)/((r**2)*(B**2))

    ddv = (2)/(r**2*B**2)
    ddr = (-2)*(2*V)/(r**3*B**2)
    ddb = (-2)*(2*V)/(r**2*B**3)
    em_uncertainty = np.sqrt((ddv*voltage_uncert)**2 + (ddr*radius_uncert)**2 + (ddb*b_uncert)**2 )
    return em, em_uncertainty





def main():
    print "\n----------Method 1-------------------"
    method1_B, method1_B_uncertainty = magnetic_field(method1_current)


    method1_ratio,method1_ratio_uncertainty = ratio(method1_B,method1_potentials,method1_radii, method1_B_uncertainty)
    print "Method 1 potentials"
    print method1_potentials
    print "Method 1 charge to mass ratios"
    print method1_ratio
    print "Method 1 charge to mass ratio uncertainties"
    print method1_ratio_uncertainty


    method1_average, method1_average_uncertainty = average(method1_ratio,method1_ratio_uncertainty)
    #method1_average, method1_average_uncertainty = weighted_average(method1_ratio,method1_ratio_uncertainty)
    method1_stdev = standard_deviation(method1_ratio, method1_average)
    print " "
    print "Method 1 average"
    print method1_average
    print "Method1 uncertainty error prop"
    print method1_average_uncertainty*1.96
    print "Method 1 AE stats"
    print method1_stdev*1.96


    print "----------------------------------------\n"

    print "\n----------Method 2-------------------"
    method2_B , method2_B_uncertainty= magnetic_field(method2_currents)
    method2_ratio, method2_ratio_uncertainty = ratio(method2_B,method2_potential,method2_radii, method1_B_uncertainty)
    print "Method 2 potentials"
    print method2_currents
    print "Method 2 charge to mass ratios"
    print method2_ratio
    print "Method 2 charge to mass ratio uncertainties"
    print method2_ratio_uncertainty

    method2_average, method2_average_uncertainty = average(method2_ratio,method2_ratio_uncertainty)
    method2_stdev = standard_deviation(method2_ratio, method2_average)
    print " "
    print "Method 2 average"
    print method2_average
    print "Method 2 uncertainty error prop"
    print method2_average_uncertainty*1.96
    print "Method 2 AE stats"
    print method2_stdev*1.96



    print "----------------------------------------\n"



    print "\n----------Method 3-------------------"
    method3_B, method3_B_uncertainty = magnetic_field(method3_currents)
    method3_ratio, method3_ratio_uncertainty = ratio(method3_B,method3_potential,method3_radii, method3_B_uncertainty)
    print "Method 3 potentials"
    print method3_currents
    print "Method 3 charge to mass ratios"
    print method3_ratio
    print "Method 3 charge to mass ratio uncertainties"
    print method3_ratio_uncertainty

    method3_average, method3_average_uncertainty = average(method3_ratio,method3_ratio_uncertainty)
    method3_stdev = standard_deviation(method3_ratio, method3_average)
    print " "
    print "Method 3 average"
    print method3_average
    print "Method 3 uncertainty error prop"
    print method3_average_uncertainty*1.96
    print "Method 3 AE stats"
    print method3_stdev*1.96



    print "----------------------------------------\n"

    print "\n-----Averageing all methods-------------"

    all_em = np.array([method1_average,method2_average,method3_average])
    all_prop = np.array([method1_average_uncertainty,method2_average_uncertainty,method3_average_uncertainty])
    all_stats = np.array([method1_stdev,method2_stdev,method3_stdev])

    weighted_avg_stats, weighted_avg_stats_uncert = weighted_average(all_em,all_stats)
    weighted_avg_prop, weighted_avg_prop_uncert = weighted_average(all_em,all_prop)

    print "Weighted average stats"
    print weighted_avg_stats, weighted_avg_stats_uncert*1.96

    print "weighted average prop"
    print weighted_avg_prop, weighted_avg_prop_uncert

    print "----------------------------------------\n"

    print "fastest electron"
    speed = weighted_avg_stats * fastest_electron_radii*method1_B
    print speed
    c = 2.99*10.0**8
    print (speed/c) *100





main()
