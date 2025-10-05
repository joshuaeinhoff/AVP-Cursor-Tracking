import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

tracker = cv.TrackerGOTURN.create()

# Read video 
video = cv.VideoCapture("../img/ShortPositionTest.mp4") 
# Exit if video not opened 
if not video.isOpened():     
     print("Could not open video")
     sys.exit() 
# Read first frame 
ok,frame = video.read() 
if not ok:
     print("Cannot read video file")
     sys.exit()

# Define a bounding box 
# bbox = (276, 23, 86, 320) 
# Uncomment the line below to select a different bounding box 
bbox = cv.selectROI(frame, False) 

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
 
    # Start timer
    timer = cv.getTickCount()
 
    # Update tracker
    ok, bbox = tracker.update(frame)
 
    # Calculate Frames per second (FPS)
    fps = cv.getTickFrequency() / (cv.getTickCount() - timer);
 
    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv.putText(frame, "Tracking failure detected", (100,80), cv.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
    # Display tracker type on frame
    cv.putText(frame, "GOTURN Tracker", (100,20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
 
    # Display FPS on frame
    cv.putText(frame, "FPS : " + str(int(fps)), (100,50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
    # Display result
    cv.imshow("Tracking", frame)
  
    # Exit if ESC pressed
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break
	
# Initialize tracker with first frame and bounding box 
ok = tracker.init(frame,bbox)

'''
img = cv.imread('../img/DetectionTestframeBestcase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
#cv.convertScaleAbs(img2, alpha=1.2,beta=0)



img = cv.imread('../img/DetectionTestframeOcclusioncase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img3 = img.copy()
#cv.convertScaleAbs(img3, alpha=1.2,beta=0)



img = cv.imread('../img/DetectionTestframeWorstcase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img4 = img.copy()
#cv.convertScaleAbs(img4, alpha=1.2,beta=0)



template = cv.imread('../img/ViewIndicator.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path exists()"
w, h = template.shape[::-1]

methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
            'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']


# Testing different image cases.
# Bestcase:
for meth in methods:
    img = img2.copy()
    method = getattr(cv, meth)

    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.title('Detection Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()

# Occlusion case:
for meth in methods:
    img = img3.copy()
    method = getattr(cv, meth)

    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.title('Detection Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()

# potential worst case:
for meth in methods:
    img = img4.copy()
    method = getattr(cv, meth)

    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.title('Detection Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()


orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(template,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)

result = cv.drawMatches(template,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(result),plt.show()
'''
'''
sift = cv.SIFT_create()
 
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(template,None)
kp2, des2 = sift.detectAndCompute(img2,None)
 
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
 
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
 
# cv.drawMatchesKnn expects list of lists as matches.
result = cv.drawMatchesKnn(template,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
 
plt.imshow(result),plt.show()
'''
