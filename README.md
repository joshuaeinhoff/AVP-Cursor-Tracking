# AVP-Cursor-Tracking
Goal:
Trying to figure out how to track the cursor from the apple vision pro, indicating where the user is looking. Initial idea is to parse each frame and "compare" a block of pixels with the cursor. I think in this case colour information is relevant since otherwise it can collide with other UI elements. 
### Example 1: Recording of AVP view with cursor enabled
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracker/blob/main/DetectionTestframeBestcase.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/DetectionTestframeBestcase.png)
### Example 2: Cursor
![https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/ViewIndicator.png](https://github.com/joshuaeinhoff/AVP-Cursor-Tracking/blob/main/ViewIndicator.png)
