#Importações necessárias.
import os
import cv2

#def rodaYolo

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

    #Carrega imagem.
    img = cv2.imread(img)

    #Definie dimensões
    largura = img.shape[1]
    altura = img.shape[0]
    
    #Desnormaliza as informações da imagem.
    x = float(infos[1]) * largura
    y = float(infos[2]) * altura
    w = float(infos[3]) * largura
    h = float(infos[4]) * altura
    
    #Define coordenadas de corte.
    starting_x_coordinate = x - (w/2)
    starting_y_coordinate = y - (h/2)
    ending_x_coordinate = x + (w/2)
    ending_y_coordinate = y + (h/2)

    #Recorta pedaço da imagem de acordo com os parametros passados.
    crop_image = img[round(starting_y_coordinate):round(ending_y_coordinate), round(starting_x_coordinate):round(ending_x_coordinate)]
    
    #Salva imagem.
    cv2.imwrite(pasta + "\\" + nomeImg, crop_image)


