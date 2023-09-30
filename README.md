# Mediapipe Pose Comparison

A python program capable of comparing poses within images to check for accuracy, with the help of Mediapipe.

This example compares the yoga 'Warrior Pose' as shown below.  
![istockphoto-1335980515-170667a](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/b0f6a149-8c1b-4f31-adce-520cb3164498)  
The /yoga directory contains image files that are used for comparison to a test image.
  
Each image file in this directory, has its distance from each landmark calculated as so
<img width="524" alt="Screenshot 2023-09-25 191858" src="https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/e7473c3f-e588-4f6a-a878-9eba003774b6">  
The distance from landmark 0 to landmark 1 is calculated, then landmark 1 to landmark 2... until distances have been calculated between all 33 pose landmarks.  
  
This process takes place on every image within the /yoga directory.
We then store the minimum and maximum values calculated for each distance amongst all images and use this for comparison for the test pose.  

The test pose has its distance between all 33 landmarks calculated. If 75% of the landmark distances falls within the min max range calculated from the training images, then the pose is deemed accurate. If not, it is deemed unaccurate.

![out](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/19eb32c5-4fd8-4182-b232-1f10d79bc1ea)
![out](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/b64e69d9-54de-43d9-933a-45d1c8d8823c)
