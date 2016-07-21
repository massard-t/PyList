#!/usr/bin/env python
import urllib
import os
import time


urls = ["http://i.imgur.com/dLIds6a.gif"] * 1

def download_image_urllib(urls):
    t_start = time.time()
    t_tot = 0
    for url in urls:
        t_b = time.time()
        urllib.urlretrieve(url, os.getcwd() + "/image.gif")
        t_a = time.time()
        t_tot += t_b - t_a
        os.remove(os.getcwd()+"/image.gif")
    print t_start - t_tot
        
download_image_urllib(urls)
