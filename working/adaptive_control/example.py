# IMPORT START
import numpy as np
from numpy import pi

import matplotlib.pyplot as plt

from dqrobotics import *
from dqrobotics.robot_modeling import DQ_SerialManipulator
from dqrobotics.utils.DQ_Math import deg2rad
import dqrobotics_extensions.pyplot as dqp

from marinholab.papers.tro2022.adaptive_control import *
from marinholab.papers.tro2022.adaptive_control.Example_ParameterSpaceEDH import *
# IMPORT END

# SETUP PLOT START
def setup_plot():
    # Set up the plot
    fig = plt.figure()
    plot_size = 0.5
    ax = plt.axes(projection='3d')
    ax.set_xlabel('$x$')
    ax.set_xlim((-plot_size, plot_size))
    ax.set_ylabel('$y$')
    ax.set_ylim((-plot_size, plot_size))
    ax.set_zlabel('$z$')
    ax.set_zlim((-plot_size, plot_size))
    return fig, ax
# SETUP PLOT END

# ROBOT RAW KINEMATICS START
def vs050_raw_kinematics() -> Example_SerialManipulatorEDH:
    """
    Gets the ideal kinematics of the VS050 robot.
    :return: A Suitable Example_SerialManipulatorEDH with VS050 kinematics.
    """
    VS050_dh_matrix = np.array([
        [-pi, pi / 2, -pi / 2, 0, pi, 0],
        [0.345, 0, 0, 0.255, 0, 0.07],
        [0, 0.250, 0.01, 0, 0, 0],
        [pi / 2, 0, -pi / 2, pi / 2, pi / 2, 0],
        [0, 0, 0, 0, 0, 0]
    ])

    lower_joint_limits = np.array([-170, -100, -60, -265, -119, -355]) * pi / 180
    upper_joint_limits = np.array([170, 100, 124, 265, 89.9, 355]) * pi / 180

    robot = Example_SerialManipulatorEDH(VS050_dh_matrix)
    robot.set_lower_q_limit(lower_joint_limits)
    robot.set_upper_q_limit(upper_joint_limits)

    robot.set_base_frame(DQ([1]))
    robot.set_effector_frame(DQ([1]))

    return robot
# ROBOT RAW KINEMATICS END

# PARAMETER SPACE START
def set_parameter_space_boundaries(r: Example_SerialManipulatorEDH,
                                   other_parameters_linear_confidence_meters:float = 0.001,
                                   other_parameters_angular_confidence_degrees:float = 1):

    # Helpful shorthand
    opa = other_parameters_angular_confidence_degrees
    opl = other_parameters_linear_confidence_meters

    theta = Example_ParameterType.theta
    d = Example_ParameterType.d
    a = Example_ParameterType.a
    alpha = Example_ParameterType.alpha

    # Let us suppose we have inaccuracies at the first joint
    parameter_space: list[Example_Parameter] = [
        Example_Parameter(0, theta, r.get_theta(0), r.get_theta(0) - deg2rad(opa), r.get_theta(0) + deg2rad(opa)),
        Example_Parameter(0, d, r.get_d(0), r.get_d(0) - opl, r.get_d(0) + opl),
        Example_Parameter(0, a, r.get_a(0), r.get_a(0) - opl, r.get_a(0) + opl),
        Example_Parameter(0, alpha, r.get_alpha(0), r.get_alpha(0) - deg2rad(opa), r.get_alpha(0) + deg2rad(opa))
    ]

    r.set_parameter_space(parameter_space)
# PARAMETER SPACE END

def main():
    # MAIN START
    fig, ax = setup_plot()

    estimated_robot = vs050_raw_kinematics()
    q_init = np.array([0, pi/4, pi/2, 0, pi/4, 0])

    set_parameter_space_boundaries(estimated_robot)

    dqp.plot(estimated_robot,
             q = q_init,
             line_color = 'r',
             cylinder_color = "r",
             cylinder_alpha = 0.3,
             ax = ax)

    return fig, ax
    # MAIN END

if __name__ == "__main__":
    fig, ax = main()
    plt.show()
