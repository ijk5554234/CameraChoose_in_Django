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
    photos = getphotos("123")
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


def compare(request):
    if not request.POST or request.POST.get("action") is None:
        return render(request, "compare.html", )

    # initialize the session
    camera1 = request.POST.get("camera1")
    camera2 = request.POST.get("camera2")
    pic1 = getphotos(camera1)
    pic2 = getphotos(camera2)
    urllist = []
    for i in range(10):
        if (i & 1) == 0:
            urllist.append(pic1.pop(0))
        else:
            urllist.append(pic2.pop(0))
    request.session["index"] = 0
    request.session["camera1"] = camera1
    request.session["camera2"] = camera2
    request.session["count1"] = 0
    request.session["count2"] = 0
    request.session["urllist"] = urllist
    return test(request)


def test(request):
    index = request.session["index"]
    camera1 = request.session["camera1"]
    camera2 = request.session["camera2"]
    urllist = request.session["urllist"]

    #return condition
    if index == 11:
        return render(request, "result.html", )

    #set the url and index
    url = urllist.pop(0)
    request.session["index"] += 1

    if request.POST.get("action") == "like":
        if (index & 1) == 0:
            request.session["count1"] += 1
        else:
            request.session["count2"] += 1

    return render(request, "blind.html", {"url": url})


def getphotos(cameramodel):
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
