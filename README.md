# Mediapipe Pose Comparison
A python program capable of comparing poses within images to check for accuracy, with the help of Mediapipe.
The pose used is the yoga 'Warrior Pose' as shown below.  
![istockphoto-1335980515-170667a](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/406839af-b879-4190-9035-580e942fd726)  
The /yoga directory contains image files that are used for comparison to a test image.
Each image file in this directory, has its distance from each landmark calculated as so  
<img width="524" alt="Screenshot 2023-09-25 191858" src="https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/a7082a1c-a859-476f-8d92-a810c1b6c5e9">  
The distance from landmark 0 to landmark 1 is calculated, then landmark 1 to landmark 2... until distances have been calculated between all 33 pose landmarks.  
  
This process takes place on every image within the /yoga directory. The minimum and maximum values are calculated for each distance amongst all images and used for comparison against the test pose.  

The test pose has its distance between all 33 landmarks calculated. If 75% of the landmark distances falls within the min max range calculated from the training images, then the pose is deemed accurate. If not, it is deemed unaccurate.
![](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/7c122c9f-d26d-4a3c-9229-d13baf249d72)
![](https://github.com/Amber-Abuah/Mediapipe-Pose-Comparison/assets/107321078/700e00ee-1ede-4e45-bd8b-5df2ce30acc9)
