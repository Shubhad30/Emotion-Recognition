import cv2

faceCascade = cv2.CascadeClassifier('F:/pythonproject/haarcascade_frontalface_default.xml')

def find_faces(image):
    faces_coordinates = _locate_faces(image)
    cutted_faces = [image[y:y + h, x:x + w] for (x, y, w, h) in faces_coordinates]
    normalized_faces = [_normalize_face(face) for face in cutted_faces]
    return zip(normalized_faces, faces_coordinates)

def _normalize_face(face):
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face, (640, 490))
    return face

def _locate_faces(image):
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(70, 70)
    )
    return faces

if __name__ == "__main__":
    image = cv2.imread('F:/pythonproject/sorted_set/happy/14_005_00000017.png')
    cv2.imshow("face", image)

    for index, face in enumerate(find_faces(image)):
        cv2.imshow("face %s" %index[0], face[0])
        print(index)

    cv2.waitKey(0)
