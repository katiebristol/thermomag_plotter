# Thermomag Plotter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Purpose

This software was created to streamline the process of plotting thermomagnetic curves with matplotlib.
It was designed for use with data files output by AGICO MFK1-FA Kappabridges but may work with other 
AGICO instruments as well. The script takes low- and high-temperature thermomagnetic data, converts units
of temperature from Celsius to Kelvin, and then plots the data using a figure scheme that is common in 
the field of paleomagnetism/rock magnetism.

## Inputs

This software requires three input files:
-Pre-heating low-temperature thermomagnetic susceptibility
-High-temperature thermomagnetic susceptibility
-Post-heating low-temperature thermomagnetic susceptibility

All files should be converted from their original .clw and .cur files to .csv format before using this software.

## Outputs

If inputs are correct, the software should output a figure (.pdf extension) of the thermomagnetic curves. 
In addition, the corrected data files will be output in .json format. 

## Notes

The arrows indicating the direction of measurement will need to be tailored to each set of data. To do this,
edit the x, y, dx, dy parameters of each arrow. For a more detailed description, see:
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html

## License

This Simple Plotting Library is published under the [MIT license](LICENSE.txt).