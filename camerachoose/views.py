from django.shortcuts import render
from twython import Twython
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from camerachoose.models import Camera
from django import forms

APP_KEY = "foWNuG5j0oJdoXoCktS8jdltP"
APP_SECRET = "O0oojri6fKpIbAo53ktesqInSnJbfoWYSzU7FAaeJxTPwfC9Yk"


def index(request):
    photos = getphotos("popular")
    while len(photos) > 10:
        photos.pop()
    return render(request, 'login.html', {'photos': photos})


def login(request):
    t = Twython(APP_KEY, APP_SECRET)
    auth = t.get_authentication_tokens(callback_url='http://127.0.0.1:8000/callback/')
    access_url = str(auth['auth_url'])
    request.session["OAUTH_TOKEN"] = auth['oauth_token']
    request.session["OAUTH_TOKEN_SECRET"] = auth['oauth_token_secret']
    request.session["login"] = False
    return HttpResponseRedirect(access_url)


def compare(request):
    if not request.POST:
        token = request.session["OAUTH_TOKEN"]
        secret = request.session["OAUTH_TOKEN_SECRET"]
        t = Twython(APP_KEY, APP_SECRET, token, secret)
        final_step = t.get_authorized_tokens(request.GET["oauth_verifier"])
        request.session["OAUTH_TOKEN"] = final_step['oauth_token']
        request.session["OAUTH_TOKEN_SECRET"] = final_step['oauth_token_secret']
        request.session["login"] = True
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
    print("length of url==" + str(len(urllist)))
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
    if index == 11 or len(urllist) == 0:
        return HttpResponseRedirect("/camerachoose/result")

    #set the url and index
    url = urllist.pop(0)["url"]
    request.session["index"] += 1

    if request.POST.get("action") == "like":
        if (index & 1) == 0:
            request.session["count1"] += 1
        else:
            request.session["count2"] += 1

    return render(request, "blind.html", {"url": url})


def result(request):
        ctx = {}
        wincamera = request.session["camera1"]
        if request.session["count2"] > request.session["count2"]:
            wincamera = request.session["camera2"]
        ctx['camera'] = wincamera

        #update the database
        from datetime import date
        today = date.today()
        from camerachoose.models import Camera
        new_record = Camera(model=wincamera, date=today)
        new_record.save()


        #prepare from the diagram


        #search the popular tweets
        token = request.session["OAUTH_TOKEN"]
        secret = request.session["OAUTH_TOKEN_SECRET"]
        t = Twython(APP_KEY, APP_SECRET, token, secret)
        #tweets = t.search(q=wincamera, result_type='popular')
        tweets = []
        from twython import TwythonRateLimitError
        try:
            results = t.cursor(t.search, q=wincamera, lang="en")
            for tweet in results:
                tweets.append(tweet)
            ctx["tweets"] = tweets["statuses"]
        except TwythonRateLimitError:
            ctx["msg"] = "Request rate limits exceed"
        if not request.POST or request.POST["action"]is None:
            return render(request, "result.html", ctx)

        #tweet the result
        text = request.POST["text"]
        from twython import TwythonError
        try:
            t.update_status(status=text)
        except TwythonError:
            ctx["msg"] = "You result has already been tweeted"
            return render(request, "result.html", ctx)
        ctx["msg"] = "Result has been tweeted"
        return render(request, "result.html", ctx)


def anothertest(request):
    return render(request, "compare.html", )


def logout(request):
    del request.session
    return HttpResponseRedirect("camerachoose/index")


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
        photo_url = "https://farm" + farm + ".staticflickr.com/" + server + "/" + id + "_" + secret + ".jpg"
        p = {"title": photo.get("title"), "url": photo_url}
        photos.append(p)
        if len(photos) > 25:
            break
    return photos
