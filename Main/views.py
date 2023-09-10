from django.http import JsonResponse
import base64, time
import json, utils
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import cv2
from skimage.metrics import structural_similarity as ssim

# Create your views here.

#! Getting the user detail


def Home(request):
    context = {}
    if request.method == "GET":
        return render(request, "form.html", context)

    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        # print(f"Name,Email and Phone number is {name} {email} {phone}")
        # return JsonResponse({"message": "Successfully submitted the data"})
        db = utils.Connect_To_DB()
        collection = db["users"]

        data = {"name": name, "email": email, "phone": phone}
        collection.insert_one(data)
        response = redirect("/image/")
        response.set_cookie("email", email, path="/")
        return response


#! Getting the image of the user


def Capture_Image(request):
    if request.method == "POST":
        # Get the raw JSON data from the request body
        data = json.loads(request.body)
        image_data = data.get("image_data", None)
        _, base64_data = image_data.split(";base64,")
        image_binary = base64.b64decode(base64_data)
        with open("reference_image.jpg", "wb") as f:
            f.write(image_binary)
        db = utils.Connect_To_DB()
        collection = db["image"]
        email = request.COOKIES.get("email")
        img_data = {"email": email, "image": image_data}
        print(f"Captured image is {image_data}")
        collection.insert_one(img_data)
        response_data = {"message": "Image received and processed."}
        return JsonResponse(response_data)

    else:
        return render(request, "image.html")


#! This function will start test


def Test(request):
    return render(request, "test.html")


@csrf_exempt
def cheat(request):
    if request.method == "POST":
        image = request.POST.get("image")
        email = request.COOKIES.get("email")
        db = utils.Connect_To_DB()
        collection = db["image"]
        img_data = collection.find_one({"email": email})

        if img_data is None:
            # Handle the case when the reference image is missing
            print("Reference image is missing.")
            return JsonResponse({"message": "Reference image is missing."}, status=400)

        reference_image = cv2.imread("reference_image.jpg")

        if image:
            _, base64_data = image.split(";base64,")
            image_binary = base64.b64decode(base64_data)
            with open("exam_image.jpg", "wb") as f:
                f.write(image_binary)

            exam_image = cv2.imread("exam_image.jpg")
            
            time.sleep(5)

            if exam_image is None:
                # Handle the case when the exam image is missing
                print("Exam image is missing.")
                return JsonResponse({"message": "Exam image is missing."}, status=400)

            # Convert images to grayscale
            reference_image_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
            exam_image_gray = cv2.cvtColor(exam_image, cv2.COLOR_BGR2GRAY)

            # Calculate Mean Squared Error (MSE)
            mse = ((reference_image_gray - exam_image_gray) ** 2).mean()
            print(f"MSE: {mse}")

            # Threshold for cheating detection
            threshold = 100  

           
            if mse > threshold:
                message = "Cheating detected ."
            else:
                message = "No cheating detected ."
                
            print(message)

            os.remove("exam_image.jpg")
    return HttpResponse()