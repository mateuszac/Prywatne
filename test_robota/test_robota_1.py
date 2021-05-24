import clr

# POŁĄCZENIE Z DLL
clr.AddReference("C:\Program Files\Autodesk\Autodesk Robot Structural Analysis Professional 2020\System\Exe\Interop.RobotOM.dll")
# IMPORT WSZYSTKICH BIBLIOTEK KTÓRE UDOSTĘPNIA AUTODESK DO ROBOTA
from RobotOM import *
# POŁĄCZENIE Z WŁĄCZONYM PROGRAMEM ROBOTA
Robapp = RobotApplicationClass()
# POŁĄCZENIE Z WŁĄCZONYM PROJEKTEM
Robproj = Robapp.Project
# POŁĄCZENIE Z WŁĄCZONĄ STRUKTURĄ
rStruct = Robproj.Structure

# PROGRAM ROBOTOWY
n1 = rStruct.Nodes.FreeNumber
rStruct.Nodes.Create(n1,0.0,0.0,0.0)
for i in range(5):
    nn = rStruct.Nodes.FreeNumber
    rStruct.Nodes.Create(nn,5.0,0.40*i,0.0)
    nb = rStruct.Bars.FreeNumber
    rStruct.Bars.Create(nb, n1, nn)


# przydatny kod :
# bar1 = IRobotBar(bars.Get(1))
# labelbar1 = IRobotLabel(bar1.GetLabel(3))
#
# data = IRobotBarSectionData(labelbar1.Data)