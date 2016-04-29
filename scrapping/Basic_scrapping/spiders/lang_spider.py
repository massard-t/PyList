import scrapy


<<<<<<< HEAD
class basic_scrapping(scrapy.Spider):
    """Spider looking for languages-related content"""
    name = "basic_scrapping"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Functional_programming",
        "https://en.wikipedia.org/wiki/Python_%28programming_language%29",
        "https://en.wikipedia.org/wiki/Node.js"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
