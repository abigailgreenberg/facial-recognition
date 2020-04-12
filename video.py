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




print(images)

known_images = []

for imagefile in images:
    print("the imagefile is", imagefile)
    if imagefile.startswith('.'): 
        continue
    known_image = face_recognition.load_image_file('picturesforcode/'+imagefile)
    #print(known_image)
    #print("going to encode image")
    known_image_encoded = face_recognition.face_encodings(known_image)[0]
    #print(known_image_encoded) 
    known_images.append(known_image_encoded)
#print("print known images", known_images)

input_movie = cv2.VideoCapture("videosforcode/abigailgreenberg.MP4")



while True:
    frame_left, frame = input_movie.read()
    #print(frame_left, frame)
    if frame_left == False: 
        break 
    rgb_frame = frame
    #rgb_frame = frame[:, :, ::-1]
    #print(rgb_frame)
    face_locations = face_recognition.face_locations(rgb_frame)
    print(face_locations)
    rgb_frame_encoded = face_recognition.face_encodings(rgb_frame, face_locations)
    if len(rgb_frame_encoded) != 0:
        print("found a face")
        results = face_recognition.compare_faces(known_images, rgb_frame_encoded)
        #print(results)
        results.index(True)
        index_of_true = results.index(True)
        name = images[index_of_true]
        print(os.path.splitext(name)[0])

(''') 
1. find location of true in the results
2. find same number in images list
3. print the name of file ? (''')
