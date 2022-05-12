import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/5cigarro/cigarro2.png'


class Cigarro2:

    def __init__(self, x, y):
        branco = 255

        fumaca_r = 220
        fumaca_g = 220
        fumaca_b = 220

        cigarro_r = 240
        cigarro_g = 220
        cigarro_b = 130

        cigarrodetalhe_r = 230
        cigarrodetalhe_g = 210
        cigarrodetalhe_b = 120

        braza_r = 255
        braza_g = 0
        braza_b = 0

        def geraPixels(matriz,
                       cigarro,
                       cigarrodetalhe,
                       fumaca,
                       braza):

            matriz[0:24, 0:60] = branco

            matriz[24, 0:4] = branco
            matriz[24, 4:6] = fumaca
            matriz[24, 6:60] = branco

            matriz[25, 0:5] = branco
            matriz[25, 5:7] = fumaca
            matriz[25, 7:60] = branco

            matriz[26, 0:6] = branco
            matriz[26, 6:8] = fumaca
            matriz[26, 8:60] = branco

            matriz[27, 0:60] = branco

            matriz[28, 0:7] = branco
            matriz[28, 7:9] = fumaca
            matriz[28, 9:60] = branco

            matriz[29, 0:8] = branco
            matriz[29, 8:10] = fumaca
            matriz[29, 10:18] = branco
            matriz[29, 18:21] = cigarro
            matriz[29, 21:60] = branco

            matriz[30, 0:17] = branco
            matriz[30, 17:19] = cigarro
            matriz[30, 19:20] = cigarrodetalhe
            matriz[30, 20:60] = branco

            matriz[31, 0:10] = branco
            matriz[31, 10:12] = fumaca
            matriz[31, 12:16] = branco
            matriz[31, 16:17] = cigarrodetalhe
            matriz[31, 17:18] = cigarro
            matriz[31, 18:19] = cigarrodetalhe
            matriz[31, 19:60] = branco

            matriz[32, 0:15] = branco
            matriz[32, 15:16] = cigarrodetalhe
            matriz[32, 16:18] = cigarro
            matriz[32, 18:60] = branco

            matriz[33, 0:11] = branco
            matriz[33, 11:13] = fumaca
            matriz[33, 13:14] = branco
            matriz[33, 14:16] = cigarro
            matriz[33, 16:17] = cigarrodetalhe
            matriz[33, 17:60] = branco

            matriz[34, 0:14] = branco
            matriz[34, 14:15] = braza
            matriz[34, 15:16] = cigarro
            matriz[34, 16:60] = branco

            matriz[35:50, 0:60] = branco

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       cigarro_r,
                       cigarrodetalhe_r,
                       fumaca_r,
                       braza_r)

        g = geraPixels(g,
                       cigarro_g,
                       cigarrodetalhe_g,
                       fumaca_g,
                       braza_g
                       )

        b = geraPixels(b,
                       cigarro_b,
                       cigarrodetalhe_b,
                       fumaca_b,
                       braza_b
                       )


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b


        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches = 0)

        # plt.show()


# base = Cigarro2(5, 4)
