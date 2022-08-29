from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_Dot(object):
    def setupUi(self, Dot):
        Dot.setObjectName("Dot")
        Dot.setWindowModality(QtCore.Qt.NonModal)
        Dot.resize(1200, 800)
        Dot.setStyleSheet("background-color:black;")

        # --------------------------- Setting Logo_bg Image------------------------#

        self.lbl_logo_bg = QtWidgets.QLabel(Dot)
        self.lbl_logo_bg.setGeometry(QtCore.QRect(30, 60, 211, 71))
        self.lbl_logo_bg.setStyleSheet("background-color:turquoise;")
        self.lbl_logo_bg.setText("")
        self.lbl_logo_bg.setScaledContents(True)
        self.lbl_logo_bg.setObjectName("lbl_logo_bg")

        # --------------------------- Setting Logo Image------------------------#
        self.lbl_logo = QtWidgets.QLabel(Dot)
        self.lbl_logo.setGeometry(QtCore.QRect(40, 70, 191, 51))
        self.lbl_logo.setStyleSheet("background-image: transparent;")
        self.lbl_logo.setPixmap(QtGui.QPixmap("images/logo/logo.png"))
        self.lbl_logo.setText("")
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setObjectName("lbl_logo")

        # ---------------------Setting label for dot.gif -------------------------#
        self.face = QtWidgets.QLabel(Dot)
        self.face.setGeometry(QtCore.QRect(50, 190, 441, 571))
        self.face.setStyleSheet("background-image: url(images/gifs/dot.gif);")
        self.face.setText("")
        self.face.setScaledContents(True)
        self.face.setObjectName("face")

        # --------------------------Play dot.gif -----------------------------------#
        self.movie_energy = QMovie("images/gifs/dot.gif")
        self.face.setMovie(self.movie_energy)
        self.movie_energy.start()

        # ---------------------Setting label for energy.gif --------------
        self.lbl_energy = QtWidgets.QLabel(Dot)
        self.lbl_energy.setGeometry(QtCore.QRect(670, 280, 411, 331))
        self.lbl_energy.setStyleSheet("background-image: url(images/gifs/energy.gif);")
        self.lbl_energy.setText("")
        self.lbl_energy.setScaledContents(True)
        self.lbl_energy.setObjectName("lbl_energy")

        # --------------------------- Setting start/exit button ------------------------#

        self.btn_start = QtWidgets.QPushButton(Dot)
        self.btn_start.setGeometry(QtCore.QRect(683, 720, 151, 41))
        self.btn_start.setStyleSheet("border-radius:20px;\n"
                                     "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(170, 255, 255);\n"
                                     "font: 14pt \\\"MS Shell Dlg 2\\\"")
        self.btn_start.setObjectName("btn_start")

        self.btn_exit = QtWidgets.QPushButton(Dot)
        self.btn_exit.setGeometry(QtCore.QRect(910, 720, 151, 41))
        self.btn_exit.setStyleSheet("border-radius:20px;\n"
                                    "background-color: rgb(170, 255, 255);\n"
                                    "font: 14pt \\\"MS Shell Dlg 2\\;")
        self.btn_exit.setObjectName("btn_exit")

        # --------------------------- Setting Label for energy.gif ------------------------#

        self.lbl_blue = QtWidgets.QLabel(Dot)
        self.lbl_blue.setGeometry(QtCore.QRect(270, -110, 921, 371))
        self.lbl_blue.setScaledContents(True)
        self.lbl_blue.setStyleSheet("background-image:url(images/gifs/initial.gif);"
                                    "background: no repeat;")
        self.lbl_blue.setText("")
        self.lbl_energy.setObjectName("lbl_blue")




        # self.btn_login.raise_()
        #self.btn_manual.raise_()
        self.btn_start.raise_()
        self.lbl_blue.raise_()
        self.face.raise_()
        self.btn_exit.raise_()
        self.lbl_energy.raise_()
        self.lbl_logo_bg.raise_()
        self.lbl_logo.raise_()

        self.retranslateUi(Dot)
        QtCore.QMetaObject.connectSlotsByName(Dot)

    def retranslateUi(self, Dot):
        _translate = QtCore.QCoreApplication.translate
        Dot.setWindowTitle(_translate("Dot", "Dot"))
        self.lbl_energy.setText(_translate("Dot", ""))
        self.lbl_energy.setText(_translate("Dot", ""))
        # self.btn_login.setText(_translate("Dot", "LOGIN"))
        #self.btn_manual.setText(_translate("Dot", "MANUAL"))
        self.btn_start.setText(_translate("Dot", "START"))
        self.btn_exit.setText(_translate("Dot", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dot = QtWidgets.QWidget()
    ui = Ui_Dot()
    ui.setupUi(Dot)
    Dot.show()
    sys.exit(app.exec_())
