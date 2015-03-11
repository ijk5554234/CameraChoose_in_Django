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
        print(photo_url)

def getTweets(word):
    from twython import Twython
    APP_KEY = "foWNuG5j0oJdoXoCktS8jdltP"
    APP_SECRET = "O0oojri6fKpIbAo53ktesqInSnJbfoWYSzU7FAaeJxTPwfC9Yk"
    t = Twython(APP_KEY, APP_SECRET)
    results = t.cursor(t.search, q="camera", lang="en")
    for tweet in results:
        if tweet['text'] is not None:
            print(str(tweet['text']))


import json
import urllib
import json
import urllib.request, urllib.parse

def showsome(searchfor):
  query = urllib.parse.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  print('Total results: %s' % data['cursor']['estimatedResultCount'])
showsome("JikeLi")