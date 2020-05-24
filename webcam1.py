from cv2 import WINDOW_NORMAL
import random, glob
from pygame import mixer
import cv2
import time
from face_detect import find_faces
from image_commons import nparray_as_image, draw_with_alpha

emotions = ['neutral', 'anger','happy', 'sadness']

def _load_emoticons(emotions):
    return [nparray_as_image(cv2.imread('graphics/%s.png' % emotion, -1), mode=None) for emotion in emotions]


def show_webcam_and_run(model, emoticons, window_size=None, window_name='webcam', update_time=10):
    cv2.namedWindow(window_name, WINDOW_NORMAL)
    if window_size:
        width, height = window_size
        cv2.resizeWindow(window_name, width, height)

    vc = cv2.VideoCapture(0)
    if vc.isOpened():
        read_value, webcam_image = vc.read()
    else:
        print("webcam not found")
        return
    cs,ch,cn,ca=0,0,0,0
    while read_value:
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):
            prediction = model.predict(normalized_face)  
            print(prediction[1])
            if(prediction[1]>700 and prediction[1]<860 ):
                prediction=0
                cn+=1;
                if(cn>=3):
                    pattern = "songs/neutral/*" 
                    filename = random.choice(glob.glob(pattern))
                    print(filename)
                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play(-1,0.0)
                    time.sleep(10)
                    mixer.music.stop()
                    cn=0
            elif(prediction[1]>420 and prediction[1]<650):
                prediction=2
                ch+=1;
                if(ch>=3):
                    pattern = "songs/happy/*" 
                    filename = random.choice(glob.glob(pattern))
                    print(filename)
                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play(-1,0.0)
                    time.sleep(10)
                    mixer.music.stop()
                    ch=0
            elif(prediction[1]>860 and prediction[1]<1300):
                prediction=3
                cs+=1;
                if(cs>=3):
                    pattern = "songs/sad/*" 
                    filename = random.choice(glob.glob(pattern))
                    print(filename)
                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play(-1,0.0)
                    time.sleep(10)
                    mixer.music.stop()
                    cs=0
            elif(prediction[1]>1000 and prediction[1]<3300):
                prediction=1
                ca+=1;
                if(ca>=3):
                    pattern = "songs/anger/*" 
                    filename = random.choice(glob.glob(pattern))
                    print(filename)
                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play(-1,0.0)
                    time.sleep(10)
                    mixer.music.stop()
                    ca=0
            else:
                prediction=0
            time.sleep(2)
            image_to_draw = emoticons[prediction]
            font=cv2.FONT_HERSHEY_SIMPLEX
            text=emotions[prediction]
            webcam_image=cv2.putText(webcam_image,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
            draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
            time.sleep(2)
        cv2.imshow(window_name, webcam_image)
        read_value, webcam_image = vc.read()
        key = cv2.waitKey(update_time)

        if key == 27:  
            break

    cv2.destroyWindow(window_name)


#if __name__ == '__main__':
def fn1():
    emotions = ['neutral', 'anger','happy', 'sadness']
    emoticons = _load_emoticons(emotions)

    fisher_face = cv2.face.FisherFaceRecognizer_create()
    fisher_face.read('F:/pythonproject/emotion_detection_model.xml')

    window_name = 'WEBCAM (press ESC to exit)'
    show_webcam_and_run(fisher_face, emoticons, window_size=(900, 700), window_name=window_name, update_time=8)

