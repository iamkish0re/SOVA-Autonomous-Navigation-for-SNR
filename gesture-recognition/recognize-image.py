import cv2
import imutils
import numpy as np
from sklearn.metrics import pairwise


def segment(image, grayimage, threshold=75):

    thresholded = cv2.threshold(grayimage, threshold, 255, cv2.THRESH_BINARY)[1]


    (cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #nothing detected
    if len(cnts) == 0:
        return
    else:     
        # max contour
        segmented = max(cnts, key=cv2.contourArea)
        
        return (thresholded, segmented)


def count(image, thresholded, segmented):

    chull = cv2.convexHull(segmented)


    extreme_top    = tuple(chull[chull[:, :, 1].argmin()][0])
    extreme_bottom = tuple(chull[chull[:, :, 1].argmax()][0])
    extreme_left   = tuple(chull[chull[:, :, 0].argmin()][0])
    extreme_right  = tuple(chull[chull[:, :, 0].argmax()][0])


    cX = int((extreme_left[0] + extreme_right[0]) / 2)
    cY = int((extreme_top[1] + extreme_bottom[1]) / 2)


    distances = pairwise.euclidean_distances([(cX, cY)], Y=[extreme_left, extreme_right, extreme_top, extreme_bottom])[0]
    max_distance = distances[distances.argmax()]

    radius = int(0.8 * max_distance)


    circumference = (2 * np.pi * radius)


    circular_roi = np.zeros(thresholded.shape[:2], dtype="uint8")


    cv2.circle(circular_roi, (cX, cY), radius, 255, 1)

    circular_roi = cv2.bitwise_and(thresholded, thresholded, mask=circular_roi)


    (cnts, _) = cv2.findContours(circular_roi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    count = 0

    # loop through the contours found
    for i, c in enumerate(cnts):

        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)

        if ((cY + (cY * 0.25)) > (y + h)) and ((circumference * 0.25) > c.shape[0]):
            count += 1

    return count

if __name__ == "__main__":

    frame = cv2.imread("resources/hand-sample.jpg")


    frame = imutils.resize(frame, width=700)

    clone = frame.copy()


    (height, width) = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    hand = segment(clone, gray)


    if hand is not None:

        (thresholded, segmented) = hand


        fingers = count(clone, thresholded, segmented)

        cv2.putText(clone, "This is " + str(fingers), (70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Image", clone)

    cv2.waitKey(0)
    cv2.destroyAllWindows()