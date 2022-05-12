import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/4oculos/tapaolho.png'


class TapaOlho:

    def __init__(self, x, y):
        branco = 255

        tapaolho_r = 30
        tapaolho_g = 30
        tapaolho_b = 30

        tapaolho2_r = 40
        tapaolho2_g = 40
        tapaolho2_b = 40

        def geraPixels(matriz,
                       tapaolho,
                       tapaolho2):

            matriz[0:12, 0:60] = branco

            matriz[12, 0:20] = branco
            matriz[12, 20:21] = tapaolho
            matriz[12, 21:60] = branco

            matriz[13, 0:19] = branco
            matriz[13, 19:20] = tapaolho
            matriz[13, 20:60] = branco

            matriz[14, 0:18] = branco
            matriz[14, 18:19] = tapaolho
            matriz[14, 19:60] = branco

            matriz[15, 0:14] = branco
            matriz[15, 14:16] = tapaolho
            matriz[15, 16:17] = branco
            matriz[15, 17:18] = tapaolho
            matriz[15, 18:60] = branco

            matriz[16, 0:13] = branco
            matriz[16, 13:17] = tapaolho
            matriz[16, 17:60] = branco

            matriz[17, 0:12] = branco
            matriz[17, 12:13] = tapaolho
            matriz[17, 13:14] = tapaolho2
            matriz[17, 14:18] = tapaolho
            matriz[17, 18:60] = branco

            matriz[18, 0:12] = branco
            matriz[18, 12:13] = tapaolho
            matriz[18, 13:14] = tapaolho2
            matriz[18, 14:18] = tapaolho
            matriz[18, 18:60] = branco

            matriz[19, 0:13] = branco
            matriz[19, 13:14] = tapaolho
            matriz[19, 14:15] = tapaolho2
            matriz[19, 15:17] = tapaolho
            matriz[19, 17:60] = branco

            matriz[20, 0:12] = branco
            matriz[20, 12:13] = tapaolho
            matriz[20, 13:14] = branco
            matriz[20, 14:16] = tapaolho
            matriz[20, 16:60] = branco

            matriz[21:50, 0:60] = branco

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       tapaolho_r,
                       tapaolho2_r)

        g = geraPixels(g,
                       tapaolho_g,
                       tapaolho2_g)

        b = geraPixels(b,
                       tapaolho_b,
                       tapaolho2_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches = 0)

        # plt.show()


# base = TapaOlho(5,4)