import clr

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
    rStruct.Bars.Create(n_bar, n_start, n_end)      # tworzę obiekt, do którego nie mogę się odwoływać bez referencji
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


def nowy_profil_preta(nazwa, srednica):
    """Tworzy nowy profil pręta
    nazwa = string : nazwa
    srednica = int : srednica pręta w [cm]"""

    srednica = srednica/100     # robot widzi w metrach

    lab_serv = IRobotLabelServer(Robproj.Structure.Labels)
    section = IRobotLabel(lab_serv.Create(IRobotLabelType.I_LT_BAR_SECTION, nazwa)) # obiekt przekroju section
    data = IRobotBarSectionData(section.Data)   # obiekt który modyfikuje dane przekroju

    data.Type = IRobotBarSectionType.I_BST_STANDARD
    data.ShapeType = IRobotBarSectionShapeType.I_BSST_CONCR_COL_C # typ przekroju żelbetowy słup w kształcie koła
    concrete_data = IRobotBarSectionConcreteData(data.Concrete)   # to daje dostęp do atrybutów żelbetowych profili
    concrete_data.SetValue(IRobotBarSectionConcreteDataValue.I_BSCDV_COL_DE, srednica)

    # data.SetValue() tu jakbym chciał typowe nie dla żelbetu np. Wx albo gamma atrybuty

    lab_serv.Store(section)  # zapisuje stworzony przekrój żeby się wyświetlał na liście



def nowa_grubosc_panelu(nazwa, grubosc, kz, klasa_betonu):
    """Tworzy nową grubość panelu
    nazwa = string : nazwa
    srednica = int : srednica pręta w [cm]
    kz = int : kz w [kN/m3]
    klasa_betonu = string"""

    grubosc = grubosc/100 # robot widzi w metrach
    kz = kz*1000 # robot widzi w N/m3

    thickness = IRobotLabel(Robproj.Structure.Labels.Create(IRobotLabelType.I_LT_PANEL_THICKNESS, nazwa))
    data = IRobotThicknessData(thickness.Data)

    data.MaterialName = klasa_betonu    # dobieram materiał z dostępnych w szablonie w robocie

    data.ThicknessType = IRobotThicknessType.I_TT_HOMOGENEOUS

    homoType = IRobotThicknessHomoData(data.Data)   #obiekt zawierający atrybuty modyfikacji grubości panela
    homoType.ThickConst = grubosc

    data.ElasticFoundation = kz
    ### kx, ky  nie są zaimplementowane w API :/

    Robproj.Structure.Labels.Store(thickness)

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
    bar_robot("S_C_30", [5, 5, 0], [5, 5, 10])
    nowa_grubosc_panelu("testowa_fat", 48, 10000, "B37")

