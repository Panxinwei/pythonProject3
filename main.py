# This is a sample Python script.
import sys

import numpy as np
from PyQt5.QtChart import QLineSeries, QChart, QChartView, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
#from PyQt5.QtWidgets import QApplication, QMainWindow
import filedialogs
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtMultimediaWidgets import QVideoWidget
from filedialogs import filedialogs

import PBRTQCUI
import data
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import importdata
import Methods

inputdata_dict=[]
Methods_points=[]


class MyMainForm(QMainWindow, PBRTQCUI.Ui_Dialog):








    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.importButton.clicked.connect(self.importDatadef)
        #取出inputdata 未解决，打开就直接要求打开csv
       # inputdata=self.importDatadef()
        #传参
        self.confirmButton.clicked.connect(lambda: self.MethodsCal(inputdata_dict[0]))
        #按下确定键，执行画图
       # self.confirmButton.clicked.connect(lambda:self.createChart(Methods_points[0],inputdata_dict[0]))


        self.MethodsBox.addItems(["SMA", "WMA", "EWMA", "FM"])


    #导入数据
    def importDatadef(self):
        #全局变量

        inputdata =importdata.getimportdata(self)
        inputdata_dict.append(inputdata)
        #print(inputdata)
        TestNameList = inputdata['TestName'].values
        TestNameList2 = TestNameList.tolist()
        InstrumentList=inputdata['InstrumentName'].values
        InstrumentList2 = InstrumentList.tolist()
       # arrTest = np.array(ListMA)
       # print(TestNameList2)
       # print(type(TestNameList2))
        for TestName in TestNameList2:
            num = 0

           # print(len(self.TestBox))
            for i in range(0, len(self.TestBox)):
                if TestName ==self.TestBox.itemText(i):
                   num=num+1
            if num==0:
                self.TestBox.addItem(TestName)

        for InstrumentName in InstrumentList2:
            num = 0

            # print(len(self.TestBox))
            for i in range(0, len(self.InstrumentBox)):
                if InstrumentName == self.InstrumentBox.itemText(i):
                    num = num + 1
            if num == 0:
                self.InstrumentBox.addItem(InstrumentName)



       # self.TestBox.addItem(inputdata['TestName'].values)

        return inputdata


    #导入计算
    def MethodsCal(self,inputdata):
        Methods_points.clear()
        if (len(self.NEdit.toPlainText()) > 0):
            N=int(self.NEdit.toPlainText())
        if(len(self.WeightEdit.toPlainText())>0):
            weight = float(self.WeightEdit.toPlainText())
        #   print(weight)
        #  print(self.NEdit.toPlainText())
        # print(inputdata)
        if self.MethodsBox.currentText()=="FM":
            Methods_points.append(Methods.FM(N, inputdata))
        if self.MethodsBox.currentText() == "SMA":
            Methods_points.append(Methods.MA(N, inputdata))
        if self.MethodsBox.currentText() == "WMA":
            Methods_points.append(Methods.WMA(N, inputdata))
        if self.MethodsBox.currentText() == "EWMA":
            Methods_points.append(Methods.EWMA(N, weight, inputdata))

        self.createChart(Methods_points[0],inputdata_dict[0])
       # return Methods_points


    #画图
    def createChart(self,Methods_Points,inputdata):

       # self.MethodsBox.currentText()
            # 设置折线数据
        #折线图
        lineSeries=data.getlineSeries(self,Methods_Points,inputdata)
        lineSeries.setVisible(True)
        lineSeries.setPointLabelsFormat("@yPoint")
        lineSeries.setPointLabelsVisible(True)
        # 创建图表
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(lineSeries)
        chart.setTitle('PBRTQC模拟图')

        axisX=QDateTimeAxis()
        axisX.setFormat('hh:mm')
        chart.addAxis(axisX,Qt.AlignBottom)
        lineSeries.attachAxis(axisX)
       # chart.createDefaultAxes()

        axisY=QValueAxis()
        chart.addAxis(axisY,Qt.AlignLeft)
        lineSeries.attachAxis(axisY)
        #chart.legend().setVisible(True)
        # 图表视图

        self.graphicsView.setChart(chart)
        #self.createChart()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myapp=QApplication(sys.argv)
    #myDlg=QDialog()
    myDlg=MyMainForm()
    #myUI=PBRTQCUI.Ui_Dialog()
    #myUI.setupUi(myDlg)
    myDlg.show()
    sys.exit(myapp.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
