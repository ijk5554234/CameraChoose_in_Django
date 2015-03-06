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

getPhotos("nike")