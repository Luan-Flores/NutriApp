# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 762)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -20, 911, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../img/white.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, -10, 231, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../img/logoLfNutri.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.labelVerde = QtWidgets.QLabel(self.centralwidget)
        self.labelVerde.setGeometry(QtCore.QRect(120, 180, 631, 421))
        self.labelVerde.setStyleSheet("\n"
"background-color:transparent;\n"
"border-radius: 18px;")
        self.labelVerde.setText("")
        self.labelVerde.setPixmap(QtGui.QPixmap("../../img/cadastro.png"))
        self.labelVerde.setScaledContents(True)
        self.labelVerde.setObjectName("labelVerde")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.lineNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNome.setGeometry(QtCore.QRect(160, 280, 231, 31))
        self.lineNome.setStyleSheet("border-radius: 10px;\n"
"color: rgb(120, 120, 120);\n"
"padding-left: 10px;")
        self.lineNome.setText("")
        self.lineNome.setCursorPosition(0)
        self.lineNome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineNome.setObjectName("lineNome")
        self.enviar = QtWidgets.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(560, 550, 75, 23))
        self.enviar.setStyleSheet("border-radius: 10px;\n"
"background-color: white;\n"
"")
        self.enviar.setObjectName("enviar")
        self.lineIdade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIdade.setGeometry(QtCore.QRect(160, 330, 121, 31))
        self.lineIdade.setStyleSheet("border-radius: 10px;\n"
"color: rgb(120, 120, 120);\n"
"padding-left: 10px;")
        self.lineIdade.setText("")
        self.lineIdade.setObjectName("lineIdade")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 400, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.radioM = QtWidgets.QRadioButton(self.centralwidget)
        self.radioM.setGeometry(QtCore.QRect(280, 390, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioM.setFont(font)
        self.radioM.setStyleSheet("color:white;")
        self.radioM.setObjectName("radioM")
        self.radioF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioF.setGeometry(QtCore.QRect(280, 410, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioF.setFont(font)
        self.radioF.setStyleSheet("color:white;")
        self.radioF.setObjectName("radioF")
        self.lineAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineAltura.setGeometry(QtCore.QRect(160, 460, 121, 31))
        self.lineAltura.setStyleSheet("border-radius: 10px;\n"
"color: rgb(120, 120, 120);\n"
"padding-left: 10px;")
        self.lineAltura.setText("")
        self.lineAltura.setObjectName("lineAltura")
        self.linePeso = QtWidgets.QLineEdit(self.centralwidget)
        self.linePeso.setGeometry(QtCore.QRect(160, 510, 121, 31))
        self.linePeso.setStyleSheet("border-radius: 10px;\n"
"color: rgb(120, 120, 120);\n"
"padding-left: 10px;")
        self.linePeso.setText("")
        self.linePeso.setObjectName("linePeso")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.radioGanharPeso = QtWidgets.QRadioButton(self.centralwidget)
        self.radioGanharPeso.setGeometry(QtCore.QRect(450, 250, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioGanharPeso.setFont(font)
        self.radioGanharPeso.setStyleSheet("color:white;")
        self.radioGanharPeso.setObjectName("radioGanharPeso")
        self.radioPerderPeso = QtWidgets.QRadioButton(self.centralwidget)
        self.radioPerderPeso.setGeometry(QtCore.QRect(450, 270, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioPerderPeso.setFont(font)
        self.radioPerderPeso.setStyleSheet("color:white;")
        self.radioPerderPeso.setObjectName("radioPerderPeso")
        self.radioOutro = QtWidgets.QRadioButton(self.centralwidget)
        self.radioOutro.setGeometry(QtCore.QRect(450, 290, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioOutro.setFont(font)
        self.radioOutro.setStyleSheet("color:white;")
        self.radioOutro.setObjectName("radioOutro")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 260, 231, 16))
        self.label_7.setStyleSheet("border-top: 2px solid rgb(255, 255, 255)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineObjetivo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineObjetivo.setGeometry(QtCore.QRect(440, 320, 281, 111))
        self.lineObjetivo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineObjetivo.setStyleSheet("border-radius: 10px;\n"
"border: 6px solid white;\n"
"color: rgb(120, 120, 120);\n"
"padding-left: 10px;")
        self.lineObjetivo.setText("")
        self.lineObjetivo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineObjetivo.setDragEnabled(False)
        self.lineObjetivo.setReadOnly(False)
        self.lineObjetivo.setObjectName("lineObjetivo")
        self.radioIntermediario = QtWidgets.QRadioButton(self.centralwidget)
        self.radioIntermediario.setGeometry(QtCore.QRect(520, 500, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioIntermediario.setFont(font)
        self.radioIntermediario.setStyleSheet("color:white;")
        self.radioIntermediario.setObjectName("radioIntermediario")
        self.radioBasico = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBasico.setGeometry(QtCore.QRect(450, 500, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioBasico.setFont(font)
        self.radioBasico.setStyleSheet("color:white;")
        self.radioBasico.setObjectName("radioBasico")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: white;")
        self.label_9.setObjectName("label_9")
        self.radioAvancado = QtWidgets.QRadioButton(self.centralwidget)
        self.radioAvancado.setGeometry(QtCore.QRect(640, 500, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioAvancado.setFont(font)
        self.radioAvancado.setStyleSheet("color:white;")
        self.radioAvancado.setObjectName("radioAvancado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Cadastro"))
        self.lineNome.setPlaceholderText(_translate("MainWindow", "Nome:"))
        self.enviar.setText(_translate("MainWindow", "Enviar"))
        self.lineIdade.setPlaceholderText(_translate("MainWindow", "Idade:"))
        self.label_4.setText(_translate("MainWindow", "Sexo:"))
        self.radioM.setText(_translate("MainWindow", "Masculino"))
        self.radioF.setText(_translate("MainWindow", "Feminino"))
        self.lineAltura.setPlaceholderText(_translate("MainWindow", "Altura:"))
        self.linePeso.setPlaceholderText(_translate("MainWindow", "Peso:"))
        self.label_6.setText(_translate("MainWindow", "Objetivo"))
        self.radioGanharPeso.setText(_translate("MainWindow", "Ganhar peso"))
        self.radioPerderPeso.setText(_translate("MainWindow", "Perder peso"))
        self.radioOutro.setText(_translate("MainWindow", "Outro"))
        self.lineObjetivo.setPlaceholderText(_translate("MainWindow", "Descreva melhor seu objetivo..."))
        self.radioIntermediario.setText(_translate("MainWindow", "Intermediário"))
        self.radioBasico.setText(_translate("MainWindow", "Básico"))
        self.label_9.setText(_translate("MainWindow", "Escolha seu plano"))
        self.radioAvancado.setText(_translate("MainWindow", "Avançado"))
