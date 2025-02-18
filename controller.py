import time
import os
import numpy as np

class PIDController:
    def __init__(self,kp,ki,kd,setpoint):
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.setpoint=setpoint        
        self.previous_error=0
        self.integral=0
    def compute(self,process_variable,dt):

        #generate error signal
        error=self.setpoint-process_variable

        #PID contributions
        P_out=self.kp*error
        
        self.integral +=error*dt
        I_out=self.ki*self.integral

        derivative=(error-self.previous_error)/dt
        D_out=self.Ki*derivative

        output=P_out + I_out + D_out
        self.previous_error=error

        return output
    

def system(m,b,k):
    