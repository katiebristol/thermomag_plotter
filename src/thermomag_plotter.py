# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create arrays with each leg of thermomagnetic data 
raw_lt_data = np.genfromtxt("data/DA7_1-L1.csv", delimiter=',', skip_header=0)
raw_ht_data = np.genfromtxt("data/DA7_1-H1.csv", delimiter=',', skip_header=0)
raw_lt2_data = np.genfromtxt("data/DA7_1-L2.csv", delimiter=',', skip_header=0)
#print(raw_lt_data)

# Select the data range we are interested in, convert it into a new array, full of numbers
lt_data = np.array(raw_lt_data[1:,:], dtype=float)
ht_data = np.array(raw_ht_data[1:,:], dtype=float)
lt2_data = np.array(raw_lt2_data[1:,:], dtype=float)

# Convert temperature units from celsius to kelvin
lt_conversion = (lt_data[:,0,None] + 273.15)
ht_conversion = (ht_data[:,0,None] + 273.15)
lt2_conversion = (lt2_data[:,0,None] + 273.15)

# Append these new columns to the existing data arrays
processed_lt_data = np.append(lt_data, lt_conversion,1)
processed_ht_data = np.append(ht_data, ht_conversion,1)
processed_lt2_data = np.append(lt2_data, lt2_conversion,1)
print (processed_lt_data[1])

# Create a figure of the processed data
thermomag_figure = plt.figure()

## Plotting each dataset as a line
plt.plot(processed_lt_data[:,9],
        processed_lt_data[:,2],
        color='blue', 
        linestyle='dashed', 
        linewidth='1.5', 
        label="L1")

plt.plot(processed_ht_data[:,9],
         processed_ht_data[:,2],
         color='firebrick', 
         linestyle='solid', 
         linewidth='1.5', 
         label="H1")

plt.plot(processed_lt2_data[:,9],
         processed_lt2_data[:,2],
         color='blue', 
         linestyle='dotted',
         linewidth='2',
         label="L2")

## Adding arrows to indicate direction of measurement
plt.arrow(522,2280, 100, 0, head_width=20, head_length=18, fc='k', ec='k')
plt.arrow(852,2119, 15, -150, head_width=18, head_length=22, fc='k', ec='k')
plt.arrow(866,1196, -20, 150, head_width=18, head_length=22, fc='k', ec='k')
plt.arrow(444,1858, -55, 150, head_width=18, head_length=22, fc='k', ec='k')

## Specifying parameters for fonts
titlefont = {'family': 'serif',
             'color': 'black',
             'weight': 'bold',
             'size': 14}
axesfont = {'family': 'sans-serif',
            'style': 'italic',
            'color': 'darkslategray',
            'weight': 'normal',
            'size': 12}

## Adding title, axes labels, and legend
plt.title('Thermomagnetic Behavior', fontdict=titlefont)
plt.xlabel('Temperature (K)', fontdict=axesfont)
plt.ylabel('Magnetic Susceptibility (unitless)', fontdict=axesfont)
plt.text(150, 1600, 'Daule L5', fontdict=axesfont)
plt.text(170, 1530, 'Ordinary Chondrite', fontdict=axesfont)
plt.legend()

## Showing and saving the figure to results folder
plt.show(block=True)
thermomag_figure.savefig('results/thermomag-plot.png')

# Converting the data to pandas dataframes and then outputting as json format
lt_data_pd = pd.read_csv("data/DA7_1-L1.csv", header=0)
#lt_data_pd.info()
lt_data_pd.to_json("results/lt_output.json")
ht_data_pd = pd.read_csv("data/DA7_1-h1.csv", header=0)
#ht_data_pd.info()
ht_data_pd.to_json("results/ht_output.json")
lt2_data_pd = pd.read_csv("data/DA7_1-L2.csv", header=0)
#lt2_data_pd.info()
lt2_data_pd.to_json("results/lt2_output.json")

lt_json_data = pd.read_json("results/lt_output.json")
#lt_json_data.info()
h1_json_data = pd.read_json("results/ht_output.json")
#h1_json_data.info()
lt2_json_data = pd.read_json("results/lt2_output.json")
#lt2_json_data.info()