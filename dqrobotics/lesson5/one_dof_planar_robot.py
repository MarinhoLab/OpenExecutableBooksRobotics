from dqrobotics import *
from math import cos, sin, acos, asin
import matplotlib.pyplot as plt
import numpy as np

class OneDofPlanarRobot():
    '''OneDofPlanarRobot regarding all methods related to the 1-DoF planar robot'''
    
    def __init__(self, l1):
        self.l1_ = l1

        
    def fkm(self,theta1):
        """Calculate the FKM for the 1-DoF planar robot."""

        # In some operations, theta1 can be converted to a ndarray
        theta1 if np.isscalar(theta1) else np.ndarray.item(theta1)
        
        # The rotation about the joint
        x_w_1 = cos(theta1/2.0) + k_*sin(theta1/2.0)
        # The translation about the length
        x_1_r = 1 + 0.5*E_*i_*self.l1_
        # Pose transformation
        x_w_r = x_w_1*x_1_r
        
        # Get the translation
        return translation(x_w_r)
    
    def ikm_tx(self,tx):
        """Calculate the IKM for the 1-DoF planar robot using the
           desired x-axis translation."""
        
        # Return the angle to reach the desired tx
        return acos(tx/self.l1_)
    
    
    def ikm_ty(self,ty):
        """Calculate the IKM for the 1-DoF planar robot using the
           desired y-axis translation."""
        
        # Return the angle to reach the desired ty
        return asin(ty/self.l1_)
    
    def translation_jacobian(self,theta1):
        """ Calculate the translation Jacobian of the 1-DoF planar
           robot. """
        
        j = self.l1_*(-i_*sin(theta1)+j_*cos(theta1))
        return vec3(j)
    
    def plot(obj,theta1):
        """
        Plot the 1-DoF planar robot in the xy-plane
        """
        
        # Get the fkm
        t_w_r = obj.fkm(theta1);
        
        # Plot
        plt.plot([0, t_w_r.q[1]],[0, t_w_r.q[2]],'r')
        # Mark the base with an o
        plt.plot(0,0,'o')
        # Mark the end effector with an x
        plt.plot(t_w_r.q[1],t_w_r.q[2],'x')
        
        plt.title('The One DoF planar robot in the xy-plane')
        plt.xlim([-2, 2])
        plt.xlabel('x [m]')
        plt.ylim([-2, 2])
        plt.ylabel('y [m]')
        
        
        
    
