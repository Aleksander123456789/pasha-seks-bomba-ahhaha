import cv2
import numpy as np

# Чтение гиф-изображения
gif_path = 'test_1.gif.mp4'
cap = cv2.VideoCapture(gif_path)

# Определение цветового диапазона для синего цвета
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

# Пустой список для хранения координат центра синего кружка
trajectory = []

# Проход по каждому кадру гиф-изображения
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование кадра в цветовое пространство HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Создание маски для определения синего цвета
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Поиск контуров объектов на изображении
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Отображение траектории движения синего кружка
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # минимальная площадь для обнаружения объекта
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Нахождение центра контура и добавление координат в список траектории
            center_x = x + w // 2
            center_y = y + h // 2
            trajectory.append((center_x, center_y))

    # Отображение кадра с выделенной траекторией
    cv2.imshow('Trajectory', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Вывод траектории движения
for point in trajectory:
    print(point)
