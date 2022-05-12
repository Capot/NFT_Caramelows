import numpy as np
import cv2
import os


class Suavizacao():

    def __init__(self):

        pasta7 = "imgs_geradas/7chapeu"
        dir7 = os.listdir(pasta7)

        for arquivos7 in dir7:
            img = cv2.imread(pasta7 + "/" + arquivos7)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta7 + "/" + arquivos7, suave)

        ########################################################################

        pasta1 = "imgs_geradas/1fundo"
        dir1 = os.listdir(pasta1)

        for arquivos1 in dir1:
            img = cv2.imread(pasta1 + "/" + arquivos1)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta1 + "/" + arquivos1, suave)

        ########################################################################

        pasta2 = "imgs_geradas/2imgBase"
        dir2 = os.listdir(pasta2)

        for arquivos2 in dir2:
            img = cv2.imread(pasta2 + "/" + arquivos2)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta2 + "/" + arquivos2, suave)

        ########################################################################

        pasta3 = "imgs_geradas/3coleira"
        dir3 = os.listdir(pasta3)

        for arquivos3 in dir3:
            img = cv2.imread(pasta3 + "/" + arquivos3)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta3 + "/" + arquivos3, suave)

        ########################################################################

        pasta4 = "imgs_geradas/4oculos"
        dir4 = os.listdir(pasta4)

        for arquivos4 in dir4:
            img = cv2.imread(pasta4 + "/" + arquivos4)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])

        #########################################################################

        pasta5 = "imgs_geradas/5cigarro"
        dir5 = os.listdir(pasta5)

        for arquivos5 in dir5:
            img = cv2.imread(pasta5 + "/" + arquivos5)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta5 + "/" + arquivos5, suave)

        ##########################################################################

        pasta6 = "imgs_geradas/6roupa"
        dir6 = os.listdir(pasta6)

        for arquivos6 in dir6:
            img = cv2.imread(pasta6 + "/" + arquivos6)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta6 + "/" + arquivos6, suave)

        ###########################################################################

        pasta8 = "imgs_geradas/8brinquedos"
        dir8 = os.listdir(pasta8)

        for arquivos8 in dir8:
            img = cv2.imread(pasta8 + "/" + arquivos8)
            suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
                               ])
            cv2.imwrite(pasta8 + "/" + arquivos8, suave)


# img = cv2.imread('imgs_geradas/2imgBase/caramelow.png')
# suave = np.vstack([np.hstack([cv2.medianBlur(img, 3)]),
# # np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
# # np.hstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)]),
# ])
# cv2.imshow("Imagem original e suavisadas pela mediana", suave)
# cv2.waitKey(0)

# suav = suavizacao()