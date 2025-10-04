# AVP-Cursor-Tracking
Goal:
Trying to figure out how to track the cursor from the apple vision pro, indicating where the user is looking.

### Example 1: Recording of AVP view with cursor enabled
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracker/blob/main/data/ReadMeFiles/DetectionTestframeBestcase.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/data/ReadMeFiles/DetectionTestframeBestcase.png)
### Example 2: Cursor
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/data/ReadMeFiles/ViewIndicator.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/data/ReadMeFiles/ViewIndicator.png)

# Approach 1: Using only OpenCV
## Best case
- TM_CCOEFF -> Failed | Mismatch
- TM_CCOEFF_NORMED -> Success
- TM_CCORR -> Failed | Mismatch
- TM_CCORR_NORMED -> Success
- TM_SQDIFF -> Success
- TM_SQDIFF_NORMED -> Success


## Occlusion case
- TM_CCOEFF -> Failed | Mismatch
- TM_CCOEFF_NORMED -> Failed | Mismatch
- TM_CCORR -> Failed | Mismatch
- TM_CCORR_NORMED -> Failed | Mismatch
- TM_SQDIFF -> Failed | Mismatch
- TM_SQDIFF_NORMED -> Failed | Mismatch

## Worst case
- TM_CCOEFF -> Failed | Mismatch
- TM_CCOEFF_NORMED -> Failed | Mismatch
- TM_CCORR -> Failed | 
- TM_CCORR_NORMED -> Failed | Mismatch
- TM_SQDIFF -> Failed | Mismatch
- TM_SQDIFF_NORMED -> Failed | Mismatch

---

# Approach 2: Using OpenCV and Ultralytics YOLO
Since the first approach did not achieve the required accuracy a different approach had to be found.

1. Using captured video material similar to the user test environment 431 training images were generated
2. Labeling images with bounding boxes in Label Studio
3. Training data in google colab using Ultralytics yolo11m
4. Using detection model for futher analysis in python

## Results
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/data/ReadMeFiles/CursorAvatarTracking.gif](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/data/ReadMeFiles/CursorAvatarTracking.gif)
## Training Results
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/model/y11m_800/results.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/model/y11m_800/results.png)