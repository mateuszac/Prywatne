# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_qt.ui',
# licensing of 'gui_qt.ui' applies.
#
# Created: Sat May 29 17:26:41 2021
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Zuraw_window(object):
    def setupUi(self, Zuraw_window):
        Zuraw_window.setObjectName("Zuraw_window")
        Zuraw_window.resize(840, 460)
        Zuraw_window.setMinimumSize(QtCore.QSize(840, 460))
        self.centralwidget = QtWidgets.QWidget(Zuraw_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.guzik_dll_gui = QtWidgets.QPushButton(self.centralwidget)
        self.guzik_dll_gui.setObjectName("guzik_dll_gui")
        self.gridLayout.addWidget(self.guzik_dll_gui, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.guzil_sciezka_gui = QtWidgets.QPushButton(self.centralwidget)
        self.guzil_sciezka_gui.setObjectName("guzil_sciezka_gui")
        self.gridLayout.addWidget(self.guzil_sciezka_gui, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_7.addWidget(self.label_25)
        self.siatka_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.siatka_gui.setEnabled(False)
        self.siatka_gui.setDecimals(0)
        self.siatka_gui.setMinimum(2.0)
        self.siatka_gui.setMaximum(200.0)
        self.siatka_gui.setProperty("value", 10.0)
        self.siatka_gui.setObjectName("siatka_gui")
        self.horizontalLayout_7.addWidget(self.siatka_gui)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        self.szerokosc_plyty_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.szerokosc_plyty_gui.setMinimum(1.0)
        self.szerokosc_plyty_gui.setSingleStep(0.1)
        self.szerokosc_plyty_gui.setProperty("value", 5.0)
        self.szerokosc_plyty_gui.setObjectName("szerokosc_plyty_gui")
        self.horizontalLayout_5.addWidget(self.szerokosc_plyty_gui)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.sciezka_szablon_gui = QtWidgets.QLineEdit(self.centralwidget)
        self.sciezka_szablon_gui.setText("")
        self.sciezka_szablon_gui.setObjectName("sciezka_szablon_gui")
        self.gridLayout.addWidget(self.sciezka_szablon_gui, 2, 1, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_6.addWidget(self.label_24)
        self.dlugosc_plyty_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dlugosc_plyty_gui.setMinimum(1.0)
        self.dlugosc_plyty_gui.setSingleStep(0.01)
        self.dlugosc_plyty_gui.setProperty("value", 5.0)
        self.dlugosc_plyty_gui.setObjectName("dlugosc_plyty_gui")
        self.horizontalLayout_6.addWidget(self.dlugosc_plyty_gui)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.klasa_betonu_gui = QtWidgets.QComboBox(self.centralwidget)
        self.klasa_betonu_gui.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.klasa_betonu_gui.sizePolicy().hasHeightForWidth())
        self.klasa_betonu_gui.setSizePolicy(sizePolicy)
        self.klasa_betonu_gui.setMaximumSize(QtCore.QSize(80, 16777215))
        self.klasa_betonu_gui.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.klasa_betonu_gui.setMaxVisibleItems(12)
        self.klasa_betonu_gui.setDuplicatesEnabled(True)
        self.klasa_betonu_gui.setObjectName("klasa_betonu_gui")
        self.klasa_betonu_gui.addItem("")
        self.klasa_betonu_gui.addItem("")
        self.klasa_betonu_gui.addItem("")
        self.klasa_betonu_gui.addItem("")
        self.horizontalLayout_4.addWidget(self.klasa_betonu_gui)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)
        self.sciezka_dll_gui = QtWidgets.QLineEdit(self.centralwidget)
        self.sciezka_dll_gui.setObjectName("sciezka_dll_gui")
        self.gridLayout.addWidget(self.sciezka_dll_gui, 1, 1, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.sztywnosc_plyty_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sztywnosc_plyty_gui.setEnabled(False)
        self.sztywnosc_plyty_gui.setDecimals(0)
        self.sztywnosc_plyty_gui.setMaximum(300000.0)
        self.sztywnosc_plyty_gui.setProperty("value", 10000.0)
        self.sztywnosc_plyty_gui.setObjectName("sztywnosc_plyty_gui")
        self.horizontalLayout_3.addWidget(self.sztywnosc_plyty_gui)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.grubosc_plyty_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.grubosc_plyty_gui.setEnabled(False)
        self.grubosc_plyty_gui.setDecimals(1)
        self.grubosc_plyty_gui.setMinimum(1.0)
        self.grubosc_plyty_gui.setMaximum(300.0)
        self.grubosc_plyty_gui.setSingleStep(0.1)
        self.grubosc_plyty_gui.setProperty("value", 40.0)
        self.grubosc_plyty_gui.setObjectName("grubosc_plyty_gui")
        self.horizontalLayout_2.addWidget(self.grubosc_plyty_gui)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_10.addWidget(self.label_28)
        self.srednica_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.srednica_gui.setEnabled(False)
        self.srednica_gui.setSingleStep(0.01)
        self.srednica_gui.setProperty("value", 30.0)
        self.srednica_gui.setObjectName("srednica_gui")
        self.horizontalLayout_10.addWidget(self.srednica_gui)
        self.gridLayout.addLayout(self.horizontalLayout_10, 10, 2, 1, 1)
        self.nazwa_projektu_gui = QtWidgets.QLineEdit(self.centralwidget)
        self.nazwa_projektu_gui.setText("")
        self.nazwa_projektu_gui.setObjectName("nazwa_projektu_gui")
        self.gridLayout.addWidget(self.nazwa_projektu_gui, 0, 1, 1, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        self.x_stopy_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_stopy_gui.setMinimum(0.3)
        self.x_stopy_gui.setSingleStep(0.01)
        self.x_stopy_gui.setProperty("value", 1.9)
        self.x_stopy_gui.setObjectName("x_stopy_gui")
        self.horizontalLayout_8.addWidget(self.x_stopy_gui)
        self.gridLayout.addLayout(self.horizontalLayout_8, 10, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_9.addWidget(self.label_27)
        self.y_stopy_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.y_stopy_gui.setMinimum(0.3)
        self.y_stopy_gui.setSingleStep(0.01)
        self.y_stopy_gui.setProperty("value", 1.9)
        self.y_stopy_gui.setObjectName("y_stopy_gui")
        self.horizontalLayout_9.addWidget(self.y_stopy_gui)
        self.gridLayout.addLayout(self.horizontalLayout_9, 10, 1, 1, 1)
        self.guzik_stworz_projekt_gui = QtWidgets.QPushButton(self.centralwidget)
        self.guzik_stworz_projekt_gui.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.guzik_stworz_projekt_gui.setFont(font)
        self.guzik_stworz_projekt_gui.setObjectName("guzik_stworz_projekt_gui")
        self.gridLayout.addWidget(self.guzik_stworz_projekt_gui, 13, 1, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setMinimumSize(QtCore.QSize(280, 0))
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_12.addWidget(self.label_30)
        self.wspolczynnik_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.wspolczynnik_gui.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wspolczynnik_gui.sizePolicy().hasHeightForWidth())
        self.wspolczynnik_gui.setSizePolicy(sizePolicy)
        self.wspolczynnik_gui.setSingleStep(0.01)
        self.wspolczynnik_gui.setProperty("value", 1.3)
        self.wspolczynnik_gui.setObjectName("wspolczynnik_gui")
        self.horizontalLayout_12.addWidget(self.wspolczynnik_gui)
        self.gridLayout.addLayout(self.horizontalLayout_12, 11, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setMinimumSize(QtCore.QSize(0, 0))
        self.label_29.setScaledContents(False)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.obciazenie_gui = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.obciazenie_gui.setEnabled(True)
        self.obciazenie_gui.setMaximum(50000.0)
        self.obciazenie_gui.setSingleStep(0.01)
        self.obciazenie_gui.setProperty("value", 500.0)
        self.obciazenie_gui.setObjectName("obciazenie_gui")
        self.horizontalLayout_11.addWidget(self.obciazenie_gui)
        self.gridLayout.addLayout(self.horizontalLayout_11, 11, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 13, 0, 1, 1)
        self.guzik_zapis_sciezka_gui = QtWidgets.QPushButton(self.centralwidget)
        self.guzik_zapis_sciezka_gui.setObjectName("guzik_zapis_sciezka_gui")
        self.gridLayout.addWidget(self.guzik_zapis_sciezka_gui, 3, 0, 1, 1)
        self.sciezka_zapis_gui = QtWidgets.QLineEdit(self.centralwidget)
        self.sciezka_zapis_gui.setText("")
        self.sciezka_zapis_gui.setObjectName("sciezka_zapis_gui")
        self.gridLayout.addWidget(self.sciezka_zapis_gui, 3, 1, 1, 2)
        Zuraw_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Zuraw_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 26))
        self.menubar.setObjectName("menubar")
        Zuraw_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Zuraw_window)
        self.statusbar.setObjectName("statusbar")
        Zuraw_window.setStatusBar(self.statusbar)

        self.retranslateUi(Zuraw_window)
        self.klasa_betonu_gui.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Zuraw_window)

    def retranslateUi(self, Zuraw_window):
        Zuraw_window.setWindowTitle(QtWidgets.QApplication.translate("Zuraw_window", "Żuraw", None, -1))
        self.guzik_dll_gui.setText(QtWidgets.QApplication.translate("Zuraw_window", "AKTUALIZUJ ŚCIEŻKĘ DLL ROBOTA", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Zuraw_window", "Stopy żurawia:", None, -1))
        self.guzil_sciezka_gui.setText(QtWidgets.QApplication.translate("Zuraw_window", "AKTUALIZUJ ŚCIEŻKĘ SZABLONU", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Zuraw_window", "Siatka [cm] :", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Zuraw_window", "Szerokość x [m] :", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Zuraw_window", "Długość y [m] :", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("Zuraw_window", "Klasa betonu :", None, -1))
        self.klasa_betonu_gui.setCurrentText(QtWidgets.QApplication.translate("Zuraw_window", "C30/37", None, -1))
        self.klasa_betonu_gui.setItemText(0, QtWidgets.QApplication.translate("Zuraw_window", "C20/25", None, -1))
        self.klasa_betonu_gui.setItemText(1, QtWidgets.QApplication.translate("Zuraw_window", "C25/30", None, -1))
        self.klasa_betonu_gui.setItemText(2, QtWidgets.QApplication.translate("Zuraw_window", "C30/37", None, -1))
        self.klasa_betonu_gui.setItemText(3, QtWidgets.QApplication.translate("Zuraw_window", "C35/45", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Zuraw_window", "Sztywność Kz (Kx, Ky = 0.1Kz) [kPa]:", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Zuraw_window", "Grubość [cm] :", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Zuraw_window", "Średnica [cm] :", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Zuraw_window", "Odległość od środka x [m] :", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Zuraw_window", "Płyta fundamentowa:", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("Zuraw_window", "Odległość od środka y [m] :", None, -1))
        self.guzik_stworz_projekt_gui.setText(QtWidgets.QApplication.translate("Zuraw_window", "STWÓRZ PROJEKT", None, -1))
        self.label_30.setText(QtWidgets.QApplication.translate("Zuraw_window", "Współczynnik przejścia na wartość obliczeniową", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Zuraw_window", "Nazwa projektu", None, -1))
        self.label_29.setText(QtWidgets.QApplication.translate("Zuraw_window", "Wartość charakterystyczna obciążenia na stopę [kN] :", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Zuraw_window", "Program Żuraw © Copyright by Mateusz Borecki 2021", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Zuraw_window", "Typowa lokalizacja dll : C:Program FilesAutodeskAutodesk Robot Structural Analysis Professional 2020SystemExeInterop.RobotOM.dll", None, -1))
        self.guzik_zapis_sciezka_gui.setText(QtWidgets.QApplication.translate("Zuraw_window", "AKTUALIZUJ ŚCIEŻKĘ ZAPISU PROJEKTU", None, -1))

