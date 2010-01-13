#!/usr/bin/python
import sys
from urllib import urlencode
from urllib2 import urlopen

TINYURL = 'http://tinyurl.com/apicreate.php?%s'
ISGD = 'http://is.gd/api.php?%s'

def tiny_url(url):
    try:
        url = urlopen(ISGD % urlencode({'longurl':url})).read()
    except:
        url = urlopen(TINYURL % urlencode({'url':url})).read()
    finally:
        return url

args = sys.argv[1:]

if not args:
    print "Please provide at least one url to shorten"
else:
    for arg in args:
        print tiny_url(arg)


