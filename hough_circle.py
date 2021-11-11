import cv2

Img = cv2.imread('samand.jpg')

G = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # -> Grayscale
G = cv2.GaussianBlur(G, (3, 3), 0)  # Gaussian blur

canny_high_threshold = 40
edges = cv2.Canny(G,canny_high_threshold/2,canny_high_threshold)
cv2.imshow("edges" ,edges)
min_votes = 80  # minimum no. of votes to be considered as a circle
min_centre_distance = 40  # minimum distance between the centres of detected circles
resolution = 1  # resolution of parameters (centre, radius) relative to image resolution
circles = cv2.HoughCircles(G, cv2.HOUGH_GRADIENT, resolution, min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes, minRadius=10, maxRadius=80)

# for opencv 2 use cv2.cv.CV_HOUGH_GRADIENT instead of cv2.HOUGH_GRADIENT
print(circles)
for c in circles[0]:
    x = int(c[0])  # x coordinate of the centre

    y = int(c[1])  # y coordinate of the centre
    r = int(c[2])  # radius

    # draw the circle
    cv2.circle(Img, (x, y), r, (0, 255, 0), 2)

    # draw the circle center 
    cv2.circle(Img, (x, y), 5, (0, 0, 255), -1)

cv2.imshow("Img", Img)
cv2.waitKey(0)
cv2.destroyAllWindows()
