import cv2
import numpy as np

windowName = 'Imagem'

def mouseClickCallback(event, x, y, flag, param):
    global color
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pX = y
        pY = x
        color = origImg[pX][pY]
        hlSimilarPxls()
        #print("R: ", img[pX][pY][2],"G: ", img[pX][pY][1],"B: ", img[pX][pY][0])

def hlSimilarPxls():

    max_dist = 20 
    B = origImg[:, :, 0].astype(np.float32)
    G = origImg[:, :, 1].astype(np.float32)
    R = origImg[:, :, 2].astype(np.float32)

    sq_dist = (B - color[0]) ** 2 + (G - color[1]) ** 2 + (R - color[2]) ** 2

    mask = sq_dist < (max_dist ** 2)

    dispImg = origImg.copy()
    dispImg[mask!=0] = (0, 0, 255)
    cv2.imshow(windowName, dispImg)
    cv2.waitKey()


def loadImg():
    global origImg, dispImg
    origImg = cv2.imread('foto.jpg',cv2.IMREAD_COLOR)
    dispImg = origImg.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName,mouseClickCallback)
    cv2.imshow(windowName, dispImg)
    cv2.waitKey()

def main():
    #print("Selecione opcao:")
    #print("1 - Escolha entrada")
    #print("2 - Escolha o modo")
    #Ler inputs
    loadImg()


if __name__  == "__main__":
    main()
