# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getforgeui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 250)
        MainWindow.setMinimumSize(QtCore.QSize(520, 250))
        MainWindow.setMaximumSize(QtCore.QSize(520, 250))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.getBut = QtWidgets.QPushButton(self.centralwidget)
        self.getBut.setGeometry(QtCore.QRect(260, 20, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.getBut.setFont(font)
        self.getBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getBut.setStyleSheet("")
        self.getBut.setObjectName("getBut")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(150, 20, 101, 21))
        self.comboBox_1.setMouseTracking(False)
        self.comboBox_1.setEditable(True)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.downBut = QtWidgets.QPushButton(self.centralwidget)
        self.downBut.setGeometry(QtCore.QRect(360, 20, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.downBut.setFont(font)
        self.downBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downBut.setStyleSheet("")
        self.downBut.setObjectName("downBut")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(19, 130, 481, 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 78))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.disFrame = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.disFrame.setGeometry(QtCore.QRect(0, 0, 481, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.disFrame.setFont(font)
        self.disFrame.setReadOnly(True)
        self.disFrame.setMarkdown("")
        self.disFrame.setObjectName("disFrame")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 220, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.depthLine = QtWidgets.QLineEdit(self.centralwidget)
        self.depthLine.setGeometry(QtCore.QRect(150, 100, 101, 21))
        self.depthLine.setObjectName("depthLine")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyGetForge-withoutAD"))
        self.getBut.setText(_translate("MainWindow", "Get"))
        self.label_1.setText(_translate("MainWindow", "Sel version："))
        self.label_2.setText(_translate("MainWindow", "Sel type:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", ".exe"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", ".zip"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", ".jar"))
        self.label_3.setText(_translate("MainWindow", "若程序卡死，请等待获取"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "1.12.2"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "1.12.1"))
        self.downBut.setText(_translate("MainWindow", "Download"))
        self.disFrame.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:16pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><a href=\'www.baidu.com\'>Forge</a><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "depth(>520):"))
        self.depthLine.setText(_translate("MainWindow", "520"))
