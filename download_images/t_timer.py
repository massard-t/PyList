import test_urllib
import test_grequests
import timeit


stp = """
import test_urllib
import test_grequests


urls = ["http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif",
"http://i.imgur.com/dLIds6a.gif"
]"""
res = []

t_urllib = timeit.Timer(stmt="test_urllib.download_image_urllib(urls)", setup=stp)
r_urllib = "Temps urllib : {}".format(' '.join(map(str, t_urllib.repeat(3))))
res.append(r_urllib)
t_grequests = timeit.Timer(stmt="test_grequests.download_image_greq(urls)", setup=stp)
r_grequests = "Temps grequests: {}".format(' '.join(map(str, t_grequests.timeit(3))))
res.append(r_grequests)

for result in res:
    print result
