import os
import numpy as np
import pandas as pd
import cv2

def imageds_to_csv(IMG_SIZE = 64):
    '''
    (int) --> (DataFrame)

    Esta función recibe un entero IMG_SIZE que representa el número de pixeles en una imagen.
    Luego reajusta el tamaño de todas las imágenes en un directorio y las convierte en un DataFrame
    que tiene por columnas: los pixeles y su respectiva etiqueta.
    '''
    data = []
    label = []
    path = "./parrots/original_size/test_set/"
    for directory in os.listdir(path):
        l_path = path + directory + "/"
        for image in os.listdir(l_path):
            img = cv2.imread(l_path + image)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = img.astype('float32')
            data.append(img)
            label.append(directory)
    
    for i in range(len(data)):
         data[i] = np.asarray(data[i])
         data[i] = data[i].flatten()

    columns = [f"Pixel {i}" for i in range(IMG_SIZE*IMG_SIZE)]
    data = pd.DataFrame(data = data, columns = columns)
    data['Family'] = label
    data.to_csv("./parrots_test.csv")
    return data

if __name__ == '__main__':
    imageds_to_csv(IMG_SIZE=80)