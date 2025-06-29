# AVP-Cursor-Tracking
Goal:
Trying to figure out how to track the cursor from the apple vision pro, indicating where the user is looking. Initial idea is to parse each frame and "compare" a block of pixels with the cursor. I think in this case colour information is relevant since otherwise it can collide with other UI elements. 

<p align="center">
    <img src="https://github.com/joshuaeinhoff/AVP-Cursor-Tracker/DetectionTestframeBestcase.png">
</p>