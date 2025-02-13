from dqrobotics import *
from math import cos, sin, acos, asin

class OneDofPlanarRobot():
    '''OneDofPlanarRobot regarding all methods related to the 1-DoF planar robot'''
    
    def __init__(self, l1):
        self.l1_ = l1

        
    def fkm(self,theta1):
        '''fkm calculates the FKM for the 1-DoF planar robot.'''
        
        # The rotation about the joint
        x_w_1 = cos(theta1/2.0) + k_*sin(theta1/2.0)
        # The translation about the length
        x_1_r = 1 + 0.5*E_*i_*self.l1_
        # Pose transformation
        x_w_r = x_w_1*x_1_r
        
        # Get the translation
        return translation(x_w_r)
    
    def ikm_tx(self,tx):
        '''fkm calculates the IKM for the 1-DoF planar robot using the 
           desired x-axis translation.'''
        
        # Return the angle to reach the desired tx
        return acos(tx/self.l1_)
    
    
    def ikm_ty(self,ty):
        '''fkm calculates the IKM for the 1-DoF planar robot using the 
           desired y-axis translation.'''
        
        # Return the angle to reach the desired ty
        return asin(ty/self.l1_)
    
    def translation_jacobian(self,theta1):
        ''' Calculates the translation Jacobian of the 1-DoF planar
           robot. '''
        
        j = self.l1_*(-i_*sin(theta1)+j_*cos(theta1))
        return vec3(j)
    
    '''function plot(obj,theta1)
        % Plot the 1-DoF planar robot in the xy-plane
        
        % Get the fkm
        t_w_r = obj.fkm(theta1);
        
        % Plot
        plot([0 t_w_r.q(2)],[0 t_w_r.q(3)],'r')
        hold on
        % Mark the base with an o
        plot(0,0,'o')
        % Mark the end effector with an x
        plot(t_w_r.q(2),t_w_r.q(3),'x')
        hold off
        title('The One DoF planar robot in the xy-plane')
        xlim([-2 2])
        xlabel('x [m]')
        ylim([-2 2])
        ylabel('y [m]')
        end
    end'''
