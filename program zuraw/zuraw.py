""" Ten plik odpowiedzialny jest za wczytanie wszystkich elementów interfejsu graficznego, dopisanie funkcjonalności
do elementów GUI oraz definicję klasy, której obiekt będzie włączał program zuraw """

from PySide2 import QtWidgets # import biblioteki Pyside
import gui_qt
import json
import datetime

class ZurawGUI(gui_qt.Ui_Zuraw_window, QtWidgets.QMainWindow):
    """Ta klasa obsługuje cały interfejs graficzny żurawia"""
    def __init__(self):
        """Konstruktor GUI, wszystko co jest w tej metodzie zostanie wykonane przed pokazaniem GUI użytkownikowi"""
        super(ZurawGUI, self).__init__()
        self.setupUi(self)
        # DODATKOWA MODYFIKACJA STARTOWA GUI
        today = str(datetime.date.today())[0:4] + str(datetime.date.today())[5:7] + str(datetime.date.today())[8:]
        self.nazwa_projektu_gui.setText("model_zuraw_{}".format(today))
        self.uzupelnij_domyslne_sciezki()

        # dopisać tutaj żeby startowo wpisywało ścieżkę do szablonu i dll z pliku json

        # DODATKOWE FUNKCJE
        self.guzik_dll_gui.clicked.connect(self.dobierz_sciezke_dll)
        self.guzil_sciezka_gui.clicked.connect(self.dobierz_sciezke_szablonu)
        self.guzik_stworz_projekt_gui.clicked.connect(self.stworz_projekt)
        self.guzik_zapis_sciezka_gui.clicked.connect(self.dobierz_sciezke_zapisu)

    def dobierz_sciezke_dll(self):
        """Metoda otwierająca okno gdzie można dobrać ścieżkę DLL"""
        nazwa_pliku, rozszerzenie = QtWidgets.QFileDialog.getOpenFileName(self, "wybierz plik", filter="*.dll")
        self.sciezka_dll_gui.setText(nazwa_pliku)

    def dobierz_sciezke_szablonu(self):
        """Metoda otwierająca okno gdzie można dobrać ścieżkę szablonu"""
        nazwa_pliku, rozszerzenie = QtWidgets.QFileDialog.getOpenFileName(self, "wybierz plik", filter="*.rtd")
        self.sciezka_szablon_gui.setText(nazwa_pliku)

    def dobierz_sciezke_zapisu(self):
        """Metoda otwierająca okno gdzie można dobrać ścieżkę zapisu"""
        nazwa_sciezki = QtWidgets.QFileDialog.getExistingDirectory(self, "wybierz plik")
        self.sciezka_zapis_gui.setText(nazwa_sciezki)

    def stworz_projekt(self):
        """Metoda otwierająca projekt w robocie i tworząca żurawia"""
        # zbieranie danych
        szerokosc = self.szerokosc_plyty_gui.value()    # [m]
        dlugosc = self.dlugosc_plyty_gui.value()        # [m]
        klasa_betonu = self.klasa_betonu_gui.currentText()   # [string]
        grubosc = self.grubosc_plyty_gui.value()        # [cm]
        kz = self.sztywnosc_plyty_gui.value()           # [kPa]
        x_stopy = self.x_stopy_gui.value()              # [m]
        y_stopy = self.y_stopy_gui.value()              # [m]
        srednica = self.srednica_gui.value()            # [cm]
        obc_char = self.obciazenie_gui.value()          # [kN]
        wspolczynnik = self.wspolczynnik_gui.value()    # [-]

        self.zapis_json()
        import funkcje_robot

        try:
            # tworzę panel płyty fundamentowej o zadanej grubości i konturze
            funkcje_robot.panel_robot("GR20_FUND", 0, [[-szerokosc/2, -dlugosc/2, 0],
                                                       [szerokosc/2, -dlugosc/2, 0],
                                                       [szerokosc/2, dlugosc/2, 0],
                                                       [-szerokosc/2, dlugosc/2, 0]])
        except:
            nazwa_zapisu = self.sciezka_zapis_gui.text() + "/" + self.nazwa_projektu_gui.text() + ".rtd"
            funkcje_robot.open_project(self.sciezka_szablon_gui.text(), nazwa_zapisu)
            funkcje_robot.panel_robot("GR20_FUND", 0, [[-szerokosc / 2, -dlugosc / 2, 0],
                                                       [szerokosc / 2, -dlugosc / 2, 0],
                                                       [szerokosc / 2, dlugosc / 2, 0],
                                                       [-szerokosc / 2, dlugosc / 2, 0]])

        # tworzę 4 jednometrowe pręty w miejscach przyłożenia stóp żurawia o zadanym profilu
        funkcje_robot.bar_robot("S_C_30", [-x_stopy, -y_stopy, 0], [-x_stopy, -y_stopy, 1])
        funkcje_robot.bar_robot("S_C_30", [x_stopy, -y_stopy, 0], [x_stopy, -y_stopy, 1])
        funkcje_robot.bar_robot("S_C_30", [x_stopy, y_stopy, 0], [x_stopy, y_stopy, 1])
        funkcje_robot.bar_robot("S_C_30", [-x_stopy, y_stopy, 0], [-x_stopy, y_stopy, 1])

    def zapis_json(self):
        """Zapisuje ścieżki do pliku json"""
        dll = self.sciezka_dll_gui.text()
        szablon = self.sciezka_szablon_gui.text()
        zapis = self.sciezka_zapis_gui.text()

        sciezki = {
                    "sciezka_robot_dll": dll,
                    "sciezka_szablon": szablon,
                    "sciezka_zapis": zapis
                  }

        with open("./sciezki.json", 'w') as plik_json:
            plik_json.write(json.dumps(sciezki, indent=3, sort_keys=True))

    def uzupelnij_domyslne_sciezki(self):
        """uzupełnia domyślne ścieżki szablonu i dll"""
        try:
            with open("./sciezki.json") as plik_json:
                dane_pliku = json.load(plik_json)

            sciezka_dll = dane_pliku["sciezka_robot_dll"]
            sciezka_szablon = dane_pliku["sciezka_szablon"]
            zapis = dane_pliku["sciezka_zapis"]

            self.sciezka_dll_gui.setText(sciezka_dll)
            self.sciezka_szablon_gui.setText(sciezka_szablon)
            self.sciezka_zapis_gui.setText(zapis)

        except (FileNotFoundError, KeyError):
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = ZurawGUI()
    qt_app.show()
    app.exec_()
