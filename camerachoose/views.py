from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from camerachoose.models import Camera
from django import forms



def list(request):
    list = Camera.objects.all()
    cameras = []
    for i in range(len(list)):
        cameras.append(list[i].model)
    return render(request, 'templay.html', {'cameras': cameras})

class CameraForm(forms.Form):
    model = forms.CharField(max_length=20, min_length=5)
    date = forms.DateField()

def form(request):
    form = CameraForm()
    ctx = {}
    ctx['form'] = form
    return render(request, "form.html", ctx)

def investigate(request):
    ctx = {}
    if request.POST:
        form = CameraForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['model']
            new_record = Camera(model=data)
            new_record.save()
            ctx['model'] = form.cleaned_data['model']
        else:
            ctx['model'] = 'Wrong'

    ctx['form'] = CameraForm()
    return render(request, "form.html", ctx)





def index(request):
    photos = getPhotos("123")
    while len(photos) > 10:
        photos.pop()
    return render(request, 'login.html', {'photos': photos})

def login(request):
    from twython import Twython
    APP_KEY = "foWNuG5j0oJdoXoCktS8jdltP"
    APP_SECRET = "O0oojri6fKpIbAo53ktesqInSnJbfoWYSzU7FAaeJxTPwfC9Yk"
    t = Twython(APP_KEY, APP_SECRET)
    auth = t.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    access_url = str(auth['auth_url'])
    return HttpResponseRedirect(access_url)

def test(request):
    picture = request.session.get("picture")

    # initialize the session
    if picture is None:
        camera1model = request.POST.get("camera1")
        camera2model = request.POST.get("camera2")
        camera1 = Camera(camera1model)
        camera2 = Camera(camera2model)
        picture = Picture(camera1, camera2)
        pic1 = getPhotos(camera1model)
        pic2 = getPhotos(camera2model)
        for i in range(10):
            if (i & 1) == 0:
                picture.urllist.append(pic1.pop(0))
            else:
                picture.urllist.append(pic2.pop(0))
        request.session["picture"] = picture
    #return condition
    if picture.index == 11:
        cameras = {"camera1": camera1, "camera2": camera2}
        request.session["cameras"] = cameras
        return render(request, "result.html", )

    #set the url and index
    picture.url = picture.urllist.pop(0)
    picture.index += 1

    if request.POST.get("action") == "like":
        if (picture.index & 1) == 0:
            picture.camera1.count += 1
        else:
            picture.camera2.count += 1

    return render(request, "blind.html",)






def getPhotos(cameramodel):
    import flickrapi
    api_key = "522bd85601ed0e20cca4fcb60762131f"
    api_secret = "fbc62843365374ac"
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    photos = []
    for photo in flickr.walk(tag_mode='all', tags=cameramodel, min_taken_date='2012-08-20', max_taken_date='2015-08-30',per_page=15):
        id = photo.get("id")
        secret = photo.get("secret")
        server = photo.get("server")
        farm = photo.get("farm")
        photo_url = "https://farm" + farm + ".staticflickr.com/" + server + "/" + id + "_"+ secret + ".jpg";
        p = {"title": photo.get("title"), "url": photo_url}
        photos.append(p)
        if len(photos) > 25:
            break
    return photos

class Camera:
    def __init__(self, model):
        self.count = 0;
        self.model = model

class Picture:
    def __init__(self, camera1, camera2):
        self.url = ""
        self.index = 0
        self.camera1 = camera1
        self.camera2 = camera2
        self.urllist = []
