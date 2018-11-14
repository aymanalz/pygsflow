import os
import numpy as np
from control import Control as Cont
from parameter import Parameters as Param
from prms_data import Prms_data
import supports


class Prms(object):
    def __init__(self, Control=None, Parameters=None, control_file=None):

        if isinstance(Control, Cont):
            self.Control = Control
            self.control_file = Control.control_file
        else:
            print("Warning: the Control object is not correct, it is assumed to be empty")
            self.control_file = control_file
            self.Control = Control

        if isinstance(Parameters, Param):
            self.Parameters = Parameters
        else:
            print("Warning: the Parameter object is not correct, it is assumed to be empty."
                  "If a control file exists, we will try to upload it.")
            self.Parameters = Parameters
        self.load()

    def load(self):
        # load control information
        if not(self.control_file == None):
            self.Control = Cont(control_file=self.control_file)
        else:
            raise ValueError("Error: cannot load becuase the control file does not exit")

        # load parameters
        abs_files = []
        parm_files = self.Control.get_values('param_file')
        for ffn in parm_files:
            f = supports._get_file_abs(control_file=self.control_file, fn=ffn)
            abs_files.append(f)
        self.Parameters = Param(parameter_files=abs_files)

        # load data
        data_file = self.Control.get_values('data_file')
        data_file = supports._get_file_abs(control_file=self.control_file, fn=data_file[0])
        self.Data = Prms_data(data_file=data_file)

        print ("Prms model is loaded .....")
