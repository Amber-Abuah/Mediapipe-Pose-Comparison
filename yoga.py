import cv2
import mediapipe as mp
import math
import os
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Training ----------------------------------------------------------------------------------------------------------------------------------------------
# Find distances between landmarks for all sample images
sample_image_folder = "yoga"
path = os.path.relpath(sample_image_folder)
files = os.listdir(path=path)

pose_images = []

for file in files:
    img = cv2.imread(path + "/" + file)
    pose_images.append(cv2.resize(img, (0,0), fx=1000/img.shape[0], fy=1000/img.shape[0])) # Resize all images to have same length

results = []

# Process all sample images and append to list
for image in pose_images:
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        result = holistic.process(image)
        mp_drawing.draw_landmarks(image, result.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        #cv2.imshow("result", image) # View landmark detections
        #cv2.waitKey(0)
        results.append(result)

def calculate_distance(c1, c2):
    return math.sqrt( c1.x ** 2  + c1.y ** 2 + c1.z ** 2 + c2.x ** 2 + c2.y ** 2 + c2.z ** 2)

# Calculate the min and max values for all possible landmark distances across all sample images
min_max_distances = []
landmarks_num = len(results[0].pose_landmarks.landmark)

for i in range (landmarks_num):
    if i != landmarks_num - 1:
        dist = []
        for j in range(len(results)):
            dist.append(calculate_distance(results[j].pose_world_landmarks.landmark[i], results[j].pose_landmarks.landmark[i + 1]))
        min_max = np.array([np.min(dist), np.max(dist)])
        min_max_distances.append(min_max)


# Testing --------------------------------------------------------------------------------------------------------------------------------------------------

# Load and find landmarks for test image
test_pose = cv2.imread("testpose.jpg")
test_pose = cv2.resize(test_pose, (0,0), fx=1000/test_pose.shape[0], fy=1000/test_pose.shape[0]) # Scale to similar size as training data

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    test_result = holistic.process(test_pose)
    mp_drawing.draw_landmarks(test_pose, test_result.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

# Calculate how many test image landmark distances fall within the min max range
in_range = 0
for i in range (len(test_result.pose_landmarks.landmark)):
    if i != len(test_result.pose_landmarks.landmark) - 1:
        distance = calculate_distance(test_result.pose_world_landmarks.landmark[i], test_result.pose_landmarks.landmark[i + 1])
        if distance >= min_max_distances[i][0] and distance <= min_max_distances[i][1]:
            in_range += 1


# If more than 75% of the distances lied between the min max range from the sample images, correct pose, else incorrect pose.
accuracy_threshold = 0.75
accurate_pose = in_range/len(test_result.pose_landmarks.landmark) > accuracy_threshold

# Display image with accuracy result
cv2.rectangle(test_pose, (0,0), (350, 75), (245, 117,16), -1)
cv2.putText(test_pose, "Accurate" if accurate_pose else "Inaccurate", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4, cv2.LINE_AA)
cv2.imshow("Pose", test_pose)
cv2.waitKey(0)