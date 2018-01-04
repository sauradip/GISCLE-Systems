#Step 1:- Import the required packages
import cv2
# Step 2:- Create a VideoCapture object to capture the video
cap=cv2.VideoCapture("v1.mp4")# COSTA.mp4 is the filename of the video along with the format name
fourcc = cv2.VideoWriter_fourcc(*'XVID') # For fourcc visit fourcc.org
out=cv2.VideoWriter('ConvertedVideo.mp4',fourcc,20,(1920,1080))
    
#Step 3: Return the video frame by frame
while(cap.isOpened()):
    ret ,frame=cap.read()
    if ret==True:
        #Step 4:- Displaying it to the user after performing color inversion
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Step 5:- Write the file into the disk with specific format
        cv2.imshow("DIPLAYING TO USER",gray)
        out.write(gray)
        
        if cv2.waitKey(25) & 0xFF==ord('a'):
            break
    else:
        break
# Step 6 : Release everything after use
cap.release()
out.release()
cv2.destroyAllWindows()
    
