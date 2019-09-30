import numpy as np
import scipy as sci
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

############ measured data being put into various vars #################
reader = list(csv.reader(open("red.dat", "rb"), delimiter=' '))
red = np.array(reader).astype('float')

reader = list(csv.reader(open("green.dat", "rb"), delimiter=' '))
green = np.array(reader).astype('float')

reader = list(csv.reader(open("white.dat", "rb"), delimiter=' '))
white = np.array(reader).astype('float')

total = red + green + white


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



def main():
    red1 = red[0:216]
    red2 = red[0:432]
    red3 = red[0:648]

    green1 = green[0:216]
    green2 = green[0:432]
    green3 = green[0:648]

    white1 = white[0:216]
    white2 = white[0:432]
    white3 = white[0:648]

    total1 = total[0:216]
    total2 = total[0:432]
    total3 = total[0:648]

    #for i in range(len(red1)):
        #print str(i) + " " + str(red1[i])+ " " + str(white1[i]) + " " + str(green1[i]) + str(total1[i])


    red1_average = average(red1)
    red1_stdev = standard_deviation(red1,red1_average)
    white1_average = average(white1)
    white1_stdev = standard_deviation(white1,white1_average)
    green1_average = average(green1)
    green1_stdev = standard_deviation(green1,green1_average)
    total1_average = average(total1)
    total1_stdev = standard_deviation(total1,total1_average)
    
    print "red1 average: " + str(red1_average) + " stdev: " + str(red1_stdev)
    print "green1 average: " + str(green1_average) + " stdev: " + str(green1_stdev)
    print "white1 average: " + str(white1_average) + " stdev: " + str(white1_stdev)
    print "total1 average: " + str(total1_average) + " stdev: " + str(total1_stdev)

    n, bins, patches = plt.hist(red1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red die 216 tosses')
    plt.show()

    n, bins, patches = plt.hist(green1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green die 216 tosses')
    plt.show()

    n, bins, patches = plt.hist(white1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White die 216 tosses')
    plt.show()

    n, bins, patches = plt.hist(total1, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All die 216 tosses')
    plt.show()


    red2_average = average(red2)
    red2_stdev = standard_deviation(red2,red2_average)
    white2_average = average(white2)
    white2_stdev = standard_deviation(white2,white2_average)
    green2_average = average(green2)
    green2_stdev = standard_deviation(green2,green2_average)
    total2_average = average(total2)
    total2_stdev = standard_deviation(total2,total2_average)

    print " "
    print "red2 average: " + str(red2_average) + " stdev: " + str(red2_stdev)
    print "green2 average: " + str(green2_average) + " stdev: " + str(green2_stdev)
    print "white2 average: " + str(white2_average) + " stdev: " + str(white2_stdev)
    print "total2 average: " + str(total2_average) + " stdev: " + str(total2_stdev)


    n, bins, patches = plt.hist(red2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red die 432 tosses')
    plt.show()

    n, bins, patches = plt.hist(green2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green die 432 tosses')
    plt.show()

    n, bins, patches = plt.hist(white2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White die 432 tosses')
    plt.show()

    n, bins, patches = plt.hist(total2, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All die 432 tosses')
    plt.show()






    red3_average = average(red3)
    red3_stdev = standard_deviation(red3,red3_average)
    white3_average = average(white3)
    white3_stdev = standard_deviation(white3,white3_average)
    green3_average = average(green3)
    green3_stdev = standard_deviation(green3,green3_average)
    total3_average = average(total3)
    total3_stdev = standard_deviation(total3,total3_average)

    print " "
    print "red3 average: " + str(red3_average) + " stdev: " + str(red3_stdev)
    print "green3 average: " + str(green3_average) + " stdev: " + str(green3_stdev)
    print "white3 average: " + str(white3_average) + " stdev: " + str(white3_stdev)
    print "total3 average: " + str(total3_average) + " stdev: " + str(total3_stdev)


    n, bins, patches = plt.hist(red3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red die 648 tosses')
    plt.show()

    n, bins, patches = plt.hist(green3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green die 648 tosses')
    plt.show()

    n, bins, patches = plt.hist(white3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White die 648 tosses')
    plt.show()

    n, bins, patches = plt.hist(total3, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All die 648 tosses')
    plt.show()






    red_average = average(red)
    red_stdev = standard_deviation(red,red_average)
    white_average = average(white)
    white_stdev = standard_deviation(white,white_average)
    green_average = average(green)
    green_stdev = standard_deviation(green,green_average)
    total_average = average(total)
    total_stdev = standard_deviation(total,total_average)

    print " "
    print "red average: " + str(red_average) + " stdev: " + str(red_stdev)
    print "green average: " + str(green_average) + " stdev: " + str(green_stdev)
    print "white average: " + str(white_average) + " stdev: " + str(white_stdev)
    print "total average: " + str(total_average) + " stdev: " + str(total_stdev)


    n, bins, patches = plt.hist(red, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red die 864 tosses')
    plt.show()

    n, bins, patches = plt.hist(green, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green die 864 tosses')
    plt.show()

    n, bins, patches = plt.hist(white, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White die 864 tosses')
    plt.show()

    n, bins, patches = plt.hist(total, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All die 864 tosses')
    plt.show()





main()
