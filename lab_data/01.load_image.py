import cv2

file_name = input()

image = cv2.imread('../data/images/'+file_name)

cv2.namedWindow('img')
cv2.imshow('img', image)
cv2.waitKey(0)

print(type(image))