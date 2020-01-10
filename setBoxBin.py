
import  struct
import os
import binascii

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QStandardItemModel
import sys
import mainui as mui

ui = mui.Ui_MainWindow()
model = QStandardItemModel()

bValid="是否有效"
devAddr="设备地址"
collAddr="采集器地址"
protoType="规约类型"
devType="设备类型"

ColumnCount = 5
RowCount=1

headlist = [bValid, devAddr, collAddr, protoType, devType]

def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9') :
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata

DevInfo={bValid:'1', devAddr:'100000000001', collAddr:'000000000000', protoType:'3', devType:'1'}

def saveDev(devinfo):
    binfile=open('parmmetbox.bin', 'ab+')
    databytes = str2hex(devinfo[bValid]).to_bytes(1, byteorder='big')
    binfile.write(databytes)
    databytes = str2hex(devinfo[devAddr]).to_bytes(6, byteorder='big')
    binfile.write(databytes)
    databytes = str2hex(devinfo[collAddr]).to_bytes(6, byteorder='big')
    binfile.write(databytes)
    databytes = str2hex(devinfo[protoType]).to_bytes(1, byteorder='big')
    binfile.write(databytes)
    databytes = str2hex(devinfo[devType]).to_bytes(1, byteorder='big')
    binfile.write(databytes)

    binfile.close()



def addButtonSlot():
    global RowCount
    RowCount = RowCount + 1

    model.setColumnCount(ColumnCount)
    model.setRowCount(RowCount)
    model.setHorizontalHeaderLabels(headlist)
    ui.devInfotableView.setModel(model)

def saveButtonSlot():
    global DevInfo

    os.remove("parmmetbox.bin")

    for i in range(0, RowCount):
        j = 0
        DevInfo[bValid] = model.item(i,j).text()
        j += 1
        print(DevInfo[bValid])

        DevInfo[devAddr] = model.item(i,j).text()
        j += 1
        print(DevInfo[devAddr])

        DevInfo[collAddr] = model.item(i,j).text()
        j += 1
        print(DevInfo[collAddr])

        DevInfo[protoType] = model.item(i,j).text()
        j += 1
        print(DevInfo[protoType])

        DevInfo[devType] = model.item(i,j).text()
        print(DevInfo[devType])

        saveDev(DevInfo)

    ui.statusbar.showMessage("保存成功", 5000)

def readButtonSlot():
    global RowCount
    RowCount = 1

    binfile = open('parmmetbox.bin', 'rb')
    filesize = os.path.getsize("parmmetbox.bin")
    print(filesize)

    Count = int(filesize/15)

    print(Count)
    for i in range(0,Count):
        DevInfo[bValid] = binascii.b2a_hex(binfile.read(1)).decode()
        DevInfo[devAddr] = binascii.b2a_hex(binfile.read(6)).decode()
        DevInfo[collAddr] = binascii.b2a_hex(binfile.read(6)).decode()
        DevInfo[protoType] = binascii.b2a_hex(binfile.read(1)).decode()
        DevInfo[devType] = binascii.b2a_hex(binfile.read(1)).decode()

        #print(DevInfo)

        model.setItem(i, 0, QtGui.QStandardItem(DevInfo[bValid]))
        model.setItem(i, 1, QtGui.QStandardItem(DevInfo[devAddr]))
        model.setItem(i, 2, QtGui.QStandardItem(DevInfo[collAddr]))
        model.setItem(i, 3, QtGui.QStandardItem(DevInfo[protoType]))
        model.setItem(i, 4, QtGui.QStandardItem(DevInfo[devType]))

    model.setColumnCount(ColumnCount)
    RowCount = RowCount + Count - 1
    model.setRowCount(RowCount)
    model.setHorizontalHeaderLabels(headlist)
    ui.devInfotableView.setModel(model)
    ui.statusbar.showMessage("读取成功", 5000)

    binfile.close()


def CreatUI():
    print(111111)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    model.setColumnCount(ColumnCount)
    model.setRowCount(RowCount)
    model.setHorizontalHeaderLabels(headlist)
    ui.devInfotableView.setModel(model)

    ui.addDevButton.clicked.connect(addButtonSlot)
    ui.SaveButton.clicked.connect(saveButtonSlot)
    ui.ReadButton.clicked.connect(readButtonSlot)

    MainWindow.statusBar().setStyleSheet("color:blue")

    MainWindow.setWindowTitle("MeterBoxBin")
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    CreatUI()