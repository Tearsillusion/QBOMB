# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_success.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qq_send_success(object):
    def setupUi(self, qq_send_success):
        qq_send_success.setObjectName("qq_send_success")
        qq_send_success.resize(540, 440)
        self.verticalLayout = QtWidgets.QVBoxLayout(qq_send_success)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(qq_send_success)
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
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 35))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(qq_send_success)
        QtCore.QMetaObject.connectSlotsByName(qq_send_success)

    def retranslateUi(self, qq_send_success):
        _translate = QtCore.QCoreApplication.translate
        qq_send_success.setWindowTitle(_translate("qq_send_success", "QBOMB "))
        self.label_6.setText(_translate("qq_send_success", "????????????"))
        self.label.setText(_translate("qq_send_success", "??????????????????"))
        self.label_2.setText(_translate("qq_send_success", "???????????????"))
        self.label_3.setText(_translate("qq_send_success", "???????????????"))
        self.pushButton_2.setText(_translate("qq_send_success", "??????"))
