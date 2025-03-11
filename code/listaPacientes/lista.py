import sys, os, json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from listaPacientes import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table = self.ui.tabelaLista
        self.preencher_itens_vazios()
        self.centralizar()
        self.exibir()
        # self.imprimir_itens()

    def centralizar(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    print("Centralização impossibilitada")
    
    def exibir(self):
        # Caminho relativo ao diretório do script
        caminho_json = "../../save/luan.json"
        print("Número de linhas:", self.table.rowCount())  # Depuração
        print("Número de colunas:", self.table.columnCount())  # Depuração

        # Abrindo o arquivo JSON
        # with open(caminho_json, "r", encoding="utf-8") as arquivo:
        #     dados = json.load(arquivo)

        # print(dados)  # Mostra o conteúdo do JSON
        # print(dados['nome'])
        caminho = "../../save"
        # Listar os arquivos da pasta de save 
        arquivos = os.listdir(caminho)
        for arq in arquivos:
            print(arq)
            # Abrir o arquivo JSON
            with open(f"../../save/{arq}", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                print(dados, " Dados aí")
                # Daqui para baixo em implementação
                # Precisa passar os dados dos arquivos JSON para a tabela de Pacientes





                # for row in range(self.table.rowCount()):
                #     for col in range(self.table.columnCount()):
                #         item = self.table.item(row, col)
                # print(dados["nome"])
                
# for row in range(self.table.rowCount()):
#             for col in range(self.table.columnCount()):
#                 item = self.table.item(row, col)  # Pega o item na célula (row, col)
#                 if item:  # Se o item existe (não é None)
#                     print(f"Item na célula ({row}, {col}): {item.text()}")
#                 else:
#                     print(f"Célula ({row}, {col}) está vazia")



        # for arquivo in 
        # for row in range(self.table.rowCount()):
        #     for col in range(self.table.columnCount()):
        #         item = self.table.item(row, col)
        #         if item:

        # self.nomeItem = self.table.item(0, 0).text()
        # print(self.nomeItem)

    def preencher_itens_vazios(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                if self.table.item(row, col) is None:
                    texto = self.table.model().index(row, col).data() or ""  # Pega o texto exibido no Qt Designer
                    item = QTableWidgetItem(texto)  # Cria um novo item com o texto
                    self.table.setItem(row, col, item)

    def imprimir_itens(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)  # Pega o item na célula (row, col)
                if item:  # Se o item existe (não é None)
                    print(f"Item na célula ({row}, {col}): {item.text()}")
                else:
                    print(f"Célula ({row}, {col}) está vazia")


    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())