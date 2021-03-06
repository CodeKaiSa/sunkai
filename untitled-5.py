# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled-5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import sys,threading
from PyQt5.QtCore import *
from tkinter import messagebox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setMinimumSize(QtCore.QSize(0, 22))
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ms = MySignal()  # 实例化一个信号类
        self.ms.pic.connect(self.showData)
        self.ms.txt.connect(self.printToGui)
        self.toolButton.clicked.connect(self.openDirectory)
        self.pushButton.clicked.connect(self.thread_3)
        self.pushButton_3.clicked.connect(self.thread_1)
        self.pushButton_2.clicked.connect(self.evevt_set)
        self.pushButton_4.clicked.connect(self.thread_2)

    def openDirectory(self):  # 打开文件夹（目录）
        global directory  # 将路径定位全局变量，以便于在下载图片里可以直接使用
        directory = QtWidgets.QFileDialog.getOpenFileName(self.toolButton, "选择文件", "")[0]
        self.lineEdit.setText(directory)

    def readData(self):
        global data, name_list
        data = pd.read_excel(directory)
        name_list = data['姓名']
        name_list = list(set(name_list))
        self.ms.txt.emit('表格数据已经读取完毕！可以进行下一步！')
        # messagebox.showinfo("提示", '数据已读取完成！')

    def delData(self):
        global new_data, name
        plt.rcParams['font.sans-serif'] = ["SimHei"]
        plt.rcParams["axes.unicode_minus"] = False

        for name in name_list:
            data_name = data[data['姓名'] == name]
            new_data = data_name.reset_index(drop=True)
            print(name)
            plt.figure(figsize=(6, 4))
            plt.plot(new_data.index, new_data['数学'], label='数学')
            plt.plot(new_data.index, new_data['英语'], label='英语')
            plt.xlabel('序号', fontsize=10)
            plt.ylabel('成绩', fontsize=10)
            plt.legend(fontsize=10)
            plt.title(name)
            plt.savefig(f'data.jpg')
            self.ms.pic.emit(f'data.jpg')
            event.clear()
            event.wait()
        self.ms.txt.emit('已是最后一位同学！')

    def evevt_set(self):
        event.set()


    def event_save(self):
        self.ms.txt.emit(f'正在保存{name}.xlsx，请稍等')
        new_data.to_excel(f'{name}.xlsx')
        self.ms.txt.emit(f'{name}.xlsx已经保存，可以进行下一步！')

    def showData(self, image):
        image1 = cv2.imdecode(np.fromfile(image, dtype=np.uint8), -1)  # 读取爬取的图片
        height = image1.shape[0]  # 图片高度
        width = image1.shape[1]  # 图片宽度
        # fy = self.graphicsView.height() / height  # 计算图片缩放的比例
        # jpg = QtGui.QPixmap(image).scaled(int(width * fy), self.graphicsView.height())  # 调整图片在graphicsView里显示的尺寸。
        jpg = QtGui.QPixmap(image).scaled(width, height)
        frame = QtGui.QImage(jpg)
        pix = QtGui.QPixmap.fromImage(frame)
        self.item = QtWidgets.QGraphicsPixmapItem(pix)
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)
        # self.graphicsView.fitInView(jpg)

    def printToGui(self,txt):
        self.textBrowser.append(txt)
        self.textBrowser.ensureCursorVisible()
    def thread(self):
        t = threading.Thread(target=self.showData)

        t.start()

    def thread_1(self):
        t = threading.Thread(target=self.readData)
        t.start()

    def thread_2(self):
        t = threading.Thread(target=self.delData)
        t.start()

    def thread_3(self):
        t = threading.Thread(target=self.event_save)
        t.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_3.setText(_translate("MainWindow", "读取数据"))
        self.pushButton.setText(_translate("MainWindow", "保存数据"))
        self.pushButton_4.setText(_translate("MainWindow", "生成图表"))
        self.pushButton_2.setText(_translate("MainWindow", "下一位同学"))
class MySignal(QObject):
    pic = pyqtSignal(str,name='graphicsView')
    txt = pyqtSignal(str, name='textBrowser')
if __name__ == '__main__':

    event = threading.Event()
    save_event = threading.Event()
    app = QtWidgets.QApplication(sys.argv)
    mywin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mywin)
    #ui.showData()
    mywin.show()
    sys.exit(app.exec_())