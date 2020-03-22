"""
1. get known images
2. load known images
3. analyze known images (create vector)
4. get unknown image
5. load unknown image
6. analyze unknown image
7. compare uknown image with known images (compare vectors)
8. print the identified person 

1. create an empty list
2. load the image
2.5. encode the image
3. put encoded image in the list """ 

# import the libraries
import os
import face_recognition




images = os.listdir('picturesforcode')




print(images)

known_images = []

for imagefile in images:
    print("the imagefile is", imagefile)
    known_image = face_recognition.load_image_file('picturesforcode/'+imagefile)
    print(known_image)
    print("going to encode image")
    known_image_encoded = face_recognition.face_encodings(known_image)[0]
    print(known_image_encoded) 
    known_images.append(known_image_encoded)
print("print known images", known_images)

unknown_image = face_recognition.load_image_file('abigail2.jpg')
print(unknown_image)
unknown_image_encoded = face_recognition.face_encodings(
unknown_image)[0]
print("unknown image encoded")
print(unknown_image_encoded)

results = face_recognition.compare_faces(known_images, unknown_image_encoded)
print(results)

results.index(True)
index_of_true = results.index(True)

name = images[index_of_true]


print(os.path.splitext(name)[0])

(''') 
1. find location of true in the results
2. find same number in images list
3. print the name of file ? (''')
