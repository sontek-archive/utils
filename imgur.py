#!/usr/bin/python
import pycurl
import sys

args = sys.argv[1:]
if not args:
    print "Please provide at least one image to upload"
else:
    for arg in args:
        c = pycurl.Curl()
        values = [
                  ("key", "INSERT YOUR KEY HERE"),
                  ("image", (c.FORM_FILE, arg))]
    # OR:         ("image", "http://example.com/example.jpg"))]

        c.setopt(c.URL, "http://imgur.com/api/upload.xml")
        c.setopt(c.HTTPPOST, values)

        c.perform()
        c.close()
""" <?xml version="1.0" encoding="utf-8"?>
<rsp stat="ok"><image_hash>FJSuD</image_hash><delete_hash>8DzqFsdlLk</delete_hash><original_image>http://imgur.com/FJSuD.png</original_image><large_thumbnail>http://imgur.com/FJSuDl.png</large_thumbnail><small_thumbnail>http://imgur.com/FJSuDs.png</small_thumbnail><imgur_page>http://imgur.com/FJSuD</imgur_page><delete_page>http://imgur.com/delete/8DzqFsdlLk</delete_page></rsp>
"""
