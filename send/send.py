# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qq_send(object):
    def setupUi(self, qq_send):
        qq_send.setObjectName("qq_send")
        qq_send.resize(540, 575)
        self.verticalLayout = QtWidgets.QVBoxLayout(qq_send)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(qq_send)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(75, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(75, 0))
        self.label_4.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_3.setStyleSheet("border-radius:5px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox.setMinimumSize(QtCore.QSize(200, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox.setStyleSheet("border-radius:5px")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(75, 0))
        self.label_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_6)
        self.spinBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.spinBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox_2.setStyleSheet("border-radius:5px")
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_5.addWidget(self.spinBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(75, 0))
        self.label_8.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.radioButton = QtWidgets.QRadioButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_8.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_2.setMaximumSize(QtCore.QSize(116, 16777215))
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_8.addWidget(self.radioButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(7, 0, 7, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setStyleSheet("border-radius:5px")
        self.textEdit.setReadOnly(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.excel_send = QtWidgets.QPushButton(self.widget_9)
        self.excel_send.setMinimumSize(QtCore.QSize(0, 35))
        self.excel_send.setMaximumSize(QtCore.QSize(120, 35))
        self.excel_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excel_send.setObjectName("excel_send")
        self.horizontalLayout_3.addWidget(self.excel_send)
        self.excel_send_model = QtWidgets.QPushButton(self.widget_9)
        self.excel_send_model.setMinimumSize(QtCore.QSize(0, 35))
        self.excel_send_model.setMaximumSize(QtCore.QSize(120, 35))
        self.excel_send_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excel_send_model.setObjectName("excel_send_model")
        self.horizontalLayout_3.addWidget(self.excel_send_model)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 35))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.send_submit = QtWidgets.QPushButton(self.widget_5)
        self.send_submit.setMaximumSize(QtCore.QSize(120, 35))
        self.send_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_submit.setObjectName("send_submit")
        self.horizontalLayout_4.addWidget(self.send_submit)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(qq_send)
        QtCore.QMetaObject.connectSlotsByName(qq_send)

    def retranslateUi(self, qq_send):
        _translate = QtCore.QCoreApplication.translate
        qq_send.setWindowTitle(_translate("qq_send", "QBOMB "))
        self.label_6.setText(_translate("qq_send", "QBOMB "))
        self.label_4.setText(_translate("qq_send", "?????????"))
        self.label_3.setText(_translate("qq_send", "???????????????"))
        self.label_5.setText(_translate("qq_send", "????????????"))
        self.label_8.setText(_translate("qq_send", "?????????"))
        self.radioButton.setText(_translate("qq_send", "QQ"))
        self.radioButton_2.setText(_translate("qq_send", "??????"))
        self.textEdit.setPlaceholderText(_translate("qq_send", "?????????????????????"))
        self.excel_send.setText(_translate("qq_send", "Excel??????"))
        self.excel_send_model.setText(_translate("qq_send", "Excel??????"))
        self.pushButton_2.setText(_translate("qq_send", "??????"))
        self.send_submit.setText(_translate("qq_send", "??????"))
