import matplotlib.pyplot as plt
import numpy as np

def plot_td_dot_and_t_dot(np_stored_td_dot: np.array, np_stored_t_dot: np.array, np_stored_time: np.array):
    """
    plot_td_dot_and_t_dot Example function to plot the task-space velocity
    and desired task-space velocity for the open-loop velocity controller
    """

    # x-axis
    ax1 = plt.subplot(1,3,1)
    plt.plot(np_stored_time,np_stored_td_dot[:,0])
    plt.plot(np_stored_time,np_stored_t_dot[:,0])
    plt.title('x-axis velocity')
    plt.ylabel('Velocity [m/s]')
    plt.ylim([-5, 5])
    plt.xlabel('Time [s]')
    ax1.legend(['desired','actual','Location','southeast'])
    
    # y-axis
    ax2 = plt.subplot(1,3,2)
    plt.plot(np_stored_time,np_stored_td_dot[:,1])
    plt.plot(np_stored_time,np_stored_t_dot[:,1])
    plt.title('y-axis velocity')
    plt.ylabel('Velocity [m/s]')
    plt.ylim([-5, 5])
    plt.xlabel('Time [s]')
    ax2.legend(['desired','actual','Location','southeast'])
    
    # z-axis
    ax3 = plt.subplot(1,3,3)
    plt.plot(np_stored_time,np_stored_td_dot[:,2])
    plt.plot(np_stored_time,np_stored_t_dot[:,2])
    plt.title('z-axis velocity')
    plt.ylabel('Velocity [m/s]')
    plt.ylim([-5, 5])
    plt.xlabel('Time [s]')
    ax3.legend(['desired','actual','Location','southeast'])
    

