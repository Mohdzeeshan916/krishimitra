from django.shortcuts import render
import cv2
import numpy as np
from .utils import predict_disease, is_leaf_like


def home(request):
    return render(request, "core/home.html")


def soil_recommendation(request):
    result = None

    if request.method == "POST":
        soil = request.POST.get("soil")
        season = request.POST.get("season")
        ph = float(request.POST.get("ph"))
        rainfall = float(request.POST.get("rainfall"))

        # simple logic
        if soil == "Loamy" and season == "Kharif":
            crop = "Rice"
            fertilizer = "Urea"
            water = "High"
        elif soil == "Sandy":
            crop = "Millet"
            fertilizer = "DAP"
            water = "Low"
        else:
            crop = "Wheat"
            fertilizer = "NPK"
            water = "Medium"

        result = {
            "crop": crop,
            "fertilizer": fertilizer,
            "water": water
        }

    return render(request, "core/soil.html", {"result": result})


def leaf_upload(request):
    result = None

    if request.method == "POST" and request.FILES.get("leaf"):
        image_file = request.FILES["leaf"]
        img = cv2.imdecode(
            np.frombuffer(image_file.read(), np.uint8),
            cv2.IMREAD_COLOR
        )

        if not is_leaf_like(img):
            result = "❌ This does not look like a leaf image"
        else:
            label, conf = predict_disease(img)
            result = f"{label} ({conf*100:.2f}%)"

    return render(request, "core/leaf.html", {"result": result})
