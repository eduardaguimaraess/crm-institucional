# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateMatriculaDialog.ui'
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

class Ui_AtualizarMatriculaDialog(object):
    def setupUi(self, AtualizarMatriculaDialog):
        if not AtualizarMatriculaDialog.objectName():
            AtualizarMatriculaDialog.setObjectName(u"AtualizarMatriculaDialog")
        AtualizarMatriculaDialog.resize(550, 325)
        AtualizarMatriculaDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(AtualizarMatriculaDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(AtualizarMatriculaDialog)
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
        self.layoutWidget = QWidget(AtualizarMatriculaDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 260, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.atualizar_Matricular_btn = QPushButton(self.layoutWidget)
        self.atualizar_Matricular_btn.setObjectName(u"atualizar_Matricular_btn")
        self.atualizar_Matricular_btn.setMinimumSize(QSize(0, 41))
        font1 = QFont()
        font1.setBold(True)
        self.atualizar_Matricular_btn.setFont(font1)
        self.atualizar_Matricular_btn.setStyleSheet(u"QPushButton#atualizar_Matricular_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#atualizar_Matricular_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.atualizar_Matricular_btn)

        self.atualizar_cancel_matricula_btn = QPushButton(self.layoutWidget)
        self.atualizar_cancel_matricula_btn.setObjectName(u"atualizar_cancel_matricula_btn")
        self.atualizar_cancel_matricula_btn.setMinimumSize(QSize(0, 41))
        self.atualizar_cancel_matricula_btn.setFont(font1)
        self.atualizar_cancel_matricula_btn.setStyleSheet(u"QPushButton#atualizar_cancel_matricula_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#atualizar_cancel_matricula_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.atualizar_cancel_matricula_btn)

        self.layoutWidget1 = QWidget(AtualizarMatriculaDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 100, 531, 66))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.atualizar_aluno_matricula_comboBox = QComboBox(self.layoutWidget1)
        self.atualizar_aluno_matricula_comboBox.setObjectName(u"atualizar_aluno_matricula_comboBox")
        self.atualizar_aluno_matricula_comboBox.setStyleSheet(u"\n"
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

        self.verticalLayout.addWidget(self.atualizar_aluno_matricula_comboBox)

        self.layoutWidget2 = QWidget(AtualizarMatriculaDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 180, 531, 66))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.atualizar_turma_matricula_comboBox_2 = QComboBox(self.layoutWidget2)
        self.atualizar_turma_matricula_comboBox_2.setObjectName(u"atualizar_turma_matricula_comboBox_2")
        self.atualizar_turma_matricula_comboBox_2.setStyleSheet(u"\n"
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

        self.gridLayout.addWidget(self.atualizar_turma_matricula_comboBox_2, 1, 0, 1, 1)

        self.atualizar_data_matricula_dateEdit = QDateEdit(self.layoutWidget2)
        self.atualizar_data_matricula_dateEdit.setObjectName(u"atualizar_data_matricula_dateEdit")

        self.gridLayout.addWidget(self.atualizar_data_matricula_dateEdit, 1, 1, 1, 1)

        self.atualizar_status_matricula_comboBox_3 = QComboBox(self.layoutWidget2)
        self.atualizar_status_matricula_comboBox_3.addItem("")
        self.atualizar_status_matricula_comboBox_3.addItem("")
        self.atualizar_status_matricula_comboBox_3.addItem("")
        self.atualizar_status_matricula_comboBox_3.setObjectName(u"atualizar_status_matricula_comboBox_3")
        self.atualizar_status_matricula_comboBox_3.setStyleSheet(u"\n"
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

        self.gridLayout.addWidget(self.atualizar_status_matricula_comboBox_3, 1, 2, 1, 1)

        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.widget.raise_()
        self.layoutWidget1.raise_()
        self.line.raise_()

        self.retranslateUi(AtualizarMatriculaDialog)

        QMetaObject.connectSlotsByName(AtualizarMatriculaDialog)
    # setupUi

    def retranslateUi(self, AtualizarMatriculaDialog):
        AtualizarMatriculaDialog.setWindowTitle(QCoreApplication.translate("AtualizarMatriculaDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Atualizar Matr\u00edcula", None))
        self.atualizar_Matricular_btn.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Matricular", None))
        self.atualizar_cancel_matricula_btn.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Aluno:", None))
        self.label_4.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Turma:", None))
        self.label_5.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Data da Matr\u00edcula:", None))
        self.label_6.setText(QCoreApplication.translate("AtualizarMatriculaDialog", u"Status:", None))
        self.atualizar_status_matricula_comboBox_3.setItemText(0, QCoreApplication.translate("AtualizarMatriculaDialog", u"Ativa", None))
        self.atualizar_status_matricula_comboBox_3.setItemText(1, QCoreApplication.translate("AtualizarMatriculaDialog", u"Desativada", None))
        self.atualizar_status_matricula_comboBox_3.setItemText(2, QCoreApplication.translate("AtualizarMatriculaDialog", u"Conclu\u00edda", None))

    # retranslateUi

