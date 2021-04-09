"""This file contains all tests for our plotting libarary."""

import sys, os
import numpy as np
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

import src.thermomag_plotter as thermomag_plotter

def test_plot():
    assert(thermomag_plotter.plot() == None)

def test_process_data():
    input_data = np.array([[0,0],[1,100]])
    function_output = thermomag_plotter.process_data(input_data)
    expected_output = np.array([[0,0,273.15],[1,100,373.15]])
    """The input can maybe be arbitrary? and then function is just my function and
    then expected output is input,what-it-should-be I guess?"""
    
    assert(np.all(function_output == expected_output))

def test_read_data():
    lt_input_file = ("DA7_1-L1.csv")
    ht_input_file = ("DA7_1-H1.csv")
    lt2_input_file = ("DA7_1-L2.csv")
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    lt_input_filename = os.path.join(data_directory,lt_input_file)
    ht_input_filename = os.path.join(data_directory,ht_input_file)
    lt2_input_filename = os.path.join(data_directory,lt2_input_file)
    lt_data = thermomag_plotter.read_data(lt_input_filename)
    ht_data = thermomag_plotter.read_data(ht_input_filename)
    lt2_data = thermomag_plotter.read_data(lt2_input_filename)

    assert(lt_data.shape == (206,8))
    assert(ht_data.shape == (311,8))
    assert(lt2_data.shape == (207,8))
    assert(lt_data[0,1] == 2200.3)
    assert(ht_data[0,1] == 2142)
    assert(lt2_data[0,1] == 2225)

def test_plot_data():
    plot_file = "test_plot_data.pdf"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[0,0,273],[1,100,373]])

    if os.path.exists(plot_filename):
        os.remove(plot_filename)
        
    thermomag_plotter.plot_data(input_data, plot_filename)

    assert (os.path.exists(plot_filename))

def test_convert_data():
    lt_input_file = ("DA7_1-L1.csv")
    ht_input_file = ("DA7_1-H1.csv")
    lt2_input_file = ("DA7_1-L2.csv")
    lt_json_output_file = "lt_data_output.json"
    ht_json_output_file = "ht_data_output.json"
    lt2_json_output_file = "lt2_data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    lt_input_filename = os.path.join(data_directory,lt_input_file)
    ht_input_filename = os.path.join(data_directory,ht_input_file)
    lt2_input_filename = os.path.join(data_directory,lt2_input_file)
    lt_json_filename = os.path.join(results_directory,lt_json_output_file)
    ht_json_filename = os.path.join(results_directory,ht_json_output_file)
    lt2_json_filename = os.path.join(results_directory,lt2_json_output_file)

    thermomag_plotter.convert_data(lt_input_filename, lt_json_filename)
    thermomag_plotter.convert_data(ht_input_filename, ht_json_filename)
    thermomag_plotter.convert_data(lt2_input_filename, lt2_input_filename)

    lt_input_data = pd.read_csv(lt_input_filename, index_col='TEMP', header=0)
    ht_input_data = pd.read_csv(ht_input_filename, index_col='TEMP', header=0)
    lt2_input_data = pd.read_csv(lt2_input_filename, index_col='TEMP', header=0)
    lt_output_data = pd.read_json(lt_json_filename)
    ht_output_data = pd.read_json(ht_json_filename)
    lt2_output_data = pd.read_json(lt2_json_filename)

    assert lt_input_data.info() is lt_output_data.info()
    assert ht_input_data.info() is ht_output_data.info()
    assert lt2_input_data.info() is lt2_output_data.info