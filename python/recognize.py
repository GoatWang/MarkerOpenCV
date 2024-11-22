import cv2
from matplotlib import pyplot as plt

arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
arucoParams = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)


# img = cv2.imread("IMG_2241.jpg")
img = cv2.imread("camera_images/IMG_2247.jpg")
# img = cv2.imread("camera_images/marker23.png")
# img = cv2.imread("camera_images/singlemarkersoriginal.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(img)
# plt.show()
marker_corners, marker_ids, marker_rejected = detector.detectMarkers(img)

# print(marker_corners)
# print(marker_ids)
# print(marker_ids)
# print(marker_rejected)
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

for id, corner in zip(marker_ids, marker_corners):
    print(id, corner)
    ax.text(corner[0][0][0], corner[0][0][1], str(id), color='red', fontsize=20)
    ax.scatter(corner[0][:, 0], corner[0][:, 1], c='r', s=100)
    # ax.scatter(marker_corners[0][0][:, 0], marker_corners[0][0][:, 1], c='r', s=100)
plt.show()


