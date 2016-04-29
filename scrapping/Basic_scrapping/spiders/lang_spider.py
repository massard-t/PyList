import scrapy


class LangSpider(scrapy.Spider):
    """Spider looking for languages-related content"""
    name = "lang"
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