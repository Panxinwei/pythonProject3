#N值
import numpy as np
import pandas as pd

#    ma=5
#    zhishu=0.1
    # 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
#    FM(ma,input_data)

def WMA(ma,input_data):
    weights=np.array(range(1,len(input_data['ResultValue'])+1))
   # print(len(input_data['ResultValue']))
    sum_weights=np.sum(weights)
    input_data['WMA_' + str(ma)] = input_data['ResultValue'].rolling(ma).mean()

    ListWMA = input_data['ResultValue'].rolling(ma).apply(lambda x: x[::-1].cumsum().sum() *2 / ma /(ma+1))

    arrWMA = np.array(ListWMA)
    print(arrWMA)
    return arrWMA


def FM(ma,input_data):
    ListFM = input_data['ResultValue'].rolling(ma).median().values
    arrFM = np.array(ListFM)
    print(arrFM)
    return arrFM

def MA(ma,input_data):
    #MA 算法
   # for ma in malist:

      #  input_data['MA_' + str(ma)] = input_data['ResultValue'].rolling(ma).mean()
        ListMA= input_data['ResultValue'].rolling(ma).mean().values
        arrMA=np.array(ListMA)
        print(arrMA)
        return arrMA


def EWMA(ma,zhishu,input_data):
    #EWMA  算法
   # for ma in malist:
       ## input_data['EMA_' + str(ma)] =input_data['ResultValue'].ewm(span=ma, min_periods=ma).mean()
       #adjust false为Infinity的算法
    arrresult = input_data['ResultValue'].array
    ListEwma2 = []
    #print(arrresult)
    for i in range (ma-1, len(input_data)):

        arr_new=arrresult[i-ma+1:i+1]
        df=pd.DataFrame({'EWMA':arr_new})
         #   print(arr_new)
        TrueEwma=df.ewm(alpha=zhishu, adjust=False,min_periods=ma).mean()
        assert isinstance(TrueEwma, object)
        df2=pd.DataFrame(TrueEwma)
        ListEwma=df2.values.tolist()[ma-1]
      #  ListEwma2=[]

        ListEwma3 = []

        for j in range(0,len(ListEwma)):
          #  ListEwma2[j]=ListEwma[j]
            ListEwma2.append(ListEwma[j])


        #ListEwma3=list(arrewma)
    for k in range(0,ma-1):
        ListEwma2.insert(k,'')
    arrewma=np.array(ListEwma2)
    #print(ListEwma2)
    print(arrewma)
    return arrewma

        #for k in range(0, len(arrewma)):
        #  #  ListEwma2[j]=ListEwma[j]
        #    ListEwma3.append(arrewma[k])

        #print(arrewma)
        #arrewma = np.array(ListEwma2[0])

      #  ListEwma3=arrewma.tolist()


       # for k in range(0,ma-1):

       #     np.insert(arrewma, k,111)
       # print(arrewma)

          #  print(ListEwma2)
        #    for k in range(0,ma-1):
         #       ListEwma2.insert(k,'')
          #  ListEwma2.append(ListEwma.__dict__.get(ma-1))
     #   print(ListEwma2)
           # input_data['EMA_']
         #   print(arr_new)
        #input_data['EMA_' + str(ma)] = input_data['ResultValue'].ewm(alpha=zhishu, adjust=False,min_periods=ma).mean()
        #input_data['EMA_' + str(ma)] =  df3
    # ========== 将算好的数据输出到csv文件 - 注意：这里请填写输出文件在您电脑中的路径，这里用gbk编码方便用Excel打开展示，实际csv建议输出utf-8格式

 #   input_data.to_csv(r'D:\Users\Killua\PycharmProjects\pythonProject1\sz300001_ma.csv', encoding='gbk', index=False)