# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dzenis Madzovic\OneDrive - Högskolan Kristianstad\Skrivbordet\Projects\GoldApp\src\examples\meetings_events_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 881)
        Form.setStyleSheet("background-color: rgb(220, 221, 255);")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(1800, 900))
        self.widget_3.setStyleSheet("padding-left: 5cm;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.app_logo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.app_logo.setFont(font)
        self.app_logo.setStyleSheet("QLabel{\n"
"color: rgb(255, 203, 99);\n"
"background-color: white;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"margin-left: 0px;\n"
"margin-right: 0px;\n"
"}")
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.horizontalLayout_5.addWidget(self.app_logo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setEnabled(True)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 9, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.events_location = QtWidgets.QLabel(self.widget_2)
        self.events_location.setMinimumSize(QtCore.QSize(404, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.events_location.setFont(font)
        self.events_location.setStyleSheet("")
        self.events_location.setScaledContents(False)
        self.events_location.setAlignment(QtCore.Qt.AlignCenter)
        self.events_location.setObjectName("events_location")
        self.horizontalLayout.addWidget(self.events_location)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 466, 710))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setStyleSheet("margin-bottom: 8px;\n"
"max-height: 500px;\n"
"background:white;\n"
"border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.photo = QtWidgets.QLabel(self.widget)
        self.photo.setMinimumSize(QtCore.QSize(109, 108))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setStyleSheet("display: inline-block;\n"
"min-width: 100px;\n"
"min-height: 100px;\n"
"max-width: 300px;\n"
"max-height: 300px;\n"
"margin-left:9px;\n"
"border-radius: 3px;\n"
"")
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("c:\\Users\\Dzenis Madzovic\\OneDrive - Högskolan Kristianstad\\Skrivbordet\\Projects\\GoldApp\\src\\examples\\../image/chess.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.horizontalLayout_2.addWidget(self.photo)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.event = QtWidgets.QLabel(self.widget)
        self.event.setStyleSheet("font-size: 18px;")
        self.event.setObjectName("event")
        self.verticalLayout_4.addWidget(self.event)
        self.date = QtWidgets.QLabel(self.widget)
        self.date.setStyleSheet("font-size: 13px;")
        self.date.setObjectName("date")
        self.verticalLayout_4.addWidget(self.date)
        self.location = QtWidgets.QLabel(self.widget)
        self.location.setStyleSheet("font-size: 13px;")
        self.location.setObjectName("location")
        self.verticalLayout_4.addWidget(self.location)
        self.interest = QtWidgets.QLabel(self.widget)
        self.interest.setStyleSheet("font-size: 13px;")
        self.interest.setObjectName("interest")
        self.verticalLayout_4.addWidget(self.interest)
        self.description = QtWidgets.QLabel(self.widget)
        self.description.setStyleSheet("font-size: 13px;\n"
"min-height: 100px;\n"
"max-width: 300px;")
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setObjectName("description")
        self.verticalLayout_4.addWidget(self.description)
        self.read_more = QtWidgets.QPushButton(self.widget)
        self.read_more.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: white;\n"
"padding: 10px 23px;\n"
"margin: 10px 60px 10px 60px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 13px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(255, 220, 99);\n"
"}\n"
"")
        self.read_more.setObjectName("read_more")
        self.verticalLayout_4.addWidget(self.read_more)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.widget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget1.setStyleSheet("margin-bottom: 8px;\n"
"max-height: 500px;\n"
"background:white;\n"
"border-radius: 5px;")
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.photo_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.photo_2.setFont(font)
        self.photo_2.setStyleSheet("display: inline-block;\n"
"min-width: 100px;\n"
"min-height: 100px;\n"
"max-width: 300px;\n"
"max-height: 300px;\n"
"margin-left:9px;\n"
"border-radius: 3px;\n"
"")
        self.photo_2.setText("")
        self.photo_2.setPixmap(QtGui.QPixmap("c:\\Users\\Dzenis Madzovic\\OneDrive - Högskolan Kristianstad\\Skrivbordet\\Projects\\GoldApp\\src\\examples\\../image/chess.jpg"))
        self.photo_2.setScaledContents(True)
        self.photo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_2.setObjectName("photo_2")
        self.horizontalLayout_3.addWidget(self.photo_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.event_2 = QtWidgets.QLabel(self.widget1)
        self.event_2.setStyleSheet("font-size: 18px;")
        self.event_2.setObjectName("event_2")
        self.verticalLayout_5.addWidget(self.event_2)
        self.date_2 = QtWidgets.QLabel(self.widget1)
        self.date_2.setStyleSheet("font-size: 13px;")
        self.date_2.setObjectName("date_2")
        self.verticalLayout_5.addWidget(self.date_2)
        self.location_2 = QtWidgets.QLabel(self.widget1)
        self.location_2.setStyleSheet("font-size: 13px;")
        self.location_2.setObjectName("location_2")
        self.verticalLayout_5.addWidget(self.location_2)
        self.interest_2 = QtWidgets.QLabel(self.widget1)
        self.interest_2.setStyleSheet("font-size: 13px;")
        self.interest_2.setObjectName("interest_2")
        self.verticalLayout_5.addWidget(self.interest_2)
        self.description_2 = QtWidgets.QLabel(self.widget1)
        self.description_2.setStyleSheet("font-size: 13px;\n"
"min-height: 100px;\n"
"max-width: 300px;")
        self.description_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_2.setObjectName("description_2")
        self.verticalLayout_5.addWidget(self.description_2)
        self.read_more_2 = QtWidgets.QPushButton(self.widget1)
        self.read_more_2.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: white;\n"
"padding: 10px 23px;\n"
"margin: 10px 60px 10px 60px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 13px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(255, 220, 99);\n"
"}\n"
"")
        self.read_more_2.setObjectName("read_more_2")
        self.verticalLayout_5.addWidget(self.read_more_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.widget1, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setStyleSheet("padding-right: 5cm;")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4.addWidget(self.widget_4, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.app_logo.setText(_translate("Form", "GoldApp"))
        self.events_location.setText(_translate("Form", "<html><head/><body><p align=\"center\">Local Events and Meetups<span id=\"events_location\" class=\"events_location\">:</span></p></body></html> "))
        self.event.setText(_translate("Form", "Event<span class=\"event\">:</span>"))
        self.date.setText(_translate("Form", "Date & Time<span class=\"date\">:</span>"))
        self.location.setText(_translate("Form", "Location<span class=\"address\">:</span>"))
        self.interest.setText(_translate("Form", "Interest<span class=\"interest\">:</span>"))
        self.description.setText(_translate("Form", "Description<span class=\"desc\">:</span>"))
        self.read_more.setText(_translate("Form", "Read More"))
        self.event_2.setText(_translate("Form", "Event<span class=\"event\">:</span>"))
        self.date_2.setText(_translate("Form", "Date & Time<span class=\"date\">:</span>"))
        self.location_2.setText(_translate("Form", "Location<span class=\"address\">:</span>"))
        self.interest_2.setText(_translate("Form", "Interest<span class=\"interest\">:</span>"))
        self.description_2.setText(_translate("Form", "Description<span class=\"desc\">:</span>"))
        self.read_more_2.setText(_translate("Form", "Read More"))
