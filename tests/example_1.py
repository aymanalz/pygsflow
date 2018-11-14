from gsflow import Gsflow

control_file = r"D:\Workspace\Codes\gsflow\gsflow\data\data_backup\data\sagehen\windows\gsflow.control"

gs = Gsflow(control_file = control_file )
gs.control.add_record(name = "hummingbird12", values = [1, 2]) # Notice that we do not check whether
# the new record is valid or not.

pass

