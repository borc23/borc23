import cv2
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Read image from specified file name
   # filename = ''
   # angle ='' either 0, 90, 180, 270
    try:
        filename = sys.argv[1]
        ref_angle = int(sys.argv[2])

    except IndexError:
        print("argument usage: MaskCenter.py <filename> <reference angle>")
        sys.exit(1)
    img = cv2.imread(filename)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, 0, (0, 255, 0), 2)

    M = cv2.moments(contours[0])

    cx1 = int(round(M['m10'] / M['m00']))
    cy1 = int(round(M['m01'] / M['m00']))

    cx2 = int(img.shape[0]/2) #Center of image
    cy2 = int(img.shape[1]/2) #Center of image

    cv2.line(img, (256, 0), (256, 512), (255, 255, 0), thickness=1)
    cv2.line(img, (0, 256), (512, 256), (255, 255, 0), thickness=1)
    cv2.putText(img,"0", (500,254,),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
    cv2.putText(img,"90", (260,20,),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
    cv2.putText(img,"180", (12,254,),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
    cv2.putText(img,"270", (260,500,),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

    def angle_fn(a):
        w = 0
        h = 0
        if int(a) == 0:
            print("\nAngle 0 was selected")
            w = img.shape[0]/4
            h = 0
        elif int(a) == 90:
            print("\nAngle 90 was selected")
            w = 0
            h = img.shape[0]/4
        elif int(a) == 180:
            print("\nAngle 180 was selected")
            w = -img.shape[0]/4
            h = 0
        elif int(a) == 270:
            print("\nAngle 270 was selected")
            w = 0
            h = -img.shape[0]/4

        print(f"w: {w}, h: {h}")
        return [w, h]

    def angle_between(p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    a = np.array([cx1 - cx2, cy2 - cy1])
    b = np.array([cx2, cy2])
    c = np.array([angle_fn(ref_angle)[0], angle_fn(ref_angle)[1]])
    angle = angle_between(a, c)
    print("\n Angle between reference point and mask center is %.2f degrees" % angle)
    

    def draw_it(k):
        '''
        :param k:
        k -> int
        :return:
        r -> float
        l -> float
        '''

        r = 0
        l = 0
        if int(k) == 0:
            r = img.shape[0]-img.shape[0] / 4
            l = img.shape[0]/2
        elif int(k) == 90:
            r = img.shape[0]/2
            l = img.shape[0] / 4
        elif int(k) == 180:
            r = img.shape[0] / 4
            l = img.shape[0] / 2
        elif int(k) == 270:
            r = img.shape[0] / 2
            l = img.shape[0]-img.shape[0] / 4
        return [r, l]

    axes = (img.shape[0] / 4, img.shape[0] / 4)
    cv2.circle(img, (int(draw_it(ref_angle)[0]), int(draw_it(ref_angle)[1])), 3, (0, 0, 255), -1)
    cv2.circle(img, (round(M['m10'] / M['m00']), round(M['m01'] / M['m00'])), 3, (0, 0, 255), -1)
    cv2.ellipse(img, (256, 256), axes=(128, 128), angle=0.0, startAngle=-ref_angle, endAngle=-ref_angle-angle, color=(0, 0, 255))
    cv2.line(img, (cx2, cy2), (cx1, cy1), (0, 0, 255),1)
    cv2.imshow("outline contour & centroid", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    input("Press any key.")
    plt.close("all")
    sys.exit(0)
