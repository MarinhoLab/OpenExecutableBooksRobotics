from dqrobotics.robot_modeling import DQ_SerialManipulatorDH
import numpy as np
from dqrobotics.utils.DQ_Math import * 

class ThreeDofPlanarRobotDH:
    """
    ThreeDofPlanarRobot regarding all methods related to the 3-DoF planar robot
    """
    
    def kinematics():
        """
        kinematics returns the kinematics of the ThreeDoFPlanarRobot as DQ_SerialManipulatorDH
        """
        DH_theta=  [0., 0., 0.]
        DH_d =     [0., 0., 0.]
        DH_a =     [1., 1., 1.]
        DH_alpha = [0., 0., 0.]
        DH_type  = [0,  0,  0]
        
        dh_matrix = np.matrix([
            np.array(DH_theta),
            np.array(DH_d),
            np.array(DH_a),
            np.array(DH_alpha),
            DH_type
        ])
        
        return DQ_SerialManipulatorDH(dh_matrix)
    