import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/1fundo/fundo2.png'


class Fundo2:

    def __init__(self, x, y):
        branco = 255

        fundo_r = 176
        fundo_g = 224
        fundo_b = 230

        fundoescuro_r = 156
        fundoescuro_g = 204
        fundoescuro_b = 210

        def geraPixels(matriz,
                       fundo,
                       fundoescuro):
            matriz[0:50, 0:60] = fundo
            matriz[42:50, 0:60] = fundoescuro

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       fundo_r,
                       fundoescuro_r)

        g = geraPixels(g,
                       fundo_g,
                       fundoescuro_g)

        b = geraPixels(b,
                       fundo_b,
                       fundoescuro_b)

        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        img = plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)
        # plt.show()


# fundo = fundo2()
