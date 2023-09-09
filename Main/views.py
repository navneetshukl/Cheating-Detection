#from django.http import JsonResponse
import base64
import json,utils
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#! Getting the user detail

def Home(request):
    context={}
    if request.method=='GET':
     return render(request, 'form.html',context)
 
    elif request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        #print(f"Name,Email and Phone number is {name} {email} {phone}")
        #return JsonResponse({"message": "Successfully submitted the data"})
        db=utils.Connect_To_DB()
        collection=db["users"]
        
        data={
            "name":name,
            "email":email,
            "phone":phone
        }
        collection.insert_one(data)
        response = redirect("/image/")
        response.set_cookie("email", email, path="/")
        return response

#! Getting the image of the user

def Capture_Image(request):
    if request.method == 'POST':
        # Get the raw JSON data from the request body
        data = json.loads(request.body)
        image_data = data.get('image_data', None)
        _, base64_data = image_data.split(';base64,')
        image_binary = base64.b64decode(base64_data)
        with open('captured_image.jpg', 'wb') as f:
            f.write(image_binary)
        db=utils.Connect_To_DB()
        collection=db["image"]
        email = request.COOKIES.get('email')
        img_data={
            "email":email,
            "image":image_data
        }
        print(f"Captured image is {image_data}")
        collection.insert_one(img_data)
        response_data = {'message': 'Image received and processed.'}
        return JsonResponse(response_data)

    else:
        return render(request, "image.html")

#! This function will start test

def Test(request):
    return render(request,"test.html")


@csrf_exempt
def cheat(request):
    if request.method == "POST":
         image = request.POST.get("image")
         print(image)
    return HttpResponse()