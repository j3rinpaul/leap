
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('./cascade.xml')
# Read the input image
img = cv2.imread('./p/pos4.jpg')


# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)
    print("Hello")
    

cv2.imshow('img',img)
cv2.imshow('gray',gray)
# cap = cv2.VideoCapture(0)
# while 1:

# 	# reads frames from a camera
# 	ret, img = cap.read()

# 	# convert to gray scale of each frames
# 	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 	# Detects faces of different sizes in the input image
# 	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# 	for (x,y,w,h) in faces:
# 		# To draw a rectangle in a face
# 		cv2.rectangle(img,(x,y),(x+w,y+h),(255,145,0),1)
# 		# roi_gray = gray[y:y+h, x:x+w]
# 		# roi_color = img[y:y+h, x:x+w]

# 		# # Detects eyes of different sizes in the input image
# 		# eyes = eye_cascade.detectMultiScale(roi_gray)

# 		#To draw a rectangle in eyes
# 		# for (ex,ey,ew,eh) in eyes:
# 		# 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

# 	# Display an image in a window
# 	cv2.imshow('img',img)
# 	cv2.imshow('gray',gray)

# 	# Wait for Esc key to stop
# 	k = cv2.waitKey(30) & 0xff
# 	if k == 27:
# 		break
    #pinout code
# Display the output
# cv2.imshow('img', img)
# cv2.imshow('img1', gray)
cv2.waitKey()



