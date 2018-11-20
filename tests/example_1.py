from gsflow import Gsflow
import matplotlib.pyplot as plt
control_file = r"D:\Workspace\Codes\gsflow\gsflow\data\data_backup\data\sagehen\windows\gsflow.control"
#control_file = r"D:\Workspace\Codes\gsflow\gsflow\data\data_backup\data\sagehen\windows\gsflow_prms.control"
#control_file = r"D:\Workspace\training\gsflowID2447_classrepo\exercises\saghen_pygsflow\data\model_gsflow_arcpy" \
#               r"\windows\sagehen_run.control"
#control_file = r"D:\Workspace\training\gsflowID2447_classrepo\exercises\saghen_pygsflow\data\model_gsflow_arcpy
# \windows\sagehen_run.control"

gs = Gsflow(control_file = control_file )
gs.write_input(workspace=r"D:\Workspace\Codes\gsflow\gsflow\data\proj3")
gs.run_model()

stat_output = gs.prms.get_statVar()
gs.prms.stat.plot()

pass


