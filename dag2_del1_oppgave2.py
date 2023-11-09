import cv2 # pip install opencv-python-headless or conda install opencv 
from matplotlib import pyplot as plt

# Due to jupyters architecture we can not use cv2.imshow() so we create a helper method to utilize pyplot.
def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.show()

# Create the haar cascade
cascPath = "/kaggle/input/bildebehandling/haarcascade_frontalface_default.xml" # Just an xml file that contains data about a face.
faceCascade = cv2.CascadeClassifier(cascPath) # Load the cascade into memory.

face_image_kode24 = cv2.imread("/kaggle/input/fjas-og-tull/kode24_meta_og_google.jpg") # cv2 read in BGR format.
gray_face_image_kode24 = cv2.cvtColor(face_image_kode24, cv2.COLOR_BGR2GRAY)

kode24_faces = faceCascade.detectMultiScale(
    gray_face_image_kode24,
    scaleFactor=1.1,
    minNeighbors=1,  # Endra den her, då endra det seg kor mange fjes den fant
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

# Draw a rectangle around the faces
print(kode24_faces)
for (x, y, w, h) in kode24_faces:
    cv2.rectangle(face_image_kode24, (x, y), (x+w, y+h), (0, 255, 0), 1)

show_image(cv2.cvtColor(face_image_kode24, cv2.COLOR_BGR2RGB), "Number of faces found = %s" % len(kode24_faces))
show_image(cv2.cvtColor(gray_face_image_kode24, cv2.COLOR_BGR2RGB), "Greyscale...")