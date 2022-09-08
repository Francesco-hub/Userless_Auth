import sys
import easygui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import os
import PIL


def confidence(img, template):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    conf = res.max()
    return np.where(res == conf), conf


Tk().withdraw()
filename = askopenfilename()
sample = cv2.imread(filename)

best_score = 0
best_confidence = 0
best_confidence_file = None
second_best_confidence = 0
second_best_confidence_file = None
third_best_confidence = 0
third_best_confidence_file = None
filename = None
image = None
kp1, kp2, mp = None, None, None
h, w, _ = sample.shape


counter = 0
for file in [file for file in os.listdir("assets/SOCOFing/Registered")]:
    if counter % 10 == 0:
        print(counter)
    counter += 1
    fingerprint_image = cv2.imread("assets/SOCOFing/Registered/"+ file)
    temp_confidence = (cv2.matchTemplate(fingerprint_image, sample, cv2.TM_CCOEFF_NORMED).max())
    print(temp_confidence)
    if(temp_confidence > best_confidence):
        best_confidence = temp_confidence
        best_confidence_file = file
    elif(temp_confidence > second_best_confidence):
        second_best_confidence = temp_confidence
        second_best_confidence_file = file
    elif(temp_confidence > third_best_confidence):
        third_best_confidence =temp_confidence
        third_best_confidence_file = file
    sift = cv2.SIFT_create()


    keypoints_1 , descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2 , descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
                                    {}).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []

    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    keypoints = 0
    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    if len(match_points)/ keypoints * 100 > best_score:
            best_score = len(match_points) / keypoints * 100
            filename = file
            image = fingerprint_image
            kp1, kp2, mp = keypoints_1, keypoints_2, match_points

print ("BEST CONFIDENCE: " + str(best_confidence))
print ("SECOND BEST CONFIDENCE: " + str(second_best_confidence))
print ("THIRD BEST CONFIDENCE: " + str(third_best_confidence))
print ("BEST CONFIDENCE FILE: " +str(best_confidence_file))
print ("SECOND BEST CONFIDENCE FILE: " +str(second_best_confidence_file))
print ("THIRD BEST CONFIDENCE FILE: " +str(third_best_confidence_file))
print("BEST MATCH: " + str(filename))
print("SCORE: " + str(best_score))
cv2.waitKey(0)

if(filename==None):
    cv2.imwrite(os.path.join("assets/SOCOFing/Registered", "Test1.BMP"), sample)
    #(cv2.imwrite(os.path.join(path, 'doll.jpg'), image))
'''result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
result = cv2.resize(result, None, fx=4, fy=4)
cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


