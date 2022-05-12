import criaNFT

NFTlista = []

########################################################
########################################################

def contaNFTs(listaObjetos):
    for nft in listaObjetos:
        print(nft.nft)


i = 0

# Primeiro NFT gerado, não tornar a lista inicial vazia
NFTs = criaNFT.NFT(0)
NFTlista.append(NFTs)

# Gera lista de objetos com a matriz dos NFTs
while len(NFTlista) < 10:
    verificaIgualdade = 0
    NFTs = criaNFT.NFT(i+1)

    # print("NFT na lista {}: {}" .format(i, NFTlista[i].nft))
    # print("NFT gerado: {} " .format(NFTs.nft))
    # print("Lista: {}" .format(len(NFTlista)))
    # contaNFTs(NFTlista)
    # print("------------------------------------")

    for x in NFTlista:
        if x.nft == NFTs.nft:
            verificaIgualdade = verificaIgualdade + 1
            break

    if verificaIgualdade == 0:
        NFTlista.append(NFTs)

print("------------------ FIM ------------------")
contaNFTs(NFTlista)
# print(NFTlista)
print(len(NFTlista))

# Gera Imagens NFTs
numeracao = 0
for geraNFT in NFTlista:
    print(geraNFT.nft)

    # Envia elementos de cada objeto
    geraNFT.elementos(geraNFT.nft, numeracao)
    numeracao = numeracao + 1
    # time.sleep(5)