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
def zuraw_load(obciazenie, wspolczynnik, wierzcholki):
    """tworzy przypadki obciążeniowe dla zurawia"""

    # tworzę przypadek obciążenia o nr. 1, nazwa ciężar własny, natura - stałe, analiza liniowa sprężysta
    Przypadek_1 = Robproj.Structure.Cases.CreateSimple(1, "Ciezar_Wlasny", IRobotCaseNature.I_CN_PERMANENT,
                                                 IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_1.Label = "CW_label"

    Przypadek_1.Records.Create(IRobotLoadRecordType.I_LRT_DEAD)  # tu ustawiam czy jest to siła rozłożona, czy jaka

    Load_1_1 = IRobotLoadRecord(Przypadek_1.Records.Get(1))  # tu konkretnie rozkladam siłę [rekord 1 dotyczy 1 siły w
    Load_1_1.SetValue(IRobotDeadRecordValues.I_DRV_Z, -1)    # w danym przypadku_1
    Load_1_1.SetValue(IRobotDeadRecordValues.I_DRV_ENTIRE_STRUCTURE, True)

    [n1, n2, n3, n4] = wierzcholki


    Przypadek_2 = Robproj.Structure.Cases.CreateSimple(2, "jedna_stopa", IRobotCaseNature.I_CN_EXPLOATATION,
                                                 IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_2.Label = "EXP_1"

    Przypadek_2.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE)

    Load_2_1 = IRobotLoadRecord(Przypadek_2.Records.Get(1))
    Load_2_1.Objects.FromText(str(n1))
    Load_2_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)


    Przypadek_3 = Robproj.Structure.Cases.CreateSimple(3, "dwie_stopy_ukos", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_3.Label = "EXP_2_1"

    Przypadek_3.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE)  #1
    Przypadek_3.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE)  #2


    Load_3_1 = IRobotLoadRecord(Przypadek_3.Records.Get(1))
    Load_3_1.Objects.FromText(str(n1))
    Load_3_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_3_2 = IRobotLoadRecord(Przypadek_3.Records.Get(2))
    Load_3_2.Objects.FromText(str(n3))
    Load_3_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Przypadek_4 = Robproj.Structure.Cases.CreateSimple(4, "dwie_stopy_x", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_4.Label = "EXP_2_2"

    Przypadek_4.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 1
    Przypadek_4.Records.New(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 2

    Load_4_1 = IRobotLoadRecord(Przypadek_4.Records.Get(1))
    Load_4_1.Objects.FromText(str(n1))
    Load_4_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_4_2 = IRobotLoadRecord(Przypadek_4.Records.Get(2))
    Load_4_2.Objects.FromText(str(n2))
    Load_4_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Przypadek_5 = Robproj.Structure.Cases.CreateSimple(5, "dwie_stopy_y", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_5.Label = "EXP_2_3"

    Przypadek_5.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 1
    Przypadek_5.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 2

    Load_5_1 = IRobotLoadRecord(Przypadek_5.Records.Get(1))
    Load_5_1.Objects.FromText(str(n1))
    Load_5_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_5_2 = IRobotLoadRecord(Przypadek_5.Records.Get(2))
    Load_5_2.Objects.FromText(str(n4))
    Load_5_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Przypadek_6 = Robproj.Structure.Cases.CreateSimple(6, "trzy_stopy_x", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_6.Label = "EXP_3_1"

    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 1
    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 2
    Przypadek_6.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 3

    Load_6_1 = IRobotLoadRecord(Przypadek_6.Records.Get(1))
    Load_6_1.Objects.FromText(str(n1))
    Load_6_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_6_2 = IRobotLoadRecord(Przypadek_6.Records.Get(2))
    Load_6_2.Objects.FromText(str(n2))
    Load_6_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_6_3 = IRobotLoadRecord(Przypadek_6.Records.Get(3))
    Load_6_3.Objects.FromText(str(n4))
    Load_6_3.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Przypadek_7 = Robproj.Structure.Cases.CreateSimple(7, "trzy_stopy_y", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_7.Label = "EXP_3_2"

    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 1
    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 2
    Przypadek_7.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 3

    Load_7_1 = IRobotLoadRecord(Przypadek_7.Records.Get(1))
    Load_7_1.Objects.FromText(str(n1))
    Load_7_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_7_2 = IRobotLoadRecord(Przypadek_7.Records.Get(2))
    Load_7_2.Objects.FromText(str(n4))
    Load_7_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_7_3 = IRobotLoadRecord(Przypadek_7.Records.Get(3))
    Load_7_3.Objects.FromText(str(n3))
    Load_7_3.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Przypadek_8 = Robproj.Structure.Cases.CreateSimple(8, "cztery_stopy", IRobotCaseNature.I_CN_EXPLOATATION,
                                                       IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR)
    Przypadek_8.Label = "EXP_4"

    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 1
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 2
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 3
    Przypadek_8.Records.Create(IRobotLoadRecordType.I_LRT_NODE_FORCE)  # 4

    Load_8_1 = IRobotLoadRecord(Przypadek_8.Records.Get(1))
    Load_8_1.Objects.FromText(str(n1))
    Load_8_1.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_8_2 = IRobotLoadRecord(Przypadek_8.Records.Get(2))
    Load_8_2.Objects.FromText(str(n2))
    Load_8_2.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_8_3 = IRobotLoadRecord(Przypadek_8.Records.Get(3))
    Load_8_3.Objects.FromText(str(n3))
    Load_8_3.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)

    Load_8_4 = IRobotLoadRecord(Przypadek_8.Records.Get(4))
    Load_8_4.Objects.FromText(str(n4))
    Load_8_4.SetValue(IRobotNodeForceRecordValues.I_NFRV_FZ, -wspolczynnik * obciazenie)


def nowy_profil_preta(nazwa, srednica):
    """Tworzy nowy profil pręta
    nazwa = string : nazwa
    srednica = int : srednica pręta w [cm]"""

    srednica = srednica/100     # robot widzi w metrach

    lab_serv = IRobotLabelServer(Robproj.Structure.Labels)
    try:
        section = IRobotLabel(lab_serv.Create(IRobotLabelType.I_LT_BAR_SECTION, nazwa)) # obiekt przekroju section
    except:
        return True
    data = IRobotBarSectionData(section.Data)   # obiekt który modyfikuje dane przekroju

    data.Type = IRobotBarSectionType.I_BST_STANDARD
    data.ShapeType = IRobotBarSectionShapeType.I_BSST_CONCR_COL_C # typ przekroju żelbetowy słup w kształcie koła
    concrete_data = IRobotBarSectionConcreteData(data.Concrete)   # to daje dostęp do atrybutów żelbetowych profili
    concrete_data.SetValue(IRobotBarSectionConcreteDataValue.I_BSCDV_COL_DE, srednica)
    concrete_data.CalcGeometry()

    # data.SetValue() tu jakbym chciał typowe nie dla żelbetu np. Wx albo gamma atrybuty

    lab_serv.Store(section)  # zapisuje stworzony przekrój żeby się wyświetlał na liście
    return False


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
    # kx, ky  nie są zaimplementowane w API :/

    Robproj.Structure.Labels.Store(thickness)


def open_project(sciezka, nazwa):
    """otwiera projekt rtd"""
    Robproj.Open(sciezka)
    Robproj.SaveAs(nazwa)


def bar_robot(profil, p1, p2):
    """tworzy pręt typu pręt, zadane argumenty to:
    profil - string - profil w robocie
    p1 - lista - współrzędna początku
    p2 - lista - współrzędna końca
    zwraca [n1, n2] odpowiednio numer node wierzchołków pręta"""

    rStruct = Robproj.Structure
    n_start = rStruct.Nodes.FreeNumber  # dobiera wolne numery węzłów
    rStruct.Nodes.Create(n_start, p1[0], p1[1], p1[2])    # tworzy węzeł na początku
    n_end = rStruct.Nodes.FreeNumber
    rStruct.Nodes.Create(n_end, p2[0], p2[1], p2[2])    # tworzy węzeł na końcu
    n_bar = rStruct.Bars.FreeNumber
    rStruct.Bars.Create(n_bar, n_start, n_end)      # tworzę obiekt, do którego nie mogę się odwoływać bez referencji
    bar = IRobotBar(rStruct.Bars.Get(n_bar))    # tworzę referencję do obiektu stworzonego linijkę wcześniej
    bar.SetLabel(IRobotLabelType.I_LT_BAR_SECTION, profil)
    return [n_start, n_end]


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
    panel.Main.Attribs.Meshed = True
    panel.SetLabel(IRobotLabelType.I_LT_PANEL_CALC_MODEL, "powłoka")
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