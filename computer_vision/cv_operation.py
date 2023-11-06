import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video not found \n {path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    cv2.namedWindow("Video")
    cv2.createTrackbar("ksize","Video",3,100,lambda x:None)
   
    while True:
        status,frame=video.read()
        height,width,_=frame.shape
        #print(height,width)
        if not status:
            print("Video could not be loaded")
            break


        #operations
        # 1.resize
        frame=cv2.resize(frame,(None,None),fx=0.5,fy=0.5)
        # 2. convert to grayscale
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 3. blur
        ksize=cv2.getTrackbarPos("ksize","Video")
        try:
            frame=cv2.GaussianBlur(frame,(ksize,ksize),0)
        except:
            pass
        # 4. add text
        cv2.putText(
            frame,
            "thor love and thunder",
            (width//2-500,height//5),#coordinates/orign
            cv2.FONT_HERSHEY_SIMPLEX,#font face
            1,#fontsize
            (0,0,255),
            2#thickness
        )

        # 5. add graphics




        cv2.imshow("Video",frame)
        if cv2.waitKey(1)== ord('q'):
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    videofile=r"C:\Users\pc\Videos\Thor Love and Thunder (2022) Dual Audio {HindiEnglish} 1080p CAMRip TheMoviesflix.ac.mkv"
    load_video(videofile)