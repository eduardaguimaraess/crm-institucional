# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateCursoDialog.ui'
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
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class Ui_AtualizarCursoDialog(object):
    def setupUi(self, AtualizarCursoDialog):
        if not AtualizarCursoDialog.objectName():
            AtualizarCursoDialog.setObjectName(u"AtualizarCursoDialog")
        AtualizarCursoDialog.resize(550, 494)
        AtualizarCursoDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(AtualizarCursoDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(AtualizarCursoDialog)
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
        self.layoutWidget = QWidget(AtualizarCursoDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 430, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.update_add_curso_btn = QPushButton(self.layoutWidget)
        self.update_add_curso_btn.setObjectName(u"update_add_curso_btn")
        self.update_add_curso_btn.setMinimumSize(QSize(0, 41))
        font1 = QFont()
        font1.setBold(True)
        self.update_add_curso_btn.setFont(font1)
        self.update_add_curso_btn.setStyleSheet(u"QPushButton#add_curso_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#add_curso_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.update_add_curso_btn)

        self.update_cancel_curso_btn = QPushButton(self.layoutWidget)
        self.update_cancel_curso_btn.setObjectName(u"update_cancel_curso_btn")
        self.update_cancel_curso_btn.setMinimumSize(QSize(0, 41))
        self.update_cancel_curso_btn.setFont(font1)
        self.update_cancel_curso_btn.setStyleSheet(u"QPushButton#cancel_curso_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#cancel_curso_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.update_cancel_curso_btn)

        self.layoutWidget1 = QWidget(AtualizarCursoDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 103, 531, 311))
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

        self.update_nome_curso_lineEdit = QLineEdit(self.layoutWidget1)
        self.update_nome_curso_lineEdit.setObjectName(u"update_nome_curso_lineEdit")

        self.gridLayout_2.addWidget(self.update_nome_curso_lineEdit, 1, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_7.setFont(font3)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.update_descricao_textEdit = QTextEdit(self.layoutWidget1)
        self.update_descricao_textEdit.setObjectName(u"update_descricao_textEdit")

        self.gridLayout_2.addWidget(self.update_descricao_textEdit, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.update_CargaHoraria_spinBox = QSpinBox(self.layoutWidget1)
        self.update_CargaHoraria_spinBox.setObjectName(u"update_CargaHoraria_spinBox")
        self.update_CargaHoraria_spinBox.setStyleSheet(u"QSpinBox{\n"
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

        self.gridLayout.addWidget(self.update_CargaHoraria_spinBox, 1, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.update_status_comboBox = QComboBox(self.layoutWidget1)
        self.update_status_comboBox.addItem("")
        self.update_status_comboBox.addItem("")
        self.update_status_comboBox.setObjectName(u"update_status_comboBox")

        self.gridLayout.addWidget(self.update_status_comboBox, 1, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.layoutWidget.raise_()
        self.widget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()

        self.retranslateUi(AtualizarCursoDialog)

        QMetaObject.connectSlotsByName(AtualizarCursoDialog)
    # setupUi

    def retranslateUi(self, AtualizarCursoDialog):
        AtualizarCursoDialog.setWindowTitle(QCoreApplication.translate("AtualizarCursoDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Atualizar Curso", None))
        self.update_add_curso_btn.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Adicionar Curso", None))
        self.update_cancel_curso_btn.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Nome:", None))
        self.update_nome_curso_lineEdit.setText("")
        self.update_nome_curso_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarCursoDialog", u"Insira o nome do curso", None))
        self.label_7.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Descri\u00e7\u00e3o/Ementa:", None))
        self.label_6.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Carga Hor\u00e1ria:", None))
        self.update_status_comboBox.setItemText(0, QCoreApplication.translate("AtualizarCursoDialog", u"Ativo", None))
        self.update_status_comboBox.setItemText(1, QCoreApplication.translate("AtualizarCursoDialog", u"Inativo", None))

        self.label_5.setText(QCoreApplication.translate("AtualizarCursoDialog", u"Status:", None))
    # retranslateUi

