import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

pasta = 'imgs_geradas/4oculos/oculos2.png'

class oculos2:

    def __init__(self, x, y):
        branco = 255

        oculos_r = 60
        oculos_g = 60
        oculos_b = 60

        oculosclaro_r = 80
        oculosclaro_g = 80
        oculosclaro_b = 80

        armacao_r = 105
        armacao_g = 105
        armacao_b = 105

        def geraPixels(matriz,
                       oculos,
                       oculosclaro,
                       armacao):

            matriz[0:15, 0:60] = branco

            matriz[15, 0:13] = branco
            matriz[15, 13:15] = oculosclaro
            matriz[15, 15:17] = oculos
            matriz[15, 17:20] = branco
            matriz[15, 20:22] = oculosclaro
            matriz[15, 22:24] = oculos
            matriz[15, 24:60] = branco

            matriz[16, 0:12] = branco
            matriz[16, 12:13] = oculosclaro
            matriz[16, 13:18] = oculos
            matriz[16, 18:19] = branco
            matriz[16, 19:20] = oculosclaro
            matriz[16, 20:25] = oculos
            matriz[16, 25:60] = branco

            matriz[17, 0:12] = branco
            matriz[17, 12:13] = oculos
            matriz[17, 13:14] = oculosclaro
            matriz[17, 14:18] = oculos
            matriz[17, 18:19] = armacao
            matriz[17, 19:20] = oculos
            matriz[17, 20:21] = oculosclaro
            matriz[17, 21:25] = oculos
            matriz[17, 25:60] = branco

            matriz[18, 0:12] = branco
            matriz[18, 12:13] = oculos
            matriz[18, 13:15] = oculosclaro
            matriz[18, 15:18] = oculos
            matriz[18, 18:19] = armacao
            matriz[18, 19:20] = oculos
            matriz[18, 20:22] = oculosclaro
            matriz[18, 22:25] = oculos
            matriz[18, 25:60] = branco

            matriz[19, 0:12] = branco
            matriz[19, 12:13] = oculos
            matriz[19, 13:16] = oculosclaro
            matriz[19, 16:18] = oculos
            matriz[19, 18:19] = branco
            matriz[19, 19:20] = oculos
            matriz[19, 20:23] = oculosclaro
            matriz[19, 23:25] = oculos
            matriz[19, 25:60] = branco

            matriz[20, 0:13] = branco
            matriz[20, 13:17] = oculos
            matriz[20, 17:20] = branco
            matriz[20, 20:24] = oculos
            matriz[20, 24:60] = branco

            matriz[21:50, 0:60] = branco


            return matriz


        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       oculos_r,
                       oculosclaro_r,
                       armacao_r)

        g = geraPixels(g,
                       oculos_g,
                       oculosclaro_g,
                       armacao_g)

        b = geraPixels(b,
                       oculos_b,
                       oculosclaro_b,
                       armacao_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)

        # plt.show()

# oculos = oculos2(5, 4)