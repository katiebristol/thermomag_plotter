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
    """This function processes the data by converting temperature 
    from units of Celsius to Kelvin."""
    # Compute a new column by multiplying column number 1 to Kelvin
    temp_kelvin = (data_array[:,0,None] + 273.15)

    # Append this new column to the existing data array
    processed_data = np.append(data_array, temp_kelvin,1)
    return processed_data

processed_lt_data = process_data(lt_data)
processed_ht_data = process_data(ht_data)
processed_lt2_data = process_data(lt2_data)

# Create a figure of the processed data 
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

def convert_data(filename, output_filename):
    """This function converts the processed data arrays
    into pandas dataframes and outputs them in json format."""    
    all_data = pd.read_csv(filename, header=0)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    lt_input_file = ("DA7_1-L1.csv")
    ht_input_file = ("DA7_1-H1.csv")
    lt2_input_file = ("DA7_1-L2.csv")
    lt_json_output_file = "lt_data_output.json"
    ht_json_output_file = "ht_data_output.json"
    lt2_json_output_file = "lt2_data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    
    lt_input_filename = os.path.join(data_directory,lt_input_file)
    ht_input_filename = os.path.join(data_directory,ht_input_file)
    lt2_input_filename = os.path.join(data_directory,lt2_input_file)
    lt_json_filename = os.path.join(results_directory,lt_json_output_file)
    ht_json_filename = os.path.join(results_directory,ht_json_output_file)
    lt2_json_filename = os.path.join(results_directory,lt2_json_output_file)
    
    convert_data(lt_input_filename, lt_json_filename)
    convert_data(ht_input_filename, ht_json_filename)
    convert_data(lt2_input_filename, lt2_json_filename)

if __name__ == "__main__":
    print(sys.argv)
    plot()