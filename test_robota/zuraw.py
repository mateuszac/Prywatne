import clr
import inspect

"""TE OBIEKTY MUSZĄ SIĘ WGRAĆ, ŻEBY FUNKCJĘ DZIAŁĄŁY"""
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

# PROGRAM


def bar_robot(profil, p1, p2):
    """tworzy pręt typu pręt, zadane argumenty to:
    profil - string - profil w robocie
    p1 - lista - współrzędna początku
    p2 - lista - współrzędna końca"""

    n_start = rStruct.Nodes.FreeNumber  # dobiera wolne numery węzłów
    rStruct.Nodes.Create(n_start, p1[0], p1[1], p1[2])    # tworzy węzeł na początku
    n_end = rStruct.Nodes.FreeNumber
    rStruct.Nodes.Create(n_end, p2[0], p2[1], p2[2])    # tworzy węzeł na końcu
    n_bar = rStruct.Bars.FreeNumber
    rStruct.Bars.Create(n_bar, n_start, n_end)
    bar = IRobotBar(rStruct.Bars.Get(n_bar))    # tworzę referencję do obiektu stworzonego linijkę wcześniej
    bar.SetLabel(IRobotLabelType.I_LT_BAR_SECTION, profil)


def panel_robot(thickness, type, contour):
    """tworzy panel robotowy, zadane argumenty to:
    thickness - string - grubość w robocie
    type - int - typ struktury
    contour - lista list trzyelementowych, punkty definiujące kontur"""

    panelid = rStruct.Objects.FreeNumber    # wolny numer panela
    gen_panel = rStruct.Objects
    panel = gen_panel.Create(panelid)

    c = RobotGeoContour()                   # tworzy kontur
    for i in range(len(contour)):
        node_numer = rStruct.Nodes.FreeNumber
        segment = RobotGeoSegmentLine()
        segment.P1.Set(contour[i][0], contour[i][1], contour[i][2])
        c.Add(segment)
        del segment
        rStruct.Nodes.Create(node_numer, contour[i][0], contour[i][1], contour[i][2])    # tworzy węzły
    c.Initialize()

    panel.Main.Geometry = c     # przypisanie panelowi geometrii
    panel.Main.Attribs.Meshed = True       #przypisanie panelowi siatki
    panel.Initialize()          #stworzenie panelu
    panel.StructuralType = type    #przypisanie panelowi struktury
    panel.SetLabel(IRobotLabelType.I_LT_PANEL_THICKNESS, thickness)
    panel.Update()

Robapp.Visible = True
Robapp.Interactive = True

if __name__ == "__main__":
    clr.AddReference(
        "C:\Program Files\Autodesk\Autodesk Robot Structural Analysis Professional 2020\System\Exe\Interop.RobotOM.dll")
    from RobotOM import *
    Robapp = RobotApplicationClass()
    # POŁĄCZENIE Z WŁĄCZONYM PROJEKTEM
    Robproj = Robapp.Project
    # POŁĄCZENIE Z WŁĄCZONĄ STRUKTURĄ
    rStruct = Robproj.Structure
    panel_robot("GR20_FUND", 0, [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]])
    bar_robot("S_C_30", [5, 5, 0], [5, 5, 10])
