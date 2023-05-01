#import libraries

import pandas as pd
import matplotlib.pyplot as plt
import queue


#read data
df=pd.read_csv("SPY_2016_2021.csv")
long_SSMA = queue.Queue()
short_SSMA = queue.Queue()
long_EMA = queue.Queue()
short_EMA = queue.Queue()
print(df)

capital = 100,000
print("Input 1 for SSMA or 2 for EMA, or -1 to exit the program.")
INPUT_SSMAorEMA = input(print("Enter input: \n"))
while INPUT_SSMAorEMA != -1:
    if INPUT_SSMAorEMA == 1:
        def longSSMA(t,T,i):
            t=df[i]
            T = 26
            for i in range(0,len(df)+1):
                for t in df[t-T,t]:
                    longssma=df[t]+df[t-1]
                    longssma=longssma+df[t-1]
                    queue.put(longssma)
                    print(longssma)
