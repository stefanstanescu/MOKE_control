# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SolMOKE_GUI.ui'
#
# Created: Tue Mar  8 14:04:32 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1122, 786)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1122, 786))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(1122, 760))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabMotionCtrlWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMotionCtrlWidget.sizePolicy().hasHeightForWidth())
        self.tabMotionCtrlWidget.setSizePolicy(sizePolicy)
        self.tabMotionCtrlWidget.setMaximumSize(QtCore.QSize(1104, 742))
        self.tabMotionCtrlWidget.setObjectName(_fromUtf8("tabMotionCtrlWidget"))
        self.tabTimescan = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabTimescan.sizePolicy().hasHeightForWidth())
        self.tabTimescan.setSizePolicy(sizePolicy)
        self.tabTimescan.setMaximumSize(QtCore.QSize(1100, 705))
        self.tabTimescan.setMouseTracking(False)
        self.tabTimescan.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabTimescan.setAcceptDrops(False)
        self.tabTimescan.setAccessibleName(_fromUtf8(""))
        self.tabTimescan.setAccessibleDescription(_fromUtf8(""))
        self.tabTimescan.setAutoFillBackground(False)
        self.tabTimescan.setObjectName(_fromUtf8("tabTimescan"))
        self.gridLayoutWidget = QtGui.QWidget(self.tabTimescan)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 200, 171, 321))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stopTimescanBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.stopTimescanBtn.setObjectName(_fromUtf8("stopTimescanBtn"))
        self.gridLayout.addWidget(self.stopTimescanBtn, 7, 0, 1, 1)
        self.startTimescanBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.startTimescanBtn.setObjectName(_fromUtf8("startTimescanBtn"))
        self.gridLayout.addWidget(self.startTimescanBtn, 5, 0, 1, 1)
        self.saveTimescanFileName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.saveTimescanFileName.setText(_fromUtf8(""))
        self.saveTimescanFileName.setObjectName(_fromUtf8("saveTimescanFileName"))
        self.gridLayout.addWidget(self.saveTimescanFileName, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tempLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.gridLayout_2.addWidget(self.tempLabel, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.fieldCtrlSlider = QtGui.QSlider(self.gridLayoutWidget)
        self.fieldCtrlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fieldCtrlSlider.setObjectName(_fromUtf8("fieldCtrlSlider"))
        self.gridLayout_2.addWidget(self.fieldCtrlSlider, 4, 1, 1, 1)
        self.lockInRadioBtn = QtGui.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lockInRadioBtn.setFont(font)
        self.lockInRadioBtn.setObjectName(_fromUtf8("lockInRadioBtn"))
        self.gridLayout_2.addWidget(self.lockInRadioBtn, 1, 1, 1, 1)
        self.tempRadioBtn = QtGui.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tempRadioBtn.setFont(font)
        self.tempRadioBtn.setObjectName(_fromUtf8("tempRadioBtn"))
        self.gridLayout_2.addWidget(self.tempRadioBtn, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tempCtrlSlider = QtGui.QSlider(self.gridLayoutWidget)
        self.tempCtrlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tempCtrlSlider.setObjectName(_fromUtf8("tempCtrlSlider"))
        self.gridLayout_2.addWidget(self.tempCtrlSlider, 4, 0, 1, 1)
        self.fieldLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.fieldLabel.setObjectName(_fromUtf8("fieldLabel"))
        self.gridLayout_2.addWidget(self.fieldLabel, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lcdTemp = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdTemp.setMaximumSize(QtCore.QSize(86, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdTemp.setFont(font)
        self.lcdTemp.setObjectName(_fromUtf8("lcdTemp"))
        self.gridLayout_2.addWidget(self.lcdTemp, 3, 0, 1, 1)
        self.lcdField = QtGui.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdField.sizePolicy().hasHeightForWidth())
        self.lcdField.setSizePolicy(sizePolicy)
        self.lcdField.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdField.setFont(font)
        self.lcdField.setObjectName(_fromUtf8("lcdField"))
        self.gridLayout_2.addWidget(self.lcdField, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.workDirBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.workDirBtn.setObjectName(_fromUtf8("workDirBtn"))
        self.gridLayout.addWidget(self.workDirBtn, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.graphicsViewTime = PlotWidget(self.tabTimescan)
        self.graphicsViewTime.setGeometry(QtCore.QRect(198, 8, 891, 681))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewTime.sizePolicy().hasHeightForWidth())
        self.graphicsViewTime.setSizePolicy(sizePolicy)
        self.graphicsViewTime.setMaximumSize(QtCore.QSize(1280, 1024))
        self.graphicsViewTime.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsViewTime.setLineWidth(5)
        self.graphicsViewTime.setObjectName(_fromUtf8("graphicsViewTime"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tabTimescan)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 78, 179, 32))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.LakeshoreLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.LakeshoreLabel.setMaximumSize(QtCore.QSize(53, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LakeshoreLabel.setFont(font)
        self.LakeshoreLabel.setAutoFillBackground(True)
        self.LakeshoreLabel.setObjectName(_fromUtf8("LakeshoreLabel"))
        self.horizontalLayout_2.addWidget(self.LakeshoreLabel)
        self.LakeshoreONbutn = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.LakeshoreONbutn.setObjectName(_fromUtf8("LakeshoreONbutn"))
        self.horizontalLayout_2.addWidget(self.LakeshoreONbutn)
        self.LakeshoreOFFbutn = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.LakeshoreOFFbutn.setObjectName(_fromUtf8("LakeshoreOFFbutn"))
        self.horizontalLayout_2.addWidget(self.LakeshoreOFFbutn)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tabTimescan)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(5, 48, 179, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.MagnetLabel = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.MagnetLabel.setMaximumSize(QtCore.QSize(53, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MagnetLabel.setFont(font)
        self.MagnetLabel.setAutoFillBackground(True)
        self.MagnetLabel.setObjectName(_fromUtf8("MagnetLabel"))
        self.horizontalLayout_4.addWidget(self.MagnetLabel)
        self.MagnetONbutn = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.MagnetONbutn.setObjectName(_fromUtf8("MagnetONbutn"))
        self.horizontalLayout_4.addWidget(self.MagnetONbutn)
        self.MagnetOFFbutn = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.MagnetOFFbutn.setObjectName(_fromUtf8("MagnetOFFbutn"))
        self.horizontalLayout_4.addWidget(self.MagnetOFFbutn)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tabTimescan)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(5, 18, 179, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LockInLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.LockInLabel.setMaximumSize(QtCore.QSize(53, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LockInLabel.setFont(font)
        self.LockInLabel.setAutoFillBackground(True)
        self.LockInLabel.setObjectName(_fromUtf8("LockInLabel"))
        self.horizontalLayout_3.addWidget(self.LockInLabel)
        self.LockInONbutn = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.LockInONbutn.setObjectName(_fromUtf8("LockInONbutn"))
        self.horizontalLayout_3.addWidget(self.LockInONbutn)
        self.LockInOFFbutn = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.LockInOFFbutn.setObjectName(_fromUtf8("LockInOFFbutn"))
        self.horizontalLayout_3.addWidget(self.LockInOFFbutn)
        self.tabMotionCtrlWidget.addTab(self.tabTimescan, _fromUtf8(""))
        self.tabHysteresis = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabHysteresis.sizePolicy().hasHeightForWidth())
        self.tabHysteresis.setSizePolicy(sizePolicy)
        self.tabHysteresis.setObjectName(_fromUtf8("tabHysteresis"))
        self.graphicsViewFieldSingle = PlotWidget(self.tabHysteresis)
        self.graphicsViewFieldSingle.setGeometry(QtCore.QRect(198, 1, 891, 350))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewFieldSingle.sizePolicy().hasHeightForWidth())
        self.graphicsViewFieldSingle.setSizePolicy(sizePolicy)
        self.graphicsViewFieldSingle.setMaximumSize(QtCore.QSize(911, 681))
        self.graphicsViewFieldSingle.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsViewFieldSingle.setObjectName(_fromUtf8("graphicsViewFieldSingle"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tabHysteresis)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(8, 200, 171, 308))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.startFieldLine = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.startFieldLine.setObjectName(_fromUtf8("startFieldLine"))
        self.horizontalLayout_6.addWidget(self.startFieldLine)
        self.endFieldLine = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.endFieldLine.setObjectName(_fromUtf8("endFieldLine"))
        self.horizontalLayout_6.addWidget(self.endFieldLine)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)
        self.labelHystFileName = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelHystFileName.setFont(font)
        self.labelHystFileName.setObjectName(_fromUtf8("labelHystFileName"))
        self.gridLayout_7.addWidget(self.labelHystFileName, 1, 0, 1, 1)
        self.noHystCycles = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.noHystCycles.setObjectName(_fromUtf8("noHystCycles"))
        self.gridLayout_7.addWidget(self.noHystCycles, 5, 0, 1, 1)
        self.cancelHystBtn = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.cancelHystBtn.setObjectName(_fromUtf8("cancelHystBtn"))
        self.gridLayout_7.addWidget(self.cancelHystBtn, 9, 0, 1, 1)
        self.startHystBtn = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.startHystBtn.setObjectName(_fromUtf8("startHystBtn"))
        self.gridLayout_7.addWidget(self.startHystBtn, 7, 0, 1, 1)
        self.labelCyclesNo = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelCyclesNo.setFont(font)
        self.labelCyclesNo.setObjectName(_fromUtf8("labelCyclesNo"))
        self.gridLayout_7.addWidget(self.labelCyclesNo, 4, 0, 1, 1)
        self.saveHystFileName = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.saveHystFileName.setObjectName(_fromUtf8("saveHystFileName"))
        self.gridLayout_7.addWidget(self.saveHystFileName, 2, 0, 1, 1)
        self.workDirBtn_1 = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.workDirBtn_1.setObjectName(_fromUtf8("workDirBtn_1"))
        self.gridLayout_7.addWidget(self.workDirBtn_1, 0, 0, 1, 1)
        self.graphicsViewFieldSingleMulti = PlotWidget(self.tabHysteresis)
        self.graphicsViewFieldSingleMulti.setGeometry(QtCore.QRect(197, 355, 891, 350))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewFieldSingleMulti.sizePolicy().hasHeightForWidth())
        self.graphicsViewFieldSingleMulti.setSizePolicy(sizePolicy)
        self.graphicsViewFieldSingleMulti.setMaximumSize(QtCore.QSize(911, 681))
        self.graphicsViewFieldSingleMulti.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsViewFieldSingleMulti.setObjectName(_fromUtf8("graphicsViewFieldSingleMulti"))
        self.tabMotionCtrlWidget.addTab(self.tabHysteresis, _fromUtf8(""))
        self.tabTemperature = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabTemperature.sizePolicy().hasHeightForWidth())
        self.tabTemperature.setSizePolicy(sizePolicy)
        self.tabTemperature.setObjectName(_fromUtf8("tabTemperature"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.tabTemperature)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 360, 171, 214))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.labelHystFileName_2 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelHystFileName_2.setFont(font)
        self.labelHystFileName_2.setObjectName(_fromUtf8("labelHystFileName_2"))
        self.gridLayout_8.addWidget(self.labelHystFileName_2, 2, 0, 1, 1)
        self.cancelTempBtn = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.cancelTempBtn.setObjectName(_fromUtf8("cancelTempBtn"))
        self.gridLayout_8.addWidget(self.cancelTempBtn, 8, 0, 1, 1)
        self.startTempBtn = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.startTempBtn.setObjectName(_fromUtf8("startTempBtn"))
        self.gridLayout_8.addWidget(self.startTempBtn, 6, 0, 1, 1)
        self.workDirBtn_4 = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.workDirBtn_4.setObjectName(_fromUtf8("workDirBtn_4"))
        self.gridLayout_8.addWidget(self.workDirBtn_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.startTempLine = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.startTempLine.setObjectName(_fromUtf8("startTempLine"))
        self.horizontalLayout_5.addWidget(self.startTempLine)
        self.endTempLine = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.endTempLine.setObjectName(_fromUtf8("endTempLine"))
        self.horizontalLayout_5.addWidget(self.endTempLine)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.saveTempFileName = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.saveTempFileName.setObjectName(_fromUtf8("saveTempFileName"))
        self.gridLayout_8.addWidget(self.saveTempFileName, 4, 0, 1, 1)
        self.graphicsViewTemp = PlotWidget(self.tabTemperature)
        self.graphicsViewTemp.setGeometry(QtCore.QRect(198, 8, 891, 681))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewTemp.sizePolicy().hasHeightForWidth())
        self.graphicsViewTemp.setSizePolicy(sizePolicy)
        self.graphicsViewTemp.setMaximumSize(QtCore.QSize(911, 681))
        self.graphicsViewTemp.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsViewTemp.setObjectName(_fromUtf8("graphicsViewTemp"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tabTemperature)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 148, 191, 151))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.readTempLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.readTempLabel.setAutoFillBackground(True)
        self.readTempLabel.setText(_fromUtf8(""))
        self.readTempLabel.setObjectName(_fromUtf8("readTempLabel"))
        self.gridLayout_3.addWidget(self.readTempLabel, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.setTempLine = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.setTempLine.setObjectName(_fromUtf8("setTempLine"))
        self.gridLayout_3.addWidget(self.setTempLine, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.tempHeaterOutputBar = QtGui.QProgressBar(self.gridLayoutWidget_2)
        self.tempHeaterOutputBar.setProperty("value", 0)
        self.tempHeaterOutputBar.setOrientation(QtCore.Qt.Horizontal)
        self.tempHeaterOutputBar.setObjectName(_fromUtf8("tempHeaterOutputBar"))
        self.gridLayout_3.addWidget(self.tempHeaterOutputBar, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.setTempRampLine = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.setTempRampLine.setObjectName(_fromUtf8("setTempRampLine"))
        self.gridLayout_3.addWidget(self.setTempRampLine, 3, 1, 1, 1)
        self.tabMotionCtrlWidget.addTab(self.tabTemperature, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabMotionCtrlWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabMotionCtrlWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabMotionCtrlWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tempCtrlSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdTemp.display)
        QtCore.QObject.connect(self.fieldCtrlSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdField.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MOKE CONTROL", None))
        self.stopTimescanBtn.setText(_translate("MainWindow", "STOP", None))
        self.startTimescanBtn.setText(_translate("MainWindow", "START", None))
        self.tempLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Temperature</span></p></body></html>", None))
        self.lockInRadioBtn.setText(_translate("MainWindow", "lockIn", None))
        self.tempRadioBtn.setText(_translate("MainWindow", "temp", None))
        self.label.setText(_translate("MainWindow", "Sensor", None))
        self.fieldLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#aa0000;\">Field</span></p></body></html>", None))
        self.workDirBtn.setText(_translate("MainWindow", "WorkDir", None))
        self.label_5.setText(_translate("MainWindow", "File Name", None))
        self.LakeshoreLabel.setText(_translate("MainWindow", "Lakeshore", None))
        self.LakeshoreONbutn.setText(_translate("MainWindow", "ON", None))
        self.LakeshoreOFFbutn.setText(_translate("MainWindow", "OFF", None))
        self.MagnetLabel.setText(_translate("MainWindow", "Magnet", None))
        self.MagnetONbutn.setText(_translate("MainWindow", "ON", None))
        self.MagnetOFFbutn.setText(_translate("MainWindow", "OFF", None))
        self.LockInLabel.setText(_translate("MainWindow", "LockIn", None))
        self.LockInONbutn.setText(_translate("MainWindow", "ON", None))
        self.LockInOFFbutn.setText(_translate("MainWindow", "OFF", None))
        self.tabMotionCtrlWidget.setTabText(self.tabMotionCtrlWidget.indexOf(self.tabTimescan), _translate("MainWindow", "GENERAL CONTROL", None))
        self.startFieldLine.setText(_translate("MainWindow", "start Field", None))
        self.endFieldLine.setText(_translate("MainWindow", "end Field", None))
        self.labelHystFileName.setText(_translate("MainWindow", "File Name", None))
        self.cancelHystBtn.setText(_translate("MainWindow", "CANCEL", None))
        self.startHystBtn.setText(_translate("MainWindow", "START", None))
        self.labelCyclesNo.setText(_translate("MainWindow", "No cycles", None))
        self.workDirBtn_1.setText(_translate("MainWindow", "WorkDir", None))
        self.tabMotionCtrlWidget.setTabText(self.tabMotionCtrlWidget.indexOf(self.tabHysteresis), _translate("MainWindow", "MAGNETIC CONTROL", None))
        self.labelHystFileName_2.setText(_translate("MainWindow", "File Name", None))
        self.cancelTempBtn.setText(_translate("MainWindow", "CANCEL", None))
        self.startTempBtn.setText(_translate("MainWindow", "START", None))
        self.workDirBtn_4.setText(_translate("MainWindow", "WorkDir", None))
        self.startTempLine.setText(_translate("MainWindow", "start Temp", None))
        self.endTempLine.setText(_translate("MainWindow", "end Temp", None))
        self.label_2.setText(_translate("MainWindow", "Output power", None))
        self.label_3.setText(_translate("MainWindow", "SetTemp (K)", None))
        self.label_6.setText(_translate("MainWindow", "ReadTemp (K)", None))
        self.label_7.setText(_translate("MainWindow", "SetRamp(K/min.)", None))
        self.tabMotionCtrlWidget.setTabText(self.tabMotionCtrlWidget.indexOf(self.tabTemperature), _translate("MainWindow", "TEMPERATURE CONTROL", None))
        self.tabMotionCtrlWidget.setTabText(self.tabMotionCtrlWidget.indexOf(self.tab), _translate("MainWindow", "MOTION CONTROL", None))

from pyqtgraph import PlotWidget
