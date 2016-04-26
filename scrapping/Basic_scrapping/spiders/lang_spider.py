import scrapy


<<<<<<< HEAD
class basic_scrapping(scrapy.Spider):
    """Spider looking for languages-related content"""
    name = "basic_scrapping"
=======
class LangSpider(scrapy.Spider):
    """Spider looking for languages-related content"""
    name = "lang"
>>>>>>> d58632e2f39bfd83394d0b62750311989e49ba54
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Functional_programming",
        "https://en.wikipedia.org/wiki/Python_%28programming_language%29",
        "https://en.wikipedia.org/wiki/Node.js"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
<<<<<<< HEAD
            f.write(response.body)
=======
            f.write(response.body)
>>>>>>> d58632e2f39bfd83394d0b62750311989e49ba54
