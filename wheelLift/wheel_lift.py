import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

############ measured data being put into various vars #################
heights = []
with open('heights.dat') as f:
    for line in f.readlines():
        heights.append(float(line))

forces=[]
with open('force.dat') as f:
    for line in f.readlines():
        forces.append(float(line))



pull_angle = 0 #degrees +/- .5 degrees
radius_of_wheel = 28.7 # cm +/- .5 cm
radius_of_wheel = radius_of_wheel/100 #m
radius_uncertainty = 0.5/100
mass_of_wheel = 1074.6 # g +/- .05 g
mass_of_wheel = mass_of_wheel/1000 #kg
mass_of_wheel_uncertainty = .05/1000
g = 9.81 # m/s^2


forces_by_height = []

for i in range(14):
    forces_by_height.append(forces[i*3:(i+1)*3])


forces_by_height.append(forces[14*3:14*3+24])
forces_by_height.append(forces[14*3+24:14*3+48])
#now forces_by_height[1] has the forces for heigh 1 in my tirals etc.

heights_by_height = []

for i in range(14):
    heights_by_height.append(heights[i*3:(i+1)*3])


heights_by_height.append(heights[14*3:14*3+24])
heights_by_height.append(heights[14*3+24:14*3+48])
#heights_by_height parallel array to forces_by_height

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

def wheel_force(height):
    height = height / 100 #m
    height_uncertainty = .05/100
    mg = mass_of_wheel*g


    sqrt_term = (2*radius_of_wheel*height - height**2)**0.5
    denomenator = radius_of_wheel-height


    force = mg*(sqrt_term/denomenator)

    dfdm = g*((2*radius_of_wheel*height-height**2)**.5/(radius_of_wheel-height))
    dfdr = (-1*g*height*mass_of_wheel*radius_of_wheel)/((-1*height*(height-2*radius_of_wheel))**.5)
    dfdh = (g*mass_of_wheel*(radius_of_wheel**2))/(((-1*height*(height-2*radius_of_wheel))**.5)*(radius_of_wheel-height)**2)
    uncertainty = ((dfdm*mass_of_wheel_uncertainty)**2 + (dfdr*radius_uncertainty)**2 + (dfdh*height_uncertainty)**2)**.5

    return force,uncertainty

def chi_squared(theoretical_value, measured_values):
    chi = 0
    for i in range(len(measured_values)):
        chi  += ((theoretical_value - measured_values[i])**2)/ theoretical_value
    return chi

def chi_squared2(expected, observed):
    chi = 0
    for i in range(len(expected)):
        chi += ((observed[i]-expected[i])**2)/ expected[i]
    return chi


def main():

    averages = []
    for i in range(len(heights_by_height)):
        averages.append(average(forces_by_height[i]))

    for i in range(len(heights_by_height)-2):
        print "Barrier height " + str(i) + " height: " + str(heights_by_height[i][1]) + "cm,  mean force: " + str(averages[i]) + " N"

    stdev_24pulls = []
    stdev_mean_24pulls = []
    AE_24pulls = []
    for i in range(len(heights_by_height)-2,len(heights_by_height)):
        stdev_24pulls.append(standard_deviation(forces_by_height[i],averages[i]))
    for i in range(2):
        stdev_mean_24pulls.append(stdev_24pulls[i]/(24**.5))
        AE_24pulls.append(stdev_mean_24pulls[i]*1.96)

    for i in range(2):
        print "Barrier height " + str(i+14) + " height: " + str(heights_by_height[i+14][1]) + "cm,  mean force: " + str(averages[i+14]) + "N stdev: " + str(stdev_24pulls[i]) + " stdev of the mean: " + str(stdev_mean_24pulls[i]) + " AE: " + str(AE_24pulls[i])



    expected_in_bins = [24.*.16,24.*.34,24.*.34,24.*.16]
    actual_in_bins1 = [0,0,0,0]

    mean = averages[14]
    stdev = stdev_24pulls[0]
    mean_minus_stdev = (averages[14]-stdev_24pulls[0])
    mean_plus_stdev = (averages[14]+stdev_24pulls[0])

    for j in range(len(forces_by_height[14])):
        if forces_by_height[14][j] < mean_minus_stdev:
            actual_in_bins1[0] += 1
        if forces_by_height[14][j]  < mean and forces_by_height[14][j] > mean_minus_stdev:
            actual_in_bins1[1] += 1
        if forces_by_height[14][j]  > mean and forces_by_height[14][j] < mean_plus_stdev:
            actual_in_bins1[2] += 1
        if forces_by_height[14][j]  > mean_plus_stdev:
            actual_in_bins1[3] += 1

    actual_in_bins2 = [0,0,0,0]
    for j in range(len(forces_by_height[15])):
        if forces_by_height[15][j]  < (averages[15]-stdev_24pulls[1]):
            actual_in_bins2[0] += 1
        if forces_by_height[15][j]  < averages[15] and forces_by_height[15][j] > (averages[15]-stdev_24pulls[1]):
            actual_in_bins2[1] += 1
        if forces_by_height[15][j]  > averages[15] and forces_by_height[15][j] < (averages[15]+stdev_24pulls[1]) :
            actual_in_bins2[2] += 1
        if forces_by_height[15][j]  > (averages[15]+stdev_24pulls[1]) :
            actual_in_bins2[3] += 1
    print " "
    print "expected_in_bins"
    print expected_in_bins
    print "actual_in_bins1"
    print  actual_in_bins1
    print "actual_in_bins2"
    print actual_in_bins2

    chi_squared_first_height = chi_squared2(expected_in_bins,actual_in_bins1)
    chi_squared_second_height = chi_squared2(expected_in_bins,actual_in_bins2)

    print "chi_squared_first_height"
    print chi_squared_first_height
    print "chi_squared_second_height"
    print chi_squared_second_height
    print " "


    print " "
    print "24Height 1 stdev: " + str(stdev_mean_24pulls[0]) + " fractional deviation " + str(stdev_mean_24pulls[0]/averages[14])
    print "24Height 2 stdev: " + str(stdev_mean_24pulls[1]) + " fractional deviation " + str(stdev_mean_24pulls[1]/averages[15])
    print stdev_mean_24pulls[0],averages[14]
    print stdev_mean_24pulls[1], averages[15]

    fractional_deviation = average([stdev_mean_24pulls[0],stdev_mean_24pulls[1]])
    print "fractional_deviation: " + str(fractional_deviation)
    stdev_mean_other_14_heights = [None]*14
    for i in range(14):
        stdev_mean_other_14_heights[i] = averages[i]*fractional_deviation
    print "average, stdv mean, Associated error"
    for i in range(14):
        print str(averages[i]) + ", " + str(stdev_mean_other_14_heights[i]) + ", " + str(stdev_mean_other_14_heights[i]*1.96)
    print " "

    theoretical_force = [None]*16
    theoretical_uncertainty = [None]*16
    for i in range(len(heights_by_height)):
        theoretical_force[i],theoretical_uncertainty[i] = wheel_force(heights_by_height[i][1])

    print "Average force, theoretical force, uncertainty, 2sigma"
    for i in range(len(averages)):
        print str(averages[i]) + ", " + str(theoretical_force[i]) + ", " + str(theoretical_uncertainty[i]) +", "+  str(theoretical_uncertainty[i]*2)
    print " "

    print "expected numnber of agreements between theoru and experiment for 1sigma"
    print .68*16
    print "expected numnber of agreements between theoru and experiment for 1sigma"
    print .954*16
    print "expected numnber of agreements between theoru and experiment for 95% confidence"
    print .95*16
    print " "

    xsquared = 0
    sumx = 0
    sumxy=0
    sumy=0
    N = len(forces)
    for i in range(N):
        xsquared += heights[i]**2
        sumx += heights[i]
        sumxy +=forces[i]*heights[i]
        sumy += forces[i]

    delta = (N*xsquared)-(sumx)**2
    yint = ((xsquared*sumy)-(sumx*sumxy))/delta
    slope = (N*sumxy-sumx*sumy)/delta
    sigmaysum=0
    for i in range(N):
        sigmaysum += (forces[i] - yint -slope*heights[i])**2
    sigmay = ((1/(N-2.0))*sigmaysum)**0.5
    sigmayint = sigmay*(xsquared/delta)**0.5
    sigmaslope = sigmay*(N/delta)**0.5
    print "slope, sigma slope , yint sigma yint"
    print str(slope) + " "  + str(sigmaslope*1.96) + ", " + str(yint) + ", " + str(sigmayint*1.96)
    plt.plot(heights,forces,'bo')
    plt.xlabel("height(cm)")
    plt.ylabel("Force(N)")
    plt.title("Fmin as a function of height")
    plt.show()

main()
