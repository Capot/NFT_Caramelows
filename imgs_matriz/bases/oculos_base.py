import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# pasta = 'imgs_geradas/4oculos/oculos1.png'

class oculos:

    def __init__(self):
        branco = 255

        contorno_r = 139
        contorno_g = 69
        contorno_b = 19

        amarelo_r = 204
        amarelo_g = 119
        amarelo_b = 34

        amareloqueimado_r = 218
        amareloqueimado_g = 165
        amareloqueimado_b = 32

        sombrancelha_r = 237
        sombrancelha_g = 145
        sombrancelha_b = 33

        olho1_r = 224
        olho2_r = 210

        olho1_g = 225
        olho2_g = 105

        olho1_b = 225
        olho2_b = 30

        nariz_r = 0
        nariz_g = 0
        nariz_b = 0

        vermelho_r = 255
        vermelho_g = 0
        vermelho_b = 0

        sombra_r = 128
        sombra_g = 128
        sombra_b = 128

        sombraclara_r = 211
        sombraclara_g = 211
        sombraclara_b = 211

        oculos_r = 0
        oculos_g = 71
        oculos_b = 171

        oculosclaro_r = 135
        oculosclaro_g = 206
        oculosclaro_b = 235

        armacao_r = 105
        armacao_g = 105
        armacao_b = 105

        def geraPixels(matriz,
                       contorno,
                       amarelo,
                       amareloqueimado,
                       sombrancelha,
                       olho1,
                       olho2,
                       nariz,
                       vermelho,
                       sombra,
                       sombraclara,
                       oculos,
                       oculosclaro,
                       armacao):

            matriz[0:11, 0:60] = branco

            matriz[11, 0:14] = branco
            matriz[11, 14:21] = contorno
            matriz[11, 21:60] = branco

            matriz[12, 0:13] = branco
            matriz[12, 13:14] = contorno
            matriz[12, 14:21] = amarelo
            matriz[12, 21:22] = contorno
            matriz[12, 22:60] = branco

            matriz[13, 0:12] = branco
            matriz[13, 12:13] = contorno
            matriz[13, 13:22] = amarelo
            matriz[13, 22:23] = contorno
            matriz[13, 23:60] = branco

            matriz[14, 0:11] = branco
            matriz[14, 11:12] = contorno
            matriz[14, 12:23] = amarelo
            matriz[14, 23:24] = contorno
            matriz[14, 24:60] = branco

            matriz[15, 0:10] = branco
            matriz[15, 10:12] = contorno
            matriz[15, 12:13] = amarelo
            matriz[15, 13:17] = sombrancelha
            matriz[15, 17:19] = amarelo
            matriz[15, 19:23] = sombrancelha
            matriz[15, 23:24] = amarelo
            matriz[15, 24:26] = contorno
            matriz[15, 26:60] = branco

####
            matriz[15, 13:15] = oculosclaro
            matriz[15, 15:17] = oculos
            matriz[15, 20:22] = oculosclaro
            matriz[15, 22:24] = oculos

            matriz[16, 0:9] = branco
            matriz[16, 9:10] = contorno
            matriz[16, 10:11] = amarelo
            matriz[16, 11:12] = contorno
            matriz[16, 12:24] = amarelo
            matriz[16, 24:25] = contorno
            matriz[16, 25:26] = amarelo
            matriz[16, 26:27] = contorno
            matriz[16, 27:60] = branco

###
            matriz[16, 12:13] = oculosclaro
            matriz[16, 13:18] = oculos
            matriz[16, 19:20] = oculosclaro
            matriz[16, 20:25] = oculos

            matriz[17, 0:8] = branco
            matriz[17, 8:9] = contorno
            matriz[17, 9:11] = amarelo
            matriz[17, 11:12] = contorno
            matriz[17, 12:13] = amarelo
            matriz[17, 13:15] = olho1
            matriz[17, 15:17] = olho2
            matriz[17, 17:19] = amarelo
            matriz[17, 19:21] = olho1
            matriz[17, 21:23] = olho2
            matriz[17, 23:24] = amarelo
            matriz[17, 24:25] = contorno
            matriz[17, 25:26] = amareloqueimado
            matriz[17, 26:27] = amarelo
            matriz[17, 27:28] = contorno
            matriz[17, 28:60] = branco

###
            matriz[17, 12:13] = oculos
            matriz[17, 13:14] = oculosclaro
            matriz[17, 14:18] = oculos
            matriz[17, 18:19] = armacao
            matriz[17, 19:20] = oculos
            matriz[17, 20:21] = oculosclaro
            matriz[17, 21:25] = oculos

            matriz[18, 0:8] = branco
            matriz[18, 8:9] = contorno
            matriz[18, 9:11] = amarelo
            matriz[18, 11:12] = contorno
            matriz[18, 12:13] = amarelo
            matriz[18, 13:14] = olho1
            matriz[18, 14:17] = olho2
            matriz[18, 17:19] = amarelo
            matriz[18, 19:20] = olho1
            matriz[18, 20:23] = olho2
            matriz[18, 23:24] = amarelo
            matriz[18, 24:25] = contorno
            matriz[18, 25:26] = amarelo
            matriz[18, 26:27] = amareloqueimado
            matriz[18, 27:28] = contorno
            matriz[18, 28:60] = branco
###
            matriz[18, 12:13] = oculos
            matriz[18, 13:15] = oculosclaro
            matriz[18, 15:18] = oculos
            matriz[18, 18:19] = armacao
            matriz[18, 19:20] = oculos
            matriz[18, 20:22] = oculosclaro
            matriz[18, 22:25] = oculos

            matriz[19, 0:8] = branco
            matriz[19, 8:9] = contorno
            matriz[19, 9:10] = amareloqueimado
            matriz[19, 10:12] = contorno
            matriz[19, 12:24] = amarelo
            matriz[19, 24:26] = contorno
            matriz[19, 26:27] = amarelo
            matriz[19, 27:28] = contorno
            matriz[19, 28:60] = branco
###
            matriz[19, 12:13] = oculos
            matriz[19, 13:16] = oculosclaro
            matriz[19, 16:18] = oculos
            # matriz[18, 18:19] = armacao
            matriz[19, 19:20] = oculos
            matriz[19, 20:23] = oculosclaro
            matriz[19, 23:25] = oculos

            matriz[20, 0:8] = branco
            matriz[20, 8:10] = contorno
            matriz[20, 10:11] = branco
            matriz[20, 11:12] = contorno
            matriz[20, 12:24] = amarelo
            matriz[20, 24:25] = contorno
            matriz[20, 25:26] = branco
            matriz[20, 26:28] = contorno
            matriz[20, 28:60] = branco
###
            matriz[20, 13:17] = oculos
            matriz[20, 20:24] = oculos

            matriz[21, 0:12] = branco
            matriz[21, 12:13] = contorno
            matriz[21, 13:17] = amarelo
            matriz[21, 17:18] = amareloqueimado
            matriz[21, 18:19] = amarelo
            matriz[21, 19:20] = amareloqueimado
            matriz[21, 20:24] = amarelo
            matriz[21, 24:25] = contorno
            matriz[21, 25:60] = branco

            matriz[22, 0:12] = branco
            matriz[22, 12:13] = contorno
            matriz[22, 13:17] = amarelo
            matriz[22, 17:19] = amareloqueimado
            matriz[22, 19:25] = amarelo
            matriz[22, 25:27] = contorno
            matriz[22, 27:60] = branco

            matriz[23, 0:13] = branco
            matriz[23, 13:14] = contorno
            matriz[23, 14:27] = amarelo
            matriz[23, 27:29] = contorno
            matriz[23, 29:60] = branco

            matriz[24, 0:14] = branco
            matriz[24, 14:15] = contorno
            matriz[24, 15:29] = amarelo
            matriz[24, 29:31] = contorno
            matriz[24, 31:60] = branco

            matriz[25, 0:14] = branco
            matriz[25, 14:15] = contorno
            matriz[25, 15:31] = amarelo
            matriz[25, 31:33] = contorno
            matriz[25, 33:60] = branco

            matriz[26, 0:15] = branco
            matriz[26, 15:17] = contorno
            matriz[26, 17:18] = amarelo
            matriz[26, 18:21] = nariz
            matriz[26, 21:33] = amarelo
            matriz[26, 33:34] = contorno
            matriz[26, 34:55] = branco
            matriz[26, 55:56] = contorno
            matriz[26, 56:60] = branco

            matriz[27, 0:16] = branco
            matriz[27, 16:17] = contorno
            matriz[27, 17:21] = nariz
            matriz[27, 21:34] = amarelo
            matriz[27, 34:36] = contorno
            matriz[27, 36:54] = branco
            matriz[27, 54:55] = contorno
            matriz[27, 55:56] = amarelo
            matriz[27, 56:57] = contorno
            matriz[27, 57:60] = branco

            matriz[28, 0:17] = branco
            matriz[28, 17:21] = nariz
            matriz[28, 21:36] = amarelo
            matriz[28, 36:37] = contorno
            matriz[28, 37:53] = branco
            matriz[28, 53:54] = contorno
            matriz[28, 54:56] = amarelo
            matriz[28, 56:57] = contorno
            matriz[28, 57:60] = branco

            matriz[29, 0:18] = branco
            matriz[29, 18:21] = vermelho
            matriz[29, 21:37] = amarelo
            matriz[29, 37:39] = contorno
            matriz[29, 39:53] = branco
            matriz[29, 53:54] = contorno
            matriz[29, 54:55] = amarelo
            matriz[29, 55:56] = contorno
            matriz[29, 56:60] = branco

        ######################################################

            matriz[30, 0:19] = branco
            matriz[30, 19:20] = vermelho
            matriz[30, 20:21] = branco
            matriz[30, 21:22] = contorno
            matriz[30, 22:39] = amarelo
            matriz[30, 39:40] = contorno
            matriz[30, 40:52] = branco
            matriz[30, 52:53] = contorno
            matriz[30, 53:55] = amarelo
            matriz[30, 55:56] = contorno
            matriz[30, 56:60] = branco
        ###############################################################

            matriz[31, 0:20] = branco
            matriz[31, 20:22] = contorno
            matriz[31, 22:40] = amarelo
            matriz[31, 40:41] = contorno
            matriz[31, 41:51] = branco
            matriz[31, 51:52] = contorno
            matriz[31, 52:54] = amarelo
            matriz[31, 54:55] = contorno
            matriz[31, 55:60] = branco

            matriz[32, 0:20] = branco
            matriz[32, 20:22] = contorno
            matriz[32, 22:36] = amarelo
            matriz[32, 36:38] = contorno
            matriz[32, 36:41] = amarelo
            matriz[32, 41:42] = contorno
            matriz[32, 42:50] = branco
            matriz[32, 50:51] = contorno
            matriz[32, 51:53] = amarelo
            matriz[32, 53:54] = contorno
            matriz[32, 54:60] = branco

            matriz[33, 0:20] = branco
            matriz[33, 20:22] = contorno
            matriz[33, 22:34] = amarelo
            matriz[33, 34:37] = contorno
            matriz[33, 37:42] = amarelo
            matriz[33, 42:43] = contorno
            matriz[33, 43:49] = branco
            matriz[33, 49:50] = contorno
            matriz[33, 50:52] = amarelo
            matriz[33, 52:53] = contorno
            matriz[33, 53:60] = branco

            matriz[34, 0:20] = branco
            matriz[34, 20:22] = contorno
            matriz[34, 22:24] = amarelo
            matriz[34, 24:25] = contorno
            matriz[34, 25:33] = amarelo
            matriz[34, 33:35] = contorno
            matriz[34, 35:43] = amarelo
            matriz[34, 43:44] = contorno
            matriz[34, 44:48] = branco
            matriz[34, 48:49] = contorno
            matriz[34, 49:51] = amarelo
            matriz[34, 51:52] = contorno
            matriz[34, 52:60] = branco

            matriz[35, 0:20] = branco
            matriz[35, 20:22] = contorno
            matriz[35, 22:24] = amarelo
            matriz[35, 24:25] = contorno
            matriz[35, 25:33] = amarelo
            matriz[35, 33:35] = contorno
            matriz[35, 35:44] = amarelo
            matriz[35, 44:45] = contorno
            matriz[35, 45:47] = branco
            matriz[35, 47:48] = contorno
            matriz[35, 48:50] = amarelo
            matriz[35, 50:51] = contorno
            matriz[35, 51:60] = branco

            matriz[36, 0:20] = branco
            matriz[36, 20:22] = contorno
            matriz[36, 22:24] = amarelo
            matriz[36, 24:26] = contorno
            matriz[36, 26:33] = amarelo
            matriz[36, 33:35] = contorno
            matriz[36, 35:45] = amarelo
            matriz[36, 45:47] = contorno
            matriz[36, 47:49] = amarelo
            matriz[36, 49:50] = contorno
            matriz[36, 50:60] = branco

            matriz[37, 0:20] = branco
            matriz[37, 20:22] = contorno
            matriz[37, 22:24] = amarelo
            matriz[37, 24:25] = contorno
            matriz[37, 25:26] = branco
            matriz[37, 26:27] = contorno
            matriz[37, 27:33] = amarelo
            matriz[37, 33:35] = contorno
            matriz[37, 35:48] = amarelo
            matriz[37, 48:49] = contorno
            matriz[37, 49:60] = branco

            matriz[38, 0:20] = branco
            matriz[38, 20:21] = contorno
            matriz[38, 21:24] = amarelo
            matriz[38, 24:25] = contorno
            matriz[38, 25:27] = branco
            matriz[38, 27:29] = contorno
            matriz[38, 29:33] = amarelo
            matriz[38, 33:35] = contorno
            matriz[38, 35:46] = amarelo
            matriz[38, 46:48] = contorno
            matriz[38, 48:60] = branco

            matriz[39, 0:20] = branco
            matriz[39, 20:21] = contorno
            matriz[39, 21:24] = amarelo
            matriz[39, 24:25] = contorno
            matriz[39, 25:29] = branco
            matriz[39, 29:30] = contorno
            matriz[39, 30:34] = amarelo
            matriz[39, 34:36] = contorno
            matriz[39, 36:44] = amarelo
            matriz[39, 44:46] = contorno
            matriz[39, 46:60] = branco

            matriz[40, 0:19] = branco
            matriz[40, 19:21] = contorno
            matriz[40, 21:24] = amarelo
            matriz[40, 24:25] = contorno
            matriz[40, 25:30] = branco
            matriz[40, 30:32] = contorno
            matriz[40, 32:35] = amarelo
            matriz[40, 35:37] = contorno
            matriz[40, 37:43] = amarelo
            matriz[40, 43:45] = contorno
            matriz[40, 45:60] = branco

            matriz[41, 0:18] = branco
            matriz[41, 18:21] = contorno
            matriz[41, 21:23] = amarelo
            matriz[41, 23:25] = contorno
            matriz[41, 25:32] = branco
            matriz[41, 32:37] = contorno
            matriz[41, 37:42] = amarelo
            matriz[41, 42:44] = contorno
            matriz[41, 44:60] = branco

            matriz[42, 0:14] = branco
            matriz[42, 14:17] = sombra
            matriz[42, 17:20] = contorno
            matriz[42, 20:23] = amarelo
            matriz[42, 23:25] = contorno
            matriz[42, 25:33] = sombraclara
            matriz[42, 33:37] = contorno
            matriz[42, 37:42] = amarelo
            matriz[42, 42:44] = contorno
            matriz[42, 44:46] = sombraclara
            matriz[42, 46:60] = branco

            matriz[43, 0:13] = branco
            matriz[43, 13:16] = sombra
            matriz[43, 16:18] = contorno
            matriz[43, 18:22] = amarelo
            matriz[43, 22:25] = contorno
            matriz[43, 25:26] = sombra
            matriz[43, 26:32] = sombraclara
            matriz[43, 32:34] = contorno
            matriz[43, 34:40] = amarelo
            matriz[43, 40:43] = contorno
            matriz[43, 43:47] = sombraclara
            matriz[43, 47:60] = branco

            matriz[44, 0:12] = branco
            matriz[44, 12:16] = sombra
            matriz[44, 16:17] = contorno
            matriz[44, 17:22] = amarelo
            matriz[44, 22:24] = contorno
            matriz[44, 24:29] = sombra
            matriz[44, 29:32] = sombraclara
            matriz[44, 32:33] = contorno
            matriz[44, 33:39] = amarelo
            matriz[44, 39:42] = contorno
            matriz[44, 42:46] = sombra
            matriz[44, 46:48] = sombraclara
            matriz[44, 48:60] = branco

            matriz[45, 0:12] = branco
            matriz[45, 12:17] = sombra
            matriz[45, 17:23] = contorno
            matriz[45, 23:33] = sombra
            matriz[45, 33:40] = contorno
            matriz[45, 40:48] = sombra
            matriz[45, 48:60] = branco

            matriz[46, 0:13] = branco
            matriz[46, 13:47] = sombra
            matriz[46, 47:60] = branco

            matriz[47, 0:14] = branco
            matriz[47, 14:46] = sombra
            matriz[47, 46:60] = branco

            matriz[48, 0:60] = branco
            matriz[49, 0:60] = branco

            return matriz


        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       contorno_r,
                       amarelo_r,
                       amareloqueimado_r,
                       sombrancelha_r,
                       olho1_r,
                       olho2_r,
                       nariz_r,
                       vermelho_r,
                       sombra_r,
                       sombraclara_r,
                       oculos_r,
                       oculosclaro_r,
                       armacao_r)

        g = geraPixels(g,
                       contorno_g,
                       amarelo_g,
                       amareloqueimado_g,
                       sombrancelha_g,
                       olho1_g,
                       olho2_g,
                       nariz_g,
                       vermelho_g,
                       sombra_g,
                       sombraclara_g,
                       oculos_g,
                       oculosclaro_g,
                       armacao_g)

        b = geraPixels(b,
                       contorno_b,
                       amarelo_b,
                       amareloqueimado_b,
                       sombrancelha_b,
                       olho1_b,
                       olho2_b,
                       nariz_b,
                       vermelho_b,
                       sombra_b,
                       sombraclara_b,
                       oculos_b,
                       oculosclaro_b,
                       armacao_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        print(type(r))
        print(r)
        print(r[0][1])
        print(m.dtype)


        plt.figure(figsize=(5, 4))
        img = plt.imshow(m, interpolation='nearest')
        # plt.savefig(pasta)
        plt.show()

base = oculos()