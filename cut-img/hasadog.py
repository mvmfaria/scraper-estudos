#O nome do diretório será extraído de outro algoritmo de alguma forma.
txt = "labels\\teste.txt"

with open(txt) as file:
    #Armazena todo conteúdo do arquivo em uma variável.
    #conteudo = file.read()

    #Verifica se arquivo está vazio. A Yolov7 gera o txt mesmo que não tenha nenhum classe que ela identifique na imagem?
    # if conteudo == "":
    #     print("Arquivo vazio!")

    #Percorre arquivo.
    for line in file:

        listaValores = line.split(" ")

        if listaValores[0] == "16":
            print("Tem cachorro!")

            #Essa parte é para o corte de imagem.   
            # for elem in listaValores:
            #     print(elem)
        print("Fim!")

#Se não me engano o "with" não necessita que o arquivo seja fechado no final.