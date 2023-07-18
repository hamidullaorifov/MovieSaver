from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Movie
from .forms import MovieForm
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
from googleapiclient.http import MediaFileUpload
import json
# Create your views here.
from .utils import save_data_mongodb,save_file





def index(request):
    form = MovieForm()
    messages = []
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        data = request.POST
        name = data.get('name')
        date = data.get('date')
        description = data.get('description')
        if form.is_valid():
            movie = form.save()
            video_file = request.FILES.get('video')
            picture_file = request.FILES.get('picture')
            if video_file:
                video_url = save_file(video_file)
                
            if picture_file:
                picture_url = save_file(picture_file)
                
                object_id = save_data_mongodb({
                    'video':video_url,
                    'picture':picture_url
                })
                context = {
                    'name': name,
                    'date': date,
                    'description': description,
                    'object_id':object_id,
                    'video':video_url,
                    'picture':picture_url
                }
        return render(request,'app/result.html',context)
        


    return render(request,'app/index.html',{'form':form})