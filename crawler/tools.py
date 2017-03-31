from urllib import request
from PIL import ImageFile
def getImgRatio(uri):
    try:
        file = request.urlopen(uri)
        data = file.read()
        p = ImageFile.Parser()
        p.feed(data)
        if p.image:
            return p.image.size[1]/p.image.size[0]
    except:
        pass
    return 1


def cleanUrl(domain, url):
    try:
        if not 'http' in url:
            url = domain + url
    except:
        pass
    return url