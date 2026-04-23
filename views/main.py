import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QMessageBox
from views.ui_login_form import Ui_Form as Ui_Login
from views.ui_criarconta import Ui_Form as Ui_Cadastro
from views.sidebar import MySideBar

class GerenciadorJanelas(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. container de telas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # 2. configura interface de Login
        self.janela_login = QWidget()
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self.janela_login)
        
        # 3. configura a interface de cadastro
        self.janela_cadastro = QWidget()
        self.ui_cadastro = Ui_Cadastro()
        self.ui_cadastro.setupUi(self.janela_cadastro)
        
        # 4. configura a sidebar lógica do sidebar.py)
        self.janela_sidebar = MySideBar()
        
        # add janelas ao stack
        self.stack.addWidget(self.janela_login)    # indice 0
        self.stack.addWidget(self.janela_cadastro) # indice 1
        self.stack.addWidget(self.janela_sidebar)  # indice 2
        
        # CONFIGURAÇÕES DE UI 
        self.ui_login.lineEdit.setMaxLength(11)    # trava 11 digitos do CPF no login
        self.ui_cadastro.lineEdit_3.setMaxLength(11) # trava 11 digitos do CPF no Cadastro
        self.setWindowTitle("CRM Acadêmico")
        self.resize(1440, 900)

        # CONEXÕES
        
        # login e cadastro
        self.ui_login.b1.clicked.connect(self.validar_acesso)
        self.ui_login.b2.clicked.connect(self.ir_para_cadastro)
        self.ui_cadastro.b1.clicked.connect(self.ir_para_login)

        # lógica de sair (logout) vinda da sidebar
        self.janela_sidebar.logout_requested.connect(self.ir_para_login)

    def validar_acesso(self):
        """validação fake: CPF com 11 dígitos e senha '123'"""
        cpf = self.ui_login.lineEdit.text()
        senha = self.ui_login.lineEdit_2.text()

        if len(cpf) == 11 and senha == "123":
            self.stack.setCurrentIndex(2) # vai para a Sidebar
        else:
            QMessageBox.warning(self, "Erro de Acesso", "CPF deve ter 11 dígitos e a senha ser '123'.")

    def ir_para_cadastro(self):
        self.stack.setCurrentIndex(1)

    def ir_para_login(self):
        self.stack.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GerenciadorJanelas()
    window.show()
    sys.exit(app.exec())