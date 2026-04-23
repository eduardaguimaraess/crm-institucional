from views.ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal 

class MySideBar(QMainWindow, Ui_MainWindow):
    # sinal que avisa o main.py para voltar ao login
    logout_requested = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CRM Académico")

        # esconde o menu expandido no início
        self.icon_name_widget.setHidden(True)

        # conexão do botão de menu para expandir e recolher
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)

        # conexões das páginas
        self.dashboard_1.clicked.connect(self.swich_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.swich_to_dashboardPage)

        self.alunos_1.clicked.connect(self.swich_to_alunosPage)
        self.alunos_2.clicked.connect(self.swich_to_alunosPage)

        self.cursos_1.clicked.connect(self.swich_to_cursosPage)
        self.cursos_2.clicked.connect(self.swich_to_cursosPage)

        self.professores_1.clicked.connect(self.swich_to_professoresPage)
        self.professores_2.clicked.connect(self.swich_to_professoresPage)

        self.configuracoes_1.clicked.connect(self.swich_to_configuracoesPage)
        self.configuracoes_2.clicked.connect(self.swich_to_configuracoesPage)

        # conexão dos botões de sair
        self.sair_1.clicked.connect(self.solicitar_logout)
        self.sair_2.clicked.connect(self.solicitar_logout)

    def solicitar_logout(self):
        self.logout_requested.emit()

    def swich_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def swich_to_alunosPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def swich_to_cursosPage(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def swich_to_professoresPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def swich_to_configuracoesPage(self):
        self.stackedWidget.setCurrentIndex(4)