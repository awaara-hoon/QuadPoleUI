import requests, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread, pyqtSignal
from requests.models import Response
from pyqtgraph import PlotWidget
# import pyqtgraph as pg
import numpy as np
import time
import random as rd
import pyqtgraph as pg



# BASE = "http://192.168.1.160:5000"
BASE = "http://10.0.0.17:5000"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1096, 681))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.groupBox = QtWidgets.QGroupBox(self.tab_main)
        self.groupBox.setGeometry(QtCore.QRect(25, 5, 1021, 241))
        self.groupBox.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lcd_220V_i = QtWidgets.QLCDNumber(self.groupBox)
        self.lcd_220V_i.setGeometry(QtCore.QRect(60, 40, 156, 51))
        self.lcd_220V_i.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lcd_220V_i.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_220V_i.setProperty("value", 1.16)
        self.lcd_220V_i.setObjectName("lcd_220V_i")
        self.lcd_400V_i = QtWidgets.QLCDNumber(self.groupBox)
        self.lcd_400V_i.setGeometry(QtCore.QRect(310, 40, 156, 51))
        self.lcd_400V_i.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lcd_400V_i.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_400V_i.setProperty("value", 3.55)
        self.lcd_400V_i.setObjectName("lcd_400V_i")
        self.lcd_24V = QtWidgets.QLCDNumber(self.groupBox)
        self.lcd_24V.setGeometry(QtCore.QRect(570, 40, 156, 51))
        self.lcd_24V.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lcd_24V.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_24V.setProperty("value", 23.99)
        self.lcd_24V.setObjectName("lcd_24V")
        self.lcd_tension = QtWidgets.QLCDNumber(self.groupBox)
        self.lcd_tension.setGeometry(QtCore.QRect(815, 40, 156, 51))
        self.lcd_tension.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lcd_tension.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_tension.setProperty("value", 1346.0)
        self.lcd_tension.setProperty("intValue", 1346)
        self.lcd_tension.setObjectName("lcd_tension")
        self.button_400V_onoff = QtWidgets.QPushButton(self.groupBox)
        self.button_400V_onoff.setGeometry(QtCore.QRect(326, 130, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_400V_onoff.setFont(font)
        self.button_400V_onoff.setObjectName("button_400V_onoff")
        self.button_Ziehl_onoff = QtWidgets.QPushButton(self.groupBox)
        self.button_Ziehl_onoff.setGeometry(QtCore.QRect(325, 175, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_Ziehl_onoff.setFont(font)
        self.button_Ziehl_onoff.setObjectName("button_Ziehl_onoff")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 20, 136, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 136, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(580, 20, 136, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(825, 20, 136, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_main)
        self.groupBox_2.setGeometry(QtCore.QRect(25, 275, 461, 346))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_reel_en = QtWidgets.QPushButton(self.groupBox_2)
        self.button_reel_en.setGeometry(QtCore.QRect(45, 55, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_reel_en.setFont(font)
        self.button_reel_en.setObjectName("button_reel_en")
        self.line_tension = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_tension.setGeometry(QtCore.QRect(135, 55, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_tension.setFont(font)
        self.line_tension.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_tension.setObjectName("line_tension")
        self.line_speed_reel = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_speed_reel.setGeometry(QtCore.QRect(225, 55, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_speed_reel.setFont(font)
        self.line_speed_reel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_speed_reel.setObjectName("line_speed_reel")
        self.button_reelOff = QtWidgets.QPushButton(self.groupBox_2)
        self.button_reelOff.setGeometry(QtCore.QRect(320, 55, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_reelOff.setFont(font)
        self.button_reelOff.setObjectName("button_reelOff")
        self.lcd_cableOut = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcd_cableOut.setGeometry(QtCore.QRect(135, 100, 116, 31))
        self.lcd_cableOut.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lcd_cableOut.setDigitCount(7)
        self.lcd_cableOut.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_cableOut.setProperty("value", -102.35)
        self.lcd_cableOut.setProperty("intValue", -102)
        self.lcd_cableOut.setObjectName("lcd_cableOut")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 105, 66, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(265, 105, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.button_reel_calib = QtWidgets.QPushButton(self.groupBox_2)
        self.button_reel_calib.setGeometry(QtCore.QRect(320, 105, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_reel_calib.setFont(font)
        self.button_reel_calib.setObjectName("button_reel_calib")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(50, 145, 336, 23))
        self.progressBar.setProperty("value", 25)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.label_reelState = QtWidgets.QLabel(self.groupBox_2)
        self.label_reelState.setGeometry(QtCore.QRect(55, 190, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_reelState.setFont(font)
        self.label_reelState.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_reelState.setObjectName("label_reelState")
        self.label_cableDir = QtWidgets.QLabel(self.groupBox_2)
        self.label_cableDir.setGeometry(QtCore.QRect(55, 220, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cableDir.setFont(font)
        self.label_cableDir.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_cableDir.setObjectName("label_cableDir")
        self.button_reelPanic = QtWidgets.QPushButton(self.groupBox_2)
        self.button_reelPanic.setGeometry(QtCore.QRect(160, 263, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_reelPanic.setFont(font)
        self.button_reelPanic.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(200, 0, 0);")
        self.button_reelPanic.setObjectName("button_reelPanic")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(140, 35, 48, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(230, 35, 48, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_main)
        self.groupBox_3.setGeometry(QtCore.QRect(585, 275, 461, 346))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.button_a = QtWidgets.QPushButton(self.groupBox_3)
        self.button_a.setGeometry(QtCore.QRect(70, 55, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_a.setFont(font)
        self.button_a.setObjectName("button_a")
        self.line_timeA = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_timeA.setGeometry(QtCore.QRect(250, 55, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_timeA.setFont(font)
        self.line_timeA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_timeA.setObjectName("line_timeA")
        self.button_a_go = QtWidgets.QPushButton(self.groupBox_3)
        self.button_a_go.setGeometry(QtCore.QRect(345, 55, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_a_go.setFont(font)
        self.button_a_go.setObjectName("button_a_go")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(165, 35, 48, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_speed_a = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_speed_a.setGeometry(QtCore.QRect(160, 55, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_speed_a.setFont(font)
        self.line_speed_a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_speed_a.setObjectName("line_speed_a")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(255, 35, 48, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_timeC_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_timeC_2.setGeometry(QtCore.QRect(250, 95, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_timeC_2.setFont(font)
        self.line_timeC_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_timeC_2.setObjectName("line_timeC_2")
        self.button_b = QtWidgets.QPushButton(self.groupBox_3)
        self.button_b.setGeometry(QtCore.QRect(70, 95, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_b.setFont(font)
        self.button_b.setObjectName("button_b")
        self.button_b_go = QtWidgets.QPushButton(self.groupBox_3)
        self.button_b_go.setGeometry(QtCore.QRect(345, 95, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_b_go.setFont(font)
        self.button_b_go.setObjectName("button_b_go")
        self.line_speed_b = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_speed_b.setGeometry(QtCore.QRect(160, 95, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_speed_b.setFont(font)
        self.line_speed_b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_speed_b.setObjectName("line_speed_b")
        self.line_timeC = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_timeC.setGeometry(QtCore.QRect(250, 135, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_timeC.setFont(font)
        self.line_timeC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_timeC.setObjectName("line_timeC")
        self.button_c = QtWidgets.QPushButton(self.groupBox_3)
        self.button_c.setGeometry(QtCore.QRect(70, 135, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_c.setFont(font)
        self.button_c.setObjectName("button_c")
        self.button_c_go = QtWidgets.QPushButton(self.groupBox_3)
        self.button_c_go.setGeometry(QtCore.QRect(345, 135, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_c_go.setFont(font)
        self.button_c_go.setObjectName("button_c_go")
        self.line_speed_c = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_speed_c.setGeometry(QtCore.QRect(160, 135, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_speed_c.setFont(font)
        self.line_speed_c.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_speed_c.setObjectName("line_speed_c")
        self.line_timeD = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_timeD.setGeometry(QtCore.QRect(250, 175, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_timeD.setFont(font)
        self.line_timeD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_timeD.setObjectName("line_timeD")
        self.button_d = QtWidgets.QPushButton(self.groupBox_3)
        self.button_d.setGeometry(QtCore.QRect(70, 175, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_d.setFont(font)
        self.button_d.setObjectName("button_d")
        self.button_d_go = QtWidgets.QPushButton(self.groupBox_3)
        self.button_d_go.setGeometry(QtCore.QRect(345, 175, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_d_go.setFont(font)
        self.button_d_go.setObjectName("button_d_go")
        self.line_speed_d = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_speed_d.setGeometry(QtCore.QRect(160, 175, 76, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_speed_d.setFont(font)
        self.line_speed_d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_speed_d.setObjectName("line_speed_d")
        self.button_reelPanic_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_reelPanic_2.setGeometry(QtCore.QRect(170, 265, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_reelPanic_2.setFont(font)
        self.button_reelPanic_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(200, 0, 0);")
        self.button_reelPanic_2.setObjectName("button_reelPanic_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(25, 55, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(25, 95, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(25, 135, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(25, 175, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_graph = QtWidgets.QWidget()
        self.tab_graph.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.tab_graph.setObjectName("tab_graph")
        self.graphicsView_1 = PlotWidget(self.tab_graph)
        self.graphicsView_1.setGeometry(QtCore.QRect(15, 10, 1061, 316))
        self.graphicsView_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.graphicsView_2 = PlotWidget(self.tab_graph)
        self.graphicsView_2.setGeometry(QtCore.QRect(15, 330, 1061, 316))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tabWidget.addTab(self.tab_graph, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuadPole"))
        self.button_400V_onoff.setText(_translate("MainWindow", "400V OFF"))
        self.button_Ziehl_onoff.setText(_translate("MainWindow", "Ziehl OFF"))
        self.label.setText(_translate("MainWindow", "220V - current, A"))
        self.label_2.setText(_translate("MainWindow", "400V - current, A"))
        self.label_3.setText(_translate("MainWindow", "24V"))
        self.label_4.setText(_translate("MainWindow", "Tension, g"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Reel"))
        self.button_reel_en.setText(_translate("MainWindow", "Normal"))
        self.line_tension.setText(_translate("MainWindow", "100"))
        self.line_speed_reel.setText(_translate("MainWindow", "300"))
        self.button_reelOff.setText(_translate("MainWindow", "OFF"))
        self.label_5.setText(_translate("MainWindow", "Cable out"))
        self.label_6.setText(_translate("MainWindow", "m"))
        self.button_reel_calib.setText(_translate("MainWindow", ">0<"))
        self.label_reelState.setText(_translate("MainWindow", "Reel State"))
        self.label_cableDir.setText(_translate("MainWindow", "Direction"))
        self.button_reelPanic.setText(_translate("MainWindow", "STOP"))
        self.label_7.setText(_translate("MainWindow", "Tension"))
        self.label_8.setText(_translate("MainWindow", "Speed"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Doors"))
        self.button_a.setText(_translate("MainWindow", "Open"))
        self.line_timeA.setText(_translate("MainWindow", "15"))
        self.button_a_go.setText(_translate("MainWindow", "GO"))
        self.label_9.setText(_translate("MainWindow", "Speed"))
        self.line_speed_a.setText(_translate("MainWindow", "70"))
        self.label_10.setText(_translate("MainWindow", "Time"))
        self.line_timeC_2.setText(_translate("MainWindow", "15"))
        self.button_b.setText(_translate("MainWindow", "Open"))
        self.button_b_go.setText(_translate("MainWindow", "GO"))
        self.line_speed_b.setText(_translate("MainWindow", "70"))
        self.line_timeC.setText(_translate("MainWindow", "15"))
        self.button_c.setText(_translate("MainWindow", "Open"))
        self.button_c_go.setText(_translate("MainWindow", "GO"))
        self.line_speed_c.setText(_translate("MainWindow", "70"))
        self.line_timeD.setText(_translate("MainWindow", "15"))
        self.button_d.setText(_translate("MainWindow", "Open"))
        self.button_d_go.setText(_translate("MainWindow", "GO"))
        self.line_speed_d.setText(_translate("MainWindow", "70"))
        self.button_reelPanic_2.setText(_translate("MainWindow", "STOP"))
        self.label_11.setText(_translate("MainWindow", "A"))
        self.label_12.setText(_translate("MainWindow", "B"))
        self.label_13.setText(_translate("MainWindow", "C"))
        self.label_14.setText(_translate("MainWindow", "D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_graph), _translate("MainWindow", "Graph"))

        
        self.button_a.clicked.connect(self.button_a_toggle)
        self.button_a_go.clicked.connect(self.door_a_put)
        self.button_b.clicked.connect(self.button_b_toggle)
        self.button_b_go.clicked.connect(self.door_b_put)
        self.button_c.clicked.connect(self.button_c_toggle)
        self.button_c_go.clicked.connect(self.door_c_put)
        self.button_d.clicked.connect(self.button_d_toggle)
        self.button_d_go.clicked.connect(self.door_d_put)
        self.button_reel_en.clicked.connect(self.reel_enable)
        self.button_reelOff.clicked.connect(self.reel_off)
        self.button_reel_calib.clicked.connect(self.reel_calib)
        self.button_reelPanic.clicked.connect(self.reel_off)
        self.button_400V_onoff.clicked.connect(self.button_400V_toggle)
        self.button_Ziehl_onoff.clicked.connect(self.button_Ziehl_toggle)
        self.polling()



        self.graphicsView_1.setTitle("Graph 1")
        self.graphicsView_2.setTitle("Graph 2")



    # def graph_220v_i(self):


# DOOR A CONTROL
    door_a_state = 1
    def button_a_toggle(self):
        if self.button_a.text() == "Open":
            self.button_a.setText("Close")
            self.door_a_state = -1
        else: 
            self.button_a.setText("Open")
            self.door_a_state = 1
    
    def door_a_put(self):
        if self.door_a_state == -1:
            requests.put(BASE + "/door_control?door=a", {
            'velocity':'-' + self.line_speed_a.text(),
            'duration':self.line_timeA.text()
            })
        else:
            requests.put(BASE + "/door_control?door=a", {
            'velocity':self.line_speed_a.text(),
            'duration':self.line_timeA.text()
            })

# DOOR B CONTROL
    door_b_state = 1
    def button_b_toggle(self):    
        if self.button_b.text() == "Open":
            self.button_b.setText("Close")
            self.door_b_state = -1
        else: 
            self.button_b.setText("Open")
            self.door_b_state = 1
    
    def door_b_put(self):
        if self.door_b_state == -1:
            requests.put(BASE + "/door_control?door=b", {
            'velocity':'-' + self.line_speed_b.text(),
            'duration':self.line_timeB.text()
            })
        else:
            requests.put(BASE + "/door_control?door=b", {
            'velocity':self.line_speed_b.text(),
            'duration':self.line_timeB.text()
            })

# DOOR C CONTROL
    door_c_state = 1
    def button_c_toggle(self):   
        if self.button_c.text() == "Open":
            self.button_c.setText("Close")
            self.door_c_state = -1
        else: 
            self.button_c.setText("Open")
            self.door_c_state = 1
    
    def door_c_put(self):
        if self.door_c_state == -1:
            requests.put(BASE + "/door_control?door=c", {
            'velocity':'-' + self.line_speed_c.text(),
            'duration':self.line_timeC.text()
            })
        else:
            requests.put(BASE + "/door_control?door=c", {
            'velocity':self.line_speed_c.text(),
            'duration':self.line_timeC.text()
            })

# DOOR D CONTROL
    door_d_state = 1
    def button_d_toggle(self):  
        if self.button_d.text() == "Open":
            self.button_d.setText("Close")
            self.door_d_state = -1
        else: 
            self.button_d.setText("Open")
            self.door_d_state = 1
    
    def door_d_put(self):
        if self.door_d_state == -1:
            requests.put(BASE + "/door_control?door=d", {
            'velocity':'-' + self.line_speed_d.text(),
            'duration':self.line_timeD.text()
            })
        else:
            requests.put(BASE + "/door_control?door=d", {
            'velocity':self.line_speed_d.text(),
            'duration':self.line_timeD.text()
            })

# 400V CONTROL
    def button_400V_toggle(self):
        is_on = 0      
        if self.button_400V_onoff.text() == "400V OFF":
            self.button_400V_onoff.setText("400V ON")
            self.button_400V_onoff.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 170, 0);")
            is_on = 1
        else: 
            self.button_400V_onoff.setText("400V OFF")
            is_on = 0
            self.button_400V_onoff.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(222, 222, 222);")
        requests.put(BASE + "/400v_regulator_control?is_on="+str(is_on), {})

# ZIEHL CONTROL
    def button_Ziehl_toggle(self):
        is_on = 1      
        if self.button_Ziehl_onoff.text() == "Ziehl OFF":
            self.button_Ziehl_onoff.setText("Ziehl ON")
            self.button_Ziehl_onoff.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 170, 0);")
            is_on = 0
        else: 
            self.button_Ziehl_onoff.setText("Ziehl OFF")
            is_on = 1
            self.button_Ziehl_onoff.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(222, 222, 222);")
        requests.put(BASE + "/ZIEHL_control?enabled="+str(is_on), {})

# REEL CONTROL
    def reel_enable(self):
        self.button_reel_en.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 170, 0);")
        requests.post(BASE + "/set_winch?mode=regular", {
            'tension':self.line_tension.text(),    
            'velocity':self.line_speed_reel.text()
        })
    
    def reel_off(self):
        self.button_reel_en.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(222, 222, 222);")
        requests.post(BASE + "/set_winch?mode=disable", {
            'tension':'0',    
        })

    def reel_calib(self):
        requests.post(BASE + "/set_winch?mode=calib&calib_winch?set_edge=rolled", {
            'tension':'0', 
        })
        
    def polling(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_polling.connect(self.polling_update)

    def polling_update(self,val):
        value_24v = round(val.json()["24v_vout"]/850*24,1)
        self.lcd_24V.setProperty("value", value_24v)
        value_220i = round(val.json()["220vac_ain"]/175,2)
        self.lcd_220V_i.setProperty("value", value_220i)
        value_400i = round((val.json()["400v_aout"]-20)/30.5,2)
        self.lcd_400V_i.setProperty("value", value_400i)
        value_tension = round((val.json()["load_cell"]-680)*11.2,0)
        self.lcd_tension.setProperty("value", value_tension)
        # value_rope = round(val.json()["TotalRope"]/100,2)
        # self.lcd_cableOut.setProperty("value", value_rope)
        # self.progressBar.setProperty("value", value_rope)

class WorkerThread(QThread):
    update_polling = pyqtSignal(Response)
    def run(self):
        while True:
            poll = requests.get(BASE + "/data?param=400v_aout&param=24v_vout&param=220vac_ain&param=load_cell", {})
            self.update_polling.emit(poll)
            time.sleep(0.2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
