#from django.http import JsonResponse
import json
from django.http import JsonResponse
from django.shortcuts import render,redirect

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
        print(f"Name,Email and Phone number is {name} {email} {phone}")
        #return JsonResponse({"message": "Successfully submitted the data"})
        return redirect("/api/image")

#! Getting the image of the user

def Capture_Image(request):
    if request.method == 'POST':
        # Get the raw JSON data from the request body
        data = json.loads(request.body)
        image_data = data.get('image_data', None)

        # Process image_data, save it, etc.
        # Here, you can save the image using PIL or any other library

        # You can send a JSON response back if needed
        response_data = {'message': 'Image received and processed.'}
        print(response_data)
        print(image_data)
        return JsonResponse(response_data)

    else:
        return render(request, "image.html")

#! This function will start test

def Test(request):
    return render(request,"test.html")