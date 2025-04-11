import numpy as np
import matplotlib.pyplot as plt

def plot_u(stored_u,stored_time, percentage):
    "Example function to plot the controller inputs"

    # Get the length of the data
    data_length = len(stored_u)
    # Get the first "percentage" percent of the data (as an integer)
    data_cut_length = round((percentage/100.0)*data_length)

    # Plot the desired data for each joint
    for i in range(0,7):
        plt.plot(stored_time[0:data_cut_length],stored_u[0:data_cut_length, i])
    
    # Add the rest of the plot information
    plt.title('Controller results')
    plt.ylabel('Joint velocity [rad/s]')
    plt.xlabel('Time [s]')
    plt.legend(['j1','j2','j3','j4','j5','j6','j7'])
    
