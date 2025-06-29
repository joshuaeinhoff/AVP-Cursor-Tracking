# AVP-Cursor-Tracking
Goal:
Trying to figure out how to track the cursor from the apple vision pro, indicating where the user is looking. Initial idea is to parse each frame and "compare" a block of pixels with the cursor. I think in this case colour information is relevant since otherwise it can collide with other UI elements. 
### Example 1: Recording of AVP view with cursor enabled
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracker/blob/main/img/DetectionTestframeBestcase.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/img/DetectionTestframeBestcase.png)
### Example 2: Cursor
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/img/ViewIndicator.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/img/ViewIndicator.png)

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
