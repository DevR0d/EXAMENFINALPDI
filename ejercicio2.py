# Paso 1: Importamos libreria openCV
import cv2

# Paso 2: Leer una imagen desde un archivo
imagen = cv2.imread('familia.png', cv2.IMREAD_GRAYSCALE)
if imagen is None:
    print ('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargo exitosamente')

# Paso 3: Aplicar el detector de bordes de Canny
bordes = cv2.Canny(imagen, 100, 200)

# Paso 4: Guardar la imagen con los bordes detectados
cv2.imwrite('imagen_bordes.jpg', bordes)

# Paso 5: Mostrar la imagen con los bordes detectados
cv2.imshow('Bordes Detectados', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
