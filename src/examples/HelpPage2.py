# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpPagePart2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setStyleSheet("background-color: rgb(220, 221, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1173, 725))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setStyleSheet(
            "QPushButton{\n"
            "color: white;\n"
            "background-color: rgb(255, 203, 99);\n"
            "border-width: 0px;\n"
            "border-radius:75px;\n"
            "min-height: 150px;\n"
            "min-width: 150px;\n"
            "max-height: 150px;\n"
            "max-width: 150px;\n"
            "margin-top: 50px;"
            "}"
            "QPushButton:Hover{\n"
            "background-color: rgb(255, 220, 99);\n"
            "}"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(
            self.pushButton_2, 4, 1, 1, 1, QtCore.Qt.AlignHCenter
        )
        spacerItem = QtWidgets.QSpacerItem(
            135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 313, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(520, 0))
        self.widget1.setStyleSheet(
            "background-color: white;\n" "border-radius: 5px;\n" "padding-left: 50px;\n"
        )
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "font-size: 30px;\n"
            "color: white;\n"
            "padding: 5px;\n"
            "background-color: orange;\n"
            "text-align: center;"
        )
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit, 0, QtCore.Qt.AlignVCenter)
        self.widget_3 = QtWidgets.QWidget(self.widget1)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget2 = QtWidgets.QWidget(self.widget1)
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_2.setStyleSheet("font-size: 20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_4.setStyleSheet("font-size: 20px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_3.setStyleSheet("font-size: 20px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_5.setStyleSheet("font-size: 20px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.widget_4 = QtWidgets.QWidget(self.widget2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.widget3 = QtWidgets.QWidget(self.widget1)
        self.widget3.setObjectName("widget3")
        self.gridLayout.addWidget(self.widget3, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget1)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget1)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setStyleSheet("margin-left: 15px")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.widget_6)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "color: white;\n"
            "background-color: rgb(255, 203, 99);\n"
            "border-width: 0px;\n"
            "border-radius:75px;\n"
            "min-height: 150px;\n"
            "min-width: 150px;\n"
            "max-height: 150px;\n"
            "max-width: 150px;\n"
            "}"
            "QPushButton:Hover{\n"
            "background-color: rgb(255, 220, 99);\n"
            "}"
        )
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 2, 1)
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setStyleSheet(
            " background-color: white;\n" "border-radius: 10px;\n "
        )
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labels_layout = QtWidgets.QWidget(self.widget_7)
        self.labels_layout.setStyleSheet(
            "margin-left: 7px;\n" "font-size: 30px;\n" "border-color: black;"
        )
        self.labels_layout.setObjectName("labels_layout")
        self.labels = QtWidgets.QVBoxLayout(self.labels_layout)
        self.labels.setObjectName("labels")
        self.email_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("margin-right: 130px;")
        self.email_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.email_label.setObjectName("email_label")
        self.labels.addWidget(self.email_label)
        self.first_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        self.first_label.setFont(font)
        self.first_label.setStyleSheet("margin-right: 74px;")
        self.first_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.first_label.setObjectName("first_label")
        self.labels.addWidget(self.first_label)
        self.last_label = QtWidgets.QLabel(self.labels_layout)
        self.last_label.setFont(font)
        self.last_label.setStyleSheet("margin-right: 76px;")
        self.last_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.last_label.setObjectName("last_label")
        self.labels.addWidget(self.last_label)
        self.phone_label = QtWidgets.QLabel(self.labels_layout)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("margin-right: 26px;")
        self.phone_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.phone_label.setObjectName("phone_label")
        self.labels.addWidget(self.phone_label)
        self.problem_type_label = QtWidgets.QLabel(self.labels_layout)
        self.problem_type_label.setFont(font)
        self.problem_type_label.setStyleSheet("margin-right: 120px;")
        self.problem_type_label.setObjectName("passwor_label")
        self.labels.addWidget(self.problem_type_label)
        self.location_label = QtWidgets.QLabel(self.labels_layout)
        self.location_label.setFont(font)
        self.location_label.setStyleSheet("margin-bottom: 0px;")
        self.location_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.location_label.setObjectName("rep_pass_label")
        self.labels.addWidget(self.location_label)
        self.location_label = QtWidgets.QLabel(self.labels_layout)
        self.location_label.setFont(font)
        self.location_label.setStyleSheet("margin-right: 90px;")
        self.location_label.setObjectName("passwor_label_2")
        self.labels.addWidget(self.location_label)
        self.gridLayout_4.addWidget(self.labels_layout, 0, 0, 1, 1)
        self.inputs_layout = QtWidgets.QWidget(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inputs_layout.sizePolicy().hasHeightForWidth()
        )
        self.inputs_layout.setSizePolicy(sizePolicy)
        self.inputs_layout.setStyleSheet("margin-top: 4px;\n" "margin-right: 7px;")
        self.inputs_layout.setObjectName("inputs_layout")
        self.inputs = QtWidgets.QVBoxLayout(self.inputs_layout)
        self.inputs.setObjectName("inputs")
        self.email_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.email_input.setFont(font)
        self.email_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.inputs.addWidget(self.email_input)
        self.first_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.first_input.setFont(font)
        self.first_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.first_input.setObjectName("first_input")
        self.inputs.addWidget(self.first_input)
        self.last_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.last_input.setFont(font)
        self.last_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.last_input.setObjectName("last_input")
        self.inputs.addWidget(self.last_input)
        self.phone_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.phone_input.setFont(font)
        self.phone_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.phone_input.setText("")
        self.phone_input.setObjectName("phone_input")
        self.inputs.addWidget(self.phone_input)
        self.pass_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.pass_input.setFont(font)
        self.pass_input.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.pass_input.setObjectName("pass_input")
        self.inputs.addWidget(self.pass_input)
        self.textEdit = QtWidgets.QTextEdit(self.inputs_layout)
        self.textEdit.setObjectName("textEdit")
        self.inputs.addWidget(self.textEdit)
        self.comboBox = QtWidgets.QComboBox(self.inputs_layout)
        self.comboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))

        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "padding-left: 0px;"
        )
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.inputs.addWidget(self.comboBox)
        self.gridLayout_4.addWidget(self.inputs_layout, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_7, 3, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
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
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.lineEdit.setText(
            _translate("MainWindow", "Want to talk with proffesionals?")
        )
        self.lineEdit_2.setText(
            _translate("MainWindow", "The button to the right will")
        )
        self.lineEdit_4.setText(
            _translate("MainWindow", "bring up call centers local to your area.")
        )
        self.lineEdit_3.setText(
            _translate("MainWindow", "If you want more personilized help")
        )
        self.lineEdit_5.setText(
            _translate("MainWindow", "please fill up the form below.")
        )
        self.pushButton.setText(_translate("MainWindow", "Press Here"))
        self.email_label.setText(_translate("MainWindow", "Email:"))
        self.first_label.setText(_translate("MainWindow", "First name:"))
        self.last_label.setText(_translate("MainWindow", "Last name:"))
        self.phone_label.setText(_translate("MainWindow", "Phone number:"))
        self.problem_type_label.setText(_translate("MainWindow", "Problem type:"))
        self.location_label.setText(_translate("MainWindow", "Problem description:"))
        self.location_label.setText(_translate("MainWindow", "Location:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Skåne"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Stockholm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
