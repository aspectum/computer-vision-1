import cv2
import numpy as np
from os import path

windowName = 'Imagem'
flagVideo = 0
flagImagem = 0
flagGray = 0


def mouseClickCallback(event, x, y, flag, param):
    global color, flagVideo, dispFrame

    if event == cv2.EVENT_LBUTTONDOWN:
        flagVideo = 1
        pX = y
        pY = x
        color = frame[pX][pY]

        if flagImagem:
            dispFrame = frame.copy()
            hlSimilarPxls()
            cv2.imshow(windowName, dispFrame)
            
        print("------Pixel selecionado------")
        print("Linha: ", pX, ", Coluna: ", pY)
        if flagGray:
            print("Brilho: ", frame[pX][pY][0])
        else:
            print("R: ", frame[pX][pY][2],"G: ", frame[pX][pY][1],"B: ", frame[pX][pY][0])
        print("-----------------------------")
        print()


def hlSimilarPxls():
    global dispFrame

    colorDist = 13

    B = frame[:, :, 0].astype(np.int)
    G = frame[:, :, 1].astype(np.int)
    R = frame[:, :, 2].astype(np.int)

    sq_dist = (B - color[0]) ** 2 + (G - color[1]) ** 2 + (R - color[2]) ** 2
    mask = sq_dist < (colorDist ** 2)
    dispFrame[mask!=0] = (0, 0, 255)


def isGray():
    tolerance = 50

    B = frame[:, :, 0].astype(np.int)
    G = frame[:, :, 1].astype(np.int)
    R = frame[:, :, 2].astype(np.int)

    rg = abs(R - G)
    rb = abs(R - B)
    gb = abs(G - B)

    if max(np.amax(rg),np.amax(rb),np.amax(gb)) < tolerance:
        return True
    else:
        return False


def picture():
    global frame, dispFrame,flagGray

    frame = cv2.imread(source, cv2.IMREAD_ANYCOLOR)
    dispFrame = frame.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, mouseClickCallback)

    if isGray():
        flagGray = 1

    while cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) > 0:
        cv2.imshow(windowName, dispFrame)
        if cv2.waitKey(100) & 0xFF == ord('q'): 
            break


def video():
    global frame, dispFrame

    cap = cv2.VideoCapture(source)
    if (cap.isOpened()== False):  
        print("Error opening video file") 
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName,mouseClickCallback)
    
    while cap.isOpened():
        ret, frame = cap.read()
        dispFrame = frame.copy()
        if flagVideo:
            hlSimilarPxls()
        cv2.imshow(windowName, dispFrame)

        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break


def main():
    global source, flagImagem, basepath
    

    basepath = path.dirname(__file__)

    print("Selecione opcao:")
    print("1 - RGB do pixel")
    print("2 - Destaca cor imagem")
    print("3 - Destaca cor video")
    print("4 - Destaca cor webcam")
    op = input("Digite o numero da opcao: ")
    print()

    if op == '1':
        grayscale = input("Digite 1 para imagem em escala de cinza ou qualque coisa para imagem colorida: ")
        if grayscale == '1':
            filename = "foto_gray.jpg"
        else:
            filename = "foto.jpg"
        source = path.abspath(path.join(basepath, "..", "data", filename))
        picture()
    elif op == '2':
        grayscale = input("Digite 1 para imagem em escala de cinza ou qualque coisa para imagem colorida: ")
        if grayscale == '1':
            filename = "foto_gray.jpg"
        else:
            filename = "foto.jpg"
        source = path.abspath(path.join(basepath, "..", "data", filename))
        flagImagem = 1
        picture()
    elif op == '3':
        source = path.abspath(path.join(basepath, "..", "data", "video.mp4"))
        video()
    elif op == '4':
        source = 0
        video()
    else:
        print("Opcao errada")
    
    cv2.destroyAllWindows()


if __name__  == "__main__":
    main()
