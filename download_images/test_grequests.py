#!/usr/bin/env python
import grequests
import os
import time


urls = ["http://i.imgur.com/dLIds6a.gif"] * 1


def download_image_greq(urls):
    t_tot = 0
    t_b = time.time()
    req = (grequests.get(u) for u in urls)
    res = grequests.map(req)

    for response in res:
        with open(os.getcwd() + "/image.gif", 'w') as f:
            f.write(response.content)
        t_before_rm = time.time()
        os.remove(os.getcwd() + "/image.gif")
        t_after_rm = time.time()
        t_tot += t_after_rm - t_before_rm
    print time.time() - t_tot - t_b
download_image_greq(urls)
