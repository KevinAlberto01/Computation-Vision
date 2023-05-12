import cv2 # import the library de Open vc2 
 
cam = cv2.VideoCapture(0) # save in a variable the video camera 

while True: # While the video camera is activate
    ret, frame = cam.read() # Display the resulting frame
    cv2.imshow('webCam',frame) # Show the value of the variable 
    if (cv2.waitKey(1) == ord('s')): # set the exit buttom 
        break

cam.release() # Release the cap object
cv2.destroyAllWindows() # Destroy all windows 

  
