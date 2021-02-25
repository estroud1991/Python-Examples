import cv2
import numpy as np


def calculateCorner(image):
    
    rows = len(image)
    columns = len(image[0])
    corners = np.zeros((rows, columns), np.float32)
    Ixx = np.zeros((rows, columns), np.float32)
    Iyy = np.zeros((rows, columns), np.float32)
    Ixy = np.zeros((rows, columns), np.float32)
    xGradient = np.zeros((rows, columns), np.float32)
    yGradient = np.zeros((rows, columns), np.float32)
    minimum = 0
    maximum = 0

    for i in range(rows):
        for j in range(columns):
            #Verifying boundaries
            if i-1 > 0 and j-1 > 0 and i+1 < rows and j+1 < columns:
                #Creating gradient matrices
                xGradient[i][j] = float(image[i+1][j]) - float(image[i-1][j])
                yGradient[i][j] = float(image[i][j+1]) - float(image[i][j-1])
                Ixx[i][j] = xGradient[i][j] ** 2
                Iyy[i][j] = yGradient[i][j] ** 2
                Ixy[i][j] = xGradient[i][j] * yGradient[i][j]

    #summing up Ixx, Iyy, Ixy
    for i in range(rows):
        for j in range(columns):
            sumIxx = 0
            sumIyy = 0
            sumIxy = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    try:
                        if (i + k) < 0 or (j + l) < 0:
                            raise IndexError

                        sumIxx = sumIxx + Ixx[i + k][j + l]
                        sumIyy = sumIyy + Iyy[i + k][j + l]
                        sumIxy = sumIxy + Ixy[i + k][j + l]
                    except IndexError:
                        continue

            corners[i][j] = ((sumIxx * sumIyy) - (sumIxy ** 2)) - (0.05 * (sumIxx + sumIxy))

            #getting the max and min corners
            if corners[i][j] > maximum:
                maximum = corners[i][j]

            if corners[i][j] < minimum:
                minimuim = corners[i][j]

    return corners, minimum, maximum
    


def drawCorners(image, cornernessMatrix, minimum, maximum, switch):

    #Percent
    if switch == 1:
        print("Drawing corners above a certain minimum")
        rows = len(cornernessMatrix)
        columns = len(cornernessMatrix[0])
        percent = float(input("Enter Percent (ie. .5 being 50%) for Top Percentile: "))
        limit = percent * (maximum - minimum) + minimum
        for i in range(rows):
            for j in range(columns):
                if cornernessMatrix[i][j] >= limit:
                    cv2.circle(image, (j, i), 3, (100, 0, 100), -1)
        cv2.imwrite("topPercent.jpg", image)
        return image

    #Neighborhood
    if switch == 2:
        print("\nDrawing number of corners within a neighborhood")
        rows = len(cornernessMatrix)
        columns = len(cornernessMatrix[0])
        number = int(input("Enter number of corners within neighborhood: "))
        neighborhoodSize = int(input("Enter neighborhood size: "))

        indexedCorners = []
        count = 0
        row = 0
        column = 0
        
        while row <= rows:
            while column <= columns:
                for i in range(neighborhoodSize):
                    for j in range(neighborhoodSize):
                        
                        #Exception handling since there is a good chance boundary will be broken
                        try:
                            if count < number:
                                indexedCorners.append([cornernessMatrix[i + row][j + column], i + row, j + column])
                                count += 1
                                if count == number:
                                    minimum = min(indexedCorners)
                            else:
                                if cornernessMatrix[i + row][j + column] > minimum[0]:
                                    minimumCorner = indexedCorners.index(min(indexedCorners))
                                    indexedCorners[minimumCorner] = [cornernessMatrix[i + row][j + column], i + row, j + column]
                                    minimum = min(indexedCorners)
                        except IndexError:
                            pass

                for i in range(len(indexedCorners)):
                    cv2.circle(image, (indexedCorners[i][2], indexedCorners[i][1]), 3, (100, 0, 100), -1)

                #Reset
                indexedCorners = []
                count = 0

                #shifting over to next neighborhood
                column += neighborhoodSize

            #Reset
            indexedCorners = []
            count = 0
            column = 0

            #shifting over to next neighborhood
            row += neighborhoodSize
            
        cv2.imwrite("topNeighbor.jpg", image)
        return image



#Initialization
filename = "cat.jpg"
image = cv2.imread(filename)
grayImage = cv2.imread(filename, 0)
cornernessMatrix, minCornerness, maxCornerness = calculateCorner(grayImage)

#Calculating and displaying corners
colorCopy1 = image
colorCopy2 = image
cv2.imshow("Top Percent", drawCorners(colorCopy1, cornernessMatrix, minCornerness, maxCornerness, 1))
cv2.imshow("Top Number In Neighborhood", drawCorners(colorCopy2, cornernessMatrix, minCornerness, maxCornerness, 2))


cv2.waitKey(0)
cv2.destroyAllWindows()
