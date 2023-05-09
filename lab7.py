import cv2
image = cv2.imread("image.jpg")
b,g,r = cv2.split(image)


cv2.imshow('Original_Image', image)

cv2.imshow("Model Blue Image", b)

cv2.imshow("Model Green Image", g)

cv2.imshow("Model Red Image", r)


g[:] = 0

merged_image = cv2.merge([b, g, r])

cv2.imshow('Last Merged Image', merged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()