#Importações necessárias.
import os
import cv2


def retornaListaDeConteudoNoDiretorio(path):

    #Gera lista de conteúdo presente na pasta informada.
    contents = os.listdir(path)

    #Retornando lista com todos os conteúdos.
    return contents


def retornaListaComConteudoDoArquivoDeTexto(txt):

    contents = []

    with open(txt) as file:

        #Percorre arquivo linha por linha.
        for line in file:

            #Separa conteúdo da linha por espaços em branco (" "). 
            line = line.rstrip('\n')
            elements = line.split(" ")

            contents.append(elements)
    
    #Retorna lista com lista(s) de conteúdo.
    return contents


def retornaInformacoesDeCorteDaImagem(contents):

    cutInformation = []

    for list in contents:
        
        #(verificar qual tipo dos elementos da lista).
        if list[0] == "16":
            
            #Acrescenta uma lista contendo informacoes de corte da imagem.
            cutInformation.append([list[1], list[2], list[3], list[4]])
    
    return cutInformation


def cortaRetanguloIdentificadoPelaYolo(infos, img, nomeImg, pasta):

    print(img)

    img = cv2.imread(img)
    largura = img.shape[1]
    altura = img.shape[0]
    cont = 0
    
    for info in infos:
        
        #Define parametros de corte.
        
        x = info[1] * largura
        y = info[2] * altura
        w = info[3] * largura
        h = info[4] * altura

        #Provisório: parâmetros para fazer o corte da imagem, posteriormente utilizaremos os arquivos com os dados.
        starting_x_coordinate = x - (w/2)
        starting_y_coordinate = y - (h/2)
        ending_x_coordinate = x + (w/2)
        ending_y_coordinate = y + (h/2)

        #Recorta pedaço da imagem de acordo com os parametros passados
        crop_image = img[round(starting_y_coordinate):round(ending_y_coordinate), round(starting_x_coordinate):round(ending_x_coordinate)]

        #Exibe imagem
        #cv2.imshow("Cropped", crop_image)

        #Salvando imagem. onde ele salva?
        
        cv2.imwrite(pasta + "\\" + nomeImg + cont, crop_image)
        
        cont += 1

        #Não sei o que faz
        # cv2.waitKey(0)
