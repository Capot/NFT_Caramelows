import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/5cigarro/cachimbo1.png'


class Cachimbo1:

    def __init__(self, x, y):
        branco = 255

        fumaca_r = 220
        fumaca_g = 220
        fumaca_b = 220

        cachimbo_r = 204
        cachimbo_g = 119
        cachimbo_b = 34

        cachimbodetalhe_r = 40
        cachimbodetalhe_g = 40
        cachimbodetalhe_b = 40

        def geraPixels(matriz,
                       fumaca,
                       cachimbo,
                       cachimbodetalhe):

            matriz[0:13, 0:60] = branco

            matriz[13, 0:1] = branco
            matriz[13, 1:2] = fumaca
            matriz[13, 2:60] = branco

            matriz[14, 0:1] = branco
            matriz[14, 1:2] = fumaca
            matriz[14, 2:60] = branco

            matriz[15, 0:60] = branco

            matriz[16, 0:2] = branco
            matriz[16, 2:4] = fumaca
            matriz[16, 4:60] = branco

            matriz[17, 0:3] = branco
            matriz[17, 3:4] = fumaca
            matriz[17, 4:60] = branco

            matriz[18, 0:60] = branco

            matriz[19, 0:4] = branco
            matriz[19, 4:5] = fumaca
            matriz[19, 5:60] = branco

            matriz[20, 0:4] = branco
            matriz[20, 4:6] = fumaca
            matriz[20, 6:60] = branco

            matriz[21, 0:6] = branco
            matriz[21, 6:8] = fumaca
            matriz[21, 8:60] = branco

            matriz[22, 0:60] = branco

            matriz[23, 0:8] = branco
            matriz[23, 8:10] = fumaca
            matriz[23, 10:60] = branco

            matriz[24, 0:8] = branco
            matriz[24, 8:11] = fumaca
            matriz[24, 11:60] = branco

            matriz[25, 0:9] = branco
            matriz[25, 9:11] = fumaca
            matriz[25, 11:60] = branco

            matriz[26, 0:10] = branco
            matriz[26, 10:12] = fumaca
            matriz[26, 12:60] = branco

            matriz[27, 0:10] = branco
            matriz[27, 10:12] = fumaca
            matriz[27, 12:60] = branco

            matriz[28, 0:9] = branco
            matriz[28, 9:13] = cachimbo
            matriz[28, 13:60] = branco

            matriz[29, 0:9] = branco
            matriz[29, 9:13] = cachimbo
            matriz[29, 13:18] = branco
            matriz[29, 18:21] = cachimbodetalhe
            matriz[29, 21:60] = branco

        ######################################################

            matriz[30, 0:10] = branco
            matriz[30, 10:14] = cachimbo
            matriz[30, 14:17] = branco
            matriz[30, 17:20] = cachimbodetalhe
            matriz[30, 20:60] = branco
        ###############################################################

            matriz[31, 0:11] = branco
            matriz[31, 11:19] = cachimbodetalhe
            matriz[31, 19:60] = branco

            matriz[32, 0:12] = branco
            matriz[32, 12:18] = cachimbodetalhe
            matriz[32, 18:60] = branco

            matriz[33:50, 0:60] = branco

            return matriz


        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       fumaca_r,
                       cachimbo_r,
                       cachimbodetalhe_r)

        g = geraPixels(g,
                       fumaca_g,
                       cachimbo_g,
                       cachimbodetalhe_g)

        b = geraPixels(b,
                       fumaca_b,
                       cachimbo_b,
                       cachimbodetalhe_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches = 0)

        # plt.show()


# cachimbo = Cachimbo1(5,4)