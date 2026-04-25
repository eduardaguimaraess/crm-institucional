# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'criarconta.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
from views import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 777)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -10, 943, 900))
        font = QFont()
        font.setPointSize(16)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color:rgba(255,255, 255);\n"
"")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 320, 420, 45))
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 420, 420, 45))
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.b1 = QPushButton(self.widget)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(40, 590, 231, 45))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.b1.setFont(font2)
        self.b1.setStyleSheet(u"QPushButton#b1{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#b1:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 290, 60, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 390, 60, 16))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setUnderline(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 180, 121, 16))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 90, 251, 71))
        self.label_8.setPixmap(QPixmap(u":/logo.png"))
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(500, 320, 420, 45))
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(500, 420, 420, 45))
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(40, 520, 420, 45))
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 290, 60, 16))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 490, 141, 16))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 390, 81, 16))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(500, 520, 231, 45))
        self.comboBox.setStyleSheet(u"background-color:rgba(241,241, 243);\n"
"color:rgb(85, 85, 85);\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-bottom:3px;")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(500, 490, 81, 16))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(940, 0, 501, 900))
        self.widget_2.setStyleSheet(u"background-color: rgb(55, 96, 214);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insira seu nome completo", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"xxxxxxxxxx", None))
        self.b1.setText(QCoreApplication.translate("Form", u"Fa\u00e7a login", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Senha:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Crie sua conta", None))
        self.label_8.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Digite somente n\u00fameros", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"+ 00 (XX) XXXXX XXXXX", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"xxxxxxxxxx", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CPF:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Confirme a senha:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Telefone:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Professor", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Captador Comercial", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Administrador", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Financeiro", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio:", None))
    # retranslateUi

