# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MatricularDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MatricularDialog(object):
    def setupUi(self, MatricularDialog):
        if not MatricularDialog.objectName():
            MatricularDialog.setObjectName(u"MatricularDialog")
        MatricularDialog.resize(550, 325)
        MatricularDialog.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:rgba(241,241, 243);\n"
"	color:rgb(85, 85, 85);\n"
"	border-radius:10px;\n"
"	padding-left:10px;\n"
"	padding-bottom:3px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	background-color:rgba(241,241, 243);\n"
"	color:rgb(85, 85, 85);\n"
"	border-radius:10px;\n"
"	padding-left:10px;\n"
"	padding-bottom:3px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QComboBox{\n"
"\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: rgb(55, 96, 214);\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;\n"
"}")
        self.line = QFrame(MatricularDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(MatricularDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 551, 91))
        self.widget.setStyleSheet(u"background-color: rgb(55, 96, 214);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 231, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(MatricularDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 260, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Matricular_btn = QPushButton(self.layoutWidget)
        self.Matricular_btn.setObjectName(u"Matricular_btn")
        self.Matricular_btn.setMinimumSize(QSize(0, 41))
        font1 = QFont()
        font1.setBold(True)
        self.Matricular_btn.setFont(font1)
        self.Matricular_btn.setStyleSheet(u"QPushButton#matricular_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#matricular_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Matricular_btn)

        self.cancel_matricula_btn = QPushButton(self.layoutWidget)
        self.cancel_matricula_btn.setObjectName(u"cancel_matricula_btn")
        self.cancel_matricula_btn.setMinimumSize(QSize(0, 41))
        self.cancel_matricula_btn.setFont(font1)
        self.cancel_matricula_btn.setStyleSheet(u"QPushButton#cancel_matricula_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#cancel_matricula_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel_matricula_btn)

        self.widget1 = QWidget(MatricularDialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 100, 531, 66))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.aluno_matricula_comboBox = QComboBox(self.widget1)
        self.aluno_matricula_comboBox.setObjectName(u"aluno_matricula_comboBox")
        self.aluno_matricula_comboBox.setStyleSheet(u"\n"
"\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:rgba(241,241, 243);\n"
"	color: rgb(186, 186, 186);\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;")

        self.verticalLayout.addWidget(self.aluno_matricula_comboBox)

        self.widget2 = QWidget(MatricularDialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 180, 531, 66))
        self.gridLayout = QGridLayout(self.widget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.turma_matricula_comboBox_2 = QComboBox(self.widget2)
        self.turma_matricula_comboBox_2.setObjectName(u"turma_matricula_comboBox_2")
        self.turma_matricula_comboBox_2.setStyleSheet(u"\n"
"\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:rgba(241,241, 243);\n"
"	color: rgb(186, 186, 186);\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;\n"
"")

        self.gridLayout.addWidget(self.turma_matricula_comboBox_2, 1, 0, 1, 1)

        self.data_matricula_dateEdit = QDateEdit(self.widget2)
        self.data_matricula_dateEdit.setObjectName(u"data_matricula_dateEdit")

        self.gridLayout.addWidget(self.data_matricula_dateEdit, 1, 1, 1, 1)

        self.status_matricula_comboBox_3 = QComboBox(self.widget2)
        self.status_matricula_comboBox_3.addItem("")
        self.status_matricula_comboBox_3.addItem("")
        self.status_matricula_comboBox_3.addItem("")
        self.status_matricula_comboBox_3.setObjectName(u"status_matricula_comboBox_3")
        self.status_matricula_comboBox_3.setStyleSheet(u"\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:rgba(241,241, 243);\n"
"	color: rgb(186, 186, 186);\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;\n"
"")

        self.gridLayout.addWidget(self.status_matricula_comboBox_3, 1, 2, 1, 1)

        self.layoutWidget.raise_()
        self.widget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()
        self.aluno_matricula_comboBox.raise_()
        self.turma_matricula_comboBox_2.raise_()
        self.label_4.raise_()
        self.data_matricula_dateEdit.raise_()
        self.label_5.raise_()
        self.status_matricula_comboBox_3.raise_()
        self.label_6.raise_()

        self.retranslateUi(MatricularDialog)

        QMetaObject.connectSlotsByName(MatricularDialog)
    # setupUi

    def retranslateUi(self, MatricularDialog):
        MatricularDialog.setWindowTitle(QCoreApplication.translate("MatricularDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MatricularDialog", u"Matricular Aluno", None))
        self.Matricular_btn.setText(QCoreApplication.translate("MatricularDialog", u"Matricular", None))
        self.cancel_matricula_btn.setText(QCoreApplication.translate("MatricularDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("MatricularDialog", u"Aluno:", None))
        self.label_4.setText(QCoreApplication.translate("MatricularDialog", u"Turma:", None))
        self.label_5.setText(QCoreApplication.translate("MatricularDialog", u"Data da Matr\u00edcula:", None))
        self.label_6.setText(QCoreApplication.translate("MatricularDialog", u"Status:", None))
        self.status_matricula_comboBox_3.setItemText(0, QCoreApplication.translate("MatricularDialog", u"Ativa", None))
        self.status_matricula_comboBox_3.setItemText(1, QCoreApplication.translate("MatricularDialog", u"Desativada", None))
        self.status_matricula_comboBox_3.setItemText(2, QCoreApplication.translate("MatricularDialog", u"Conclu\u00edda", None))

    # retranslateUi

