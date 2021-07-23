import cv2
image=cv2.imread("C:/Users/yashi/Desktop/dog.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
image=cv2.resize(image,(600,600))
pencil_sketch=cv2.resize(pencil_sketch,(600,600))
cv2.imshow("Original Image",image)
cv2.imshow("pencil sketch Image",pencil_sketch)
cv2.waitkey(0)
