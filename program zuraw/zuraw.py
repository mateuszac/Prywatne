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

        # dopisać tutaj żeby startowo wpisywało ścieżkę do szablonu i dll z pliku json

        # DODATKOWE FUNKCJE
        self.guzik_dll_gui.clicked.connect(self.dobierz_sciezke_dll)
        self.guzil_sciezka_gui.clicked.connect(self.dobierz_sciezke_szablonu)
        self.guzik_stworz_projekt_gui.clicked.connect(self.stworz_projekt)

    def dobierz_sciezke_dll(self):
        """Metoda otwierająca okno gdzie można dobrać ścieżkę DLL"""
        nazwa_pliku, rozszerzenie = QtWidgets.QFileDialog.getOpenFileName(self, "wybierz plik", filter="*.dll")
        self.sciezka_dll_gui.setText(nazwa_pliku)

    def dobierz_sciezke_szablonu(self):
        """Metoda otwierająca okno gdzie można dobrać ścieżkę szablonu"""
        nazwa_pliku, rozszerzenie = QtWidgets.QFileDialog.getOpenFileName(self, "wybierz plik", filter="*.rtd")
        self.sciezka_szablon_gui.setText(nazwa_pliku)

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
        funkcje_robot.bar_robot("S_C_30", [5, 5, 0], [5, 5, 10]) ##### USUN TE LINIJKE JEST TESTOWA ZEBY SIE PRET ROBIL
        funkcje_robot.panel_robot("GR20_FUND", 0, [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]]) #TA TEZ

    def zapis_json(self):
        """Zapisuje ścieżki do pliku json"""
        dll = self.sciezka_dll_gui.text()
        szablon = self.sciezka_szablon_gui.text()
        sciezki = {
                    "sciezka_robot_dll": dll,
                    "sciezka_szablon": szablon
                  }

        with open("./sciezki.json", 'w') as plik_json:
            plik_json.write(json.dumps(sciezki, indent=3, sort_keys=True))


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = ZurawGUI()
    qt_app.show()
    app.exec_()
