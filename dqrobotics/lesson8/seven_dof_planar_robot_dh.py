from dqrobotics.robot_modeling import DQ_SerialManipulatorDH
import numpy as np

class SevenDofPlanarRobotDH:
    """
    SevenDofPlanarRobot regarding all methods related to the 7-DoF planar robot.
    """
    
    def kinematics():
        """
        Returns the kinematics of the SevenDoFPlanarRobot as DQ_SerialManipulatorDH.
        """
        DH_theta=  [0.] * 7
        DH_d =     [0.] * 7
        DH_a =     [1.] * 7
        DH_alpha = [0.] * 7
        DH_type  = [0] * 7
        
        dh_matrix = np.array([
            DH_theta,
            DH_d,
            DH_a,
            DH_alpha,
            DH_type
        ])
        
        return DQ_SerialManipulatorDH(dh_matrix)
    