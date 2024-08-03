# Paso 1: Importamos libreria openCV
import cv2

# Paso 2: Leer una imagen desde un archivo
imagen = cv2.imread('iot.jpg')
if imagen is None:
    print ('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargo exitosamente')
    
# Paso 3: Cambiar el tamaño de la imagen a 300x300 píxeles
imagen_redimensionada = cv2.resize(imagen, (300, 300))

# Paso 4: Guardar la imagen redimensionada
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)

# Paso 5: Mostrar la imagen redimensionada
cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
