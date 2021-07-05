---
layout: post
title: "3D Mapping with Robotics and Image Processing"
description: "Stereo camera is probably the easist way to reconstruct the world around you."
categories: diode
thumbnail: "3d-imaging-using-stereo-vision.png"
year: 2021
---

### Mentors
-   Chandravaran Kunjeti
-   Sai Kumar Dande

### Members
-   Soma Anil Kumar
-   V Kartikeya
 
# Abstract
3D mapping is a very useful technology in present days. One of the best  benefits of 3D mapping  is that it provides the latest technical methods for  visualization and gathering information. Knowledge visualization and science  mapping become easier when a 3D map is available for the area under study.  In this project we want to implement a robot which can map a 3D model of a  room or an area and simultaneously avoid mapping humans or any other  animal. We have implemented our code from scratch and have optimized the  code to give us better features and faster computational time.

# Theory
There are various ways which can be used to find the depth of an object like LIDAR, InfraRed, Stereo matching etc.
In this project we use the stereo based approach to calculate the depth of an object. **Stereo matching** aims to identify the corresponding points and retrieve their displacement to reconstruct the geometry of the scene as a depth map. 

Let us go through the different topics needed for stereo vision one by one

## Stereo camera calibration
If we want understand the point in an image we need to know what transforms are involved in the process, there are many types of parameters which are as follows:
### Extrinsic parameters
- Rotation matrix
- Translation matrix

### Intrinsic parameters
- Intrinsic matrix
- Focal length
- Optical centre

![](/virtual-expo/assets/img/diode/3dmapping_img1.PNG)

Stereo camera calibration info is used for **rectification**.
This rectification process removes lens distortion, and turns the stereo pair into standard form where images are perfectly aligned horizontally.  After rectifiying both the left and right images of the stereo camera, calculating the disparity map is a simple search for a pixel in the left image along the corresponding horizontal epipolar line in the right image. There are various methods that are used for pixel matching which will be discussed in the later sections.


![](/virtual-expo/assets/img/diode/3dmapping_img2.PNG)

## Disparity
After the images are rectified, the disparity between the left and right images is found. **Disparity** refers to the distance between two corresponding points in the left and right image of a stereo pair. Disparity between the left and right image occurs because the cameras are placed with a certain amount of distance between them. This disparity is more for the objects that are closer to the camera than the objects which are farther. Using this principle, we can find the **depth map** or the **disparity map** of the images.

![](/virtual-expo/assets/img/diode/3dmapping_img4.PNG)
![](/virtual-expo/assets/img/diode/3dmapping_img3.PNG)
Depth of the images is then found using the formula 

### Depth = Base_length*Focal_length/Disparity
where 

 **Base_length = Distance between left and right camera**
 ![](/virtual-expo/assets/img/diode/3dmapping_img5.PNG)

 Disparity map is found through ***Multiple Block Matching***.
 **Block matching** is where we use a block of pixels for mathcing, instead of trying to find a single pixel in the right image. Here we take a certain number of pixels surrounding the pixel in the left image and try to find a closest match for the block of pixels in the right image. After finding the right match, the disparity is calculated by using the formula XL-XR, where XL is the horizontal distance of the pixel in the left image and XR is the match that is found in the right image.
 ![](/virtual-expo/assets/img/diode/3dmapping_img6.PNG)
 **Multiple block matching** takes blocks of different sizes and shapes and integrates them for a better disparity map. Single block matching technique does not work well in case where the disparity values within the matching block vary drastically, for example in the case of a highly slanted surface like road, it becomes difficult using single block matching technique. The problem can be resolved by using blocks of different sizes like vertical block or horizontal block which give better correlation or matches as compared to single block matching. 
 ![](/virtual-expo/assets/img/diode/3dmapping_img7.PNG)
 The closest match between the blocks of the left and the right image can be found through three different methods namely **Sum of Absolute Difference**(SAD), **Normalized Correlation**(NC), and **Census Transform**(CT).

  ![](/virtual-expo/assets/img/diode/3dmapping_img8.PNG)

 # Results obtained

 ![](/virtual-expo/assets/img/diode/3dmapping_img9.PNG)
The results shown above are obtained when we use SAD and LCDM to obtain the disparity map using the single block matching method.

 ![](/virtual-expo/assets/img/diode/3dmapping_img10.PNG)
 This image shows us the results of the SAD and LCDM but using multi block matching method. 

 ![](/virtual-expo/assets/img/diode/3dmapping_img11.PNG)
 The above obtained disparity maps are from Normalised correlation  and filtering by LCDM.

 ![](/virtual-expo/assets/img/diode/3dmapping_img12.PNG)
 The above image gives us the results obtained from using cencus transform, we can absorve that initially it does not give very good results, but on applying LCDM we see the error dropping, and giving us the best results. 

 ![](/virtual-expo/assets/img/diode/3dmapping_img13.PNG)
 As we are aiming for real time mapping we need to understand how long each method is taking, it was observed that pure SAD had the least time but not such a great result, so we went ahead and choose Cencus transform with LCDM as the time and the error percentage were within marginal values.

 ![](/virtual-expo/assets/img/diode/3dmapping_img14.PNG)
 This gives us a final view of all the methods and there percentage of BAD Error

![](/virtual-expo/assets/img/diode/3dmapping_img15.PNG)
The final output of the implementation on gazebo

Visualisation of the depth map using point cloud. 

<iframe src="https://www.youtube.com/embed/EbajTZuaTmA" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

 Result obtained (Left), Ground truth (Right)
 For visualisation we useed open3d to get an understanding how well the algorithm was performing when compared to the ground truth, and it can be seen that the performance was good. 

 Video of the robot moving around, taking images from the stereo camera and finding depth map

<iframe src="https://www.youtube.com/embed/3W8nz7LyGsw" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

 Due to the pandemic we choose to test our algorithm in a simulator called Gazebo, the whole robot was designed by us for this specific task. Due to the high computation time we only took pictures at different instances and found the depth map, we are working on making the algorithm faster!! 

### Thank You!!!

For the code of the Ros package used for this project please go to the following [GitHub](https://github.com/IEEE-NITK/3_D_Mapping_and_Localization.git) link. 
For the code of the various algorithms used for this project please go to the following [GitHub](https://github.com/chandravaran/Stereo_camera_3D_map_generation.git) link.  

# References
- L. Ma, J. Li, J. Ma and H. Zhang, "A Modified Census Transform Based on the Neighborhood Information for Stereo Matching Algorithm," 2013 Seventh International Conference on Image and Graphics, Qingdao, China, 2013, pp. 533-538, doi: 10.1109/ICIG.2013.113.

- N. Einecke and J. Eggert, "A multi-block-matching approach for stereo," 2015 IEEE Intelligent Vehicles Symposium (IV), Seoul, Korea (South), 2015, pp. 585-592, doi: 10.1109/IVS.2015.7225748. 

- Yang, Q., Yang, R., Davis, J., & Nister, D. (2007). Spatial-Depth Super Resolution for Range Images. 2007 IEEE Conference on Computer Vision and Pattern Recognition. doi:10.1109/cvpr.2007.383211

 

 




