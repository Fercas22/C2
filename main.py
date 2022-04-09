import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

import logica as lg

# import AG as ag
qtCreatorFile = "./view/mainView.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Title
        self.setWindowTitle('.:: ALGORITMOS GENETICOS ::.')
        # self.setFixedSize(800, 600)
        #Buttons
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnSalir.clicked.connect(self.exit)
    
    def iniciar(self):
        area, limiteP = self.getValues()
        # print(area)
        # print(limiteP)
        if (not area or not limiteP) or (not area and not limiteP):
            QMessageBox.warning(None, "Campo(s) Vaciios", "Se detectaron campos vacios")
        else:
            area = float(area)
            limiteP = int(limiteP)

            lg.proceso(area, limiteP)

    def getValues(self):
        area = self.areaCubrir.text()
        limitePoblacion = self.limitePoblacion.text()

        return area, limitePoblacion

    def exit(self):
        # self.close()
        salir = QMessageBox.question(self, 'Salir','¿Esta seguro que desea salir?',QMessageBox.Yes, QMessageBox.No)

        if salir == QMessageBox.Yes:
            self.close()
    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())