# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateAlunos.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AtualizarAlunosDialog(object):
    def setupUi(self, AtualizarAlunosDialog):
        if not AtualizarAlunosDialog.objectName():
            AtualizarAlunosDialog.setObjectName(u"AtualizarAlunosDialog")
        AtualizarAlunosDialog.resize(551, 776)
        AtualizarAlunosDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(AtualizarAlunosDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(AtualizarAlunosDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 551, 91))
        self.widget.setStyleSheet(u"background-color: rgb(55, 96, 214);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 331, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(AtualizarAlunosDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 450, 531, 251))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_32 = QLabel(self.layoutWidget)
        self.label_32.setObjectName(u"label_32")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_32.setFont(font1)

        self.verticalLayout_31.addWidget(self.label_32)

        self.atualizar_nome_responsavel_lineEdit = QLineEdit(self.layoutWidget)
        self.atualizar_nome_responsavel_lineEdit.setObjectName(u"atualizar_nome_responsavel_lineEdit")

        self.verticalLayout_31.addWidget(self.atualizar_nome_responsavel_lineEdit)


        self.gridLayout_5.addLayout(self.verticalLayout_31, 0, 0, 1, 2)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_34 = QLabel(self.layoutWidget)
        self.label_34.setObjectName(u"label_34")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_34.setFont(font2)

        self.verticalLayout_33.addWidget(self.label_34)

        self.atualizar_telefone_responsavel_lineEdit = QLineEdit(self.layoutWidget)
        self.atualizar_telefone_responsavel_lineEdit.setObjectName(u"atualizar_telefone_responsavel_lineEdit")

        self.verticalLayout_33.addWidget(self.atualizar_telefone_responsavel_lineEdit)


        self.gridLayout_5.addLayout(self.verticalLayout_33, 1, 1, 1, 1)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_35 = QLabel(self.layoutWidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.verticalLayout_34.addWidget(self.label_35)

        self.atualizar_cpf_responsavel_lineEdit = QLineEdit(self.layoutWidget)
        self.atualizar_cpf_responsavel_lineEdit.setObjectName(u"atualizar_cpf_responsavel_lineEdit")

        self.verticalLayout_34.addWidget(self.atualizar_cpf_responsavel_lineEdit)


        self.gridLayout_5.addLayout(self.verticalLayout_34, 2, 0, 1, 1)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_48 = QLabel(self.layoutWidget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_48)

        self.endereco_responsavel_lineEdit = QLineEdit(self.layoutWidget)
        self.endereco_responsavel_lineEdit.setObjectName(u"endereco_responsavel_lineEdit")

        self.verticalLayout_46.addWidget(self.endereco_responsavel_lineEdit)


        self.gridLayout_5.addLayout(self.verticalLayout_46, 3, 0, 1, 2)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_33 = QLabel(self.layoutWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.verticalLayout_32.addWidget(self.label_33)

        self.genero_responsavel_comboBox = QComboBox(self.layoutWidget)
        self.genero_responsavel_comboBox.addItem("")
        self.genero_responsavel_comboBox.addItem("")
        self.genero_responsavel_comboBox.setObjectName(u"genero_responsavel_comboBox")

        self.verticalLayout_32.addWidget(self.genero_responsavel_comboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_32, 1, 0, 1, 1)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_36 = QLabel(self.layoutWidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.verticalLayout_35.addWidget(self.label_36)

        self.atualizar_email_responsavel_lineEdit = QLineEdit(self.layoutWidget)
        self.atualizar_email_responsavel_lineEdit.setObjectName(u"atualizar_email_responsavel_lineEdit")

        self.verticalLayout_35.addWidget(self.atualizar_email_responsavel_lineEdit)


        self.gridLayout_5.addLayout(self.verticalLayout_35, 2, 1, 1, 1)

        self.widget_2 = QWidget(AtualizarAlunosDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 410, 551, 31))
        self.widget_2.setStyleSheet(u"background-color: rgb(55, 96, 214);")
        self.layoutWidget1 = QWidget(AtualizarAlunosDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 100, 531, 301))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.atualizar_nome_aluno_lineEdit = QLineEdit(self.layoutWidget1)
        self.atualizar_nome_aluno_lineEdit.setObjectName(u"atualizar_nome_aluno_lineEdit")

        self.verticalLayout_2.addWidget(self.atualizar_nome_aluno_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.atualizar_genero_aluno_comboBox = QComboBox(self.layoutWidget1)
        self.atualizar_genero_aluno_comboBox.addItem("")
        self.atualizar_genero_aluno_comboBox.addItem("")
        self.atualizar_genero_aluno_comboBox.setObjectName(u"atualizar_genero_aluno_comboBox")

        self.verticalLayout_6.addWidget(self.atualizar_genero_aluno_comboBox)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.atualizar_telefone_aluno_lineEdit = QLineEdit(self.layoutWidget1)
        self.atualizar_telefone_aluno_lineEdit.setObjectName(u"atualizar_telefone_aluno_lineEdit")

        self.verticalLayout.addWidget(self.atualizar_telefone_aluno_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.atualizar_dob_dateEdit = QDateEdit(self.layoutWidget1)
        self.atualizar_dob_dateEdit.setObjectName(u"atualizar_dob_dateEdit")

        self.verticalLayout_8.addWidget(self.atualizar_dob_dateEdit)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.atualizar_endereco_aluno_lineEdit = QLineEdit(self.layoutWidget1)
        self.atualizar_endereco_aluno_lineEdit.setObjectName(u"atualizar_endereco_aluno_lineEdit")

        self.verticalLayout_5.addWidget(self.atualizar_endereco_aluno_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.atualizar_cpf_aluno_lineEdit = QLineEdit(self.layoutWidget1)
        self.atualizar_cpf_aluno_lineEdit.setObjectName(u"atualizar_cpf_aluno_lineEdit")

        self.verticalLayout_3.addWidget(self.atualizar_cpf_aluno_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.atualizar_email_aluno_lineEdit = QLineEdit(self.layoutWidget1)
        self.atualizar_email_aluno_lineEdit.setObjectName(u"atualizar_email_aluno_lineEdit")

        self.verticalLayout_4.addWidget(self.atualizar_email_aluno_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 2)

        self.layoutWidget2 = QWidget(AtualizarAlunosDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 710, 531, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.atualizar_aluno_btn = QPushButton(self.layoutWidget2)
        self.atualizar_aluno_btn.setObjectName(u"atualizar_aluno_btn")
        self.atualizar_aluno_btn.setMinimumSize(QSize(0, 41))
        font3 = QFont()
        font3.setBold(True)
        self.atualizar_aluno_btn.setFont(font3)
        self.atualizar_aluno_btn.setStyleSheet(u"QPushButton#atualizar_aluno_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#atualizar_aluno_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.atualizar_aluno_btn)

        self.atualizar_cancel_btn = QPushButton(self.layoutWidget2)
        self.atualizar_cancel_btn.setObjectName(u"atualizar_cancel_btn")
        self.atualizar_cancel_btn.setMinimumSize(QSize(0, 41))
        self.atualizar_cancel_btn.setFont(font3)
        self.atualizar_cancel_btn.setStyleSheet(u"QPushButton#atualizar_cancel_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#atualizar_cancel_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.atualizar_cancel_btn)

        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.widget.raise_()
        self.layoutWidget1.raise_()
        self.line.raise_()
        self.widget_2.raise_()

        self.retranslateUi(AtualizarAlunosDialog)

        QMetaObject.connectSlotsByName(AtualizarAlunosDialog)
    # setupUi

    def retranslateUi(self, AtualizarAlunosDialog):
        AtualizarAlunosDialog.setWindowTitle(QCoreApplication.translate("AtualizarAlunosDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Atualizar Informa\u00e7\u00f5es do Aluno", None))
        self.label_32.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Nome do Respons\u00e1vel:", None))
        self.atualizar_nome_responsavel_lineEdit.setText("")
        self.atualizar_nome_responsavel_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Insira o nome completo", None))
        self.label_34.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Telefone:", None))
        self.atualizar_telefone_responsavel_lineEdit.setText("")
        self.atualizar_telefone_responsavel_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"00 (XX) XXXXX XXXXX", None))
        self.label_35.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"CPF:", None))
        self.atualizar_cpf_responsavel_lineEdit.setText("")
        self.atualizar_cpf_responsavel_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Digite somente n\u00fameros", None))
        self.label_48.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Endere\u00e7o:", None))
        self.endereco_responsavel_lineEdit.setText("")
        self.endereco_responsavel_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Ex: Avenida Presidente Dutra, 1155, Cidade Nova, Itaperuna", None))
        self.label_33.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Selecione o G\u00eanero:", None))
        self.genero_responsavel_comboBox.setItemText(0, QCoreApplication.translate("AtualizarAlunosDialog", u"Masculino", None))
        self.genero_responsavel_comboBox.setItemText(1, QCoreApplication.translate("AtualizarAlunosDialog", u"Feminino", None))

        self.label_36.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"E-mail do Respons\u00e1vel:", None))
        self.atualizar_email_responsavel_lineEdit.setText("")
        self.atualizar_email_responsavel_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"E-mail ", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Nome:", None))
        self.atualizar_nome_aluno_lineEdit.setText("")
        self.atualizar_nome_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Insira o nome completo", None))
        self.label_7.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Selecione o G\u00eanero:", None))
        self.atualizar_genero_aluno_comboBox.setItemText(0, QCoreApplication.translate("AtualizarAlunosDialog", u"Masculino", None))
        self.atualizar_genero_aluno_comboBox.setItemText(1, QCoreApplication.translate("AtualizarAlunosDialog", u"Feminino", None))

        self.label_2.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Telefone:", None))
        self.atualizar_telefone_aluno_lineEdit.setText("")
        self.atualizar_telefone_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"00 (XX) XXXXX XXXXX", None))
        self.label_9.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Data de Nascimento:", None))
        self.label_6.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Endere\u00e7o:", None))
        self.atualizar_endereco_aluno_lineEdit.setText("")
        self.atualizar_endereco_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Ex: Avenida Presidente Dutra, 1155, Cidade Nova, Itaperuna", None))
        self.label_4.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"CPF:", None))
        self.atualizar_cpf_aluno_lineEdit.setText("")
        self.atualizar_cpf_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"Digite somente n\u00fameros", None))
        self.label_5.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"E-mail:", None))
        self.atualizar_email_aluno_lineEdit.setText("")
        self.atualizar_email_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("AtualizarAlunosDialog", u"E-mail ", None))
        self.atualizar_aluno_btn.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Atualizar Aluno", None))
        self.atualizar_cancel_btn.setText(QCoreApplication.translate("AtualizarAlunosDialog", u"Cancelar", None))
    # retranslateUi

