import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import *

############ measured data being put into various vars #################
method1_location = np.loadtxt('method1_location.txt', dtype='float') #mm
method1_location = method1_location/1000 #m

method1_current = np.loadtxt('method1_current.txt',dtype='float') #A

method2_periods = np.loadtxt('method2_periods.txt', dtype='float')
method2_periods = method2_periods/20 #s
method2_currents = np.loadtxt('method2_currents.txt', dtype='float') #A


method3_currents = np.loadtxt('method3_currents.txt', dtype='float') #A

method4_currents = np.loadtxt('method4_currents.txt',dtype='float') #A
method4_forces = np.loadtxt('method4_forces.txt',dtype='float') #V

method5_calib_current = np.loadtxt('method5_calib_current.txt',dtype='float') #A
method5_calib_voltage = np.loadtxt('method5_calib_voltage.txt',dtype='float') #V


method5_distances = np.loadtxt('method5_distances.txt',dtype='float')#cm
method5_distances = method5_distances/100 #m
method5_voltages = np.loadtxt('method5_voltages.txt',dtype='float')#V


##throwing out last 3 values
method5_distances = method5_distances[0:8]
method5_voltages = method5_voltages[0:8]

caliper_uncertainty = 0.005 #mm
caliper_uncertainty = caliper_uncertainty/1000 #m

scale_uncertainty = 0.0005 #g
scale_uncertainty = scale_uncertainty/1000 #kg

ammeter_uncertainty = 0.05 #A

d_ball = 53.77 #mm
d_ball = d_ball/1000 #m

mass_ball = 140.093 #g
mass_ball = mass_ball/1000 #kg

length_hand = 12.47 #mm
length_hand = length_hand/1000

len_alum_rod = 139.82 #mm
len_alum_rod = len_alum_rod/1000 #m

mass_alum_rod = 0.853 #g
mass_alum_rod = mass_alum_rod/1000 #kg

distance_ball_end_rod = 115.43 #mm
distance_ball_end_rod = distance_ball_end_rod/1000 #m

mass_slider = 1.336 #g
mass_slider = mass_slider/1000 #kg

N_coils = 195

eff_rad_coils = 0.109 #m
eff_sep_distance = 0.138 #m

mu_naught = 4*pi*(10**-7) #H/m

radius_ball = d_ball/2
radius_uncertainty = caliper_uncertainty/2

ball_moment = (2.0/5)*mass_ball*(radius_ball)**2
dI_dm = (2.0/5)*radius_ball**2
dI_dR = (4.0/5)*mass_ball*radius_ball
ball_uncertainty = sqrt( (dI_dm*scale_uncertainty)**2 + (dI_dR*caliper_uncertainty)**2)
print "Ball moment"
print ball_moment, ball_uncertainty


method3_omega= np.loadtxt('method3_omega.txt', dtype='float')
method3_omega= (2*pi)/method3_omega
method3_L = 2*pi*5 * ball_moment

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

A = (N_coils*mu_naught*eff_rad_coils**2)/2
B = 2/((eff_rad_coils**2 + (eff_sep_distance/2)**2)**(3/2.0))
C1 = A*B
print "C1", C1

def magnetic_field_constant(I):
    B = C1*I
    return B

A = (3*N_coils*mu_naught*eff_rad_coils**2*eff_sep_distance)/2
B = 1/((eff_sep_distance**2)/4 + eff_rad_coils**2)**(5/2.0)
C2 = A*B
print "C2", C2
def magnetic_field_gradient(I):
    dbdz = C2*I
    return dbdz

def method2_magnetic_moment(slope,slope_uncertainty):
    moment = (4*(pi**2)*ball_moment)/slope
    du_ds = -4*(pi**2)*ball_moment/slope**2
    du_dI = 4*(pi**2)/slope
    moment_uncertainty = sqrt((du_ds*slope_uncertainty)**2+ (du_dI*ball_uncertainty)**2)
    return moment, moment_uncertainty


def main():

############ METHOD 1 #############################
    print "\n---------Method 1 ----------------"
    method1_B_fields = magnetic_field_constant(method1_current)

    method1_r = method1_location+length_hand + d_ball/2

    slope, yint, sigma_slope, sigma_yint = regression(method1_B_fields, method1_r)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(0.0025,.006,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    plt.plot(method1_B_fields, method1_r,'bo')
    #plt.errorbar(1/method2_B_fields, averages_periods**2,yerr=(stdev_mean_periods*1.96)**2,fmt="o")
    plt.xlabel("B [T]")
    plt.ylabel("r [m] ")
    plt.title("r as a function of B ")
    plt.show()

    y_int_expected = -mass_alum_rod*(len_alum_rod/2)/mass_slider
    print "y_int_expected"
    print y_int_expected

    moment1 = slope*mass_slider*9.81
    moment1_uncertainty = moment1*sqrt((sigma_slope/slope)**2 + (scale_uncertainty/mass_slider)**2)
    print "moment method 1"
    print moment1, moment1_uncertainty*1.96


    print "-------------------------------\n"
############# METHOD 2 #############################
    print "\n---------Method 2 ----------------"
    method2_B_fields = magnetic_field_constant(method2_currents)


    averages_periods = np.array([average(period) for period in method2_periods])
    stdev_periods = np.array([standard_deviation(period,average_value) for period,average_value in zip(method2_periods,averages_periods)])
    stdev_mean_periods = stdev_periods/sqrt(5)

    '''
    print ""
    print "Periods average"
    print averages_periods
    print "Period 1.96*stdev(mean angles)"
    print stdev_mean_periods*1.96
    '''

    slope, yint, sigma_slope, sigma_yint = regression(1/method2_B_fields, averages_periods**2)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(150,750,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    #plt.plot(1/method2_B_fields, averages_periods**2,'bo')
    plt.errorbar(1/method2_B_fields, averages_periods**2,yerr=(stdev_mean_periods*1.96)**2,fmt="o")
    plt.xlabel("Period^2 [s^2]")
    plt.ylabel("1/B [1/T]")
    plt.title("T^2 as a function of 1/B")
    plt.show()

    moment2, moment2_uncertainty = method2_magnetic_moment(slope, sigma_slope)
    print "Method 2 moment "
    print moment2, moment2_uncertainty*1.96

    print "-------------------------------\n"


############# METHOD 3 #############################
    print "\n---------Method 3 ----------------"
    method3_Bfields = magnetic_field_constant(method3_currents)


    slope, yint, sigma_slope, sigma_yint = regression(method3_Bfields/method3_L,method3_omega)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(1,4.5,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    plt.plot(method3_Bfields/method3_L,method3_omega,'bo')
    #plt.errorbar(1/method2_B_fields, averages_periods**2,yerr=(stdev_mean_periods*1.96)**2,fmt="o")
    plt.xlabel("B/L [T s/kg m^2]")
    plt.ylabel("Angular frequency [Hz] ")
    plt.title("Angular frequency as a function of B/L")
    plt.show()


    print "-------------------------------\n"

############# METHOD 4 #############################
    print "\n---------Method 4 ----------------"
    method4_gradient = magnetic_field_gradient(method4_currents)

    slope, yint, sigma_slope, sigma_yint = regression(method4_gradient,method4_forces)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(0,0.07,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    plt.plot(method4_gradient,method4_forces,'bo')
    plt.xlabel("Magnetic Field Gradient [T/m]")
    plt.ylabel("Force [N]")
    plt.title("Gravitational force as a function of magnetic field gradient")
    plt.show()

    print "-------------------------------\n"


############# METHOD 5 #############################
    print "\n---------Method 5 ----------------"
    method5_calib_field = magnetic_field_constant(method5_calib_current) #T

    slope, yint, sigma_slope, sigma_yint = regression(method5_calib_voltage, method5_calib_field)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(0,5.5,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    plt.plot(method5_calib_voltage, method5_calib_field,'bo')
    #plt.errorbar(1/method2_B_fields, averages_periods**2,yerr=(stdev_mean_periods*1.96)**2,fmt="o")
    plt.xlabel("voltage [V]")
    plt.ylabel("B [T]")
    plt.title("B as a function of voltage")
    plt.show()
    print " "

##########end of calibration ##################

    method5_fields = method5_voltages*slope


    slope, yint, sigma_slope, sigma_yint = regression(1/(method5_distances**3),method5_fields)
    print "slope"
    print slope,sigma_slope*1.96
    print "yint"
    print yint, sigma_yint*1.96

    x = np.linspace(1500,10000,100)
    y = slope*x+yint
    plt.plot(x,y,'-b')

    plt.plot(1/(method5_distances**3),method5_fields,'bo')
    #plt.errorbar(1/method2_B_fields, averages_periods**2,yerr=(stdev_mean_periods*1.96)**2,fmt="o")
    plt.xlabel("1/distance^3 [1/m^3]")
    plt.ylabel("B [T] ")
    plt.title("B as a function of 1/distance^3")
    plt.show()

    method5_moment = (2*pi/mu_naught)*slope
    print "method5 moment"
    print method5_moment
    method5_moment_uncertainty = (2*pi/mu_naught)*sigma_slope
    print "method5 moment uncertainty"
    print method5_moment_uncertainty *1.96



    print "-------------------------------\n"

main()
