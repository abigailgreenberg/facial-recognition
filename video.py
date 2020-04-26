'''
0. install cv2
1. load and encode known images
2. load video
3. go through every frame in video
4. encode frame by frame
4a. check if there is a face in the frame
5. if yes, compare to known images
6. print when match is found '''



# import the libraries
import os
import face_recognition
import cv2 


images = os.listdir('picturesforcode')



#print(images)

known_images = []


image_faces = [imagefile for imagefile in images if not imagefile.startswith('.') ]
for imagefile in image_faces:
    known_image = face_recognition.load_image_file('picturesforcode/'+imagefile)
    known_image_encoded = face_recognition.face_encodings(known_image)[0] 
    known_images.append(known_image_encoded)


input_movie = cv2.VideoCapture("videosforcode/abigail.mp4")



while True:
    frame_left, frame = input_movie.read()
    if frame_left == False: 
        break 
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame) 
    rgb_frame_encoded = face_recognition.face_encodings(rgb_frame, face_locations)
    if len(rgb_frame_encoded) != 0:
        print("found a face")
        results = face_recognition.compare_faces(known_images, rgb_frame_encoded[0], tolerance=0.5)
        try:
            results.index(True)
            index_of_true = results.index(True)
            name = image_faces[index_of_true]
            print(os.path.splitext(name)[0])
        except ValueError:
            print("no match")
(''') 
1. find location of true in the results
2. find same number in images list
3. print the name of file ? (''')
