import cv2
import json

# file_name = input()
f = open('../data/labels/labels.json')
label = json.load(f)

red = (0, 0, 255)

image = cv2.imread('../data/images/'+label[0]['name'])
image = cv2.rectangle(image, (int(label[0]['labels'][0]['box2d']['x1']), int(label[0]['labels'][0]['box2d']['y1'])), (int(label[0]['labels'][0]['box2d']['x2']), int(label[0]['labels'][0]['box2d']['y2'])), red, 3)
cv2.namedWindow('img')
cv2.imshow('img', image)
cv2.waitKey(0)

