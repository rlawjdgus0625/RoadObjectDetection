import cv2

file_name = input()

red = (0, 0, 255)

image = cv2.imread('../data/images/'+file_name)
image = cv2.rectangle(image, (10, 10), (100, 100), red, 3)
cv2.namedWindow('img')
cv2.imshow('img', image)
cv2.waitKey(0)

print(type(image))