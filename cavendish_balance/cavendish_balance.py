import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import optimize
from math import *
import sys

############ measured data being put into various vars #################
positions = np.loadtxt(str(sys.argv[1]), dtype='float')
positions = positions/1000 #m
times =np.loadtxt(str(sys.argv[2]), dtype='float')


method3_positions = positions[3:24]
method3_times = times[3:24]

G_expected = 6.67408 * 10**-11

radius = 9.55 #mm
radius = radius/1000 #m
radius_uncertainty = 0.005/1000

d = 50.0 #mm
d = d/1000 #m
d_uncertainty = 0.5/1000

b = 46.5 #mm
b = b/1000 #m
b_uncertainty = 0.05/1000

m1 = 1.5 #kg
m1_uncertainty = 0.05

####### need to re measure L ##########
L = 3.73 #m
L_uncertainty = 0.005

#for method 1
dimensionless_b = b**3 / (b**2 + 4*d**2)**(3/2)
print dimensionless_b
#########################################################################

def percent_error(expected,measured):
    return (abs(expected-measured)/expected) * 100

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

def G_method1(period,period_uncertainty, equilibrium_change,delta_S_uncertainty):

    delta_S = equilibrium_change/ 1000.0 # mm to m
    delta_S_uncertainty = delta_S_uncertainty/1000
    numerator = (d**2)+(2.0/5)*(radius**2)
    denomenator = (period**2)*m1*L*d
    G = (pi**2)*delta_S*(b**2)*(numerator/denomenator)


    #### error prop
    d_deltaS = pi**2*b**2 * (numerator/denomenator)

    d_db = 2*pi**2*delta_S*b* (numerator/denomenator)

    denomenator = (period**3)*m1*L*d
    d_dT = -2*pi**2*delta_S*b**2 * (numerator/denomenator)

    denomenator = (period**2)*m1**2*L*d
    d_dm = -pi**2 *delta_S*b**2 * (numerator/denomenator)

    denomenator = (period**2)*m1*L**2*d
    d_dL = -pi**2*delta_S*b**2 *(numerator/denomenator)

    numerator = (4.0/5)*(radius)
    denomenator = (period**2)*m1*L*d
    d_dr = pi**2*delta_S*b**2 * (numerator/denomenator)

    numerator = 5*d**2 - 2*radius**2
    denomenator = 5*d**2*L*m1*period**2
    d_dd = pi**2*delta_S*b**2 * (numerator/denomenator)

    G_uncertainty = sqrt((d_deltaS*delta_S_uncertainty)**2 + (d_db*b_uncertainty)**2 + (d_dT*period_uncertainty)**2 + (d_dm*m1_uncertainty)**2 + (d_dL*L_uncertainty)**2 + (d_dr*radius_uncertainty)**2 + (d_dd*d_uncertainty)**2)

    return G, G_uncertainty



def G_method1_correction(G):
    return G/(1-dimensionless_b)

def G_method3(slope, slope_uncertainty):
    G = (d*(b**2)*slope)/(m1*2*L)
    G_uncertainty = G*sqrt((d_uncertainty/d)**2 + (2*b_uncertainty/b)**2 + (slope_uncertainty/slope)**2 + (m1_uncertainty/m1)**2 + (L_uncertainty/L)**2 )/2
    return G, G_uncertainty

def method2_function(x,A1,A2,A3,A4,A5):
    return A1*np.exp(-A2*x)*np.cos((x*2*np.pi)/A3 + A4) + A5

def main():
    #print G_method1(540,95) from last groups data
    #period = 1995.55/4
    period = 4461.87/9
    period_uncertainty = 0.005/9
    method1, method1_uncertainty = G_method1(period,period_uncertainty ,96.68, 0.005)
    method1_correction = G_method1_correction(method1)
    print "\n-----Method 1 ----------"
    print "method 1, uncetainty "
    print method1, method1_uncertainty*1.96
    print "percent error"
    print percent_error(G_expected,method1)
    print "method 1 correction"
    print method1_correction
    print "percent error"
    print percent_error(G_expected,method1_correction)

    print "\n-----Method 2-----------"

    params, params_covariance = optimize.curve_fit(method2_function, times, positions, [.175,.0001,500,1,0.08])
    #print params, params_covariance
    perr = np.sqrt(np.diag(params_covariance))
    print params
    print perr

    #y = method2_function(x,params[0],params[1],params[2],params[3],params[4])
    plt.plot(times, method2_function(times,params[0],params[1],params[2],params[3],params[4]))

    method2, method2_uncertainty = G_method1(params[2],perr[2] ,params[4]*1000, perr[4]*1000)
    method2_correction = G_method1_correction(method2)
    print "\nmethod 2, uncetainty "
    print method2, method2_uncertainty*1.96
    print "percent error"
    print percent_error(G_expected,method2)
    print "method 2 correction"
    print method2_correction
    print "percent error"
    print percent_error(G_expected,method2_correction)

    #x = np.linspace(3,6.1,100)
    #y = n_slope*x+n_yint
    plt.plot(times,positions,'bo')
    #plt.plot(1/(wavelengths_mercury**2), n_average,'bo')
    #plt.errorbar(1/(wavelengths_mercury**2),n_average,yerr=n_error,fmt="o")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.title("Position vs Time graph")
    plt.show()


    print "\n-----Method 3 -----------"
    n_slope, n_yint, n_sigma_slope, n_sigma_yint = regression(method3_times**2, method3_positions)
    print "slope"
    print n_slope,n_sigma_slope*1.96
    print "yint"
    print n_yint, n_sigma_yint*1.96

    print "\nmethod 3"
    method3, method3_uncertainty = G_method3(n_slope,n_sigma_slope)
    print method3, method3_uncertainty*1.96
    print "percent error"
    print percent_error(G_expected,method3)


    x = np.linspace(0,13000,100)
    y = n_slope*x+n_yint
    plt.plot(x,y,'-b')

    plt.plot(method3_times**2,method3_positions,'bo')
    plt.xlabel("Time^2 (s^2)")
    plt.ylabel("Position (m)")
    plt.title("Position vs Time graph \nMethod 3")
    plt.show()

main()
