# upload_app/views.py
from django.shortcuts import render
from django.conf import settings
from django_user_agents.utils import get_user_agent
import os

MAX_UPLOADS_PER_IP = 5

def upload(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, 'mobile_only.html')
    
    if request.method == 'POST' and request.FILES.get('zip_file'):
        zip_file = request.FILES['zip_file']
        handle_uploaded_file(zip_file)
        return render(request, 'upload.html', {'message': 'File uploaded successfully'})
    
    return render(request, 'upload.html')

def handle_uploaded_file(f):
    media_root = settings.MEDIA_ROOT
    images_folder = os.path.join(media_root, 'images')
    os.makedirs(images_folder, exist_ok=True)  # Create 'images' folder if it doesn't exist
    destination = os.path.join(images_folder, f.name) 
    print(destination)# Path to save the uploaded file
    with open(destination, 'wb+') as destination_file:
        for chunk in f.chunks():
            destination_file.write(chunk)
            





