"""
# Naveen Reddy
# C0838989
# Final Project.
"""
import matplotlib.pyplot as plt
from numpy import random
import numpy as np
import csv  
from matplotlib.animation import FuncAnimation

#Setting the per page year display to 30
limit = 30

# Declaring lists to to used to display data
year = []
rate = []

# Declaring lists to store data to be diaplyed
yearData = []
rateData = []

# Generating random data and storing in x and y lists
for i in range(1900,2022):
    yearData.append(i)
    rateData.append(str(round(random.uniform(1.4,15.78),1)))

# Writing the x and y lists to inflation.csv file
with open('inflation.csv', 'w', encoding='UTF8',newline='') as fileData:
    writer = csv.writer(fileData)
    # Looping through x and y list
    for i in range(len(rateData)):
        text = yearData[i],rateData[i] # Appending each value of x and y with a comma in between
        writer.writerow(text) # Writing each appended value to file

# Clearing teh data from x and y lists after written in file
yearData.clear()
rateData.clear()

# Reading data from inflation.csv file
with open('inflation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # Setting delimiter as a comma
    for row in csv_reader:
        # Reading add data in 1st column (year) to list x and 2nd column (inflation rate) to list y
        yearData.append(int(row[0])) # Data is returned in string and converted to int for x list and float for y string
        rateData.append(float(row[1]))

font1 = {'family':'serif','color':'Crimson','size':20}
font2 = {'family':'serif','color':'coral','size':15}

fig,ax = plt.subplots()
# Setting x axis and y axis limits
ax.set_xlim(1900,1930)
ax.set_ylim(-2,16)
# Setting title of the plot
ax.set_title('Inflation rate from the year 1900 to 2022 showing 30 years at time',fontdict = font1)
# Setting labels of the axis and displayin max and min value from the list
plt.xlabel("Years - From 1900 to 1930",fontdict = font2)
plt.ylabel("Infaltion Rate\nMaximum rate - "+str(max(rateData))+" - Minimum rate - "+str(min(rateData)),fontdict = font2)

line, = ax.plot(0,0)


# Animation frame method to be called from funcAnimation method
def animation_frame(i):
    global limit # Setting limit method as global

    # Called when the entire x list has been iterated i.e the year has been reached to 2022
    if(i == len(yearData)-1) :
        
        limit=30 # limit se set back to 30
        ax.set_xlim(1900,1930) # Axis limits are reset i.e set to 1900 to 1930
        plt.xlabel("Years - From 1900 to 1930") # Label is reset
        # Appending data to year and rate list from x and y list
        year.append(yearData[i])
        rate.append(float(rateData[i]))
        # Shwoing line on graph
        line.set_xdata(year)
        line.set_ydata(rate)
        # Clearing the lists
        year.clear()
        rate.clear()
    
    # Called when limit has been reached
    elif(i == limit):
        # Data is appended to list
        year.append(yearData[i])
        rate.append(float(rateData[i]))
        # Showing data on line
        line.set_xdata(year)
        line.set_ydata(rate)
        # Setting axis limits to the current year and current year + 30 year
        ax.set_xlim(yearData[i],yearData[i]+30)
        # Updating the label of x axis to show the year range being shown
        plt.xlabel("Years - From "+str(yearData[i])+" to "+str(yearData[i]+30))
        # Increasing the limit to do 30 more years
        limit = limit+30
        # Clearing the lists
        year.clear()
        rate.clear()
        # Adding new data to lists after being cleared
        year.append(yearData[i])
        rate.append(float(rateData[i]))
        # Showing the data from teh lists
        line.set_xdata(year)
        line.set_ydata(rate)
    
    else :
        # Adding data to the list
        year.append(yearData[i])
        rate.append(float(rateData[i]))
        # Showing the lines on the graph
        line.set_xdata(year)
        line.set_ydata(rate)
        # Returning line
    return line,

# Calling the funcAnimation method with the arguments:
# figure, 
# animation frame method that is called repeatedly, 
# arange method from numpy sets the range of i in animation_frame method from 0 to 123 with an gap of 1 
# Setting time interval to 150 miliseconds
animation = FuncAnimation(fig, func=animation_frame,frames=np.arange(0,123,1), interval=170)

# Showing the plot
plt.show()