import numpy as np
import scipy as sci
import csv

############ measured data being put into various vars #################
balance_scale_reading_error = 0.05 #grams

small_nails_container = 756.1 #grams
large_nails_container = 922.6 #grams
loops_container = 974.5 #grams

small_nails_full = 1997.5 #grams
large_nails_full = 2519.5 #grams
loops_full = 1149.2 #grams


reader = list(csv.reader(open("small_nails.dat", "rb"), delimiter=' '))
small_nails = np.array(reader).astype('float') #grams

reader = list(csv.reader(open("large_nails.dat", "rb"), delimiter=' '))
large_nails = np.array(reader).astype('float') #grams

reader = list(csv.reader(open("fruit_loops.dat", "rb"), delimiter=' '))
fruit_loops = np.array(reader).astype('float') #grams

#########################################################################


def average(data_set):
    sum = 0
    for val in data_set:
        sum = sum + val[0]
    average = sum/np.size(data_set)
    return average

def standard_deviation(data_set,average):
    sum = 0
    for val in data_set:
        sum = sum + (val[0]-average) ** 2

    standard_deviation = (sum/(np.size(data_set)-1))**(.5)
    return standard_deviation

def number(average, stdev, container, measured_total):

    total = measured_total - container
    total_uncertainty =(balance_scale_reading_error**2 + balance_scale_reading_error**2)**0.5


    number_in = total/average
    number_in_uncertainty = ( (total_uncertainty/total)**2 + (stdev/average)**2  )**0.5 * number_in


    return number_in, number_in_uncertainty


def main():

    small_nails_average = average(small_nails)
    large_nails_average = average(large_nails)
    fruit_loops_average = average(fruit_loops)

    small_nails_SE = standard_deviation(small_nails,small_nails_average)/(np.size(small_nails)**.5)
    large_nails_SE = standard_deviation(large_nails,large_nails_average)/(np.size(large_nails)**.5)
    fruit_loops_SE = standard_deviation(fruit_loops,fruit_loops_average)/(np.size(fruit_loops)**.5)

    print("Small nail: " + str(small_nails_average) + " +/- " + str(1.96*small_nails_SE) + " grams")
    print("Large nail: " + str(large_nails_average) + " +/- " + str(1.96*large_nails_SE) + " grams")
    print("Fruit loop: " + str(fruit_loops_average) + " +/- " + str(1.96*fruit_loops_SE) + " grams")


    small_nails_number, small_nails_number_uncertainty = number(small_nails_average, small_nails_SE, small_nails_container, small_nails_full)
    large_nails_number, large_nails_number_uncertainty = number(large_nails_average, large_nails_SE, large_nails_container, large_nails_full)
    fruit_loops_number, fruit_loops_number_uncertainty = number(fruit_loops_average, fruit_loops_SE, loops_container, loops_full)

    print("Small nails in container: " + str(small_nails_number) + " +/- " + str(1.96*small_nails_number_uncertainty))
    print("Large nails in container: " + str(large_nails_number) + " +/- " + str(1.96*large_nails_number_uncertainty))
    print("Fruit loops in container: " + str(fruit_loops_number) + " +/- " + str(1.96*fruit_loops_number_uncertainty))



main()
