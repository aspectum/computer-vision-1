import cv2
import numpy as np

windowName = 'Imagem'
freg = 0
def mouseClickCallback(event, x, y, flag, param):
    global color, freg, frame
    if event == cv2.EVENT_LBUTTONDBLCLK:
        freg = 1
        pX = y
        pY = x
        color = frame[pX][pY]
        #hlSimilarPxls()
        #print("R: ", img[pX][pY][2],"G: ", img[pX][pY][1],"B: ", img[pX][pY][0])

def hlSimilarPxls():
    global frame, dispFrame

    max_dist = 20

    B = frame[:, :, 0].astype(np.float32)
    G = frame[:, :, 1].astype(np.float32)
    R = frame[:, :, 2].astype(np.float32)

    sq_dist = (B - color[0]) ** 2 + (G - color[1]) ** 2 + (R - color[2]) ** 2

    mask = sq_dist < (max_dist ** 2)

    dispFrame[mask!=0] = (0, 0, 255)




def main():
    global dispFrame, frame
    #print("Selecione opcao:")
    #print("1 - Escolha entrada")
    #print("2 - Escolha o modo")
    #Ler inputs
    origImg = cv2.VideoCapture('video.mp4')
    if (origImg.isOpened()== False):  
        print("Error opening video  file") 
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName,mouseClickCallback)
    while origImg.isOpened():
        ret, frame = origImg.read()
        dispFrame = frame.copy()
        if freg:
            hlSimilarPxls()
        cv2.imshow(windowName, dispFrame)
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break




if __name__  == "__main__":
    main()
