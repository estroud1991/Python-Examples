import math
import numpy as np

sigma = float(input("Please enter your sigma/variance: "))
size = int(input("Please enter the size of the guassian filter, must be odd: "))
decPlaces = int(input("Decimal places to round to for final value: "))

x = int((size-1)/2)
valueList = []

for i in range(-x,x+1,1):
    for j in range(-x,x+1,1):
        value = (1/(2*math.pi*(sigma**2)))*(math.exp(-(((i**2)+(j**2))/(2*(sigma**2)))))
        valueList.append(value)
        
scaler = valueList[0]
for i in range(len(valueList)):
        valueList[i]= round(valueList[i]*(1/scaler), decPlaces)

filterMat = np.zeros([size,size],dtype = float)
index = 0
for i in range(size):
    for j in range(size):
            filterMat[i][j] = valueList[index]
            index+=1

print(filterMat)
