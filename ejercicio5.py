# Paso 1: Importar librerías
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 2: Leer la imagen desde un archivo
imagen = cv2.imread('cara.jpg')

# Paso 3: Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargo exitosamente')

# Paso 4: Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
# Paso 5: Aplicar la ecualización de histograma a la imagen en escala de grises
img_ecualizada = cv2.equalizeHist(imagen_gris)

#Paso 6: Guardar la imagen ecualizada
cv2.imwrite('imagen_ecualizada.jpg', img_ecualizada)

#Paso 7: Calcular el histograma de la imagen original en escala de grises
hist_original = cv2.calcHist([imagen_gris], [0], None, [256], [0, 256])

# Paso 8: Calcular el histograma de la imagen ecualizada
hist_ecualizada = cv2.calcHist([img_ecualizada], [0], None, [256], [0, 256])

# Paso 9: Configurar el tamaño de la figura para mostrar las imágenes y los histogramas
plt.figure(figsize=(10, 7))

# Paso 10: Mostrar la imagen original en escala de grises
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR))
plt.title('Imagen Original')
plt.axis('off')

# Paso 11: Mostrar la imagen ecualizada
plt.subplot(2, 2, 3)
plt.imshow(img_ecualizada, cmap='gray')
plt.title('Imagen Ecualizada')
plt.axis('off')

# Paso 12: Mostrar el histograma de la imagen original
plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Histograma de la Imagen Original')
plt.xlabel('Intensidad de los píxeles')
plt.ylabel('Número de píxeles')

# Paso 13: Mostrar el histograma de la imagen ecualizada
plt.subplot(2, 2, 4)
plt.plot(hist_ecualizada, color='black')
plt.title('Histograma de la Imagen Ecualizada')
plt.xlabel('Intensidad de los píxeles')
plt.ylabel('Número de píxeles')

# Paso 14: Ajustar el diseño de la figura para que no haya superposición entre las subplots
plt.tight_layout()

# Paso 15: Guardar la figura con las imágenes y los histogramas
plt.savefig('histogramas_ecualizacion.png')

# Paso 16: Mostrar la figura con las imágenes y los histogramas
plt.show()
