# This Python file uses the following encoding: utf-8
import sys
from design import Ui_MainWindow
from PySide6.QtWidgets import *
# from PySide6.QtCore import *
from PySide6.QtGui import QAction, QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class App(QMainWindow):



    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        menu_bar = QMenuBar(self.ui.ManualPage)
        menu_tools = menu_bar.addMenu('Инструменты')
        menu_graphs = menu_bar.addMenu('Графики')
        menu_analysis = menu_bar.addMenu('Тех анализ')
        menu_metrics = menu_bar.addMenu('Метрики')
        self.ui.MenuLayout.addWidget(menu_bar)

        addMainGraph = QAction(QIcon('graph_main.svg'), "Отобразить цену", self)
        addSecondGraph = QAction(QIcon('graph_second.svg'), "Отобразить динамику", self)
        # openAction.setShortcut("Ctrl+O")
        MainGraph = menu_graphs.addAction(addMainGraph)
        SecondGraph = menu_graphs.addAction(addSecondGraph)
        addMainGraph.triggered.connect(lambda: self.plotMainGraph(self.ui.MainGraph))
        addSecondGraph.triggered.connect(lambda: self.plotMainGraph(self.ui.SecondGraph))


        self.ui.LoginButton.clicked.connect(lambda: self.showDevelop())
        self.ui.SignUpButton.clicked.connect(lambda: self.showDevelop())
        self.ui.ForgotPassword.clicked.connect(lambda: self.showDevelop())
        self.ui.FreeButton.clicked.connect(lambda: self.showManual())

        self.ui.BackButton.clicked.connect(lambda: self.showLobby())


    def plotMainGraph(self, container):
        scene = QGraphicsScene()
        container.setScene(scene)
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        fig = Figure(figsize=(5,3))
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()
        scene.addWidget(canvas)
        ax = fig.add_subplot()
        ax.plot(hour, temperature)
    def showDevelop(self):
        self.ui.stackedWidget.setCurrentIndex(2) #0 - Lobby, 2 - Development, 1 - Manual
    def showManual(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def showLobby(self):
        self.ui.stackedWidget.setCurrentIndex(0)

app = QApplication(sys.argv)
window = App()
window.show()


sys.exit(app.exec_())
