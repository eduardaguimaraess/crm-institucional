# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisciplinaDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTimeEdit,
    QWidget)

class Ui_DisciplinaDialog(object):
    def setupUi(self, DisciplinaDialog):
        if not DisciplinaDialog.objectName():
            DisciplinaDialog.setObjectName(u"DisciplinaDialog")
        DisciplinaDialog.resize(550, 403)
        DisciplinaDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(DisciplinaDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(DisciplinaDialog)
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
        self.layoutWidget = QWidget(DisciplinaDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 330, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_disciplina_btn = QPushButton(self.layoutWidget)
        self.add_disciplina_btn.setObjectName(u"add_disciplina_btn")
        self.add_disciplina_btn.setMinimumSize(QSize(0, 41))
        font1 = QFont()
        font1.setBold(True)
        self.add_disciplina_btn.setFont(font1)
        self.add_disciplina_btn.setStyleSheet(u"QPushButton#add_disciplina_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#add_disciplina_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.add_disciplina_btn)

        self.cancel_disciplina_btn = QPushButton(self.layoutWidget)
        self.cancel_disciplina_btn.setObjectName(u"cancel_disciplina_btn")
        self.cancel_disciplina_btn.setMinimumSize(QSize(0, 41))
        self.cancel_disciplina_btn.setFont(font1)
        self.cancel_disciplina_btn.setStyleSheet(u"QPushButton#cancel_disciplina_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#cancel_disciplina_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel_disciplina_btn)

        self.layoutWidget1 = QWidget(DisciplinaDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 104, 531, 63))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.nome_disciplina_lineEdit = QLineEdit(self.layoutWidget1)
        self.nome_disciplina_lineEdit.setObjectName(u"nome_disciplina_lineEdit")

        self.gridLayout_2.addWidget(self.nome_disciplina_lineEdit, 1, 0, 1, 1)

        self.layoutWidget2 = QWidget(DisciplinaDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 170, 531, 66))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.disciplina_curso_comboBox = QComboBox(self.layoutWidget2)
        self.disciplina_curso_comboBox.setObjectName(u"disciplina_curso_comboBox")

        self.gridLayout.addWidget(self.disciplina_curso_comboBox, 1, 0, 1, 1)

        self.professor_disciplina_comboBox_2 = QComboBox(self.layoutWidget2)
        self.professor_disciplina_comboBox_2.setObjectName(u"professor_disciplina_comboBox_2")
        self.professor_disciplina_comboBox_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.professor_disciplina_comboBox_2, 1, 1, 1, 1)

        self.layoutWidget3 = QWidget(DisciplinaDialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(11, 251, 531, 66))
        self.gridLayout_3 = QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout_3.addWidget(self.label_10, 0, 3, 1, 1)

        self.CargaHoraria_disciplina_spinBox = QSpinBox(self.layoutWidget3)
        self.CargaHoraria_disciplina_spinBox.setObjectName(u"CargaHoraria_disciplina_spinBox")
        self.CargaHoraria_disciplina_spinBox.setStyleSheet(u"QSpinBox{\n"
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
"}")

        self.gridLayout_3.addWidget(self.CargaHoraria_disciplina_spinBox, 1, 0, 1, 1)

        self.dia_semana_disciplina_comboBox = QComboBox(self.layoutWidget3)
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.addItem("")
        self.dia_semana_disciplina_comboBox.setObjectName(u"dia_semana_disciplina_comboBox")

        self.gridLayout_3.addWidget(self.dia_semana_disciplina_comboBox, 1, 1, 1, 1)

        self.inicio_disciplina_timeEdit = QTimeEdit(self.layoutWidget3)
        self.inicio_disciplina_timeEdit.setObjectName(u"inicio_disciplina_timeEdit")
        self.inicio_disciplina_timeEdit.setStyleSheet(u"border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:rgba(241,241, 243);\n"
"	color: rgb(186, 186, 186);\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;")

        self.gridLayout_3.addWidget(self.inicio_disciplina_timeEdit, 1, 2, 1, 1)

        self.fim_disciplina_timeEdit_2 = QTimeEdit(self.layoutWidget3)
        self.fim_disciplina_timeEdit_2.setObjectName(u"fim_disciplina_timeEdit_2")
        self.fim_disciplina_timeEdit_2.setStyleSheet(u"border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:rgba(241,241, 243);\n"
"	color: rgb(186, 186, 186);\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: 2980B9;")

        self.gridLayout_3.addWidget(self.fim_disciplina_timeEdit_2, 1, 3, 1, 1)

        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.widget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()

        self.retranslateUi(DisciplinaDialog)

        QMetaObject.connectSlotsByName(DisciplinaDialog)
    # setupUi

    def retranslateUi(self, DisciplinaDialog):
        DisciplinaDialog.setWindowTitle(QCoreApplication.translate("DisciplinaDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DisciplinaDialog", u"Adicionar Disciplina", None))
        self.add_disciplina_btn.setText(QCoreApplication.translate("DisciplinaDialog", u"Adicionar Disciplina", None))
        self.cancel_disciplina_btn.setText(QCoreApplication.translate("DisciplinaDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("DisciplinaDialog", u"Nome da Disciplina:", None))
        self.nome_disciplina_lineEdit.setText("")
        self.nome_disciplina_lineEdit.setPlaceholderText(QCoreApplication.translate("DisciplinaDialog", u"Ex: Algoritmos e Programa\u00e7\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("DisciplinaDialog", u"Curso", None))
        self.label_8.setText(QCoreApplication.translate("DisciplinaDialog", u"Professor Respons\u00e1vel:", None))
        self.label_6.setText(QCoreApplication.translate("DisciplinaDialog", u"Carga Hor\u00e1ria:", None))
        self.label_7.setText(QCoreApplication.translate("DisciplinaDialog", u"Dia da semana:", None))
        self.label_9.setText(QCoreApplication.translate("DisciplinaDialog", u"In\u00edcio:", None))
        self.label_10.setText(QCoreApplication.translate("DisciplinaDialog", u"Fim:", None))
        self.dia_semana_disciplina_comboBox.setItemText(0, QCoreApplication.translate("DisciplinaDialog", u"Segunda", None))
        self.dia_semana_disciplina_comboBox.setItemText(1, QCoreApplication.translate("DisciplinaDialog", u"Ter\u00e7a", None))
        self.dia_semana_disciplina_comboBox.setItemText(2, QCoreApplication.translate("DisciplinaDialog", u"Quarta", None))
        self.dia_semana_disciplina_comboBox.setItemText(3, QCoreApplication.translate("DisciplinaDialog", u"Quinta", None))
        self.dia_semana_disciplina_comboBox.setItemText(4, QCoreApplication.translate("DisciplinaDialog", u"Sexta", None))
        self.dia_semana_disciplina_comboBox.setItemText(5, QCoreApplication.translate("DisciplinaDialog", u"S\u00e1bado", None))
        self.dia_semana_disciplina_comboBox.setItemText(6, QCoreApplication.translate("DisciplinaDialog", u"Domingo", None))

    # retranslateUi

