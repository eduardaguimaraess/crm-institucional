# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login-form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 777)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(960, 0, 483, 900))
        font = QFont()
        font.setPointSize(16)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color:rgba(255,255, 255);\n"
"border-radius:20px;")
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
        self.b1.setGeometry(QRect(40, 560, 420, 45))
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
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(420, 320, 45, 45))
        self.widget_3.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 24, 24))
        self.label_7.setPixmap(QPixmap(u":/mail_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"))
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(420, 420, 45, 45))
        self.widget_4.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 24, 24))
        self.label_6.setPixmap(QPixmap(u":/lock_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"))
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
        self.label_3.setGeometry(QRect(190, 220, 141, 16))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(85, 85, 85);")
        self.b2 = QPushButton(self.widget)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(40, 690, 420, 45))
        self.b2.setFont(font2)
        self.b2.setStyleSheet(u"QPushButton#b2{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QPushButton#b2:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 640, 21, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(194, 194, 194);")
        self.line_1 = QFrame(self.widget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(30, 650, 190, 1))
        self.line_1.setStyleSheet(u"background-color: rgba(194, 194, 194,);\n"
"")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(280, 650, 180, 1))
        self.line_3.setStyleSheet(u"background-color: rgba(194, 194, 194,);\n"
"")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 140, 251, 71))
        self.label_8.setPixmap(QPixmap(u":/logo.png"))
        self.b3 = QPushButton(self.widget)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(330, 480, 131, 32))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setUnderline(True)
        self.b3.setFont(font4)
        self.b3.setStyleSheet(u"QPushButton#b3{\n"
"color: rgb(55, 96, 214);\n"
"}\n"
"QPushButton#b3:pressed{\n"
"color:rgb(85, 85, 85);\n"
"}")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 943, 900))
        self.widget_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:20px;")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 90, 651, 681))
        self.label_9.setPixmap(QPixmap(u":/Imagens/Slice 1.png"))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Digite somente n\u00fameros", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Digite sua senha", None))
        self.b1.setText(QCoreApplication.translate("Form", u"Fa\u00e7a login", None))
        self.label_7.setText("")
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"CPF:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Senha:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Acesse sua Conta", None))
        self.b2.setText(QCoreApplication.translate("Form", u"Criar Conta", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"OU", None))
        self.label_8.setText("")
        self.b3.setText(QCoreApplication.translate("Form", u"Esqueceu a senha?", None))
        self.label_9.setText("")
    # retranslateUi

