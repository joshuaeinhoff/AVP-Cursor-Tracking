import cv2 as cv
#from pynput import keyboard

video_path = "../data/video/Demo0.MP4"

video_cap = cv.VideoCapture(video_path)
count = 0


while True:
	img_path = "../data/img/labelingImages/Demo%d.png" % count
	ret, frame = video_cap.read()
	if not ret:
		break
	cv.imshow("Frame", frame)
	count += 1
	if count % 30 == 0:
		cv.imwrite(img_path,frame)
	if cv.waitKey(1) == ord("q"):
		break

video_cap.release()
cv.destroyAllWindows()	
