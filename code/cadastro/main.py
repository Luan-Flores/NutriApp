import sys, json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from cadastro import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.enviar.clicked.connect(self.cadastrar)
        
        # Criando os grupos para os radio buttons
        self.grupoSexo = QButtonGroup()
        self.grupoObjetivo = QButtonGroup()
        self.grupoPlano = QButtonGroup()

        # Adicionando ao grupo (somente um poderá ser selecionado)
        self.grupoObjetivo.addButton(self.ui.radioGanharPeso)
        self.grupoObjetivo.addButton(self.ui.radioPerderPeso)
        self.grupoObjetivo.addButton(self.ui.radioOutro)

        # Adicionando ao grupo (somente um poderá ser selecionado)
        self.grupoPlano.addButton(self.ui.radioBasico)
        self.grupoPlano.addButton(self.ui.radioIntermediario)
        self.grupoPlano.addButton(self.ui.radioAvancado)
        
        # Adicionando ao grupo (somente um poderá ser selecionado)
        self.grupoSexo.addButton(self.ui.radioM)
        self.grupoSexo.addButton(self.ui.radioF)

        self.campos = [self.ui.lineNome, self.ui.lineIdade, self.ui.lineAltura, self.ui.linePeso, self.ui.lineSenha]


        
    def clear(self):
        self.ui.lineNome.clear()
        self.ui.lineIdade.clear()
        self.ui.lineAltura.clear()
        self.ui.linePeso.clear()
        self.ui.lineObjetivo.clear()
        self.ui.lineSenha.clear()
        self.ui.radioF.setChecked(False)
        self.ui.radioM.setChecked(False)
        self.ui.radioPerderPeso.setChecked(False)
        self.ui.radioGanharPeso.setChecked(False)
        self.ui.radioOutro.setChecked(False)
        
    def novoJogo(self):
        self.clear()
        QtWidgets.QMessageBox.information(self, "Novo jogo", "Novo jogo iniciado!")
    
    def cadastrar(self):
        
        data = {
            "nome" : self.ui.lineNome.text(),
            "idade" : self.ui.lineIdade.text(),
            "peso": self.ui.linePeso.text(),
            "altura" : self.ui.lineAltura.text(),
            "sexo" : "Feminino" if self.ui.radioF.isChecked() else "Masculino" if self.ui.radioM.isChecked() else "Não informado",
            "objetivo" : "Perder peso" if self.ui.radioPerderPeso.isChecked() else "Ganhar peso" if self.ui.radioGanharPeso.isChecked() else f"{self.ui.lineObjetivo.text()}" if self.ui.radioOutro.isChecked() else "Nada consta",
            "plano" : "Básico" if self.ui.radioBasico.isChecked() else "Intermediário" if self.ui.radioIntermediario.isChecked() else "Avançado" if self.ui.radioAvancado.isChecked() else "Não informado" 
        }

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Cadastrar", "", "Arquivos JSON (*.json)")

        if file_path:
            try:
                #Verifica se o arquivo termina com '.json'
                if not file_path.endswith('.json'):
                    file_path += '.json'
                
                #Salva o arquivo JSON no local escolhido
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Cadastro feito com sucesso! ")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao realizar o cadastro: {e}")
        else:
            data = {
                "nome" : self.ui.lineNome.text(),
                "senha" : self.ui.lineSenha.text(),
                "idade" : self.ui.lineIdade.text(),
                "peso": self.ui.linePeso.text(),
                "altura" : self.ui.lineAltura.text(),
                "sexo" : "Feminino" if self.ui.radioF.isChecked() else "Masculino" if self.ui.radioM.isChecked() else "Não informado",
                "objetivo" : "Perder peso" if self.ui.radioPerderPeso.isChecked() else "Ganhar peso" if self.ui.radioGanharPeso.isChecked() else f"{self.ui.lineObjetivo.text()}" if self.ui.radioOutro.isChecked() else "Nada consta" 
            }

            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Cadastrar", "", "Arquivos JSON (*.json)")

            if file_path:
                try:
                    #Verifica se o arquivo termina com '.json'
                    if not file_path.endswith('.json'):
                        file_path += '.json'
                    
                    #Salva o arquivo JSON no local escolhido
                    with open(file_path, "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

                    QtWidgets.QMessageBox.information(self, "Sucesso", "Cadastro feito com sucesso! ")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao realizar o cadastro: {e}")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado ")

    def login(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Carregar jogo", "", "Arquivos JSON (*.json)")
        

    def carregarJogo(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Carregar jogo", "", "Arquivos JSON (*.json)")
        
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    
                    data = json.load(file)
                    
                    self.ui.lineNome.setText(data.get("nome", ""))
                    self.ui.dateEdit.setDate(QtCore.QDate.fromString(data.get("data_nascimento", "2000-01-01"), "yyyy-MM-dd"))
                    self.ui.lineIdade.setText(data.get("idade", ""))
                    self.ui.lineAltura.setText(data.get("altura", ""))

                    if data.get("sexo") == "Feminino":
                        self.ui.checkF.setChecked(True)
                    elif data.get("sexo") == "Masculino":
                        self.ui.checkM.setChecked(True)
                    else:
                        self.ui.checkF.setChecked(False)
                        self.ui.checkM.setChecked(False)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo carregado com sucesso")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar o jogo : {e}")
        else:
            QtWidgets.QMessageBox.warning(self, 'Erro', 'Nenhum arquivo selecionado')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())