import glob
import os
from shutil import copyfile

import cv2

from face_detect import find_faces


def remove_old_set(emotions):
    print("Removing old dataset")
    for emotion in emotions:
        filelist = glob.glob("data/sorted_set/%s/*" % emotion)
        for f in filelist:
            os.remove(f)


def harvest_dataset(emotions):
    print("Harvesting dataset")
    participants = glob.glob('data/source_emotions/*')  

    for participant in participants:
        neutral_added = False

        for sessions in glob.glob("%s/*" % participant):  
            for files in glob.glob("%s/*" % sessions):
                current_session = files[20:-30]
                file = open(files, 'r')
                
                emotion = int(float(file.readline()))
                images = glob.glob("data/source_images/%s/*" % current_session)

                source_filename = images[-1].split('/')[-1]
                destination_filename = "data/sorted_set/%s/%s" % (emotions[emotion], source_filename)
                copyfile("data/source_images/%s/%s" % (current_session, source_filename), destination_filename)

                if not neutral_added:
                    source_filename = images[0].split('/')[-1]
                    destination_filename = "data/sorted_set/neutral/%s" % source_filename
                    copyfile("data/source_images/%s/%s" % (current_session, source_filename), destination_filename)
                    neutral_added = True


def extract_faces(emotions):
    print("Extracting faces")
    for emotion in emotions:
        photos = glob.glob('data/sorted_set/%s/*' % emotion)

        for file_number, photo in enumerate(photos):
            frame = cv2.imread(photo)
            normalized_faces = find_faces(frame)
            os.remove(photo)

            for face in normalized_faces:
                try:
                    cv2.imwrite("data/sorted_set/%s/%s.png" % (emotion, file_number + 1), face[0])
                except:
                    print("error in processing %s" % photo)


if __name__ == '__main__':
    emotions = ['neutral', 'anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness', 'surprise']
    remove_old_set(emotions)
    harvest_dataset(emotions)
    extract_faces(emotions)
