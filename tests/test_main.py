import cv2

import main
img = cv2.imread("test_assets/Test1.BMP")
sample =cv2.imread("test_assets/Test1.BMP")


def test_confidence():
    assert 1.0 == main.confidence(img, sample)
