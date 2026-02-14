import cv2
import os
import shutil
import numpy as np

import mediapipe as mp

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array


print("Loading models...")

# face detection - mediapipe
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1)

# animal detection - mobilenet
animal_model = MobileNetV2(weights="imagenet")

# smile detection - opencv haar cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# eye detection - opencv haar cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)


tags = [
    "Eyes_Closed",
    "Blurry",
    "Smiled",
    "Solo",
    "Group",
    "No_Human",
    "Animals"
]

os.makedirs("output", exist_ok=True)

for t in tags:
    os.makedirs("output/" + t, exist_ok=True)


# detect blurred images
def is_blurry(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    return score < 80


# detect number of faces in the iamge
def count_faces(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = mp_face.process(rgb)

    if result.detections:
        return len(result.detections)
    return 0


# detect smile in the image
def has_smile(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(
        gray,
        scaleFactor=1.7,
        minNeighbors=20
    )

    return len(smiles) > 0


# detect closed eyes in the image
def eyes_closed(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    return len(eyes) == 0


# detect animals in the image
def is_animal(img):
    resized = cv2.resize(img, (224, 224))
    arr = img_to_array(resized)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)

    preds = animal_model.predict(arr, verbose=0)
    label = decode_predictions(preds, top=1)[0][0][1]

    if "dog" in label or "cat" in label or "animal" in label:
        return True
    return False


# sorting

dataset_folder = "dataset"

print("\nSorting images...\n")

for file in os.listdir(dataset_folder):

    img_path = os.path.join(dataset_folder, file)
    img = cv2.imread(img_path)

    if img is None:
        continue

    face_count = count_faces(img)
    print(file, "Faces Detected:", face_count)

    # no human found inthe image
    if face_count == 0:
        if is_animal(img):
            shutil.copy(img_path, "output/Animals/")
            print(file, "→ Animals")
        else:
            shutil.copy(img_path, "output/No_Human/")
            print(file, "→ No_Human")
        continue

    # if greater than or equal to 2 faces found in the image
    # then it is given to group folder
    if face_count >= 2:
        shutil.copy(img_path, "output/Group/")
        print(file, "→ Group")
        continue

    # if only one face is found in the image
    # then it is given to solo folder
    if face_count == 1:
        shutil.copy(img_path, "output/Solo/")
        print(file, "→ Solo")

    # if image is blurry
    # then it is passed to blurry folder
    if is_blurry(img):
        shutil.copy(img_path, "output/Blurry/")
        print(file, "→ Blurry")

    # if image has smile then itis passed to smiled folder
    if has_smile(img):
        shutil.copy(img_path, "output/Smiled/")
        print(file, "→ Smiled")

    # closed eyes
    if eyes_closed(img):
        shutil.copy(img_path, "output/Eyes_Closed/")
        print(file, "→ Eyes Closed")


print("\n Sorting Completed Successfully!")
print("Check the output/ folder.")
