from PyQt5.QtChart import QLineSeries, QChart
from PyQt5.QtCore import QDateTime


def getlineSeries(self,Methods_points,importdata):

    ResultValueTimeList=importdata['ResultValueTime'].tolist()


  #  print(ResultValueTimeList)
  #  print(type(ResultValueTimeList))



    Methods_pointList = Methods_points.tolist()

  #  print(Methods_pointList)
  #  print(type(Methods_pointList))


    lineSeries = QLineSeries()


    for i in range(0,len(ResultValueTimeList)):

        if(Methods_pointList[i] is not None ):

            if(Methods_points[i] !=''):
               # print(type(Methods_points[i]))
                Methods_pointsF=float(Methods_points[i])
                if(Methods_pointsF>0):
                   # xValue=QDateTime()

                    strResultValueTime = ResultValueTimeList[i].strftime("%Y-%m-%d %H:%M:%S")
                    #print(strResultValueTime)
                    xValue=QDateTime.fromString(strResultValueTime,"yyyy-MM-dd hh:mm:ss")
                    #print(xValue.toMSecsSinceEpoch())
                    #

                    lineSeries.append(xValue.toMSecsSinceEpoch(), Methods_pointsF)
        '''
        lineSeries.append(2, 4)
        lineSeries.append(3, 8)
        lineSeries.append(7, 4)
        lineSeries.append(10, 5)
        lineSeries.append(11, 1)
        lineSeries.append(13, 3)
        lineSeries.append(17, 6)
        lineSeries.append(18, 3)
        lineSeries.append(20, 2)
        '''
    return lineSeries

    # self.graphicsView.setRenderHint(QPainter.Antialiasing)

