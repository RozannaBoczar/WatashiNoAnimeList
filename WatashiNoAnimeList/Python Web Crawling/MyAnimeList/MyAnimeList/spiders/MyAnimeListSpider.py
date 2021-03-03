# https://myanimelist.net/#
import scrapy

name_eng = ""
description = ""
num_episodes = 0
status = ""
premiered = ("", "")
studio = ""
source = ""
genres = []
duration = 0
score = 0
# image - obrazek


class MyAnimeListSpider(scrapy.Spider):
    name = "MyAnimeList"

    # start_urls = ["https://myanimelist.net/topanime.php"] -> it's the same as the def start_request(), kinda shortcut

    anime_url = " "

    def start_requests(self):
        urls = ["https://myanimelist.net/topanime.php"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for anime in response.css("tr.ranking-list"):
            print(anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get())
            next_page = anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get()
            if next_page is not None:
                next_page = anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get()
                yield scrapy.Request(next_page, callback=self.parse_info)

    def parse_info(self, response):
        titles = response.xpath("//*[@id='contentWrapper']/div[1]/div/div[1]/div")
        title_eng = titles.xpath(".//h1/strong/text()").get()
        case = titles.xpath(".//p/text()").get()

        print(title_eng)
        if case is not None:
            print(case)


