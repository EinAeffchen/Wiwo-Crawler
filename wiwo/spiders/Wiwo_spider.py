import scrapy
from pathlib import Path

class QuotesSpider(scrapy.Spider):
    name = "wiwo_all"
    allowed_domains = ["wiwo.de"]
    start_urls = [
        "https://www.wiwo.de/"
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "raw-wiwo-{}.html".format(page)
        article = response.css("article").extract_first()
        
        if article != None:
            yield {
                "url": response.url,
                "topic" : response.css("span.c-overline::text").extract_first(),
                "author" : response.css("a span.u-font-bold::text").extract_first(),
                "time" : response.css("time::attr(datetime)").extract_first(),
                "title" : response.css("h2.c-headline::text").extract_first(),
                "leadtext" : response.css("p.c-leadtext::text").extract_first(),
                "body" : " ".join(response.css("div.o-article__content div.o-article__content-element").css("::text").extract()),
            }
            RAWS = Path("Raws/")
            RAWS.mkdir(exist_ok=True)
            with open(RAWS/filename, "wb") as f:
                f.write(response.body)

        next_articles = response.css("div.c-teaser div.u-lastchild a::attr(href)").extract()
        next_pages = response.css("div.u-flex__item a.c-button::attr(href)").extract()
        new_authors = response.css("div.c-metadata a::attr(href)").extract()

        if new_authors != None:
            for link in new_authors:
                yield response.follow(link, callback=self.parse)

        if next_pages != None:
            for link in next_pages:
                yield response.follow(link, callback=self.parse)

        if next_articles != None:
            for link in next_articles:
                yield response.follow(link[:-5]+"-all.html", callback=self.parse)