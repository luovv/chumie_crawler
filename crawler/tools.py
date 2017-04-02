from urllib import request
from PIL import ImageFile
import re
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


def removeTags(text, tag):
    try:
        for i in tag:
            p = re.compile(r'</?%s.*?>'%i)
            text = p.sub('', text)
    except:
        pass
    return text


def removeAllTags(text):
    try:
        p = re.compile(r'<.*?>')
        text = p.sub('', text)
    except:
        pass
    return text