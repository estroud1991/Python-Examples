import math
import numpy as np
import cv2

def generateGuass(): 
    sigma = float(input("Please enter your sigma/variance: "))
    size = int(input("Please enter the size of the guassian filter, must be odd: "))

    
    x = int((size-1)/2)
    valueList = []

    for i in range(-x,x+1,1):
        for j in range(-x,x+1,1):

            #using formula to calulate value for filter
            value = (1/(2*math.pi*(sigma**2)))*(math.exp(-(((i**2)+(j**2))/(2*(sigma**2)))))
            valueList.append(value)
            
    scaler = valueList[0]
   
    filterMat = np.zeros([size,size, 3],dtype = float)
    index = 0
    for i in range(size):
        for j in range(size):
                filterMat[i][j] = valueList[index], valueList[index], valueList[index]
                index+=1

    return filterMat

def applyFilter(image, filterMat):
    padding = (len(filterMat)-1)//2
    iRow = len(image)
    iCol =  len(image[0])
    #Adds border that is equal to the padding in order to get the corner pixels to correct values
    image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_REPLICATE)
    processedImage = np.zeros((iRow, iCol), dtype="float32")

    for i in range(padding, iRow+padding):
        for j in range(padding, iCol+padding):
            #Getting portion of image for convolution, summing the multiplied values, setting new image values
            iBlock = image[i - padding:i + padding + 1, j - padding: j + padding + 1]
            iSum =  (iBlock * filterMat).sum()
            processedImage[i - padding, j - padding] = iSum

    return processedImage

image = cv2.imread("cat.png")
cv2.imshow("orig",image/255.0)

for i in range(3):

    filterMat = generateGuass()
    newImage = applyFilter(image, filterMat)
    cv2.imshow("New" + str(i), newImage/255.0)

