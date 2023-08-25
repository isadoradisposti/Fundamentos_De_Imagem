import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def main():
    image_pillow = Image.open('image/lena_gray_512.tif')
    f_image_nd = np.array(image_pillow)
    g_image_nd = np.zeros(f_image_nd.shape)

    #neighborhood operation (operação por vizinhança)
    l = f_image_nd.shape[0]
    c = f_image_nd.shape[1]
    k = 3
    #print("Imagem")

    #print(f_image_nd[0:5,0:5])
    for x in range(k, l-k): #linhas
        for y in range(k, c-k): #colunas
            s_xy = f_image_nd[x-k:x+k+1,y-k:y+k+1]
            g_image_nd[x,y] = np.median(s_xy).astype(int)
            #print('janela')
            #print(s_xy)

    #create two columns plot
    fig = plt.figure()
    plt1 = plt.subplot(1,2,1)
    plt2 = plt.subplot(1,2,2)
    plt1.title.set_text('Original Image')
    plt2.title.set_text('Filtred Image')

    plt1.imshow(f_image_nd, cmap='gray')
    plt2.imshow(g_image_nd, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()