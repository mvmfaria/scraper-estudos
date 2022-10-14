#importa a biblioteca.
import cv2
# import math

#define imagem que estamos trabalhando.
image = cv2.imread(r"C:\Users\marcos\isdog\cut-img\120px-Bouledogue_am%C3%A9ricain%2C_t%C3%AAte%2C_profil.jpg")

#definindo atributos da imagem.
largura = image.shape[1]
# print(largura)
altura = image.shape[0]
# print(altura)

x = 0.583333 * largura
y = 0.5375 * altura
w = 0.833333 * largura
h = 0.925 * altura

# print("ponto do central: ", altura * 0.583333)
# print("ponto do central: ", largura * 0.5375)

# print(f"ponto superior esquerdo: ({x - (w/2)}, {y - (h/2)}) ")

# print(f"ponto inferior direito: ({x + (w/2)}, {y + (h/2)}) ")

#provisório: parâmetros para fazer o corte da imagem, posteriormente utilizaremos os arquivos com os dados.
starting_x_coordinate = x - (w/2)
starting_y_coordinate = y - (h/2)
ending_x_coordinate = x + (w/2)
ending_y_coordinate = y + (h/2)

#recorta pedaço da imagem de acordo com os parametros passados
crop_image = image[round(starting_y_coordinate):round(ending_y_coordinate), round(starting_x_coordinate):round(ending_x_coordinate)]

#exibe imagem
cv2.imshow("Cropped", crop_image)

#não sei o que faz
cv2.waitKey(0)