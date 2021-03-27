# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

def read_data(filename, delimiter=',', starting_row=0):
        """This function reads data from a specified filename.
        The specified filename should point to a .csv file."""
        # Create an array (a multi-dimensional table) out of our data file, full of text
        thermomag_data = np.genfromtxt(filename, delimiter=delimiter, skip_header=0)

        # Select the data range we are interested in, convert it into a new array, full of numbers
        data_array = np.array(thermomag_data[starting_row:,:], dtype=float)
        return data_array

lt_data = read_data("data/DA7_1-L1.csv")
ht_data = read_data("data/DA7_1-H1.csv")
lt2_data = read_data("data/DA7_1-L2.csv")

def process_data(data_array):
    # Compute a new column by multiplying column number 1 to Kelvin
    temp_kelvin = (data_array[:,0,None] + 273.15)

    # Append this new column to the existing temperature_data array
    processed_data = np.append(data_array, temp_kelvin,1)
    return processed_data

processed_lt_data = process_data(lt_data)
processed_ht_data = process_data(ht_data)
processed_lt2_data = process_data(lt2_data)
print(processed_ht_data)

# Create a figure of the processed data
## I tried everything I could think of to make this a function but nothing worked
## My issue seems that each dataset (lt, ht, lt2) require different parameters for plotting so one function wouldn't work.
## I tried an if statement to at least separate the lt's from ht but could not get all three to plot on one graph
## without it yelling at me about "unexpected" indents. I need to get gud. 
thermomag_figure = plt.figure()

## Plotting each dataset as a line with unique colors and line styles
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

# Converting the data to pandas dataframes and then outputting as .json format
## Maybe this can be a function, try later 
#lt_data_pd = pd.read_csv("data/DA7_1-L1.csv", header=0)
#lt_data_pd.to_json("results/lt_output.json")
#ht_data_pd = pd.read_csv("data/DA7_1-h1.csv", header=0)
#ht_data_pd.to_json("results/ht_output.json")
#lt2_data_pd = pd.read_csv("data/DA7_1-L2.csv", header=0)
#lt2_data_pd.to_json("results/lt2_output.json")

#lt_json_data = pd.read_json("results/lt_output.json")
#h1_json_data = pd.read_json("results/ht_output.json")
#lt2_json_data = pd.read_json("results/lt2_output.json")

def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, header=0)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    input_file = ("DA7_1-L1.csv", "DA7_1-H1.csv", "DA7_1-L2.csv")
    plot_file = "thermomag_plot.pdf"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    
    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)
    
    data_array = read_data(input_filename, starting_row=0)
    processed_data = process_data(data_array)
#    plot_data(processed_data, plot_filename)
    convert_data(input_filename, json_filename)

if __name__ == "__main__":
    print(sys.argv)
    plot()