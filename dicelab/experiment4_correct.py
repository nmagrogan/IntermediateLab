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

def chi_squared(theoretical_values, measured_values):
    chi = 0
    if type(theoretical_values) is float :
        for i in range(len(measured_values)):
            chi  += ((theoretical_values - measured_values[i])**2)/ theoretical_values
    else:
        for i in range(len(measured_values)):
            chi += ((theoretical_values[i] - measured_values[i])**2)/ theoretical_values[i]
    return chi


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

##########################################216 rolls################################################################################
    print ""
    print "216 dice calculations"
    print ""

    stdev_outcome_each_dice = (216.*(1./6.0)*(5./6.0))**(0.5)
    print "Standared deviation each dice : " + str(stdev_outcome_each_dice)
    theoretical_value = 216.*(1./6)
    print "Theoretical value and range individual dice 216: " + str(theoretical_value) + "+/-" +str(stdev_outcome_each_dice*1.96)

    print " "
    stdev_outcome_3and18 = (216.*(1./216)*(215./216))**(0.5)
    print "Standared deviation 3 and 18 : " + str(stdev_outcome_3and18)
    theoretical_value_3and18 = 216.*(1./216)
    print "Theoretical value and range 3 and 18 216: " + str(theoretical_value_3and18) + "+/-" +str(stdev_outcome_3and18*1.96)

    print " "
    stdev_outcome_4and17 = (216.*(3./216)*(213./216))**(0.5)
    print "Standared deviation 4 and 17 : " + str(stdev_outcome_4and17)
    theoretical_value_4and17 = 216.*(3./216)
    print "Theoretical value and range 4 and 17 216: " + str(theoretical_value_4and17) + "+/-" +str(stdev_outcome_4and17*1.96)

    print " "
    stdev_outcome_5and16 = (216.*(6./216)*(210./216))**(0.5)
    print "Standared deviation 5 and 16 : " + str(stdev_outcome_5and16)
    theoretical_value_5and16 = 216.*(6./216)
    print "Theoretical value and range 5 and 16  216: " + str(theoretical_value_5and16) + "+/-" +str(stdev_outcome_5and16*1.96)

    print " "
    stdev_outcome_6and15 = (216.*(10./216)*(206./216))**(0.5)
    print "Standared deviation 6 and 15 : " + str(stdev_outcome_6and15)
    theoretical_value_6and15 = 216.*(10./216)
    print "Theoretical value and range 6 and 15  216: " + str(theoretical_value_6and15) + "+/-" +str(stdev_outcome_6and15*1.96)

    print " "
    stdev_outcome_7and14 = (216.*(15./216)*(201./216))**(0.5)
    print "Standared deviation 7 and 14 : " + str(stdev_outcome_7and14)
    theoretical_value_7and14 = 216.*(15./216)
    print "Theoretical value and range 7 and 14  216: " + str(theoretical_value_7and14) + "+/-" +str(stdev_outcome_7and14*1.96)

    print " "
    stdev_outcome_8and13 = (216.*(21./216)*(195./216))**(0.5)
    print "Standared deviation 8 and 13 : " + str(stdev_outcome_8and13)
    theoretical_value_8and13 = 216.*(21./216)
    print "Theoretical value and range 8 and 13  216: " + str(theoretical_value_8and13) + "+/-" +str(stdev_outcome_8and13*1.96)

    print " "
    stdev_outcome_9and12 = (216.*(25./216)*(191./216))**(0.5)
    print "Standared deviation 9 and 12 : " + str(stdev_outcome_5and16)
    theoretical_value_9and12 = 216.*(25./216)
    print "Theoretical value and range 9 and 12  216: " + str(theoretical_value_9and12) + "+/-" +str(stdev_outcome_9and12*1.96)

    print " "
    stdev_outcome_10and11 = (216.*(27./216)*(189./216))**(0.5)
    print "Standared deviation 10 and 11 : " + str(stdev_outcome_5and16)
    theoretical_value_10and11 = 216.*(27./216)
    print "Theoretical value and range 10 and 11  216: " + str(theoretical_value_10and11) + "+/-" +str(stdev_outcome_10and11*1.96)

    theoretical_values=[theoretical_value_3and18,theoretical_value_4and17,theoretical_value_5and16,theoretical_value_6and15,theoretical_value_7and14,theoretical_value_8and13,theoretical_value_9and12,theoretical_value_10and11,
                        theoretical_value_10and11,theoretical_value_9and12,theoretical_value_8and13,theoretical_value_7and14,theoretical_value_6and15,theoretical_value_5and16,theoretical_value_4and17,theoretical_value_3and18]

    n, bins, patches = plt.hist(red1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red dice 216 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_red = chi_squared(theoretical_value,n)
    print "chisquared red 216 " + str(chisquared_red)


    n, bins, patches = plt.hist(green1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green dice 216 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_green = chi_squared(theoretical_value,n)
    print "chisquared green 216 " + str(chisquared_green)



    n, bins, patches = plt.hist(white1, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White dice 216 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_white = chi_squared(theoretical_value,n)
    print "chisquared white 216 " + str(chisquared_white)


    n, bins, patches = plt.hist(total1, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All dice 216 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+3,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_all = chi_squared(theoretical_values,n)
    print "chisquared all 216 " + str(chisquared_all)











##########################################432 rolls################################################################################
    print ""
    print " 432 dice calculations"
    print ""
    stdev_outcome_each_dice = (432.*(1./6.0)*(5./6.0))**(0.5)
    print "Standared deviation each dice : " + str(stdev_outcome_each_dice)
    theoretical_value = 432.*(1./6)
    print "Theoretical value and range individual dice 432: " + str(theoretical_value) + "+/-" +str(stdev_outcome_each_dice*1.96)

    print " "
    stdev_outcome_3and18 = (432.*(1./216)*(215./216))**(0.5)
    print "Standared deviation 3 and 18 : " + str(stdev_outcome_3and18)
    theoretical_value_3and18 = 432.*(1./216)
    print "Theoretical value and range 3 and 18 432: " + str(theoretical_value_3and18) + "+/-" +str(stdev_outcome_3and18*1.96)

    print " "
    stdev_outcome_4and17 = (432.*(3./216)*(213./216))**(0.5)
    print "Standared deviation 4 and 17 : " + str(stdev_outcome_4and17)
    theoretical_value_4and17 = 432.*(3./216)
    print "Theoretical value and range 4 and 17 432: " + str(theoretical_value_4and17) + "+/-" +str(stdev_outcome_4and17*1.96)

    print " "
    stdev_outcome_5and16 = (432.*(6./216)*(210./216))**(0.5)
    print "Standared deviation 5 and 16 : " + str(stdev_outcome_5and16)
    theoretical_value_5and16 = 432.*(6./216)
    print "Theoretical value and range 5 and 16  432: " + str(theoretical_value_5and16) + "+/-" +str(stdev_outcome_5and16*1.96)

    print " "
    stdev_outcome_6and15 = (432.*(10./216)*(206./216))**(0.5)
    print "Standared deviation 6 and 15 : " + str(stdev_outcome_6and15)
    theoretical_value_6and15 = 432.*(10./216)
    print "Theoretical value and range 6 and 15  432: " + str(theoretical_value_6and15) + "+/-" +str(stdev_outcome_6and15*1.96)

    print " "
    stdev_outcome_7and14 = (432.*(15./216)*(201./216))**(0.5)
    print "Standared deviation 7 and 14 : " + str(stdev_outcome_7and14)
    theoretical_value_7and14 = 432.*(15./216)
    print "Theoretical value and range 7 and 14  432: " + str(theoretical_value_7and14) + "+/-" +str(stdev_outcome_7and14*1.96)

    print " "
    stdev_outcome_8and13 = (432.*(21./216)*(195./216))**(0.5)
    print "Standared deviation 8 and 13 : " + str(stdev_outcome_8and13)
    theoretical_value_8and13 = 432.*(21./216)
    print "Theoretical value and range 8 and 13  432: " + str(theoretical_value_8and13) + "+/-" +str(stdev_outcome_8and13*1.96)

    print " "
    stdev_outcome_9and12 = (432.*(25./216)*(191./216))**(0.5)
    print "Standared deviation 9 and 12 : " + str(stdev_outcome_5and16)
    theoretical_value_9and12 = 432.*(25./216)
    print "Theoretical value and range 9 and 12  432: " + str(theoretical_value_9and12) + "+/-" +str(stdev_outcome_9and12*1.96)

    print " "
    stdev_outcome_10and11 = (432.*(27./216)*(189./216))**(0.5)
    print "Standared deviation 10 and 11 : " + str(stdev_outcome_5and16)
    theoretical_value_10and11 = 432.*(27./216)
    print "Theoretical value and range 10 and 11  432: " + str(theoretical_value_10and11) + "+/-" +str(stdev_outcome_10and11*1.96)

    theoretical_values=[theoretical_value_3and18,theoretical_value_4and17,theoretical_value_5and16,theoretical_value_6and15,theoretical_value_7and14,theoretical_value_8and13,theoretical_value_9and12,theoretical_value_10and11,
                        theoretical_value_10and11,theoretical_value_9and12,theoretical_value_8and13,theoretical_value_7and14,theoretical_value_6and15,theoretical_value_5and16,theoretical_value_4and17,theoretical_value_3and18]


    n, bins, patches = plt.hist(red2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red dice 432 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_red = chi_squared(theoretical_value,n)
    print "chisquared red 432 " + str(chisquared_red)

    n, bins, patches = plt.hist(green2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green dice 432 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_green = chi_squared(theoretical_value,n)
    print "chisquared green 432 " + str(chisquared_green)

    n, bins, patches = plt.hist(white2, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White dice 432 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_white = chi_squared(theoretical_value,n)
    print "chisquared white 432 " + str(chisquared_white)

    n, bins, patches = plt.hist(total2, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All dice 432 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+3,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_all = chi_squared(theoretical_values,n)
    print "chisquared all 432 " + str(chisquared_all)





##########################################648 rolls################################################################################
    print ""
    print " 648 dice calculations"
    print ""

    stdev_outcome_each_dice = (648.*(1./6.0)*(5./6.0))**(0.5)
    print "Standared deviation each dice : " + str(stdev_outcome_each_dice)
    theoretical_value = 648.*(1./6)
    print "Theoretical value and range individual dice 648: " + str(theoretical_value) + "+/-" +str(stdev_outcome_each_dice*1.96)

    print " "
    stdev_outcome_3and18 = (648.*(1./216)*(215./216))**(0.5)
    print "Standared deviation 3 and 18 : " + str(stdev_outcome_3and18)
    theoretical_value_3and18 = 648.*(1./216)
    print "Theoretical value and range 3 and 18 648: " + str(theoretical_value_3and18) + "+/-" +str(stdev_outcome_3and18*1.96)

    print " "
    stdev_outcome_4and17 = (648.*(3./216)*(213./216))**(0.5)
    print "Standared deviation 4 and 17 : " + str(stdev_outcome_4and17)
    theoretical_value_4and17 = 648.*(3./216)
    print "Theoretical value and range 4 and 17 648: " + str(theoretical_value_4and17) + "+/-" +str(stdev_outcome_4and17*1.96)

    print " "
    stdev_outcome_5and16 = (648.*(6./216)*(210./216))**(0.5)
    print "Standared deviation 5 and 16 : " + str(stdev_outcome_5and16)
    theoretical_value_5and16 = 648.*(6./216)
    print "Theoretical value and range 5 and 16  648: " + str(theoretical_value_5and16) + "+/-" +str(stdev_outcome_5and16*1.96)

    print " "
    stdev_outcome_6and15 = (648.*(10./216)*(206./216))**(0.5)
    print "Standared deviation 6 and 15 : " + str(stdev_outcome_6and15)
    theoretical_value_6and15 = 648.*(10./216)
    print "Theoretical value and range 6 and 15  648: " + str(theoretical_value_6and15) + "+/-" +str(stdev_outcome_6and15*1.96)

    print " "
    stdev_outcome_7and14 = (648.*(15./216)*(201./216))**(0.5)
    print "Standared deviation 7 and 14 : " + str(stdev_outcome_7and14)
    theoretical_value_7and14 = 648.*(15./216)
    print "Theoretical value and range 7 and 14  648: " + str(theoretical_value_7and14) + "+/-" +str(stdev_outcome_7and14*1.96)

    print " "
    stdev_outcome_8and13 = (648.*(21./216)*(195./216))**(0.5)
    print "Standared deviation 8 and 13 : " + str(stdev_outcome_8and13)
    theoretical_value_8and13 = 648.*(21./216)
    print "Theoretical value and range 8 and 13  648: " + str(theoretical_value_8and13) + "+/-" +str(stdev_outcome_8and13*1.96)

    print " "
    stdev_outcome_9and12 = (648.*(25./216)*(191./216))**(0.5)
    print "Standared deviation 9 and 12 : " + str(stdev_outcome_5and16)
    theoretical_value_9and12 = 648.*(25./216)
    print "Theoretical value and range 9 and 12  648: " + str(theoretical_value_9and12) + "+/-" +str(stdev_outcome_9and12*1.96)

    print " "
    stdev_outcome_10and11 = (648.*(27./216)*(189./216))**(0.5)
    print "Standared deviation 10 and 11 : " + str(stdev_outcome_5and16)
    theoretical_value_10and11 = 648.*(27./216)
    print "Theoretical value and range 10 and 11  648: " + str(theoretical_value_10and11) + "+/-" +str(stdev_outcome_10and11*1.96)

    theoretical_values=[theoretical_value_3and18,theoretical_value_4and17,theoretical_value_5and16,theoretical_value_6and15,theoretical_value_7and14,theoretical_value_8and13,theoretical_value_9and12,theoretical_value_10and11,
                        theoretical_value_10and11,theoretical_value_9and12,theoretical_value_8and13,theoretical_value_7and14,theoretical_value_6and15,theoretical_value_5and16,theoretical_value_4and17,theoretical_value_3and18]


    n, bins, patches = plt.hist(red3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red dice 648 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_red = chi_squared(theoretical_value,n)
    print "chisquared red 648 " + str(chisquared_red)

    n, bins, patches = plt.hist(green3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green dice 648 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_green = chi_squared(theoretical_value,n)
    print "chisquared green 648 " + str(chisquared_green)

    n, bins, patches = plt.hist(white3, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White dice 648 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_white = chi_squared(theoretical_value,n)
    print "chisquared white 648 " + str(chisquared_white)

    n, bins, patches = plt.hist(total3, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All dice 648 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+3,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_all = chi_squared(theoretical_values,n)
    print "chisquared all 648 " + str(chisquared_all)



##########################################864 rolls################################################################################
    print ""
    print " 864 dice calculations"
    print ""

    stdev_outcome_each_dice = (864.*(1./6.0)*(5./6.0))**(0.5)
    print "Standared deviation each dice : " + str(stdev_outcome_each_dice)
    theoretical_value = 864.*(1./6)
    print "Theoretical value and range individual dice 864: " + str(theoretical_value) + "+/-" +str(stdev_outcome_each_dice*1.96)

    print " "
    stdev_outcome_3and18 = (864.*(1./216)*(215./216))**(0.5)
    print "Standared deviation 3 and 18 : " + str(stdev_outcome_3and18)
    theoretical_value_3and18 = 864.*(1./216)
    print "Theoretical value and range 3 and 18 864: " + str(theoretical_value_3and18) + "+/-" +str(stdev_outcome_3and18*1.96)

    print " "
    stdev_outcome_4and17 = (864.*(3./216)*(213./216))**(0.5)
    print "Standared deviation 4 and 17 : " + str(stdev_outcome_4and17)
    theoretical_value_4and17 = 864.*(3./216)
    print "Theoretical value and range 4 and 17 864: " + str(theoretical_value_4and17) + "+/-" +str(stdev_outcome_4and17*1.96)

    print " "
    stdev_outcome_5and16 = (864.*(6./216)*(210./216))**(0.5)
    print "Standared deviation 5 and 16 : " + str(stdev_outcome_5and16)
    theoretical_value_5and16 = 864.*(6./216)
    print "Theoretical value and range 5 and 16  864: " + str(theoretical_value_5and16) + "+/-" +str(stdev_outcome_5and16*1.96)

    print " "
    stdev_outcome_6and15 = (864.*(10./216)*(206./216))**(0.5)
    print "Standared deviation 6 and 15 : " + str(stdev_outcome_6and15)
    theoretical_value_6and15 = 864.*(10./216)
    print "Theoretical value and range 6 and 15  864: " + str(theoretical_value_6and15) + "+/-" +str(stdev_outcome_6and15*1.96)

    print " "
    stdev_outcome_7and14 = (864.*(15./216)*(201./216))**(0.5)
    print "Standared deviation 7 and 14 : " + str(stdev_outcome_7and14)
    theoretical_value_7and14 = 864.*(15./216)
    print "Theoretical value and range 7 and 14  864: " + str(theoretical_value_7and14) + "+/-" +str(stdev_outcome_7and14*1.96)

    print " "
    stdev_outcome_8and13 = (864.*(21./216)*(195./216))**(0.5)
    print "Standared deviation 8 and 13 : " + str(stdev_outcome_8and13)
    theoretical_value_8and13 = 864.*(21./216)
    print "Theoretical value and range 8 and 13  864: " + str(theoretical_value_8and13) + "+/-" +str(stdev_outcome_8and13*1.96)

    print " "
    stdev_outcome_9and12 = (864.*(25./216)*(191./216))**(0.5)
    print "Standared deviation 9 and 12 : " + str(stdev_outcome_5and16)
    theoretical_value_9and12 = 864.*(25./216)
    print "Theoretical value and range 9 and 12  864: " + str(theoretical_value_9and12) + "+/-" +str(stdev_outcome_9and12*1.96)

    print " "
    stdev_outcome_10and11 = (864.*(27./216)*(189./216))**(0.5)
    print "Standared deviation 10 and 11 : " + str(stdev_outcome_5and16)
    theoretical_value_10and11 = 864.*(27./216)
    print "Theoretical value and range 10 and 11  864: " + str(theoretical_value_10and11) + "+/-" +str(stdev_outcome_10and11*1.96)

    theoretical_values=[theoretical_value_3and18,theoretical_value_4and17,theoretical_value_5and16,theoretical_value_6and15,theoretical_value_7and14,theoretical_value_8and13,theoretical_value_9and12,theoretical_value_10and11,
                        theoretical_value_10and11,theoretical_value_9and12,theoretical_value_8and13,theoretical_value_7and14,theoretical_value_6and15,theoretical_value_5and16,theoretical_value_4and17,theoretical_value_3and18]



    n, bins, patches = plt.hist(red, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Red dice 864 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_red = chi_squared(theoretical_value,n)
    print "chisquared red 864 " + str(chisquared_red)

    n, bins, patches = plt.hist(green, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'Green dice 864 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_green = chi_squared(theoretical_value,n)
    print "chisquared green 864 " + str(chisquared_green)

    n, bins, patches = plt.hist(white, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'White dice 864 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+1,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_white = chi_squared(theoretical_value,n)
    print "chisquared white 864 " + str(chisquared_white)

    n, bins, patches = plt.hist(total, bins=[2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5], facecolor='blue', alpha=0.5, ec='black')
    plt.xlabel('Dice Number')
    plt.ylabel('Count')
    plt.title(r'All dice 864 tosses')
    for i in range(len(n)):
        plt.annotate(str(n[i]), xy=(i+3,0),xycoords=('data', 'axes fraction'), xytext=(0, 25), textcoords='offset points', va='top', ha='center')
    plt.show()

    chisquared_all = chi_squared(theoretical_values,n)
    print "chisquared all 864 " + str(chisquared_all)





main()
