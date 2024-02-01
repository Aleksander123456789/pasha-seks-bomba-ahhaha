import cv2
import numpy as np

# Функция обработки событий мыши
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 20, (0, 255, 0), -1)
        cv2.imshow('Aortic Valve Contours', image)

# Загрузка изображения аортального клапана
image = cv2.imread('aortic-stenosis.jpg')

# Создание окна для отображения изображения
cv2.namedWindow('Aortic Valve Contours', cv2.WINDOW_NORMAL)

# Привязка функции обработки событий мыши к окну
cv2.setMouseCallback('Aortic Valve Contours', mouse_callback)

# Отображение изначального изображения
cv2.imshow('Aortic Valve Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
