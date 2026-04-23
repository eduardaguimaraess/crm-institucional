# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from views import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1367, 850)
        MainWindow.setStyleSheet(u"background-color:rgba(244,244, 244);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(0, 850))
        self.icon_name_widget.setMaximumSize(QSize(140, 850))
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:center;\n"
"	height:30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.label_4 = QLabel(self.icon_name_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 10, 50, 50))
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/iconcoruja.png"))
        self.label_4.setScaledContents(True)
        self.layoutWidget = QWidget(self.icon_name_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 78, 122, 761))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.dashboard_2 = QPushButton(self.layoutWidget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setMinimumSize(QSize(120, 50))
        self.dashboard_2.setMaximumSize(QSize(120, 50))
        self.dashboard_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon = QIcon()
        icon.addFile(u":/dashboard_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setIconSize(QSize(24, 24))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setChecked(False)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.dashboard_2)

        self.alunos_2 = QPushButton(self.layoutWidget)
        self.alunos_2.setObjectName(u"alunos_2")
        self.alunos_2.setMinimumSize(QSize(120, 50))
        self.alunos_2.setMaximumSize(QSize(120, 50))
        self.alunos_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon1 = QIcon()
        icon1.addFile(u":/person_book_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alunos_2.setIcon(icon1)
        self.alunos_2.setIconSize(QSize(24, 24))
        self.alunos_2.setCheckable(True)
        self.alunos_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.alunos_2)

        self.cursos_2 = QPushButton(self.layoutWidget)
        self.cursos_2.setObjectName(u"cursos_2")
        self.cursos_2.setMinimumSize(QSize(120, 50))
        self.cursos_2.setMaximumSize(QSize(120, 50))
        self.cursos_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon2 = QIcon()
        icon2.addFile(u":/play_lesson_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cursos_2.setIcon(icon2)
        self.cursos_2.setIconSize(QSize(24, 24))
        self.cursos_2.setCheckable(True)
        self.cursos_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.cursos_2)

        self.professores_2 = QPushButton(self.layoutWidget)
        self.professores_2.setObjectName(u"professores_2")
        self.professores_2.setMinimumSize(QSize(120, 50))
        self.professores_2.setMaximumSize(QSize(120, 50))
        self.professores_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon3 = QIcon()
        icon3.addFile(u":/school_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.professores_2.setIcon(icon3)
        self.professores_2.setIconSize(QSize(24, 24))
        self.professores_2.setCheckable(True)
        self.professores_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.professores_2)

        self.configuracoes_2 = QPushButton(self.layoutWidget)
        self.configuracoes_2.setObjectName(u"configuracoes_2")
        self.configuracoes_2.setMinimumSize(QSize(120, 50))
        self.configuracoes_2.setMaximumSize(QSize(120, 50))
        self.configuracoes_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon4 = QIcon()
        icon4.addFile(u":/settings_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.configuracoes_2.setIcon(icon4)
        self.configuracoes_2.setIconSize(QSize(24, 24))
        self.configuracoes_2.setCheckable(True)
        self.configuracoes_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.configuracoes_2)

        self.verticalSpacer_2 = QSpacerItem(20, 375, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.sair_2 = QPushButton(self.layoutWidget)
        self.sair_2.setObjectName(u"sair_2")
        self.sair_2.setMinimumSize(QSize(120, 50))
        self.sair_2.setMaximumSize(QSize(120, 50))
        self.sair_2.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon5 = QIcon()
        icon5.addFile(u":/mode_off_on_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sair_2.setIcon(icon5)
        self.sair_2.setIconSize(QSize(24, 24))
        self.sair_2.setCheckable(True)
        self.sair_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.sair_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(80, 850))
        self.icon_only_widget.setMaximumSize(QSize(80, 850))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:center;\n"
"	height:30px;\n"
"}")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 12, 50, 50))
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/iconcoruja.png"))
        self.label.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.icon_only_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(12, 77, 66, 761))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 15, 0, 0)
        self.dashboard_1 = QPushButton(self.layoutWidget1)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setMinimumSize(QSize(50, 50))
        self.dashboard_1.setMaximumSize(QSize(50, 50))
        self.dashboard_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(24, 24))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.alunos_1 = QPushButton(self.layoutWidget1)
        self.alunos_1.setObjectName(u"alunos_1")
        self.alunos_1.setMinimumSize(QSize(50, 50))
        self.alunos_1.setMaximumSize(QSize(50, 50))
        self.alunos_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.alunos_1.setIcon(icon1)
        self.alunos_1.setIconSize(QSize(24, 24))
        self.alunos_1.setCheckable(True)
        self.alunos_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.alunos_1)

        self.cursos_1 = QPushButton(self.layoutWidget1)
        self.cursos_1.setObjectName(u"cursos_1")
        self.cursos_1.setMinimumSize(QSize(50, 50))
        self.cursos_1.setMaximumSize(QSize(50, 50))
        self.cursos_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.cursos_1.setIcon(icon2)
        self.cursos_1.setIconSize(QSize(24, 24))
        self.cursos_1.setCheckable(True)
        self.cursos_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cursos_1)

        self.professores_1 = QPushButton(self.layoutWidget1)
        self.professores_1.setObjectName(u"professores_1")
        self.professores_1.setMinimumSize(QSize(50, 50))
        self.professores_1.setMaximumSize(QSize(50, 50))
        self.professores_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.professores_1.setIcon(icon3)
        self.professores_1.setIconSize(QSize(24, 24))
        self.professores_1.setCheckable(True)
        self.professores_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.professores_1)

        self.configuracoes_1 = QPushButton(self.layoutWidget1)
        self.configuracoes_1.setObjectName(u"configuracoes_1")
        self.configuracoes_1.setMinimumSize(QSize(50, 50))
        self.configuracoes_1.setMaximumSize(QSize(50, 50))
        self.configuracoes_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.configuracoes_1.setIcon(icon4)
        self.configuracoes_1.setIconSize(QSize(24, 24))
        self.configuracoes_1.setCheckable(True)
        self.configuracoes_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.configuracoes_1)

        self.verticalSpacer = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sair_1 = QPushButton(self.layoutWidget1)
        self.sair_1.setObjectName(u"sair_1")
        self.sair_1.setMinimumSize(QSize(50, 50))
        self.sair_1.setMaximumSize(QSize(50, 50))
        self.sair_1.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.sair_1.setIcon(icon5)
        self.sair_1.setIconSize(QSize(24, 24))
        self.sair_1.setCheckable(True)

        self.verticalLayout.addWidget(self.sair_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(0, 0, 1191, 48))
        self.header_widget.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        icon6 = QIcon()
        icon6.addFile(u":/density_medium_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(24, 24))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(411, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_12 = QPushButton(self.header_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: rgb(55, 96, 214);\n"
"border-radius:10px;")
        icon7 = QIcon()
        icon7.addFile(u":/search_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_12)

        self.horizontalSpacer = QSpacerItem(411, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon8 = QIcon()
        icon8.addFile(u":/person_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_15)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 60, 1201, 801))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_5 = QLabel(self.dashboard_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 340, 291, 51))
        font = QFont()
        font.setPointSize(40)
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.alunos_page = QWidget()
        self.alunos_page.setObjectName(u"alunos_page")
        self.label_6 = QLabel(self.alunos_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 261, 51))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_10 = QLabel(self.alunos_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 70, 271, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_10.setFont(font2)
        self.info_aluno_table = QTableWidget(self.alunos_page)
        if (self.info_aluno_table.columnCount() < 11):
            self.info_aluno_table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.info_aluno_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.info_aluno_table.setObjectName(u"info_aluno_table")
        self.info_aluno_table.setGeometry(QRect(20, 200, 1101, 511))
        self.info_aluno_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA\n"
"}")
        self.info_aluno_table.setAlternatingRowColors(True)
        self.layoutWidget2 = QWidget(self.alunos_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 100, 481, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AddAluno_btn = QPushButton(self.layoutWidget2)
        self.AddAluno_btn.setObjectName(u"AddAluno_btn")
        self.AddAluno_btn.setMinimumSize(QSize(0, 41))
        font3 = QFont()
        font3.setBold(True)
        self.AddAluno_btn.setFont(font3)
        self.AddAluno_btn.setStyleSheet(u"QPushButton#AddAluno_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#AddAluno_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/account_circle_40dp_E3E3E3_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddAluno_btn.setIcon(icon9)
        self.AddAluno_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.AddAluno_btn)

        self.exportExcel_btn = QPushButton(self.layoutWidget2)
        self.exportExcel_btn.setObjectName(u"exportExcel_btn")
        self.exportExcel_btn.setMinimumSize(QSize(0, 41))
        self.exportExcel_btn.setFont(font3)
        self.exportExcel_btn.setStyleSheet(u"QPushButton#exportExcel_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#exportExcel_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.exportExcel_btn)

        self.exportPDF_btn = QPushButton(self.layoutWidget2)
        self.exportPDF_btn.setObjectName(u"exportPDF_btn")
        self.exportPDF_btn.setMinimumSize(QSize(0, 41))
        self.exportPDF_btn.setFont(font3)
        self.exportPDF_btn.setStyleSheet(u"QPushButton#exportPDF_btn:pressed{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#exportPDF_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/picture_as_pdf_24dp_3760D6_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportPDF_btn.setIcon(icon10)
        self.exportPDF_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.exportPDF_btn)

        self.layoutWidget3 = QWidget(self.alunos_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 150, 711, 43))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.genero_aluno_comboBox = QComboBox(self.layoutWidget3)
        self.genero_aluno_comboBox.addItem("")
        self.genero_aluno_comboBox.addItem("")
        self.genero_aluno_comboBox.setObjectName(u"genero_aluno_comboBox")
        self.genero_aluno_comboBox.setMinimumSize(QSize(150, 0))
        self.genero_aluno_comboBox.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_3.addWidget(self.genero_aluno_comboBox)

        self.pesquisar_aluno_lineEdit = QLineEdit(self.layoutWidget3)
        self.pesquisar_aluno_lineEdit.setObjectName(u"pesquisar_aluno_lineEdit")
        self.pesquisar_aluno_lineEdit.setMinimumSize(QSize(0, 35))
        self.pesquisar_aluno_lineEdit.setStyleSheet(u"	border-bottom-color: rgba(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: black;\n"
"	height: 35px;\n"
"	border-radius: 10px;\n"
"")

        self.horizontalLayout_3.addWidget(self.pesquisar_aluno_lineEdit)

        self.stackedWidget.addWidget(self.alunos_page)
        self.cursos_page = QWidget()
        self.cursos_page.setObjectName(u"cursos_page")
        self.label_7 = QLabel(self.cursos_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 30, 91, 51))
        self.label_7.setFont(font1)
        self.label_11 = QLabel(self.cursos_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 80, 271, 20))
        self.label_11.setFont(font2)
        self.pesquisar_Curso_lineEdit_2 = QLineEdit(self.cursos_page)
        self.pesquisar_Curso_lineEdit_2.setObjectName(u"pesquisar_Curso_lineEdit_2")
        self.pesquisar_Curso_lineEdit_2.setGeometry(QRect(750, 110, 361, 35))
        self.pesquisar_Curso_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.pesquisar_Curso_lineEdit_2.setStyleSheet(u"	border-bottom-color: rgba(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: black;\n"
"	height: 35px;\n"
"	border-radius: 10px;\n"
"")
        self.Curso_tableWidget = QTableWidget(self.cursos_page)
        if (self.Curso_tableWidget.columnCount() < 9):
            self.Curso_tableWidget.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Curso_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.Curso_tableWidget.setObjectName(u"Curso_tableWidget")
        self.Curso_tableWidget.setGeometry(QRect(20, 170, 811, 511))
        self.Curso_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA\n"
"}")
        self.widget = QWidget(self.cursos_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(7, 110, 731, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.AddCurso_btn_2 = QPushButton(self.widget)
        self.AddCurso_btn_2.setObjectName(u"AddCurso_btn_2")
        self.AddCurso_btn_2.setMinimumSize(QSize(0, 41))
        self.AddCurso_btn_2.setFont(font3)
        self.AddCurso_btn_2.setStyleSheet(u"QPushButton#AddCurso_btn_2{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#AddCurso_btn_2:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/add_2_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddCurso_btn_2.setIcon(icon11)
        self.AddCurso_btn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.AddCurso_btn_2)

        self.AddDisciplina_btn_3 = QPushButton(self.widget)
        self.AddDisciplina_btn_3.setObjectName(u"AddDisciplina_btn_3")
        self.AddDisciplina_btn_3.setMinimumSize(QSize(0, 41))
        self.AddDisciplina_btn_3.setFont(font3)
        self.AddDisciplina_btn_3.setStyleSheet(u"QPushButton#AddDisciplina_btn_3{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#AddDisciplina_btn_3:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.AddDisciplina_btn_3.setIcon(icon11)
        self.AddDisciplina_btn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.AddDisciplina_btn_3)

        self.AddTurma_btn = QPushButton(self.widget)
        self.AddTurma_btn.setObjectName(u"AddTurma_btn")
        self.AddTurma_btn.setMinimumSize(QSize(0, 41))
        self.AddTurma_btn.setFont(font3)
        self.AddTurma_btn.setStyleSheet(u"QPushButton#AddTurma_btn{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#AddTurma_btn:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.AddTurma_btn.setIcon(icon11)
        self.AddTurma_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.AddTurma_btn)

        self.Matricular_btn_2 = QPushButton(self.widget)
        self.Matricular_btn_2.setObjectName(u"Matricular_btn_2")
        self.Matricular_btn_2.setMinimumSize(QSize(0, 41))
        self.Matricular_btn_2.setFont(font3)
        self.Matricular_btn_2.setStyleSheet(u"QPushButton#Matricular_btn_2{\n"
"background-color: rgb(55, 96, 214);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#Matricular_btn_2:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(55, 96, 214);\n"
"border: 1px solid rgb(55, 96, 214);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.Matricular_btn_2.setIcon(icon11)
        self.Matricular_btn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.Matricular_btn_2)

        self.stackedWidget.addWidget(self.cursos_page)
        self.professores_page = QWidget()
        self.professores_page.setObjectName(u"professores_page")
        self.label_12 = QLabel(self.professores_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 80, 301, 20))
        self.label_12.setFont(font2)
        self.label_13 = QLabel(self.professores_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 30, 151, 51))
        self.label_13.setFont(font1)
        self.tableWidget = QTableWidget(self.professores_page)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 210, 401, 192))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA\n"
"}")
        self.widget1 = QWidget(self.professores_page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 110, 541, 91))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.widget1)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget{\n"
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

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)

        self.pesquisar_aluno_lineEdit_2 = QLineEdit(self.widget1)
        self.pesquisar_aluno_lineEdit_2.setObjectName(u"pesquisar_aluno_lineEdit_2")
        self.pesquisar_aluno_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.pesquisar_aluno_lineEdit_2.setStyleSheet(u"	border-bottom-color: rgba(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: black;\n"
"	height: 35px;\n"
"	border-radius: 10px;\n"
"")

        self.gridLayout_2.addWidget(self.pesquisar_aluno_lineEdit_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.professores_page)
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.label_9 = QLabel(self.menu_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(400, 350, 201, 51))
        self.label_9.setFont(font)
        self.stackedWidget.addWidget(self.menu_page)

        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.configuracoes_1.toggled.connect(self.configuracoes_2.setChecked)
        self.professores_1.toggled.connect(self.professores_2.setChecked)
        self.cursos_1.toggled.connect(self.cursos_2.setChecked)
        self.alunos_1.toggled.connect(self.alunos_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.alunos_2.toggled.connect(self.alunos_1.setChecked)
        self.cursos_2.toggled.connect(self.cursos_1.setChecked)
        self.professores_2.toggled.connect(self.professores_1.setChecked)
        self.configuracoes_2.toggled.connect(self.configuracoes_1.setChecked)
        self.sair_1.toggled.connect(MainWindow.close)
        self.sair_2.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.alunos_2.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.cursos_2.setText(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.professores_2.setText(QCoreApplication.translate("MainWindow", u"Professores", None))
        self.configuracoes_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.sair_2.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.alunos_1.setText("")
        self.cursos_1.setText("")
        self.professores_1.setText("")
        self.configuracoes_1.setText("")
        self.sair_1.setText("")
        self.menu.setText("")
        self.pushButton_12.setText("")
        self.pushButton_15.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es do Aluno", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo \u00e0 p\u00e1gina de informa\u00e7\u00f5es dos alunos", None))
        ___qtablewidgetitem = self.info_aluno_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.info_aluno_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem2 = self.info_aluno_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel", None));
        ___qtablewidgetitem3 = self.info_aluno_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Id Aluno", None));
        ___qtablewidgetitem4 = self.info_aluno_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem5 = self.info_aluno_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Curso", None));
        ___qtablewidgetitem6 = self.info_aluno_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"G\u00eanero", None));
        ___qtablewidgetitem7 = self.info_aluno_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem8 = self.info_aluno_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem9 = self.info_aluno_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem10 = self.info_aluno_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.AddAluno_btn.setText(QCoreApplication.translate("MainWindow", u"Adicionar Aluno", None))
        self.exportExcel_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar para o Excel", None))
        self.exportPDF_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar para PDF", None))
        self.genero_aluno_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.genero_aluno_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.pesquisar_aluno_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo \u00e0 p\u00e1gina de informa\u00e7\u00f5es dos Cursos", None))
        self.pesquisar_Curso_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        ___qtablewidgetitem11 = self.Curso_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem12 = self.Curso_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Disciplina", None));
        ___qtablewidgetitem13 = self.Curso_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem14 = self.Curso_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Carga Hor\u00e1ria", None));
        ___qtablewidgetitem15 = self.Curso_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem16 = self.Curso_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem17 = self.Curso_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Professor", None));
        ___qtablewidgetitem18 = self.Curso_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Vagas", None));
        self.AddCurso_btn_2.setText(QCoreApplication.translate("MainWindow", u"Adicionar Curso", None))
        self.AddDisciplina_btn_3.setText(QCoreApplication.translate("MainWindow", u"Adicionar Disciplina", None))
        self.AddTurma_btn.setText(QCoreApplication.translate("MainWindow", u"Nova Turma", None))
        self.Matricular_btn_2.setText(QCoreApplication.translate("MainWindow", u"Matricular", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo \u00e0 p\u00e1gina de informa\u00e7\u00f5es dos Professores", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Professores", None))
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Curso", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Disciplina", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None));
        self.pesquisar_aluno_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Menu Page", None))
    # retranslateUi

