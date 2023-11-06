import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video not found \n {path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    while True:
        status,frame=video.read()
        if not status:
            print("Video could not be loaded")
            break
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)== ord('q'):
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    videofile=r"C:\Users\pc\Videos\Thor Love and Thunder (2022) Dual Audio {HindiEnglish} 1080p CAMRip TheMoviesflix.ac.mkv"
    load_video(videofile)