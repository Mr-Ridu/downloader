from django.shortcuts import render,redirect,HttpResponse
from pytube import YouTube,Playlist
import os
from django.contrib import messages
from pytube.exceptions import PytubeError
from django.http import FileResponse


#for go to homepage
def downloadyt(request):
    return render (request, 'homepage.html')



#for go to youtube video details
def ytdetails(request):
    if request.method == "POST":
        global LINK 
        LINK= request.POST['url']
        ini = YouTube(LINK)
        title = ini.title
        dis = ini.description
        alls=ini.streams.filter(adaptive=True)
        context={'lnk':LINK,'title':title,'all':alls, 'link':ini,'dis':dis}             
        return render (request, 'homepage.html',context)

        

#for download video
def newdown(request, itag):
        if request.method == "POST":
            homedir = os.path.expanduser("~")
            directory = homedir + '/Downloads'
            # directory = request.FILES.get('dir', '')
            YouTube(LINK).streams.get_by_itag(itag).download(directory)
            messages.success(request, "Downloaded")
            return redirect ('downloadyt')



#for thow the playlist
def playlistshow(request):
    if request.method == "POST":
        global PLAYLINK
        PLAYLINK = request.POST.get('url', '')
        #try:
        plst = Playlist(PLAYLINK)
        ptitle = plst.title
        plstvideos = plst.videos
        mutvideo = len(plstvideos)
        context = {'plst':plst,'ptitle':ptitle,'plstvideos':plstvideos,'mutvideo':mutvideo}
        return render(request, 'ytplay.html', context)
        
            
     

#for downloading playlists video
# def playlist_download(request):   
#     try:
#         video_url = request.GET.get('video_url')
#         homedir = os.path.expanduser("~")
#         dir = homedir + '/Downloads'
#         yt = YouTube(video_url)
#         stream = yt.streams.filter(progressive=True).first()
#         stream.download(dir)
#         messages.success(request, "experiment done")
#         plst = Playlist(PLAYLINK)
#         ptitle = plst.title
#         plstvideos = plst.videos
#         context = {'ptitle': ptitle, 'plstvideos': plstvideos}
#         return render(request, 'ytplay.html', context)
#     except PytubeError:
#         messages.error(request,"Invalid Playlist Link")
#         return redirect('downloadyt')

def playlist_download(request):   
    try:
        video_url = request.GET.get('video_url')
        homedir = os.path.expanduser("~")
        dir = homedir + '/Downloads'
        yt = YouTube(video_url)
        
        # download first stream
        stream = yt.streams.filter(progressive=True).first()
        stream.download(dir)
        mang = Playlist(PLAYLINK)
        fel = mang.title
        bal = mang.videos
        context = {'plst':mang,'ptitle':fel,'plstvideos':bal}
        messages.success(request,"experiment done")
        return render(request, 'ytplay.html',context)
    except PytubeError:
        #return redirect('downloadyt')
        return render(request, 'ytplay.html',context)