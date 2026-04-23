# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TurmaDialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_TurmaDialog(object):
    def setupUi(self, TurmaDialog):
        if not TurmaDialog.objectName():
            TurmaDialog.setObjectName(u"TurmaDialog")
        TurmaDialog.resize(550, 342)
        TurmaDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(TurmaDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(TurmaDialog)
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
        self.layoutWidget = QWidget(TurmaDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 280, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_turma_btn = QPushButton(self.layoutWidget)
        self.add_turma_btn.setObjectName(u"add_turma_btn")
        self.add_turma_btn.setMinimumSize(QSize(0, 41))
        font1 = QFont()
        font1.setBold(True)
        self.add_turma_btn.setFont(font1)
        self.add_turma_btn.setStyleSheet(u"QPushButton#add_turma_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#add_turma_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.add_turma_btn)

        self.cancel_turma_btn = QPushButton(self.layoutWidget)
        self.cancel_turma_btn.setObjectName(u"cancel_turma_btn")
        self.cancel_turma_btn.setMinimumSize(QSize(0, 41))
        self.cancel_turma_btn.setFont(font1)
        self.cancel_turma_btn.setStyleSheet(u"QPushButton#cancel_turma_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#cancel_turma_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel_turma_btn)

        self.layoutWidget1 = QWidget(TurmaDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 103, 531, 171))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.nome_turma_lineEdit = QLineEdit(self.layoutWidget1)
        self.nome_turma_lineEdit.setObjectName(u"nome_turma_lineEdit")

        self.gridLayout_2.addWidget(self.nome_turma_lineEdit, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_4.setFont(font3)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.add_professor_turma_comboBox_2 = QComboBox(self.layoutWidget1)
        self.add_professor_turma_comboBox_2.setObjectName(u"add_professor_turma_comboBox_2")
        self.add_professor_turma_comboBox_2.setStyleSheet(u"QComboBox{\n"
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
        self.add_professor_turma_comboBox_2.setEditable(False)

        self.gridLayout.addWidget(self.add_professor_turma_comboBox_2, 1, 0, 1, 1)

        self.limite_alunos_spinBox = QSpinBox(self.layoutWidget1)
        self.limite_alunos_spinBox.setObjectName(u"limite_alunos_spinBox")
        self.limite_alunos_spinBox.setStyleSheet(u"QSpinBox{\n"
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

        self.gridLayout.addWidget(self.limite_alunos_spinBox, 1, 2, 1, 1)

        self.data_inicio_fim_dateEdit = QDateEdit(self.layoutWidget1)
        self.data_inicio_fim_dateEdit.setObjectName(u"data_inicio_fim_dateEdit")

        self.gridLayout.addWidget(self.data_inicio_fim_dateEdit, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.layoutWidget.raise_()
        self.widget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()

        self.retranslateUi(TurmaDialog)

        QMetaObject.connectSlotsByName(TurmaDialog)
    # setupUi

    def retranslateUi(self, TurmaDialog):
        TurmaDialog.setWindowTitle(QCoreApplication.translate("TurmaDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("TurmaDialog", u"Adicionar Nova Turma", None))
        self.add_turma_btn.setText(QCoreApplication.translate("TurmaDialog", u"Adicionar Curso", None))
        self.cancel_turma_btn.setText(QCoreApplication.translate("TurmaDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("TurmaDialog", u"Nome/C\u00f3digo da Turma:", None))
        self.nome_turma_lineEdit.setText("")
        self.nome_turma_lineEdit.setPlaceholderText(QCoreApplication.translate("TurmaDialog", u"Insira o nome da Turma", None))
        self.label_4.setText(QCoreApplication.translate("TurmaDialog", u"Professor:", None))
        self.label_5.setText(QCoreApplication.translate("TurmaDialog", u"Data de In\u00edcio/Fim:", None))
        self.label_6.setText(QCoreApplication.translate("TurmaDialog", u"Limite de Alunos:", None))
        self.add_professor_turma_comboBox_2.setCurrentText("")
    # retranslateUi

