import cv2
import numpy as np

def matrixMult(a, b):
        output = np.zeros((len(a), len(b[0])), np.float32)
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    output[i][j] += int(a[i][k] * b[k][j])
        return output
    
                   
def getRotationMat(degree):
    #Generates a rotation matrix
    degree = np.deg2rad(degree)
    rotMatrix = [[np.cos(degree), -(np.sin(degree))], [np.sin(degree), np.cos(degree)]]
    
    return rotMatrix

def rotateImage(degree, rImage):
        dispError = 0
        rotMatrix = getRotationMat(degree)
        rows = len(rImage)
        cols = rImage.shape[0]
        rotatedMat = np.zeros((rows, cols, 3), np.float32)

        for i in range(cols):
                for j in range(rows):

                        #creating pixel to be rotated
                        pixelMat = [[i - cols //2], [j - rows //2]]
                        #rotating pixel
                        newPixel = matrixMult(rotMatrix, pixelMat)

                        #determine the new x and y locations
                        newX = int(newPixel[0][0] + cols // 2)
                        newY = int(newPixel[1][0] + rows // 2)
                        
                        dispErrorAmount = np.sqrt(((newX - i) ** 2) + ((newY - j) ** 2))
                        dispError = dispError + dispErrorAmount

                        #Will only copy a pixel if it is within the range of the rotated image values and its origin
                        if (newX > 0 and newX < cols) and (newY > 0 and newY < rows):
                            rotatedMat[i][j] = rImage[newX][newY]
                            
        return rotatedMat, dispError

def borderedImage(image, removeBorder):

        #Will add the black border if removeBorder is 0
        if removeBorder == 0:
            newSize = int(max(image.shape[0], image.shape[1]) * 3 / 2)
            newImage = np.zeros((newSize, newSize, 3), np.float32)
            newRows = len(newImage)
            newCols = len(newImage[0])
            center = np.zeros((newRows, newCols, 3), np.float32)
            #Create a translation matrix to move image before rotating around new origin
            trans = np.float32([[1, 0, (newCols/2) - (image.shape[1] /2)],[0, 1, (newRows/2) - (image.shape[0]/2)]])
            
            for i in range(image.shape[1]):
                    for j in range(image.shape[0]):
                            newImage[i][j] = image[i][j]
                            pixelMatrix = [[i],[j],[1]]
                            newPixel = matrixMult(trans, pixelMatrix)
                            newX = int(round(newPixel[0][0]))
                            newY = int(round(newPixel[1][0]))
                            center[newX][newY] = image[i][j]
            return center

        #This will remove the border if removeBorder is 1
        if removeBorder == 1:
            
            #Reading image back in to remove the border
            origImage = cv2.imread("cat.png")
            rotImageRows = len(image)
            rotImageCols = len(image[0])
            origImageRows = len(origImage)
            origImageCols = len(origImage[0])

            borderlessTranslated = np.zeros((rotImageRows, rotImageCols, 3), np.float32)

            #Moves image back to origin to remove the border
            trans = np.float32([[1, 0, (rotImageCols / 2) - (origImageCols / 2)], [0, 1, (rotImageRows / 2) - (origImageRows / 2)]])

            borderlessFinal = np.zeros((origImageRows, origImageCols, 3), np.float32)

            for i in range(rotImageCols):
                for j in range(rotImageRows):
                    pixelMatrix = [[i],[j],[1]]
                    newPixel = matrixMult(trans, pixelMatrix)
                    newX = int(newPixel[0][0])
                    newY = int(newPixel[1][0])
                    #Only will copy pixel if it is within the image
                    if (newX > 0 and newX < rotImageCols) and (newY > 0 and newY < rotImageRows):
                        borderlessTranslated[i][j] = rotImage[newX][newY]
            #Copies it to the borderless image
            for i in range(origImageCols):
                for j in range(origImageRows):
                    borderlessFinal[i][j] = borderlessTranslated[i][j]
            return borderlessFinal
                        

def calcDisplacementError(rotImage, rotIterations, totDisp):
    pixelCount = len(rotImage) * len(rotImage[0])
    pixelDisp = totDisp / (pixelCount * rotIterations)
    return pixelDisp


#Getting first image ready    
image = cv2.imread("cat.png")
numRows = image.shape[0]
numCols = image.shape[1]

centerImage = borderedImage(image, 0)
            
cv2.imshow("Showing loaded image", centerImage/255.0)
degree = int(input("Please enter your starting degree increment: "))

#copying image before rotation and getting iterations needed
oldImage = centerImage
rotIterations = 360//degree
totalDisplacement = 0

#Rotating image
for i in range(rotIterations):
        print("Running through iteration " + str(i+1))
        rotImage, rotImageDisplacement = rotateImage(degree, oldImage)
        totalDisplacement = totalDisplacement + rotImageDisplacement
        cv2.imshow("Showing rotation step " + str(i), rotImage/255.0)
        oldImage = rotImage
        cv2.imwrite(str(degree) + " savedImage " + str(i+1) + ".png", rotImage)

print("Rotations done, removing border and calculating error rates")
colorError = 0
numPix = numRows * numCols

#Removing the black border
rotImageNoBorder = borderedImage(rotImage, 1)

#Iterating over image to determine colorError
for i in range(numCols):
    for j in range(numRows):
        for k in range(3):
            colorError = colorError + abs(rotImageNoBorder[i][j][k] - image[i][j][k])

print("Absolute Color Error: " + str(colorError/(3*numPix)))
numPix = len(rotImage) * len(rotImage[0])
print("Pixel Displacement: " + str(calcDisplacementError(rotImage, rotIterations, totalDisplacement)/1000))
print("Rotations * Pixel Displacement: " + str(rotIterations * (calcDisplacementError(rotImage, rotIterations, totalDisplacement)/1000)))
cv2.imshow("Displaying final image rotation", rotImageNoBorder/255.0)


cv2.imwrite(str(degree) + " FinalImage.png", rotImageNoBorder)
print("Image Saved")

cv2.waitKey(0)
cv2.destroyAllWindows()


