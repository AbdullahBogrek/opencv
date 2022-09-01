import cv2 as cv

#variables
record = False
gry = False
value = "" # this is for recording

filename = 'output.mp4'
fps = 20.0

cap = cv.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(filename, fourcc, 10, (frame_width,frame_height))

if (cap.isOpened() == False): 
    print("The camera cannot be read. Please check camera connection or use another camera")

while(True):
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    k = cv.waitKey(1)

    if ret == True:

        if gry == True:
            cv.imshow('frame',gray)

        else:
            cv.imshow('frame',frame)

        if k == ord("g"):
            gry = True
        
        if k == ord("n"):
            gry = False
        
        # press space key to start recording
        if k%256 == 32:
            record = True

        if record:
            out.write(frame) 
            print("Recording...")

        # press q key to close the program
        if k & 0xFF == ord('q'):
            break

    else:
        print("There is a problem. Please try again.")
        break  

cap.release()
out.release()

cv.destroyAllWindows()