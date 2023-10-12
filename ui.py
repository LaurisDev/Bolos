from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QWidget, QPushButton, \
    QLineEdit, QGroupBox
import sys


class Caja(QLabel):
    def __init__(self, color, number=None):
        super().__init__(str(number) if number is not None else "")
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        cuadricula = QGridLayout()

        # Cuadricula
        for i in range(1, 13):
            cuadricula.addWidget(Caja(" Grey", i), 0, i)

        for i in range(1, 13):
            cuadricula.addWidget(Caja("Grey"), 1, i)
            cuadricula.addWidget(Caja("Grey"), 2, i)

        # Texto y botones
        text_input = QLineEdit()
        cuadricula.addWidget(text_input, 3, 1, 1, 2)
        add_button = QPushButton("Add")
        cuadricula.addWidget(add_button, 3, 3, 1, 2)
        load_button = QPushButton("Load from file")
        cuadricula.addWidget(load_button, 3, 9, 1, 2)
        add_button = QPushButton("Restart")
        cuadricula.addWidget(add_button, 3, 11, 1, 2)

        # Labels
        label1 = QLabel("Frame")
        cuadricula.addWidget(label1, 0, 0, 1, 1)

        label2 = QLabel("Rolls")
        cuadricula.addWidget(label2, 0, 0, 3, 1)

        label3 = QLabel("Score")
        cuadricula.addWidget(label3, 0, 0, 6, 1)

        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addLayout(cuadricula)

        # Crear contenedor
        group_box = QGroupBox("BOLOS")
        group_box.setLayout(layout)
        group_box.setFixedSize(800, 400)

        # Que aparezca en la pantalla el contenedor al ejecutar
        self.setCentralWidget(group_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

