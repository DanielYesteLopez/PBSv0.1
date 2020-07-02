import pandas as pd
import xlrd
import numpy as np
import math


# Recta de regresion de 144 filas de Close
# Recta de regresion de 144 filas de High
# Recta de regresion de 144 de Low
def hvcCalculation(df):
    # xt=ln(Pt/Pt-1)->pt is close price on day t
    # xC = 1/n sum(xt)
    # Hvc= sqrt((sum(xt-xC)^2)/n-1))
    # Date Open High Low Close Adj Close Volume
    closePrice = df["Close"]
    xtValues = []
    for i in range(1, closePrice.shape[0]):
        xtValues.append(math.log(closePrice.iloc[i] / closePrice.iloc[i - 1]))
    xC = sum(xtValues) / closePrice.shape[0] - 1
    valuesForhcv = 0
    for i in range(0, (closePrice.shape[0] - 1)):
        valuesForhcv = + math.pow((xtValues[i] - xC), 2)
    hcv = math.sqrt(valuesForhcv / (closePrice.shape[0] - 1))
    print("Hcv:\n",hcv)

def linearRegression(df):
    print("linearRegression")

if __name__ == "__main__":
    df = pd.read_excel('/home/danielyeste/Desktop/PBS/EURUSD_X.xlsx')
    hvcCalculation(df)
    linearRegression(df)
