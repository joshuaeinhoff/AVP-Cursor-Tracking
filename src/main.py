import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../img/DetectionTestframeBestcase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
cv.convertScaleAbs(img2, alpha=1.2,beta=0)



img = cv.imread('../img/DetectionTestframeOcclusioncase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img3 = img.copy()
cv.convertScaleAbs(img3, alpha=1.2,beta=0)



img = cv.imread('../img/DetectionTestframeWorstcase.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img4 = img.copy()
cv.convertScaleAbs(img4, alpha=1.2,beta=0)



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