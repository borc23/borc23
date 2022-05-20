FIND ANGLE OF THE OBJECT
This program helps with finding the center of an object's mask relative to your reference angle. This was done for computer vision task in industry where the computer had to know at what angle is the object rotated so that the later automation, after object classification, is done properly.
Angle is calculated counterclockwise. Dot on the output image represents the reference point from where the code


REQUIREMENTS
cv2 == 4.5.1
numpy == 1.18.5
matplotlib == 3.5.1
sys

HOW TO RUN 
Open folder in code editor(I used VS Code). Open terminal then run the code with this line:
                python MaskCenter.py "Image path" ref_angle 
where ref_angle is an integer either 0 or 90 or 180 or 270

EXAMPLE
In folder Result there is a .png of a code run with this command:
             python MaskCenter.py "Images/34273_processed.png" 180