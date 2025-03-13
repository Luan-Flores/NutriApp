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
        self.btnCadastrar = self.ui.btnCadastrar
        self.btnEditar = self.ui.btnEditar
        self.btnRemover = self.ui.btnRemover
        self.btnSalvar = self.ui.btnSalvar
        
        self.exibir()
        self.centralizar()
        # self.imprimir_itens()

    def centralizar(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    print("Centralização impossibilitada")
    
    def addLinha(self, usuario):
        count = self.table.rowCount()
        print(count, " QUANTIDADE DE LINHAAAS")
        self.table.insertRow(count)
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem("Meu Valor"))
        print(usuario)
        
    def exibir(self):
        # Caminho relativo ao diretório do script
        print("Número de linhas:", self.table.rowCount())  # Depuração
        print("Número de colunas:", self.table.columnCount())  # Depuração

        caminho = "../../save"
        # Listar os arquivos da pasta de save 
        arrayDosIguais = []
        arquivos = os.listdir(caminho)
        i=0
        for arq in arquivos:
            i+=1
            print(i)

            self.table.insertRow(i)
            print("Número de linhas:", self.table.rowCount())  # Depuração

            # Abrir o arquivo JSON
            with open(f"../../save/{arq}", "r", encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
                self.colunas = self.table.columnCount()

                    # Iterando sobre as colunas da tabela
                for col in range(self.colunas):
                    self.colNome = self.table.horizontalHeaderItem(col).text().lower()
                    for k in self.dados:
                        print(k)
                    # Se o nome das colunas forem iguais, insira o valor
                        if self.colNome == k:
                            print(f"coluna tabela {self.colNome}  : coluna json {k}")

                            self.table.setItem(i, col, QtWidgets.QTableWidgetItem(f"{self.dados[k]}"))
                            arrayDosIguais.append(self.colNome)
                            
                        else:
                            print("Não é igual")
                            print(f"DIFERENTES !! coluna tabela// {self.colNome}   : coluna json// {k}")
                        # print(f"VALOR DA COLUNA: {self.table.horizontalHeaderItem(col).text()} : {item.text()}")
        print(arrayDosIguais)

    # def addInfo(self, colunaJSON, colunaTable):
    #     self.table.setItem(0, colunaTable, QtWidgets.QTableWidgetItem("VALOR  a"))

                
                        


        # count = self.table.rowCount()
        # print(count, " QUANTIDADE DE LINHAAAS")
        # self.table.insertRow(count)
        # self.table.setItem(1, 2, QtWidgets.QTableWidgetItem("Meu Valor"))
        # print(usuario)



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