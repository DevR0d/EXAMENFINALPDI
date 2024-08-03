# Paso 1: Importamos libreria openCV
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 2: Cargar la imagen
img = cv2.imread('tipo.jpg')

if img is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargó exitosamente')

# Paso 3: Convertir la imagen al espacio de color HSI (HSV en OpenCV)
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Paso 4: Aplicar suavizado Gaussiano con un kernel de 5x5
hsi[..., 2] = cv2.GaussianBlur(hsi[..., 2], (5, 5), 0)

# Paso 5: Convertir la imagen de nuevo a RGB
smoothed_rgb = cv2.cvtColor(hsi, cv2.COLOR_HSV2BGR)

# Guardar la imagen suavizada
cv2.imwrite('imagen_suavizada.jpg', smoothed_rgb)

# Paso 6: Mostrar las imágenes original y suavizada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(smoothed_rgb, cv2.COLOR_BGR2RGB))
plt.title('Imagen Suavizada')
plt.axis('off')

# Guardar la figura con las imágenes original y suavizada
plt.tight_layout()
plt.savefig('imagenes_comparacion.png')

# Mostrar la figura
plt.show()
