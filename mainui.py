# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.devInfotableView = QtWidgets.QTableView(self.centralwidget)
        self.devInfotableView.setObjectName("devInfotableView")
        self.horizontalLayout.addWidget(self.devInfotableView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addDevButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDevButton.setObjectName("addDevButton")
        self.verticalLayout.addWidget(self.addDevButton)
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ReadButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReadButton.setObjectName("ReadButton")
        self.verticalLayout.addWidget(self.ReadButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.verticalLayout.addWidget(self.SaveButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addDevButton.setText(_translate("MainWindow", "增加设备"))
        self.ReadButton.setText(_translate("MainWindow", "读取"))
        self.SaveButton.setText(_translate("MainWindow", "保存"))
