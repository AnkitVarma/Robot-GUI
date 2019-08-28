import numpy as np
import cv2
import datetime
import base64
import time
import argparse
import imutils
import sys
import keyboard
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=False,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=False,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

#cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

time.sleep(2)
x = datetime.datetime.now()
y = x.strftime("%f")
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
#qprint("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("C:\cctv\MobileNetSSD_deploy.prototxt.txt","C:\cctv\MobileNetSSD_deploy.caffemodel")

name = 'videos/Video' + y + '.mp4'
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(name, fourcc, 20.0, (640,480))
while(True):
    #capture frame by frame
    

    ret,frame = cap.read()
    
    if ret == True:
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > args["confidence"]:
                # extract the index of the class label from the
                # `detections`, then compute the (x, y)-coordinates of
                # the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx],
                    confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                    COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
        #cv2.imshow('frame', frame)
        out.write(frame)
        retval, buffer = cv2.imencode('.jpeg',frame)
        jpegtext = base64.b64encode(buffer).decode()
        
        print(jpegtext)
        if keyboard.is_pressed('q'):
            break
    else:
        break
cap.release()
out.release()

cv2.destroyAllWindows()



