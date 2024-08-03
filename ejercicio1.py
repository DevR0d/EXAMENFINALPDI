# Paso 1: Importamos libreria openCV
import cv2

# Paso 2: Lee la imagen a color desde el archivo
imagen_color = cv2.imread('fisi.png')
if imagen_color is None:
    print ('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargo exitosamente')

# Paso 3: Convertir imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Paso 4: Guardar imagen en escala de grises
cv2.imwrite('imagen_gris.jpg', imagen_gris)

# Paso 5: Mostrar imagen en escala de grises
cv2.imshow('Imagen en Escala de Grises', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
