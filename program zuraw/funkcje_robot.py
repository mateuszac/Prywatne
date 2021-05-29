import clr
import json

"""TE OBIEKTY MUSZĄ SIĘ WGRAĆ, ŻEBY FUNKCJĘ DZIAŁĄŁY"""
# POŁĄCZENIE Z DLL

with open("./sciezki.json") as plik_json:
    dane_pliku = json.load(plik_json)

dll = dane_pliku["sciezka_robot_dll"]

clr.AddReference(dll)
# IMPORT WSZYSTKICH BIBLIOTEK KTÓRE UDOSTĘPNIA AUTODESK DO ROBOTA
from RobotOM import *
# POŁĄCZENIE Z WŁĄCZONYM PROGRAMEM ROBOTA
Robapp = RobotApplicationClass()
# POŁĄCZENIE Z WŁĄCZONYM PROJEKTEM
Robproj = Robapp.Project
# POŁĄCZENIE Z WŁĄCZONĄ STRUKTURĄ
# rStruct = Robproj.Structure


# PROGRAM
def zuraw_load(obciazenie, wspolczynnik, x, y):
    """tworzy przypadki obciążeniowe dla zurawia"""

    # tworzę przypadek obciążenia o nr. 1, nazwa ciężar własny, natura - stałe, analiza liniowa sprężysta
    Przypadek_1 = Robproj.Structure.Cases.CreateSimple(1, "Ciezar_Wlasny", IRobotCaseNature.I_CN_PERMANENT,
                                                 IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_1.Label = "CW_label"

    Przypadek_1.Records.Create(IRobotLoadRecordType.I_LRT_DEAD)  # tu ustawiam czy jest to siła rozłożona, czy jaka

    Load_1_1 = IRobotLoadRecord(Przypadek_1.Records.Get(1))  # tu konkretnie rozkladam siłę [rekord 1 dotyczy 1 siły w
    Load_1_1.SetValue(IRobotDeadRecordValues.I_DRV_Z, -1)    # w danym przypadku_1
    Load_1_1.SetValue(IRobotDeadRecordValues.I_DRV_ENTIRE_STRUCTURE, True)


    Przypadek_2 = Robproj.Structure.Cases.CreateSimple(2, "jedna_stopa", IRobotCaseNature.I_CN_EXPLOATATION,
                                                 IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_2.Label = "EXP_1"

    Przypadek_2.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)


    Load_2_1 = IRobotLoadRecord(Przypadek_2.Records.Get(1))
    Load_2_1.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_FZ, -wspolczynnik*obciazenie)
    load_in_point(Load_2_1, -wspolczynnik * obciazenie, x, y, 1)

    Przypadek_3 = Robproj.Structure.Cases.CreateSimple(3, "dwie_stopy_ukos", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_3.Label = "EXP_2_1"

    Przypadek_3.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  #1
    Przypadek_3.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  #2


    Load_3_1 = IRobotLoadRecord(Przypadek_3.Records.Get(1))
    Load_3_1.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_FZ, -wspolczynnik * obciazenie)
    load_in_point(Load_3_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_3_2 = IRobotLoadRecord(Przypadek_3.Records.Get(2))
    Load_3_2.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_FZ, -wspolczynnik * obciazenie)
    load_in_point(Load_3_2, -wspolczynnik * obciazenie, -x, -y, 1)

    Przypadek_4 = Robproj.Structure.Cases.CreateSimple(4, "dwie_stopy_x", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_4.Label = "EXP_2_2"

    Przypadek_4.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 1
    Przypadek_4.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 2

    Load_4_1 = IRobotLoadRecord(Przypadek_4.Records.Get(1))
    load_in_point(Load_4_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_4_2 = IRobotLoadRecord(Przypadek_4.Records.Get(2))
    load_in_point(Load_4_2, -wspolczynnik * obciazenie, x, -y, 1)

    Przypadek_5 = Robproj.Structure.Cases.CreateSimple(5, "dwie_stopy_y", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_5.Label = "EXP_2_3"

    Przypadek_5.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 1
    Przypadek_5.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 2

    Load_5_1 = IRobotLoadRecord(Przypadek_5.Records.Get(1))
    load_in_point(Load_5_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_5_2 = IRobotLoadRecord(Przypadek_5.Records.Get(2))
    load_in_point(Load_5_2, -wspolczynnik * obciazenie, -x, y, 1)

    Przypadek_6 = Robproj.Structure.Cases.CreateSimple(6, "trzy_stopy_x", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_6.Label = "EXP_3_1"

    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 1
    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 2
    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 3

    Load_6_1 = IRobotLoadRecord(Przypadek_6.Records.Get(1))
    load_in_point(Load_6_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_6_2 = IRobotLoadRecord(Przypadek_6.Records.Get(2))
    load_in_point(Load_6_2, -wspolczynnik * obciazenie, x, -y, 1)

    Load_6_3 = IRobotLoadRecord(Przypadek_6.Records.Get(3))
    load_in_point(Load_6_3, -wspolczynnik * obciazenie, -x, y, 1)

    Przypadek_7 = Robproj.Structure.Cases.CreateSimple(7, "trzy_stopy_y", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_7.Label = "EXP_3_2"

    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 1
    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 2
    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 3

    Load_7_1 = IRobotLoadRecord(Przypadek_7.Records.Get(1))
    load_in_point(Load_7_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_7_2 = IRobotLoadRecord(Przypadek_7.Records.Get(2))
    load_in_point(Load_7_2, -wspolczynnik * obciazenie, -x, y, 1)

    Load_7_3 = IRobotLoadRecord(Przypadek_7.Records.Get(3))
    load_in_point(Load_7_3, -wspolczynnik * obciazenie, -x, -y, 1)

    Przypadek_8 = Robproj.Structure.Cases.CreateSimple(8, "cztery_stopy", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_8.Label = "EXP_4"

    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 1
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 2
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 3
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT)  # 4

    Load_8_1 = IRobotLoadRecord(Przypadek_8.Records.Get(1))
    load_in_point(Load_8_1, -wspolczynnik * obciazenie, x, y, 1)

    Load_8_2 = IRobotLoadRecord(Przypadek_8.Records.Get(2))
    load_in_point(Load_8_2, -wspolczynnik * obciazenie, -x, y, 1)

    Load_8_3 = IRobotLoadRecord(Przypadek_8.Records.Get(3))
    load_in_point(Load_8_3, -wspolczynnik * obciazenie, x, -y, 1)

    Load_8_4 = IRobotLoadRecord(Przypadek_8.Records.Get(4))
    load_in_point(Load_8_4, -wspolczynnik * obciazenie, -x, -y, 1)


def load_in_point(_load, obc, _x, _y, _z):
    _load.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_FZ, obc)
    _load.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_POINT_X, _x)
    _load.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_POINT_Y, _y)
    _load.SetValue(IRobotNodeForceInPointRecordValues.I_NFIPRV_POINT_Z, _z)


def open_project(sciezka, nazwa):
    """otwiera projekt rtd"""
    Robproj.Open(sciezka)
    Robproj.SaveAs(nazwa)

def bar_robot(profil, p1, p2):
    """tworzy pręt typu pręt, zadane argumenty to:
    profil - string - profil w robocie
    p1 - lista - współrzędna początku
    p2 - lista - współrzędna końca"""

    rStruct = Robproj.Structure
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

    rStruct = Robproj.Structure
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


    bar_robot("S_C_30", [5, 5, 0], [5, 5, 10])
    zuraw_load(100000, 1, 1, 2)