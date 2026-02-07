import cv2
import numpy as np

# Disease classes (Phase 1 – logic based)
CLASSES = [
    "Healthy Leaf",
    "Leaf Blight",
    "Leaf Spot",
    "Powdery Mildew"
]


def is_leaf_like(image):
    """
    Check karta hai image leaf jaisi hai ya nahi
    (green color detection)
    """
    if image is None:
        return False

    img = cv2.resize(image, (224, 224))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([25, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    green_ratio = np.sum(mask > 0) / (224 * 224)

    return green_ratio > 0.15   # 15% green mandatory


def predict_disease(image):
    """
    Dummy disease prediction (TensorFlow later)
    """
    img = cv2.resize(image, (224, 224))
    img = img / 255.0

    probs = np.random.dirichlet(np.ones(len(CLASSES)), size=1)[0]
    idx = np.argmax(probs)

    return CLASSES[idx], float(probs[idx])
