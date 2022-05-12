import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


branco = 255

contorno_r = 244
contorno_g = 196
contorno_b = 48

amarelo_r = 255
amarelo_g = 191
amarelo_b = 0

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
               sombraclara):

    matriz[0, 0:60] = branco
    matriz[1, 0:60] = branco
    matriz[2, 0:60] = branco
    matriz[3, 0:60] = branco
    matriz[4, 0:60] = branco
    matriz[5, 0:60] = branco
    matriz[6, 0:60] = branco
    matriz[7, 0:60] = branco
    matriz[8, 0:60] = branco
    matriz[9, 0:60] = branco
    matriz[10, 0:60] = branco

    matriz[11, 0:14] = branco
    matriz[11, 15:21] = contorno
    matriz[11, 22:60] = branco

    matriz[12, 0:13] = branco
    matriz[12, 14:14] = contorno
    matriz[12, 15:21] = amarelo
    matriz[12, 22:22] = contorno
    matriz[12, 23:60] = branco

    matriz[13, 0:12] = branco
    matriz[13, 13:13] = contorno
    matriz[13, 14:22] = amarelo
    matriz[13, 23:23] = contorno
    matriz[13, 24:60] = branco

    matriz[14, 0:11] = branco
    matriz[14, 12:12] = contorno
    matriz[14, 13:23] = amarelo
    matriz[14, 24:24] = contorno
    matriz[14, 25:60] = branco

    matriz[15, 0:10] = branco
    matriz[15, 11:12] = contorno
    matriz[15, 13:13] = amarelo
    matriz[15, 14:17] = sombrancelha
    matriz[15, 18:19] = amarelo
    matriz[15, 20:23] = sombrancelha
    matriz[15, 24:24] = amarelo
    matriz[15, 25:26] = contorno
    matriz[15, 27:60] = branco

    matriz[16, 0:9] = branco
    matriz[16, 10:10] = contorno
    matriz[16, 11:11] = amarelo
    matriz[16, 12:12] = contorno
    matriz[16, 13:24] = amarelo
    matriz[16, 25:25] = contorno
    matriz[16, 26:26] = amarelo
    matriz[16, 27:27] = contorno
    matriz[16, 28:60] = branco

    matriz[17, 0:8] = branco
    matriz[17, 9:9] = contorno
    matriz[17, 10:11] = amarelo
    matriz[17, 12:12] = contorno
    matriz[17, 13:13] = amarelo
    matriz[17, 14:15] = olho1
    matriz[17, 16:17] = olho2
    matriz[17, 18:19] = amarelo
    matriz[17, 20:21] = olho1
    matriz[17, 22:23] = olho2
    matriz[17, 24:24] = amarelo
    matriz[17, 25:25] = contorno
    matriz[17, 26:26] = amareloqueimado
    matriz[17, 27:27] = amarelo
    matriz[17, 28:28] = contorno
    matriz[17, 29:60] = branco

    matriz[18, 0:8] = branco
    matriz[18, 9:9] = contorno
    matriz[18, 10:11] = amarelo
    matriz[18, 12:12] = contorno
    matriz[18, 13:13] = amarelo
    matriz[18, 14:14] = olho1
    matriz[18, 15:17] = olho2
    matriz[18, 18:19] = amarelo
    matriz[18, 20:20] = olho1
    matriz[18, 21:23] = olho2
    matriz[18, 24:24] = amarelo
    matriz[18, 25:25] = contorno
    matriz[18, 26:26] = amarelo
    matriz[18, 27:27] = amareloqueimado
    matriz[18, 28:28] = contorno
    matriz[18, 29:60] = branco

    matriz[19, 0:8] = branco
    matriz[19, 9:9] = contorno
    matriz[19, 10:10] = amareloqueimado
    matriz[19, 11:12] = contorno
    matriz[19, 13:24] = amarelo
    matriz[19, 25:26] = contorno
    matriz[19, 27:27] = amarelo
    matriz[19, 28:28] = contorno
    matriz[19, 29:60] = branco

    matriz[20, 0:8] = branco
    matriz[20, 9:10] = contorno
    matriz[20, 11:11] = branco
    matriz[20, 12:12] = contorno
    matriz[20, 13:24] = amarelo
    matriz[20, 25:25] = contorno
    matriz[20, 26:26] = branco
    matriz[20, 27:28] = contorno
    matriz[20, 29:60] = branco

    matriz[21, 0:12] = branco
    matriz[21, 13:13] = contorno
    matriz[21, 14:24] = amarelo
    matriz[21, 25:60] = branco

    matriz[22, 0:12] = branco
    matriz[22, 13:13] = contorno
    matriz[22, 14:25] = amarelo
    matriz[22, 26:27] = contorno
    matriz[22, 28:60] = branco

    matriz[23, 0:13] = branco
    matriz[23, 14:14] = contorno
    matriz[23, 15:27] = amarelo
    matriz[23, 28:29] = contorno
    matriz[23, 30:60] = branco

    matriz[24, 0:14] = branco
    matriz[24, 15:15] = contorno
    matriz[24, 16:29] = amarelo
    matriz[24, 30:31] = contorno
    matriz[24, 32:60] = branco

    matriz[25, 0:14] = branco
    matriz[25, 15:15] = contorno
    matriz[25, 16:31] = amarelo
    matriz[25, 32:33] = contorno
    matriz[25, 34:60] = branco

    matriz[26, 0:15] = branco
    matriz[26, 16:17] = contorno
    matriz[26, 18:18] = amarelo
    matriz[26, 19:21] = nariz
    matriz[26, 22:33] = amarelo
    matriz[26, 34:34] = contorno
    matriz[26, 35:55] = branco
    matriz[26, 56:56] = contorno
    matriz[26, 57:60] = branco

    matriz[27, 0:16] = branco
    matriz[27, 17:17] = contorno
    matriz[27, 18:21] = nariz
    matriz[27, 22:34] = amarelo
    matriz[27, 35:36] = contorno
    matriz[27, 37:54] = branco
    matriz[27, 55:55] = contorno
    matriz[27, 56:56] = amarelo
    matriz[27, 57:57] = contorno
    matriz[27, 58:60] = branco

    matriz[28, 0:17] = branco
    matriz[28, 18:21] = nariz
    matriz[28, 22:36] = amarelo
    matriz[28, 37:37] = contorno
    matriz[28, 38:53] = branco
    matriz[28, 54:54] = contorno
    matriz[28, 55:56] = amarelo
    matriz[28, 57:57] = contorno
    matriz[28, 58:60] = branco

    matriz[29, 0:18] = branco
    matriz[29, 19:21] = vermelho
    matriz[29, 22:37] = amarelo
    matriz[29, 38:39] = contorno
    matriz[29, 40:53] = branco
    matriz[29, 54:54] = contorno
    matriz[29, 55:55] = amarelo
    matriz[29, 56:56] = contorno
    matriz[29, 57:60] = branco

######################################################

    matriz[30, 0:19] = branco
    matriz[30, 20:20] = vermelho
    matriz[30, 21:21] = branco
    matriz[30, 22:22] = contorno
    matriz[30, 23:39] = amarelo
    matriz[30, 40:40] = contorno
    matriz[30, 41:52] = branco
    matriz[30, 53:53] = contorno
    matriz[30, 54:55] = amarelo
    matriz[30, 56:56] = contorno
    matriz[30, 57:60] = branco
###############################################################

    matriz[31, 0:20] = branco
    matriz[31, 21:22] = contorno
    matriz[31, 23:40] = amarelo
    matriz[31, 41:41] = contorno
    matriz[31, 42:51] = branco
    matriz[31, 52:52] = contorno
    matriz[31, 53:54] = amarelo
    matriz[31, 55:55] = contorno
    matriz[31, 56:60] = branco

    matriz[32, 0:20] = branco
    matriz[32, 21:22] = contorno
    matriz[32, 23:36] = amarelo
    matriz[32, 37:38] = contorno
    matriz[32, 39:41] = amarelo
    matriz[32, 42:42] = contorno
    matriz[32, 43:50] = branco
    matriz[32, 51:51] = contorno
    matriz[32, 52:53] = amarelo
    matriz[32, 54] = contorno
    matriz[32, 55:60] = branco

    matriz[33, 0:20] = branco
    matriz[33, 21:22] = contorno
    matriz[33, 23:34] = amarelo
    matriz[33, 35:37] = contorno
    matriz[33, 38:42] = amarelo
    matriz[33, 43:43] = contorno
    matriz[33, 44:49] = branco
    matriz[33, 50:50] = contorno
    matriz[33, 51:52] = amarelo
    matriz[33, 53:53] = contorno
    matriz[33, 54:60] = branco

    matriz[34, 0:20] = branco
    matriz[34, 21:22] = contorno
    matriz[34, 23:24] = amarelo
    matriz[34, 25:25] = contorno
    matriz[34, 26:33] = amarelo
    matriz[34, 34:35] = contorno
    matriz[34, 36:43] = amarelo
    matriz[34, 44:44] = contorno
    matriz[34, 45:48] = branco
    matriz[34, 49:49] = contorno
    matriz[34, 50:51] = amarelo
    matriz[34, 52:52] = contorno
    matriz[34, 53:60] = branco

    matriz[35, 0:20] = branco
    matriz[35, 21:22] = contorno
    matriz[35, 23:24] = amarelo
    matriz[35, 25:25] = contorno
    matriz[35, 26:33] = amarelo
    matriz[35, 34:35] = contorno
    matriz[35, 36:44] = amarelo
    matriz[35, 45:45] = contorno
    matriz[35, 46:47] = branco
    matriz[35, 48:48] = contorno
    matriz[35, 49:50] = amarelo
    matriz[35, 51:51] = contorno
    matriz[35, 52:60] = branco

    matriz[36, 0:20] = branco
    matriz[36, 21:22] = contorno
    matriz[36, 23:24] = amarelo
    matriz[36, 25:26] = contorno
    matriz[36, 27:33] = amarelo
    matriz[36, 34:35] = contorno
    matriz[36, 36:45] = amarelo
    matriz[36, 46:47] = contorno
    matriz[36, 48:49] = amarelo
    matriz[36, 50:50] = contorno
    matriz[36, 51:60] = branco

    matriz[37, 0:20] = branco
    matriz[37, 21:22] = contorno
    matriz[37, 23:24] = amarelo
    matriz[37, 25:25] = contorno
    matriz[37, 26:26] = branco
    matriz[37, 27:27] = contorno
    matriz[37, 28:33] = amarelo
    matriz[37, 34:35] = contorno
    matriz[37, 36:46] = amarelo
    matriz[37, 47:48] = contorno
    matriz[37, 49:60] = branco

    matriz[38, 0:20] = branco
    matriz[38, 21:21] = contorno
    matriz[38, 22:24] = amarelo
    matriz[38, 25:25] = contorno
    matriz[38, 26:27] = branco
    matriz[38, 28:29] = contorno
    matriz[38, 30:33] = amarelo
    matriz[38, 34:35] = contorno
    matriz[38, 36:46] = amarelo
    matriz[38, 47:48] = contorno
    matriz[38, 49:60] = branco

    matriz[39, 0:20] = branco
    matriz[39, 21:21] = contorno
    matriz[39, 22:24] = amarelo
    matriz[39, 25:25] = contorno
    matriz[39, 26:29] = branco
    matriz[39, 30:30] = contorno
    matriz[39, 31:34] = amarelo
    matriz[39, 35:36] = contorno
    matriz[39, 37:44] = amarelo
    matriz[39, 45:46] = contorno
    matriz[39, 47:60] = branco

    matriz[40, 0:19] = branco
    matriz[40, 20:21] = contorno
    matriz[40, 22:24] = amarelo
    matriz[40, 25:25] = contorno
    matriz[40, 26:30] = branco
    matriz[40, 31:32] = contorno
    matriz[40, 33:35] = amarelo
    matriz[40, 36:37] = contorno
    matriz[40, 38:43] = amarelo
    matriz[40, 44:45] = contorno
    matriz[40, 46:60] = branco

    matriz[41, 0:18] = branco
    matriz[41, 19:21] = contorno
    matriz[41, 22:23] = amarelo
    matriz[41, 24:25] = contorno
    matriz[41, 26:32] = branco
    matriz[41, 33:37] = contorno
    matriz[41, 38:42] = amarelo
    matriz[41, 43:44] = contorno
    matriz[41, 45:60] = branco

    matriz[42, 0:14] = branco
    matriz[42, 15:17] = sombra
    matriz[42, 18:20] = contorno
    matriz[42, 21:23] = amarelo
    matriz[42, 24:25] = contorno
    matriz[42, 26:33] = sombraclara
    matriz[42, 34:37] = contorno
    matriz[42, 38:42] = amarelo
    matriz[42, 43:44] = contorno
    matriz[42, 45:46] = sombraclara
    matriz[42, 47:60] = branco

    matriz[43, 0:13] = branco
    matriz[43, 14:16] = sombra
    matriz[43, 17:18] = contorno
    matriz[43, 19:22] = amarelo
    matriz[43, 23:25] = contorno
    matriz[43, 26:26] = sombra
    matriz[43, 27:32] = sombraclara
    matriz[43, 33:34] = contorno
    matriz[43, 35:40] = amarelo
    matriz[43, 41:43] = contorno
    matriz[43, 44:47] = sombraclara
    matriz[43, 48:60] = branco

    matriz[44, 0:12] = branco
    matriz[44, 13:16] = sombra
    matriz[44, 17:17] = contorno
    matriz[44, 18:22] = amarelo
    matriz[44, 23:24] = contorno
    matriz[44, 25:29] = sombra
    matriz[44, 30:32] = sombraclara
    matriz[44, 33:33] = contorno
    matriz[44, 34:39] = amarelo
    matriz[44, 40:42] = contorno
    matriz[44, 43:46] = sombra
    matriz[44, 47:48] = sombraclara
    matriz[44, 49:60] = branco

    matriz[45, 0:12] = branco
    matriz[45, 13:17] = sombra
    matriz[45, 18:23] = contorno
    matriz[45, 24:33] = sombra
    matriz[45, 34:40] = contorno
    matriz[45, 41:48] = sombra
    matriz[45, 49:60] = branco

    matriz[46, 0:13] = branco
    matriz[46, 14:47] = sombra
    matriz[46, 48:60] = branco

    matriz[47, 0:14] = branco
    matriz[47, 15:46] = sombra
    matriz[47, 47:60] = branco

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
               sombraclara_r)

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
               sombraclara_g)

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
               sombraclara_b)


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
# plt.grid(color='red', linestyle='-.', linewidth=1)
# plt.axes(r, [0., 0., 1., 1.])
# plt.savefig('teste.png')
plt.show()

